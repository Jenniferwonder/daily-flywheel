# Mode: review (close yesterday)

Closes out **yesterday's main task** before any morning planning. Owns publish-link sync, feedback capture, ladder checkmarks, and optional focus tweaks on the objective note.

User-facing strings: `references/i18n.md` keys under `## review` for `LANGUAGE`.

Read, in this order:

1. `local.config.md` (vault paths, `PUBLISH_SLOTS`)
2. Yesterday's daily note — resolve the **main task** from `## Actions` (`- 任务：[[...]]`). If that line is missing, treat as no yesterday task: show `review.no_yesterday_task`, set nothing, exit (morning `df plan` may proceed).
3. That task file (frontmatter + `## Actions` / `## Outcomes` / `## Review`)
4. `{{DAILY_VAULT}}\{{OBJECTIVE_FILE}}` — ladders, immutable Baseline, `## Latest Snapshot` (create section if missing), `## This Week` / `## This Month`
5. Optionally yesterday's export-path article frontmatter under `{{NOTES_VAULT}}\ai\insights-to-share\` (filenames / YAML only)

**Privacy hard rule:** thresholds, counters, account names, and ladder cell text live only in the vault objective note (and gitignored local configs). Never copy those values into this repository, chat summaries destined for PRs, or example files. In chat, prefer “阶梯第 N 格已勾” over repeating raw totals when a screen-share risk exists.

**Daily note writes (minimal):** do **not** copy Review prose into the daily. If yesterday's daily `## Actions` still has `- [ ]` / `- [x]` checkbox lines (legacy duplicate of the task), **strip those lines** and leave header aggregation only — optionally keep/add `待办：只在任务卡…`. Do not rewrite week/month mirror Focus here — `df plan` Step 0c still owns mirrors after any objective edit.

## Step 0 — Sync publish links (silent)

1. Locate yesterday's article/script from task `## Outcomes` (`终稿路径`) or a shallow `pub-*` / `script-*` directory match (see `conventions.md` scoped scans).
2. Read only frontmatter keys listed in `PUBLISH_SLOTS`.
3. If a URL is non-empty and the task YAML field is empty or a non-URL placeholder: write it into the task.
4. If still empty: note `发布链接: 文章 frontmatter 仍空` under task `## Review` and include a fill-in ask in Step 1. Never invent URLs.

## Step 1 — One question block

Ask once (`review.q_block` for `LANGUAGE`), then wait.

Day one / no publishable output: drop items that do not apply rather than forcing “none”.

## Step 2 — Write task `## Review` (SSOT)

Write **only** into yesterday's main task:

- 完成率 / 耗时偏差 / 一句话自评 / `ToImprove::`
- Feedback numbers verbatim (first 7 days: say `review.feedback_no_analysis`; no trend argument until day 8+)
- Publish-link notes (if any)
- Prose in `LANGUAGE`; keep field labels (`ToImprove::`, etc.) per conventions

Set frontmatter `reviewed: YYYY-MM-DD` to **today** (the day review ran). Optionally set `DateReviewed` to the same date if the vault uses that field.

Parent backlog files are **not** required to receive `reviewed`.

## Step 3 — Latest Snapshot + auto ladder

On `{{OBJECTIVE_FILE}}`:

1. Upsert `## Latest Snapshot` with today's date and the absolute counters from Step 1 (columns should match the note's own Baseline shape — do not invent a second schema in this repo).
2. Compute net change against the **immutable** Baseline row in that note.
3. For each unchecked ladder cell in `## Milestones`, if the Snapshot now meets that cell's threshold **as written in the note**, check it `[x]` and add a one-line dated note under the objective `## Review` (or Snapshot footnote). Do not invent new rungs.
4. Never edit Baseline historical rows.

If the user cannot provide counters today, skip Snapshot refresh and ladder checks; still write task Review + `reviewed` so `df plan` can proceed.

## Step 4 — Optional focus optimization (triggered, then confirmed)

**Trigger** (any one). Do not propose every day:

- A ladder cell was newly checked in Step 3
- Completion rate on yesterday's plan was low, or the declared `goalStep` did not move
- No `article` / `script` deliverable shipped yesterday when `## This Week` expected one
- (Only after ≥7 flywheel days with feedback) engagement trend suggests a focus change

**First 7 days** since capability (or objective) `DateStarted`: argue triggers using **controllable process only** (completion, time bias, goalStep movement, pub/script shipped). Do not use like/read/follower *trends* as justification. Auto-checking a ladder when a threshold is met is allowed — that is arithmetic, not trend analysis.

When triggered, present **1–3** direction candidates (lead with `review.opt_prompt`). Table in `LANGUAGE` with `goalDim` + `goalStep` + one-line why. Wait for pick **0 / 1 / several**, or keep/none.

On confirmation only:

- Overwrite or amend `## This Week` with the chosen items (dates + deliverables + goalDim/goalStep)
- Amend `## This Month` only when the user explicitly agrees the month focus must change
- **Never** edit `## This Year` in this mode

Then say one line: morning `df plan` will read the updated objective before proposing today.

## Step 5 — Close

Chat summary only: reviewed task link, whether Snapshot/ladders moved, whether This Week changed. No essay.

If the user still needs today's plan, tell them to run `df plan` next (hard-gated on `reviewed`).
