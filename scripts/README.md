# scripts

## `trendradar_hot_topics.py`

Query a local [TrendRadar](https://github.com/sansan0/TrendRadar) clone for AI-themed
hot items and optionally write `HOT_TOPICS_FILE`. Does not copy the crawler.

```bash
python scripts/trendradar_hot_topics.py --write
python scripts/trendradar_hot_topics.py --crawl --write
```

`TRENDRADAR_DIR` / `CODESPACE_DIR` come from `local.config.md`. Clone only under `CODESPACE_DIR`.
Requires `uv` on PATH. Windows consoles need `PYTHONUTF8=1`.

## `oss_upload_images.py`

Upload local images referenced by an article markdown file to Aliyun OSS, rewrite
those links to public HTTPS URLs, and fail if any local `imgs/` refs remain.

### Config (gitignored)

Add these keys to `local.config.md` (never commit real values):

| Key | Meaning |
|-----|---------|
| `OSS_ENDPOINT` | e.g. `oss-cn-shanghai.aliyuncs.com` |
| `OSS_BUCKET` | bucket name |
| `OSS_PREFIX` | object key prefix, e.g. `articles/` |
| `OSS_ACCESS_KEY_ID` | RAM AccessKey id |
| `OSS_ACCESS_KEY_SECRET` | RAM AccessKey secret |
| `OSS_PUBLIC_BASE` | public base URL, e.g. `https://my-bucket.oss-cn-shanghai.aliyuncs.com` |

Environment variables with the same names override the file.

### Usage

```bash
python scripts/oss_upload_images.py path/to/pub-slug/pub-slug.md --dry-run
python scripts/oss_upload_images.py path/to/pub-slug/pub-slug.md
```

Stdlib only. Invoked by `df final` after illustrations and before publish handoff.
