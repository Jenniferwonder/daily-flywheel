# Conventions

Every path, schema, and constraint the flywheel depends on. Read this before any mode.

This file is the structural contract between the skill and the vault. It describes one concrete working layout rather than an abstract one, because a vague contract produces vague files. If your vault is organised differently, fork this file — that is the intended way to adapt the skill. The keys in `local.config.md` cover locations only, not layout.

Paths below use the placeholders resolved from `local.config.md`: `{{DAILY_VAULT}}`, `{{NOTES_VAULT}}`, `{{OWNER}}`.

## Language

| Key | Where | Role |
|-----|-------|------|
| `LANGUAGE` | `local.config.md` | `zh` \| `en` — chat + generated **prose** (default `zh`) |
| `draft_language` | `local.article.config.md` | Article/script body language; default = `LANGUAGE` |

User-facing prompt catalog: `references/i18n.md`.

**Not localized** (schema stability / Dataview / Tasks): `## Actions`, `## Review`, `## Outcomes`, `ToImprove::`, `维度::`, `目标格::`, frontmatter key names, Tasks emoji dates, and fixed path footnotes like `终稿路径` / `配图目录` when already used in the vault. If `LANGUAGE=en`, agents may add an English gloss in chat but must keep those keys in files.

## Target day (`df ship` / `comment` / `final`)

These three modes operate on a **target day** (the daily note whose `## Actions` to close out), which may differ from the **calendar today** (when the command runs).

**Resolve target day from the trigger phrase:**

| Input | Target day |
|-------|------------|
| omitted / bare `df ship` | calendar today |
| `YYYY-MM-DD` | that date |
| `today` / `今天` | calendar today |
| `yesterday` / `昨天` | calendar today − 1 day |

Examples: `df ship 2026-08-07`, `df comment yesterday`, `df final 昨天`. Ignore fuzzy weekday phrases; ask for an explicit date instead.

**Path:** resolve the daily note under `Daily\YYYY\YYYY-Qn\YYYY-MM\YYYY-Www\YYYY-MM-DD.md` for the **target** date (ISO week under Monday's month). Main task = that note's `## Actions` line `- 任务：[[...]]`.

**If the target daily note is missing** (or has no main task link): **stop**. Show `shared.target_missing`. Do **not** create an empty daily note.

**Stamps vs reads:**

| Write | Which date |
|-------|------------|
| Read/edit daily + task files | **target day** |
| Tasks `✅`, task `DateDone` / `DateModified`, `commented` stamp | **calendar today** (honest execution day) |

Always say one line at start: `Target day: YYYY-MM-DD` (`shared.target_announce`).

## The two vaults

| Vault | Placeholder | Role |
|-------|-------------|------|
| Daily | `{{DAILY_VAULT}}` | All flywheel state: daily notes, tasks, projects, output. Everything this skill writes goes here. |
| Notes | `{{NOTES_VAULT}}` | An existing body of technical notes. **Read-only for this skill.** Used only to avoid recommending a topic already written. Optional — skip dedup if unset. |

## Scoped scan commands

Never substitute a broader scan. On a cloud-synced or network drive a depth-2 recursive listing can take ~50 seconds.

```powershell
# Notes already written on the relevant subject (dedup source).
# Point this at the topic subtree you actually write about, not the vault root.
Get-ChildItem -LiteralPath "{{NOTES_VAULT}}\ai" -Recurse -Filter *.md -Name

# Yesterday's publishable articles / scripts (for df review link sync). Shallow.
Get-ChildItem -LiteralPath "{{NOTES_VAULT}}\ai\insights-to-share" -Directory -Filter "pub-*" -Name
Get-ChildItem -LiteralPath "{{NOTES_VAULT}}\ai\insights-to-share" -Directory -Filter "script-*" -Name
# Then read frontmatter of the matched */*.md — not the body.

# Existing and finished tasks (flat, fast)
Get-ChildItem -LiteralPath "{{DAILY_VAULT}}\Tasks\New\Backlog" -Filter *.md -Name
Get-ChildItem -LiteralPath "{{DAILY_VAULT}}\Tasks\New\Completed" -Filter *.md -Name

# Recent daily notes — year / quarter / month / ISO-week tree (on content only)
# Example current week: Daily\2026\2026-Q1\2026-03\2026-W10\
Get-ChildItem -LiteralPath "{{DAILY_VAULT}}\Daily\YYYY" -Directory -Filter "YYYY-Q*" -Name
Get-ChildItem -LiteralPath "{{DAILY_VAULT}}\Daily\YYYY\YYYY-Qn\YYYY-MM\YYYY-Www" -Filter *.md -Name
```

Week folder placement: ISO week, hung under the month that contains that week's **Monday**. Do not create empty month/week review stubs.

Weekly review note: `Daily\YYYY\YYYY-Qn\YYYY-MM\YYYY-Www\YYYY-Www.md`  
Monthly review note: `Daily\YYYY\YYYY-Qn\YYYY-MM\YYYY-MM.md`  
Templates: `Templates\Tp-Daily\tp-Weekly.md`, `Templates\Tp-Daily\tp-Monthly.md`  
`df plan` creates/fills these on ISO Sunday / calendar month-end (see `plan.md` Step 0b). Agent-written week/month notes must be fully rendered — no Templater markers. Daily close-out is `df review` (task SSOT), not `df plan`.

Filenames only. Do not read note bodies from the Notes vault; titles plus the dedup list are enough to tell whether a topic is already covered.

`draft: true` is the default in most templates and is therefore **not** a signal of an unfinished stub. To find real stubs, use `status` (empty or `🟡Doing`) and file size, not `draft`. Check this assumption against your own vault before relying on any frontmatter field as a signal — a field that is always the same value carries no information.

## Note types

The `type` field classifies every note and drives the Dataview rollups:

| Type | Meaning |
|------|---------|
| `P` | Project — has deliverables and a finish line |
| `T` | Task — a single unit of work, lives under `Tasks/` |
| `O` | Topic hub note — a long-running area with no finish line, e.g. a language or a discipline |
| `S` | Learning resource / reference collection |
| `D` | Concept or specification note |
| `A` | Action or README-style note attached to a project |

The distinction that matters most here is `P` versus `O`: anything with milestones and a completion state is `P`, anything accumulated indefinitely is `O`. Area hub rollup queries typically accept both.

## Dates

- Daily note filename and all date fields: `YYYY-MM-DD`
- Week link: `YYYY-Www` using the **ISO** week number, e.g. 2026-03-05 falls in `[[2026-W10]]`

```powershell
# Resolve today's date and ISO week before writing any file
$d = Get-Date
$d.ToString('yyyy-MM-dd')
"{0}-W{1:D2}" -f $d.Year, [System.Globalization.ISOWeek]::GetWeekOfYear($d)
```

- Sprint field format in this layout is `YY-MM-A`, e.g. `26-03-A`. This is an example of one convention, not a requirement. If a task created this month already uses a different suffix, match it rather than inventing one.

## Daily note

Path (aligned with `Daily/2023` layout):

`{{DAILY_VAULT}}\Daily\YYYY\YYYY-Qn\YYYY-MM\YYYY-Www\YYYY-MM-DD.md`

Resolve `Qn` / `MM` / `Www` from the note's date: ISO week number, week folder under the month of that week's Monday, quarter from that month. Create intermediate folders as needed. Year-level files (`YYYY.md`, `DB-Daily-YYYY.md`) stay in `Daily\YYYY\`.

Source template: `{{DAILY_VAULT}}\Templates\Tp-Daily\tp-Daily Plan.md`

If the file already exists, fill its empty sections and leave everything else alone. If it does not, write it fully rendered — every template expression resolved to a literal, none surviving. Rendered shape for 2026-03-05, substituting the real date everywhere:

````markdown
---
title: Daily Plan
tags:
  - Daily
DateStarted: 2026-03-05
DateModified: 2026-03-05
---
# Daily Plan
- Week:: [[2026-W10]]
- Next:: 
## Tasks
### Due
```tasks
not done
due before in 5 days
sort by due
```
### Todo
```tasks
not done
happens on 2026-03-05 
sort by due
```
### Done
```tasks
done
(done on 2026-03-05)
```

## Actions
_焦点头信息由 `df plan` 写入；待办 checkbox 只在任务卡 `## Actions`，本区不重复（上方 Todo / Done 查询聚合）。_
## Review
_复盘正文、反馈数字、ToImprove 写在当日主任务 `## Review`（`df review`）。本区只做聚合。_

```dataview
TABLE reviewed, commented, deliverable, status, goalDim, goalStep
FROM "Tasks/New"
WHERE DateStarted = date(2026-03-05) OR DateDone = date(2026-03-05)
SORT file.mday DESC
```

### ✍️New Notes

```dataview
TABLE title, DateStarted, status
WHERE DateStarted = date(2026-03-05)     
SORT file.mday DESC
```
### ✅ Tasks Done
```dataview
TABLE title, DateStarted, status
WHERE DateDone = date(2026-03-05)     
SORT file.mday DESC
```
### 📝Modified Notes

```dataview
TABLE title, DateStarted, status
WHERE file.cday != date(2026-03-05) AND DateModified = date(2026-03-05)
SORT modified ASC
```
````

The flywheel writes into `## Actions` (**plan headers only**). Checkbox todos live **only** on the task file `## Actions`; the daily note must not duplicate them (Tasks Todo/Done queries already aggregate by date). `## Review` is **Dataview-first**: `df review` does not copy prose into the daily note. Keep the Tasks query blocks; they populate themselves.

`## Actions` header lines are the day-level end of the focus cascade:

```markdown
- 今日产出：<one line>
- 任务：[[<task file>]]
- 维度:: `leverage`
- 目标格:: `<ladder cell>`（`{{OBJECTIVE_FILE}}` 本月焦点第 N 条）
- 目标文件：[[<objective note>]]（能力底座 [[<capability note>]]）
- 周/月：[[YYYY-Www]] · [[YYYY-MM]]
- 时间预算：2 小时（硬上限）
- 待办：只在任务卡 `## Actions`；本区不重复 checkbox
```

`维度::` and `目标格::` use Dataview inline-field syntax on purpose, so a day can be rolled up by dimension later. They must match the task file's `goalDim` / `goalStep` exactly.

**Files can be truncated by something outside this skill.** Observed once during development: a set of files across both the vault and the skill directory were touched in the same instant and several were left at 0 bytes, including two reference files and two task files. Tracked files were recovered with `git checkout --`; untracked ones were unrecoverable and had to be rewritten. Practical consequence: commit skill edits soon after making them, and treat a 0-byte read of a file you just wrote as external truncation rather than your own error.

**Writing about template syntax inside a vault file.** An article or note that needs to discuss template placeholders cannot contain a bare open-marker, even inside backticks. Observed twice during development: the sequence was silently deleted on one write and auto-closed into an empty pair on the next. The responsible plugin was not isolated — Linter and Templater are both plausible. Refer to it as 占位符 / placeholder in prose rather than reproducing the literal syntax.

**A live Obsidian instance rewrites agent edits.** Linter strips trailing whitespace after empty YAML values; `update-time-on-edit` rewrites `DateModified`. A one-line change can show up as a twenty-line diff. This is normal, not corruption.

## Task file

Path: `{{DAILY_VAULT}}\Tasks\New\Backlog\<prefix>-<slug>.md`
Source template: `{{DAILY_VAULT}}\Templates\tp-task.md`

Prefixes: `cpe-` for a content deliverable, `te-` for technical learning, `pm-` for workflow or meta work. One task file per day's deliverable.

Frontmatter, in this field order (this is the order Obsidian Linter normalizes to, so matching it avoids churn):

```yaml
---
category: AI
tags:
  - AI
  - Content-Making
DateReviewed: 
reviewed: 
commented: 
difficulty: 
comment: 
draft: true
# one empty key per name in PUBLISH_SLOTS (local.config.md), e.g.:
pub_a: 
pub_b: 
pub_c: 
title: cpe-<slug>
owner: {{OWNER}}
type: T
project: CPE
goalDim: <dimension from 维度字典>
goalStep: <ladder cell, copied verbatim>
deliverable: article
blockedBy: 
sprint: 26-03-A
points: 
priority: 
DateStarted: 2026-03-05
DateDone: 
DateModified: 2026-03-05
status: 🟡Doing
PointsDone: ""
---

# cpe-<slug>

## Purpose
## Reference

## Actions

## Outcomes

## Review
```

Field notes:

- `status` uses the Kanban board's exact values: `⚪Todo`, `🟡Doing`, `🟢Done`, `🟤Blocked`. Any other string breaks the board.
- `tags` drives every Dataview rollup. Tag with the subject area to surface under that area's hub note; tag with the content-publishing area to surface under the publishing project. A daily deliverable usually wants both.
- `category` and `project` are matched by the same Dataview queries.
- `DateStarted` set to today makes the task appear in the daily note's "New Notes" table.
- `DateDone` set on completion makes it appear in "Tasks Done" and lets the weekly and monthly rollups count it.
- Publish URL keys are whatever `PUBLISH_SLOTS` lists in `local.config.md`. Leave each empty until published, then store the URL. Never hardcode slot names into this repository.
- **`goalDim` is a hard gate.** It must be one of the dimensions the user declared in the `## 维度字典` section of `{{OBJECTIVE_FILE}}` — typically one or two result dimensions plus `leverage` (makes results cheaper or faster) and `capability` (the skill base). This repository does not define the result dimensions; read them from the note. Refuse to create a task file without a valid value.
- **`goalStep` names the exact ladder cell or month-focus item** it advances, copied verbatim from the objective note. It must contain a number, a date, or a named artifact. A slogan or uncheckable phrase with no number/date/artifact is treated as missing: ask the user which cell, do not invent one.
- **`deliverable`**: `article` | `script` | `other`. Set by `df plan`. Drives whether `df final` illustrates (`article`) or skips images (`script`). Prefer `article`/`script` every day.
- **`reviewed`**: date string set by `df review` when yesterday's close-out is written. Empty → `df plan` hard-stops. Value is the day review ran.
- **`commented`**: date string set by a successful `df comment`. Optional; does not gate `df final`.

Section usage: `## Purpose` is why this deliverable is worth today; `## Reference` is the curated learning resources and prior art; `## Actions` is the checkbox plan; `## Outcomes` holds the frozen v1 draft (+ path footnotes); `## Review` is the **SSOT** for feedback numbers, completion retro, and `ToImprove::` (written by `df review`; critique pointer may be appended by `df comment`).

## Tasks plugin syntax

Checkboxes only mean something to the Tasks plugin with its emoji fields. The daily note's Todo block queries `happens on <date>`, which matches start, scheduled, or due — so every action item needs a start date to show up:

```markdown
- [ ] 拆解 RAG 分块策略并写成对比表 🛫 2026-03-05
- [x] 跑通最小 demo 🛫 2026-03-05 ✅ 2026-03-05
```

Use `🛫` for start date and `✅` for completion date. Add `📅` for a due date only when the item genuinely has a deadline.

## Article config (ship + final)

Private files in the skill directory (gitignored, never committed):

| File | Role |
|------|------|
| `local.article.config.md` | Voice, 禁区, 术语降维, audience, export paths, illustration budget |
| `local.article.style.md` | Distilled house style for `df ship` (not long sample essays) |
| `local.article.memory.md` | ≤7 recent executable rewrite rules from v1→final (`df ship` + `df final`) |
| `local.hot-topics.md` (or `HOT_TOPICS_FILE`) | URL-backed last-7-day topics for `df plan` |

Copy `local.article.config.example.md` to create the real config. Article ship/final
refuse if the file or its required keys are missing. Publish URLs belong in the
task frontmatter keys listed by `PUBLISH_SLOTS`, synced by `df review` from article
YAML — never hardcode real URLs into this repository.

## Objective files (two layers)

### North-star objective (`type: O`)

The result ladders and the year→month→week focus live here:

`{{DAILY_VAULT}}\{{OBJECTIVE_FILE}}`

```yaml
---
title: <objective slug>
type: O
project: <Project-Name>
category: <Area>
tags:
  - <area tag>
  - <publishing tag>
DateStarted: YYYY-MM-DD
status: 🟡Doing
---
```

Required body sections: `## Purpose`, `## 维度字典`, `## 验收口径`, `## Milestones` (one ladder per result dimension), `## This Year`, `## This Month`, `## This Week`, an immutable **Baseline** table, and a rolling **`## Latest Snapshot`** table (same shape as Baseline; overwritten by `df review`).

The dimensions, their ladder thresholds, the counters, and the accounts or sources behind them are all **defined by the user in this note** and read at runtime. This repository never hardcodes them. When a ladder sums several sources, the note's baseline table is the authoritative list — do not keep a second copy in the config or in skill reference files.

`df plan` overwrites `## This Week` on ISO Sunday and `## This Month` on calendar month-end. `df review` may also amend `## This Week` (and rarely `## This Month`) after an explicit user confirmation on an optimization candidate. `## This Year` is set at bootstrap / yearly review only. `df review` auto-checks ladder boxes when Latest Snapshot meets a cell's threshold as written in the note.

### Capability sub-project (`type: P`)

Engineering / flywheel milestones, Skill Profile, Covered Topics, Open Questions:

`{{DAILY_VAULT}}\{{CAPABILITY_FILE}}`

Parent link back to the objective note. No `This Year/Month/Week` here (single source on the O note). Day 7 checkpoint still uses this file's `DateStarted`. When `CAPABILITY_FILE` is blank, keep these sections on the objective note instead of inventing a second file.

These two files are the only project-scope state the flywheel maintains outside the daily and task rhythm.

### Focus cascade (year → month → week → day)

The objective note is the **single source** of focus. Month and week notes carry a mirror, never an independent plan:

| File | Mirror section | Written by |
|------|----------------|------------|
| `Daily\YYYY\YYYY-Qn\YYYY-MM\YYYY-MM.md` | `## Focus · 本月焦点` + `## 月末分项快照` | `df plan` from `## This Month` |
| `...\YYYY-Www\YYYY-Www.md` | `## Focus · 本周焦点` + `## 分项快照` | `df plan` from `## This Week` |
| today's daily note | `## Actions` header lines (`维度::` / `目标格::`) | `df plan` Step 7 |

Rules:

- Month and week notes are created **as soon as they are needed for the mirror**, not only on review day. A mid-month note has an empty `Review` and a filled `Focus`.
- The mirror table repeats `goalDim` + `goalStep` per row so a day's candidate can be traced upward without opening the objective.
- If a mirror disagrees with the objective note, the objective wins and the mirror is overwritten. Never edit focus in a mirror only.
- Counters appear in: immutable Baseline on the objective, rolling `## Latest Snapshot` on the objective (daily via `df review`), plus week/month snapshot mirrors. Net growth is always computed against Baseline. Never paste real totals into this repository.
- Mode map: `df review` (yesterday SSOT on task + Snapshot/ladders) → `df plan` (today) → `df ship` (v1 draft) → optional `df comment` → `df final` (images/calibrate/handoff).

## Related existing structures

- Older project or publishing notes under `Projects/Scope/` may still exist; flywheel planning reads `{{OBJECTIVE_FILE}}` + `{{CAPABILITY_FILE}}` only.
- `Kanban/kb-tasks.md` — the board. Adding a task file does not add it to the board; the user drags it there, or the skill appends a link under the matching column when asked.
- Per-channel export converters and paste targets live in `local.article.config.md` under `publish_export` (gitignored). `df final` reads that block for handoff; this repository does not name any channel or converter.
