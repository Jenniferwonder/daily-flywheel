# scripts/trendradar_hot_topics.py
"""Query a local TrendRadar clone for AI-themed hot items. Does not copy the crawler."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

AI_NEEDLE = re.compile(
    r"ai|人工智能|大模型|agent|gpt|claude|deepseek|llm|chatgpt|cursor|智能体|openai|gemini|grok|anthropic",
    re.I,
)

QUERIES = ("AI", "人工智能", "大模型", "Agent", "DeepSeek", "ChatGPT")
PLATFORMS = ("zhihu", "douyin", "bilibili-hot-search")
SECTION = {
    "zhihu": "zhihu",
    "douyin": "douyin",
    "bilibili-hot-search": "bilibili",
}


def _parse_local_config(skill_dir: Path) -> dict[str, str]:
    cfg = {}
    path = skill_dir / "local.config.md"
    if not path.exists():
        return cfg
    for line in path.read_text(encoding="utf-8").splitlines():
        if ":" not in line or line.strip().startswith("#"):
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        if key and val and " " not in key:
            cfg[key] = val
    return cfg


def _trendradar_dir(skill_dir: Path) -> Path:
    env = os.environ.get("TRENDRADAR_DIR")
    if env:
        return Path(env)
    cfg = _parse_local_config(skill_dir)
    if cfg.get("TRENDRADAR_DIR"):
        return Path(cfg["TRENDRADAR_DIR"])
    codespace = cfg.get("CODESPACE_DIR")
    if codespace:
        return Path(codespace) / "TrendRadar"
    raise SystemExit("Set TRENDRADAR_DIR or CODESPACE_DIR in local.config.md")


def _is_ai(title: str) -> bool:
    return bool(AI_NEEDLE.search(title or ""))


def crawl(repo: Path) -> None:
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    env["UV_LINK_MODE"] = "copy"
    subprocess.run(
        ["uv", "run", "python", "-m", "trendradar"],
        cwd=repo,
        env=env,
        check=True,
    )


def search(repo: Path) -> dict[str, list[dict]]:
    sys.path.insert(0, str(repo))
    from mcp_server.tools.search_tools import SearchTools

    tools = SearchTools(str(repo))
    by_section: dict[str, list[dict]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    for query in QUERIES:
        result = tools.search_news_unified(
            query=query,
            search_mode="keyword",
            platforms=list(PLATFORMS),
            limit=20,
            include_url=True,
        )
        rows = result.get("data") or result.get("results") or []
        if not result.get("success"):
            continue
        for row in rows:
            title = (row.get("title") or "").strip()
            url = (row.get("url") or "").strip()
            platform = row.get("platform") or ""
            if not title or not url or not _is_ai(title):
                continue
            key = (platform, url)
            if key in seen:
                continue
            seen.add(key)
            section = SECTION.get(platform, platform)
            by_section[section].append({"title": title, "url": url, "query": query})
    return dict(by_section)


def to_markdown(grouped: dict[str, list[dict]]) -> str:
    today = date.today().isoformat()
    lines = [
        "# Hot topics",
        "",
        f"- updated: {today}",
        "- span: last 7 days",
        "- query: AI 主题（TrendRadar 优先；skill 二次过滤）",
        "- source: TrendRadar",
        "",
        "Every row needs a URL. Source with no hit → `未取到`.",
        "",
    ]
    for section in ("douyin", "zhihu", "x", "youtube", "google", "bilibili"):
        lines.append(f"## {section}")
        lines.append("")
        rows = grouped.get(section) or []
        if section in ("x", "youtube", "google") or not rows:
            if section in ("douyin", "zhihu", "bilibili") and not rows:
                lines.append("- 未取到")
            elif section in ("x", "youtube", "google"):
                lines.append("- 未取到（CN 热榜走 TrendRadar；本源由 df plan WebSearch 补，不挡验收）")
            else:
                lines.append("- 未取到")
        else:
            for row in rows:
                lines.append(f"- [{row['title']}]({row['url']}) — TrendRadar `{row['query']}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--crawl", action="store_true", help="Run one TrendRadar crawl first")
    parser.add_argument("--json", action="store_true")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write HOT_TOPICS_FILE (default local.hot-topics.md in the skill dir)",
    )
    args = parser.parse_args()
    skill_dir = Path(__file__).resolve().parent.parent
    repo = _trendradar_dir(skill_dir)
    if not repo.is_dir():
        raise SystemExit(f"TrendRadar missing at {repo}. Clone sansan0/TrendRadar into CODESPACE_DIR only.")
    if args.crawl:
        crawl(repo)
    grouped = search(repo)
    if args.json:
        print(json.dumps(grouped, ensure_ascii=False, indent=2))
        return
    md = to_markdown(grouped)
    if args.write:
        cfg = _parse_local_config(skill_dir)
        out_name = cfg.get("HOT_TOPICS_FILE", "local.hot-topics.md")
        out = Path(out_name)
        if not out.is_absolute():
            out = skill_dir / out
        out.write_text(md, encoding="utf-8")
        print(f"wrote {out}")
    else:
        print(md)


if __name__ == "__main__":
    main()
