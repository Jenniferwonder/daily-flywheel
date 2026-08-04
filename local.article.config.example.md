# local.article.config

Copy this file to `local.article.config.md` in the same directory and fill it in.
`local.article.config.md` is gitignored and never committed.

`df ship` reads this file before writing any article. If it is missing, or required
keys below are empty, ship refuses to draft and asks you to finish setup first.

Required keys: `audience`, `export_dir`, `export_slug_pattern`.

```yaml
# quality | time | hybrid
# hybrid (default): shorten before shipping; if still below bar, ship a slice
# or "stuck" post — never pad a long weak draft just to fill time.
ship_policy: hybrid

# Path to a style sample or style notes (markdown). Optional if you use `style:` instead.
style_path: 

# Inline style notes. Used when style_path is empty.
style: |

# Who reads this, what they already know, what they should leave with. Required.
audience: 

# Absolute directory where article folders are created. Required.
export_dir: D:\YourFolder\Notes\ai\insights-to-share

# Relative to export_dir. `{slug}` comes from today's task slug
# (e.g. cpe-df-ship-article-flow → df-ship-article-flow or a shorter slug you confirm).
export_slug_pattern: "pub-{slug}/{slug}.md"

# Relative to export_dir. Cover + inline images land here.
images_dir_pattern: "pub-{slug}/imgs"

# Illustration budget
cover: true
max_inline_images: 4
illustrate_confirm: false          # ship passes "按默认出图 / 跳过确认" to baoyu skills
illustrate_timebox_min: 45         # on timeout: drop inline images first, keep cover
```

## Notes

- First draft is written to **both** the task file `## Outcomes` (frozen as v1 for
  calibration) and the resolved export path (the only file you edit afterward).
- After publish, put platform URLs into the task frontmatter `wechat` / `zhihu` /
  `juejin` / `bilibili` so the next morning's `df plan` can collect feedback in one place.
- Edit patterns learned from v1→final diffs live in `local.article.memory.md`
  (also gitignored), not in this file.
