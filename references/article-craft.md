# Article craft (abstract)

Generic writing slots used by `df plan` / `df ship` / `df comment`. **No private voice, audience, or hot-topic titles here.** Those live in gitignored local files.

Private files (never commit):

| File | Read by |
|------|---------|
| `local.article.config.md` | voice / 禁区 / 术语降维 / audience |
| `local.article.style.md` | distilled house style (`df ship` — do **not** re-read long sample articles) |
| `local.article.memory.md` | v1→final calibration rules (`df ship` + `df final`) |
| `{{HOT_TOPICS_FILE}}` | last-7-day sourced topics (`df plan`) |

Script days do **not** read this file. Their outline bars live in gitignored `script-craft.md`.

## Plan — three-way filter (not per-candidate web counts)

A candidate is valid only if **all three** are non-zero:

1. **Who** — a reader already named in config `audience` / 人设
2. **Situation** — a named action from **today's task** (or work already done today) that this deliverable will report. `## This Week` / hours size it; a hot-topic row alone is **not** Situation.
3. **Information increment** — new vs Covered Topics / existing `pub-*` (vault dedup). Same topic + new angle is OK; slogan restatement is not.

Do **not** count how many posts exist on a platform per candidate. **Reject** a news recap whose spine is a hot-topic row the user did not work on today.

### Hot topics (`df plan`)

1. Include `plan.q_hot` in the one question block.
2. After the reply: if the user said **yes**, or the hot-topics file is **missing**, or `updated` is **older than 7 days** (user may still say **no** to skip): prefer **TrendRadar** (`TRENDRADAR_DIR` under `CODESPACE_DIR`; `scripts/trendradar_hot_topics.py` or MCP `search_news`) for zhihu / douyin / bilibili. Then apply the skill AI needle. WebSearch **AI-themed** topics for `x` / `youtube` / `google` (Google = News/Trends/search hits with a URL). If TrendRadar fails, also WebSearch douyin / zhihu. Every query must include `AI` / `人工智能` (or a named AI product). General trending (music, gaming, celebrity, sports) does **not** count — that source is `未取到` / `not found`. Write **only URL-backed AI rows**. Never invent a title or link. Clone TrendRadar only into `CODESPACE_DIR`.
3. Why-today must cite **goalStep** and **today's named action**. A URL-backed hot-topics row may season the angle; if none, say `无可用热点，只服务本周格子` / `no usable hot topic — week cell only`. Hot topics never replace today's action as the spine.
4. Never paste hot-topic titles into this repository.

## Ship — v1 skeleton (one status question, then draft)

**Topic gate first** (house style / memory): propose today's topic sentence + outline and wait for confirm before drafting. Then pick **one** skeleton from house style「何时用哪一套」.

### 流程短文（默认）

1. **Title** — number contrast × curiosity × low jargon (mom-test). Prefer a concrete before/after over a vague multiplier.
2. **Open (3 seconds)** — pain / contrast / counter-intuitive fact. No 随着…发展 / 在当今…时代 / 众所周知.
3. **Funnel**
   - 认知 / Why: a dedicated stretch with **≥3 reasons** (problem, payoff, why now)
   - 兴趣 / Fit: 2–4 scenes the reader might be in
   - 决策 / How: steps with evidence from **today's work** (named Actions / Outcomes). Do **not** draft a recap of `HOT_TOPICS_FILE` that the user did not do today.
   - 行动 / Next: one copyable next step
4. **Chunks** — one idea per block, about 5–7 lines; split if longer.
5. **Terms** — first paragraph has no unexplained jargon; later terms get a one-line gloss from config 术语降维.

### 深度长文（机制 / 拆解 / 源码）

House style「深度长文」节覆盖漏斗。Bake this instead:

1. **Title** — 拆解 / 从 0 到 1 / 真正不一样的几处 × 具体对象
2. **Open** — 对象 + 官方关键词；点名并跳过共识；列出本文只拆的 3–6 处；可选「只比差异」。不要「大家好 + 前几篇工作流」
3. **Spine** — one engineering question; every chapter answers it
4. **Chapters** — 一章一个机制：动机 → 源码/伪代码 → 和常见方案差在哪 → 所以呢。Evidence from **today's** clone / 本机实跑 / 文件路径
5. **Close** — 机制映射回 3–4 个产品问题 + 诚实边界；已发微信链接放文末

6. Honor config **禁区**. Draft priority (high → low): `local.article.style.md` → this file's comment/scorecard bars → `local.article.memory.md`. Memory is incremental (no 7-rule cap); skip duplicates or contradictions with a higher source. Do not draft until the topic gate is confirmed.

Hybrid timebox: 流程短文 shorten scenes and examples, **do not drop** Why-with-3-reasons or the open. 深度长文 shorten by dropping chapters that lack file-path evidence, **do not** compress back into a funnel tutorial.

## Comment — scorecard (advisory)

Score the **hand-edited** export file. Show percent + failed boxes. **Does not block** `df final`.

| Area | Checks |
|------|--------|
| Topic | three-way match readable; increment vs prior pubs |
| Outline | 流程短文：Why + ≥3 reasons + funnel。深度长文：一句脊柱 + 一章一机制，不套漏斗 |
| Body | 流程短文：3-second open；chunks；terms glossed。深度长文：跳过共识；代码/路径当证据；类比只定向 |
| Title | number or contrast; low jargon |
| Layout | H1–H3 only; lists paste-friendly; processes visualized (ASCII OK) |

≥80% → recommend publish. 60–79% → list fixes. <60% → recommend rewrite. Always still run the four-line critique (`comment.labels`).
