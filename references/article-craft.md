# Article craft (abstract)

Generic writing slots used by `df plan` / `df ship` / `df comment`. **No private voice, audience, or hot-topic titles here.** Those live in gitignored local files.

Private files (never commit):

| File | Read by |
|------|---------|
| `local.article.config.md` | voice / 禁区 / 术语降维 / audience |
| `local.article.style.md` | distilled house style (`df ship` — do **not** re-read long sample articles) |
| `local.article.memory.md` | v1→final calibration rules (`df ship` + `df final`) |
| `{{HOT_TOPICS_FILE}}` | last-7-day sourced topics (`df plan`) |

## Plan — three-way filter (not per-candidate web counts)

A candidate is valid only if **all three** are non-zero:

1. **Who** — a reader already named in config `audience` / 人设
2. **Situation** — a trigger the user actually has this week (`## This Week` or today's hours)
3. **Information increment** — new vs Covered Topics / existing `pub-*` (vault dedup). Same topic + new angle is OK; slogan restatement is not.

Do **not** count how many posts exist on a platform per candidate.

### Hot topics (`df plan`)

1. Include `plan.q_hot` in the one question block.
2. After the reply: if the user said **yes**, or the hot-topics file is **missing**, or `updated` is **older than 7 days** (user may still say **no** to skip): WebSearch the four sources named in `local.hot-topics.example.md` (AI topics, last ~7 days). Write **only rows with a URL**. If a source returns nothing, write `未取到` / `not found` for that source. Never invent a title or link.
3. Why-today must cite **goalStep** and **one row from the hot-topics file**, or explicitly `无可用热点，只服务本周格子` / `no usable hot topic — week cell only`.
4. Never paste hot-topic titles into this repository.

## Ship — v1 skeleton (one status question, then draft)

Do **not** confirm an outline in a second turn. Bake this into the draft:

1. **Title** — number contrast × curiosity × low jargon (mom-test). Prefer a concrete before/after over a vague multiplier.
2. **Open (3 seconds)** — pain / contrast / counter-intuitive fact. No 随着…发展 / 在当今…时代 / 众所周知.
3. **Funnel**
   - 认知 / Why: a dedicated stretch with **≥3 reasons** (problem, payoff, why now)
   - 兴趣 / Fit: 2–4 scenes the reader might be in
   - 决策 / How: steps with evidence from **today's work**
   - 行动 / Next: one copyable next step
4. **Chunks** — one idea per block, about 5–7 lines; split if longer.
5. **Terms** — first paragraph has no unexplained jargon; later terms get a one-line gloss from config 术语降维.
6. Honor config **禁区**. Honor `local.article.style.md` + **memory** (memory wins on conflict with style).

Hybrid timebox: shorten scenes and examples; **do not drop** Why-with-3-reasons or the open.

## Comment — scorecard (advisory)

Score the **hand-edited** export file. Show percent + failed boxes. **Does not block** `df final`.

| Area | Checks |
|------|--------|
| Topic | three-way match readable; increment vs prior pubs |
| Outline | Why section + ≥3 reasons; funnel present |
| Body | 3-second open; chunks; terms glossed; evidence |
| Title | number or contrast; low jargon |
| Layout | H1–H3 only; lists paste-friendly; processes visualized (ASCII OK) |

≥80% → recommend publish. 60–79% → list fixes. <60% → recommend rewrite. Always still run the four-line critique (`comment.labels`).
