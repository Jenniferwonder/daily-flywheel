# Mode: ship (evening — draft only)

Marks what got done and writes the **v1 draft snapshot** plus the editable working copy. Does **not** critique, illustrate, calibrate, or hand off publish slots — those are `df comment` / `df final`.

**Manual only:** this mode runs only on explicit user request (`df ship` / 写出来 / 收工 / 生成文章). No other mode auto-triggers article generation — `study`, `plan`, and `review` never call ship.

User-facing strings: `references/i18n.md` keys under `## ship`. Draft body language: `draft_language` in article config, else `LANGUAGE`.

## Step −1 — Resolve target day

Per `conventions.md` **Target day**: parse optional date from the trigger (`df ship`, `df ship yesterday`, `df ship 2026-08-07`). Default = calendar today. Announce `shared.target_announce`. Stop with `shared.target_missing` if that daily note / main task is absent.

Read, in this order:

1. `local.config.md`
2. `local.article.config.md` — **required** when the **target day's** `deliverable` is `article` (or the plan is clearly a `pub-*` article). Also read `positioning` / `personas` / `taboos` / `term_map` when present.
3. `local.article.style.md` (or `style_path` if it already points at a **short** distilled file). **Do not** open long sample essays on every ship. If the style file is missing, use inline `style:`. If `style_path` resolves to a full sample post (long narrative, many screenshots), ignore it and use `local.article.style.md` or inline `style:`.
4. `references/article-craft.md` — **comment/scorecard rules** (funnel, Why≥3, title formula, 3-second open, chunks). These are the same bars `df comment` scores.
5. `local.article.memory.md` if it exists — **all** active rules (incremental; no 7-rule cap). Skip a rule that duplicates or contradicts a higher-priority source.
6. **Target day's** daily note and its main task file

**Draft priority (high → low, on conflict):** house style → `df comment` / article-craft bars → calibration memory. Memory never overrides style or comment bars.

Do not read further back than needed for that day.

**Hot topics:** do **not** scrape platform trending during `df ship`. If the draft needs a heat hook, read `HOT_TOPICS_FILE` as filled by `df plan` (AI-themed rows only). No AI row → skip the hook; never substitute music/gaming/celebrity trending.

### Existing v1 gate

If the target task `## Outcomes` already has frozen v1 prose: **stop** unless the user explicitly said overwrite / 重写 v1. Show `ship.v1_exists` and point them to `df comment <same date>` / `df final <same date>`. On explicit overwrite: replace Outcomes v1, append one Review line that prior v1 was discarded, then continue.

## Step 0 — Load article config (articles only)

Skip when `deliverable: script` or `other` with no companion article.

If `local.article.config.md` is missing, or any of `audience` / `export_dir` /
`export_slug_pattern` is empty:

1. Stop. Do not draft.
2. Tell the user to copy `local.article.config.example.md` → `local.article.config.md`
   and fill the required keys.
3. Exit ship.

Resolve:

| Key | Role |
|-----|------|
| `ship_policy` | `quality` \| `time` \| `hybrid` (default `hybrid`) |
| `style_path` / `style` | Distilled house style (`local.article.style.md`); not a full sample essay |
| `positioning` / `personas` / `taboos` / `term_map` | Voice + bans + jargon glosses |
| `audience` | Reader brief |
| `export_dir` + `export_slug_pattern` | Working markdown path |
| `images_dir_pattern` | Noted for later `df final`; unused here |

Confirm `{slug}` if ambiguous (default: task filename minus `cpe-` / `te-` / `pm-`).

### `ship_policy` when time is short

- **hybrid** (default): shorten before shipping; if still below bar, use Step 2 branches. Never pad.
- **quality**: if a short piece still fails the bar, mark unfinished and do not draft a fake complete article.
- **time**: must produce something linkable; enforce only the minimum bar from config/memory.

Principle: **do not sacrifice quality to fill time — compress length instead.**

## Step 1 — Collect status

One question: `ship.q_status` for `LANGUAGE`. Map answers via `ship.branch_*` (accept either language).

Mark checkboxes in the **target day's task file only** with `✅` = **calendar today**. Leave unfinished items. Do **not** add or sync checkbox lines on the daily note (daily `## Actions` stays header-only). Record actual elapsed time under task `## Review` (short; full retro is `df review`).

## Step 2 — Decide what is draftable

- **done** — draft as planned (`article` / `script`).
- **half-done** — offer: smaller honest slice, or a “stuck where” post/script; do not pretend completion.
- **changed direction** — draft about what was abandoned and why (still prefer pub-/script-).
- **did nothing** — do not generate. Ask `ship.ask_why_idle` → `ToImprove::` on the task → stop. **Skip** comment/final for this run.

Never draft a deliverable not backed by the **target day's** work.

## Step 3 — Write the draft (dual-write)

### `deliverable: other` (rare)

`## Outcomes` records repo/commit link, what was built, one design decision. No export article required. Stop after write-back; no comment/final expected.

### `deliverable: script`

Write the script package (title / spoken lines / shots or screen-record notes / CTA) to the export path from article config **or** the path agreed in the task Purpose (e.g. under `insights-to-share` with a `script-` slug). Dual-write the same bytes to task `## Outcomes` as frozen v1.

### `deliverable: article`

**Topic gate (articles, hard — never auto-draft):** After status is `done` / `half-done` / `changed direction`, do **not** write the article body yet. Run these gates in order, waiting for confirmation at each:

1. **定题 (brainstorm).** Use the `brainstorming` skill when available to sharpen the topic: propose today's one topic sentence + why it is the highest-value finishable piece from **today's Actions**. User confirms or revises.
2. **大纲 (outline).** After the topic is confirmed, build a short outline (spine + chapter list). Use the `writing-assistant` skill when available (its outline bars: a “why” section with ≥3 reasons, 3–5 scenarios covering ≥3 personas, a specific/credible/attractive promise, ≤15 chapters). User confirms or revises.
3. **Draft.** Only after topic AND outline are both confirmed, write the v1.

Generating several full drafts to “see which one lands” is forbidden. If the `brainstorming` / `writing-assistant` skills are unavailable, run the same gates with the built-in bars (`article-craft.md`).

Write markdown, first person, sized under `ship_policy`. **流程短文** prefer 1500–2500 characters of substance when time allows. **深度长文**（house style「何时用哪一套」）不压这个字数；长度 = 跳过共识后仍能指到文件的机制。

Inject: config voice (`taboos`, `term_map`), then house style, then comment/scorecard bars, then memory (style wins on conflict).

v1 skeleton (`article-craft.md` — pick 流程短文 or 深度长文; do not drop that skeleton's required slots under hybrid):

- 流程短文：Title → 3-second open → Why≥3 / Fit / How / Next → 5–7 line chunks
- 深度长文：对象+跳过共识+切口 → 一句脊柱 → 一章一机制（动机/源码/差异/所以呢）→ 机制映射回产品问题。Do not force the funnel.

Hard rules: no 随着…的发展 / 在当今…时代 / 众所周知; every claim has evidence from **today's Actions / Outcomes** (hot-topic URLs may illustrate a pull, not stand in for work); no news recap of `HOT_TOPICS_FILE` with no lived step; no empty heading scaffolding; keep the user's voice; honor `taboos`.

**Dual-write (same bytes, once):**

1. Task `## Outcomes` — **v1 frozen**. Do not edit the prose again (later modes may only append 终稿路径 / 配图目录 / 发布链接).
2. Export path — **only working copy** for human edits, `df comment`, and `df final`.

Show the draft in chat. State the export path as the edit target.

## Step 4 — Write-back + handoff

Task:

- `status: 🟡Doing` until `df final` (or `🟢Done` for `other` with Outcomes only)
- `DateModified` / `DateDone` (when setting Done) = **calendar today**
- Ensure `deliverable` is set

Target-day daily: leave `## Actions` headers alone (no checkbox writes). Leave `## Review` for Dataview / `df review`.

Close with `ship.closer` for `LANGUAGE` (mention same target date for follow-up `comment` / `final` when not today).

Do not critique, illustrate, upload OSS, calibrate, or collect publish URLs in this mode.
