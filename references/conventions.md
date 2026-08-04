# Conventions

Every path, schema, and constraint the flywheel depends on. Read this before any mode.

This file is the structural contract between the skill and the vault. It describes one concrete working layout rather than an abstract one, because a vague contract produces vague files. If your vault is organised differently, fork this file — that is the intended way to adapt the skill. The keys in `local.config.md` cover locations only, not layout.

Paths below use the placeholders resolved from `local.config.md`: `{{DAILY_VAULT}}`, `{{NOTES_VAULT}}`, `{{OWNER}}`.

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

# Existing and finished tasks (flat, fast)
Get-ChildItem -LiteralPath "{{DAILY_VAULT}}\Tasks\New\Backlog" -Filter *.md -Name
Get-ChildItem -LiteralPath "{{DAILY_VAULT}}\Tasks\New\Completed" -Filter *.md -Name

# Recent daily notes (flat, fast)
Get-ChildItem -LiteralPath "{{DAILY_VAULT}}\Daily" -Filter *.md -Name
```

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
- Week link: `YYYY-Www` using the **ISO** week number, e.g. 2026-08-03 falls in `[[2026-W32]]`

```powershell
# Resolve today's date and ISO week before writing any file
$d = Get-Date
$d.ToString('yyyy-MM-dd')
"{0}-W{1:D2}" -f $d.Year, [System.Globalization.ISOWeek]::GetWeekOfYear($d)
```

- Sprint field format in this layout is `YY-MM-A`, e.g. `26-08-A`. This is an example of one convention, not a requirement. If a task created this month already uses a different suffix, match it rather than inventing one.

## Daily note

Path: `{{DAILY_VAULT}}\Daily\YYYY-MM-DD.md`
Source template: `{{DAILY_VAULT}}\Templates\Tp-Daily\tp-Daily Plan.md`

If the file already exists, fill its empty sections and leave everything else alone. If it does not, write it fully rendered — every template expression resolved to a literal, none surviving. Rendered shape for 2026-08-03, substituting the real date everywhere:

````markdown
---
title: Daily Plan
tags:
  - Daily
DateStarted: 2026-08-03
DateModified: 2026-08-03
---
# Daily Plan
- Week:: [[2026-W32]]
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
happens on 2026-08-03 
sort by due
```
### Done
```tasks
done
(done on 2026-08-03)
```

## Actions
## Review
- ToImprove::  
### ✍️New Notes

```dataview
TABLE title, DateStarted, status
WHERE DateStarted = date(2026-08-03)     
SORT file.mday DESC
```
### ✅ Tasks Done
```dataview
TABLE title, DateStarted, status
WHERE DateDone = date(2026-08-03)     
SORT file.mday DESC
```
### 📝Modified Notes

```dataview
TABLE title, DateStarted, status
WHERE file.cday != date(2026-08-03) AND DateModified = date(2026-08-03)
SORT modified ASC
```
````

The flywheel writes into `## Actions` (today's plan and checkboxes) and `## Review` (yesterday's close-out, `ToImprove::`). The three Dataview blocks and three Tasks blocks are left untouched — they populate themselves and are the user's built-in progress feedback.

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
difficulty: 
comment: 
draft: true
wechat: 
zhihu: 
juejin: 
bilibili: 
title: cpe-<slug>
owner: {{OWNER}}
type: T
project: CPE
blockedBy: 
sprint: 26-08-A
points: 
priority: 
DateStarted: 2026-08-03
DateDone: 
DateModified: 2026-08-03
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
- `wechat` / `zhihu` / `juejin` / `bilibili` are the publish slots. Leave empty until published, then store the URL.

Section usage: `## Purpose` is why this deliverable is worth today; `## Reference` is the curated learning resources and prior art; `## Actions` is the checkbox plan; `## Outcomes` holds the finished draft; `## Review` holds the critique, the feedback numbers, and the retro.

## Tasks plugin syntax

Checkboxes only mean something to the Tasks plugin with its emoji fields. The daily note's Todo block queries `happens on <date>`, which matches start, scheduled, or due — so every action item needs a start date to show up:

```markdown
- [ ] 拆解 RAG 分块策略并写成对比表 🛫 2026-08-03
- [x] 跑通最小 demo 🛫 2026-08-03 ✅ 2026-08-03
```

Use `🛫` for start date and `✅` for completion date. Add `📅` for a due date only when the item genuinely has a deadline.

## Article config (ship)

Private files in the skill directory (gitignored, never committed):

| File | Role |
|------|------|
| `local.article.config.md` | Style, audience, export paths, illustration budget for `df ship` |
| `local.article.memory.md` | ≤7 recent executable rewrite rules learned from v1→final diffs |

Copy `local.article.config.example.md` to create the real config. Article ship
refuses to draft if the file or its required keys are missing. Publish URLs
belong in the task frontmatter `wechat` / `zhihu` / `juejin` / `bilibili` plus a
short `发布链接` note under `## Outcomes` — that is the single retro surface.

## Objective file

The big goal, milestones, and skill profile live in one `type: P` file under the existing project tree:

`{{DAILY_VAULT}}\Projects\Scope\TechSkills\AI\ai-agent-flywheel.md`

It sits beside the area hub notes. Tagging it with the area tag makes it appear in that hub's Sub-projects rollup automatically, whose query accepts both `P` and `O`. It is typed `P` rather than `O` because it has milestones and a finish line.

```yaml
---
title: ai-agent-flywheel
type: P
project: AI-Agent-Flywheel
category: TechSkills
DateDone: 
DateReviewed: 
reviewed: 
difficulty: 
comment: 
draft: true
wechat: 
zhihu: 
juejin: 
bilibili: 
tags:
  - AI
  - Content-Making
DateStarted: 2026-08-03
status: 🟡Doing
DateModified: 2026-08-03
---
```

This is the only file the flywheel creates outside the daily and task rhythm. It is state, not a new system.

## Related existing structures

- A content-publishing objective note under `Projects/Scope/`, typed `O`, that daily deliverables link to and roll up under.
- `Kanban/kb-tasks.md` — the board. Adding a task file does not add it to the board; the user drags it there, or the skill appends a link under the matching column when asked.
- The third-party `baoyu-post-to-wechat` skill provides the markdown-to-WeChat converter used by `ship`. If it is not installed, `ship` falls back to plain markdown export.
