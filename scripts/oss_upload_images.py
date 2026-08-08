#!/usr/bin/env python3
"""Upload local images referenced by a markdown article to Aliyun OSS and rewrite links.

Reads OSS_* keys from local.config.md (skill directory) or from the environment.
Never prints secret values. Stdlib only — no pip deps.

Usage:
  python scripts/oss_upload_images.py path/to/article.md
  python scripts/oss_upload_images.py path/to/article.md --dry-run
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import mimetypes
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

IMG_MD_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
IMG_HTML_RE = re.compile(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\'][^>]*>', re.I)
YAML_KEY_RE = re.compile(r"^(OSS_[A-Z0-9_]+):\s*(.*)$")


def skill_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def parse_local_config(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    text = path.read_text(encoding="utf-8")
    # Prefer fenced yaml block; fall back to whole file.
    blocks = re.findall(r"```ya?ml\s*\n(.*?)```", text, flags=re.S | re.I)
    src = blocks[0] if blocks else text
    out: dict[str, str] = {}
    for line in src.splitlines():
        m = YAML_KEY_RE.match(line.strip())
        if not m:
            continue
        key, raw = m.group(1), m.group(2).strip().strip('"').strip("'")
        if raw:
            out[key] = raw
    return out


def load_oss_config() -> dict[str, str]:
    cfg = parse_local_config(skill_dir() / "local.config.md")
    keys = [
        "OSS_ENDPOINT",
        "OSS_BUCKET",
        "OSS_PREFIX",
        "OSS_ACCESS_KEY_ID",
        "OSS_ACCESS_KEY_SECRET",
        "OSS_PUBLIC_BASE",
    ]
    out: dict[str, str] = {}
    for k in keys:
        out[k] = os.environ.get(k) or cfg.get(k) or ""
    missing = [k for k in keys if not out[k] and k != "OSS_PREFIX"]
    # PREFIX may be empty; PUBLIC_BASE can be derived.
    if not out["OSS_PUBLIC_BASE"] and out["OSS_BUCKET"] and out["OSS_ENDPOINT"]:
        out["OSS_PUBLIC_BASE"] = f"https://{out['OSS_BUCKET']}.{out['OSS_ENDPOINT']}"
    required = ["OSS_ENDPOINT", "OSS_BUCKET", "OSS_ACCESS_KEY_ID", "OSS_ACCESS_KEY_SECRET", "OSS_PUBLIC_BASE"]
    missing = [k for k in required if not out.get(k)]
    if missing:
        raise SystemExit(
            "Missing OSS config: "
            + ", ".join(missing)
            + ". Set them in local.config.md (gitignored) or environment."
        )
    prefix = out.get("OSS_PREFIX", "")
    if prefix and not prefix.endswith("/"):
        out["OSS_PREFIX"] = prefix + "/"
    return out


def is_remote(url: str) -> bool:
    return url.startswith("https://") or url.startswith("http://") or url.startswith("data:")


def collect_local_refs(md_text: str, md_path: Path) -> list[tuple[str, Path]]:
    refs: list[str] = []
    for m in IMG_MD_RE.finditer(md_text):
        refs.append(m.group(2).strip())
    for m in IMG_HTML_RE.finditer(md_text):
        refs.append(m.group(1).strip())
    # cover: field in frontmatter
    fm = re.match(r"^---\n(.*?)\n---\n", md_text, flags=re.S)
    if fm:
        for line in fm.group(1).splitlines():
            if line.startswith("cover:"):
                val = line.split(":", 1)[1].strip().strip('"').strip("'")
                if val:
                    refs.append(val)

    seen: set[str] = set()
    out: list[tuple[str, Path]] = []
    for ref in refs:
        # strip optional title / size suffix like "imgs/a.png|575x829"
        path_part = ref.split()[0].split("|")[0]
        if not path_part or is_remote(path_part) or path_part in seen:
            continue
        seen.add(path_part)
        p = (md_path.parent / path_part).resolve()
        if not p.is_file():
            print(f"WARN: local image not found, skip: {path_part}", file=sys.stderr)
            continue
        out.append((path_part, p))
    return out


def content_type_for(path: Path) -> str:
    guess, _ = mimetypes.guess_type(str(path))
    return guess or "application/octet-stream"


def oss_sign(secret: str, string_to_sign: str) -> str:
    digest = hmac.new(secret.encode("utf-8"), string_to_sign.encode("utf-8"), hashlib.sha1).digest()
    return base64.b64encode(digest).decode("utf-8")


def put_object(cfg: dict[str, str], object_key: str, data: bytes, content_type: str, retries: int = 2) -> str:
    bucket = cfg["OSS_BUCKET"]
    endpoint = cfg["OSS_ENDPOINT"]
    date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
    resource = f"/{bucket}/{object_key}"
    string_to_sign = f"PUT\n\n{content_type}\n{date}\n{resource}"
    signature = oss_sign(cfg["OSS_ACCESS_KEY_SECRET"], string_to_sign)
    url = f"https://{bucket}.{endpoint}/{object_key}"
    last_err: Exception | None = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, data=data, method="PUT")
        req.add_header("Date", date)
        req.add_header("Content-Type", content_type)
        req.add_header("Authorization", f"OSS {cfg['OSS_ACCESS_KEY_ID']}:{signature}")
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                if resp.status not in (200, 201):
                    raise SystemExit(f"Upload failed ({resp.status}): {object_key}")
            return f"{cfg['OSS_PUBLIC_BASE'].rstrip('/')}/{object_key}"
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            raise SystemExit(f"Upload HTTP {e.code} for {object_key}: {body[:400]}") from e
        except (TimeoutError, urllib.error.URLError) as e:
            last_err = e
            print(f"WARN: upload attempt {attempt + 1} failed for {object_key}: {e}", file=sys.stderr)
    raise SystemExit(f"Upload timed out for {object_key}: {last_err}")


def object_key_for(cfg: dict[str, str], md_path: Path, local_path: Path) -> str:
    # full-stack/pub-df-goal-cascade/00-cover.png style when article is under insights-to-share
    slug = md_path.parent.name
    return f"{cfg.get('OSS_PREFIX', '')}{slug}/{local_path.name}"


def rewrite_markdown(md_text: str, mapping: dict[str, str]) -> str:
    def repl_md(m: re.Match[str]) -> str:
        alt, target = m.group(1), m.group(2).strip()
        path_part = target.split()[0].split("|")[0]
        if path_part in mapping:
            rest = target[len(target.split()[0]) :]  # keep title part if any
            # drop |WxH size hint — not needed for remote urls
            return f"![{alt}]({mapping[path_part]}{rest})"
        return m.group(0)

    def repl_html(m: re.Match[str]) -> str:
        full = m.group(0)
        src = m.group(1)
        path_part = src.split("|")[0]
        if path_part in mapping:
            return full.replace(src, mapping[path_part], 1)
        return full

    text = IMG_MD_RE.sub(repl_md, md_text)
    text = IMG_HTML_RE.sub(repl_html, text)

    def repl_cover(m: re.Match[str]) -> str:
        block = m.group(0)
        for local, remote in mapping.items():
            block = re.sub(
                rf"(cover:\s*){re.escape(local)}",
                rf"\1{remote}",
                block,
            )
        return block

    text = re.sub(r"^---\n.*?\n---\n", repl_cover, text, count=1, flags=re.S)
    return text


def head_ok(url: str) -> bool:
    req = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return 200 <= resp.status < 400
    except Exception:
        # some buckets block HEAD; try GET range
        req = urllib.request.Request(url, method="GET")
        req.add_header("Range", "bytes=0-0")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return 200 <= resp.status < 400
        except Exception as e:
            print(f"WARN: URL check failed for {url}: {e}", file=sys.stderr)
            return False


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("markdown", type=Path, help="Article markdown path")
    ap.add_argument("--dry-run", action="store_true", help="Map only; do not upload or write")
    ap.add_argument("--no-verify", action="store_true", help="Skip public URL reachability check")
    args = ap.parse_args()

    md_path = args.markdown.resolve()
    if not md_path.is_file():
        raise SystemExit(f"Markdown not found: {md_path}")

    cfg = load_oss_config()
    original = md_path.read_text(encoding="utf-8")
    locals_ = collect_local_refs(original, md_path)
    if not locals_:
        print("No local image references to upload.")
        return

    mapping: dict[str, str] = {}
    for ref, path in locals_:
        key = object_key_for(cfg, md_path, path)
        remote = f"{cfg['OSS_PUBLIC_BASE'].rstrip('/')}/{key}"
        print(f"{ref} -> {remote}")
        if args.dry_run:
            mapping[ref] = remote
            continue
        data = path.read_bytes()
        ctype = content_type_for(path)
        remote = put_object(cfg, key, data, ctype)
        mapping[ref] = remote
        if not args.no_verify and not head_ok(remote):
            raise SystemExit(f"Uploaded but URL not reachable: {remote}")

    if args.dry_run:
        print(f"Dry run OK — {len(mapping)} image(s).")
        return

    updated = rewrite_markdown(original, mapping)
    if updated == original:
        print("Upload OK; markdown already had no rewritable local refs (check cover/frontmatter).")
    else:
        md_path.write_text(updated, encoding="utf-8")
        print(f"Rewrote {md_path} ({len(mapping)} image link(s)).")

    # residual local refs?
    residual = collect_local_refs(md_path.read_text(encoding="utf-8"), md_path)
    if residual:
        left = ", ".join(r for r, _ in residual)
        raise SystemExit(f"Local image refs remain after rewrite: {left}")
    print("Smoke OK — no local image refs remain.")


if __name__ == "__main__":
    main()
