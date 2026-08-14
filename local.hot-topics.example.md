# local.hot-topics (example)

Copy to `local.hot-topics.md` (gitignored) or point `HOT_TOPICS_FILE` at another gitignored path.

`df plan` may refresh this file after you answer `plan.q_hot`. **Every topic row needs a URL.** Empty source → `未取到`. Invented trends are forbidden.

```markdown
# Hot topics

- updated: 2026-01-01
- span: last 7 days
- query: AI (adjust locally; do not commit real queries into the open skill)

## douyin
- 未取到

## zhihu
- 未取到

## x
- 未取到

## youtube
- 未取到
```

Row shape when a source hits:

```markdown
- [short title](https://example.com/item) — one-line why it matters for this week's goalStep
```
