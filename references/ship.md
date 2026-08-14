# Mode: ship (evening — draft only)

Marks what got done and writes the **v1 draft snapshot** plus the editable working copy. Does **not** critique, illustrate, calibrate, or hand off publish slots — those are `df comment` / `df final`.

User-facing strings: `references/i18n.md` keys under `## ship`. Draft body language: `draft_language` in article config, else `LANGUAGE`.

## Step −1 — Resolve target day

Per `conventions.md` **Target day**: parse optional date from the trigger (`df ship`, `df ship yesterday`, `df ship 2026-08-07`). Default = calendar today. Announce `shared.target_announce`. Stop with `shared.target_missing` if that daily note / main task is absent.

Read, in this order:

1. `local.config.md`
2. `local.article.config.md` — **required** when the **target day's** `deliverable` is `article` (or the plan is clearly a `pub-*` article). Also read `positioning` / `personas` / `taboos` / `term_map` when present.
3. `local.article.style.md` (or `style_path` if it already points at a **short** distilled file). **Do not** open long sample essays on every ship. If the style file is missing, use inline `style:`. If `style_path` resolves to a full sample post (long narrative, many screenshots), ignore it and use `local.article.style.md` or inline `style:`.
4. `local.article.memory.md` if it exists (recent 7 rules — still apply while drafting; **memory wins** over style)
5. **Target day's** daily note and its main task file
6. `references/article-craft.md` for the v1 skeleton

Do not read further back than needed for that day.

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

Write markdown, first person, sized under `ship_policy` (prefer 1500–2500 characters of substance when time allows). **One status question, then draft** — do not confirm an outline in a second turn.

Inject: config voice (`taboos`, `term_map`), `local.article.style.md`, recent **memory** rules (memory wins).

v1 skeleton (`article-craft.md` — do not drop slots under hybrid; shorten examples instead):

1. Title: number/contrast × curiosity × low jargon
2. Open (3 seconds): pain / contrast / result-first
3. Funnel: Why (≥3 reasons) → Fit (scenes) → How (today's evidence) → Next (one step)
4. Chunks ~5–7 lines; first paragraph has no unexplained jargon

Hard rules: no 随着…的发展 / 在当今…时代 / 众所周知; every claim has evidence; no empty heading scaffolding; keep the user's voice; honor `taboos`.

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
