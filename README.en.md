<h1 align="center">Daily Flywheel - AI Goal-Oriented Learning Workflow for Obsidian</h1>

<p align="center">
  <b>Turn Obsidian from a place that records learning into a system that ships something every day</b>
</p>

<p align="center"><a href="./README.md">中文</a></p>

You already have daily notes, tasks, projects, and a knowledge base — yet every morning still starts with “What should I learn, make, or write today?” The missing piece is not another recording tool. It is a loop from **long-term goal → today's action → published result → feedback**.

Daily Flywheel is an AI Agent Skill. Give it your goal and today's available hours; it proposes finishable **article/script** candidates. Pick one, ship a v1 draft, hand-edit, optionally critique, then finalize (illustrate / calibrate / hand off). **Everything remains ordinary markdown in your own Obsidian vault — no migration and no parallel system.**

## Six commands to run the flywheel

| Phase | Input | What you get |
|-------|-------|--------------|
| `df init` | Your long-term goal and current capabilities | Verifiable result ladders, capability milestones, and a topic baseline |
| `df review` | Yesterday's work + current counters | Task retro + `reviewed`, objective Snapshot/ladder ticks; optional week-focus tweak |
| `df plan` | Today's hours (requires yesterday `reviewed`) | 3–5 article/script candidates written into daily + task |
| `df ship` | What you actually completed | Frozen v1 + editable export draft (no critique/images) |
| `df comment` | Hand-edited final (optional) | Four-line critique; stamps `commented` |
| `df final` | Confirmed final draft | Article: images + OSS + calibrate + handoff; script: skip images |

## Install now

```bash
npx skills add Jenniferwonder/daily-flywheel --agent cursor --global
```

Then copy the two example configs, fill in your vault paths and article preferences, and type `df init` in Cursor. See [Install and configure](#install-and-configure) for every field.

## Why install it

- **Ship every day instead of facing a blank note.** Candidates are constrained by your long-term goal and real time budget; oversized work never enters the list.
- **Keep the Obsidian system you already own.** Daily notes, tasks, projects, and weekly/monthly reviews remain ordinary markdown.
- **Go all the way from plan to publish.** It handles the draft, critique, illustrations, publish-link sync, and later feedback collection — not just a to-do list.
- **Make later drafts sound more like you.** Differences between the first and final drafts become private editing rules, reducing repeated manual fixes over time.
- **Keep real goals and channel setup local.** Goals, numbers, accounts, and export steps never enter the open repository.
- **Bilingual UI.** Set `LANGUAGE: zh` or `en` in `local.config.md`; chat and generated prose follow it. Vault schema keys stay stable (see `references/i18n.md`).

## Features at a glance

| Feature | What it does | Where it lands |
|---------|--------------|----------------|
| Yesterday review | Sync links, capture counters/feedback, task Review, Snapshot + auto ladder ticks; propose focus tweaks when triggered | Task + objective note (vault only) |
| Today's decision | From the **latest** objective + hours, 3–5 article/script candidates | Daily `## Actions` + task file |
| Goal cascade | Year → month → week → day; tasks need `goalDim` / `goalStep` / `deliverable` | Objective / month / week notes |
| Dual-write draft | `df ship`: freeze v1 in the task; export path for hand-edits | Task `## Outcomes` + export dir |
| First-reader critique | Optional `df comment` after confirming final; stamps `commented` | Chat + task frontmatter |
| Finalize | `df final`: images/OSS/calibrate/handoff (scripts skip images) | Export draft + `local.article.memory.md` |
| Daily aggregation | Review section Dataviews task fields — no multi-write | Daily template |
| Topic dedup | Filenames + frontmatter only | Capability Covered Topics |
| Skill profile | 1–2 evidence-based questions a day | Capability Skill Profile |

## How to use it

### `df init` — once, ever

Translates a vague goal into something verifiable: countable result ladders go on the objective note, capability milestones on the capability sub-project note. Then it runs an evidence-based skill profile interview and builds the dedup baseline.

It writes files against the folder layout and frontmatter schema described in [`references/conventions.md`](./references/conventions.md). **If your vault is organised differently, edit `conventions.md` before running `df init`.**

### `df review` — first each morning

```
sync publish URLs -> capture counters/feedback -> task Review + reviewed -> Snapshot/ladders -> (if triggered) confirm week-focus edit
```

Real goal numbers stay in your vault objective note — never in the open skill repo.

### `df plan` — after review

```
require reviewed -> (Sunday/month-end gates) -> read latest objective -> candidates -> write daily + task
```

Hard-stops if yesterday is not `reviewed`. Hours are a **hard ceiling**. Defaults to article/script days.

### `df ship` → hand-edit → (optional) `df comment` → `df final`

```
ship: checkboxes + dual-write v1/export draft
comment: confirm final → four-line critique → commented date
final: confirm final → images+OSS (articles) → calibrate → publish handoff
```

Without `local.article.config.md`, article ship/final refuse rather than drafting unconstrained prose.

## Requirements

Obsidian community plugins, five required, plus core daily notes:

| Plugin | Used for |
|--------|----------|
| `dataview` | Output rollups in the daily note and project rollups |
| `templater-obsidian` | Daily note template |
| `obsidian-tasks-plugin` | Due / Todo / Done blocks |
| `obsidian-kanban` | Task board |
| `periodic-notes` | Weekly and monthly notes |

## Install and configure

**1. Install the skill** (skip if you already ran the command above)

```bash
npx skills add Jenniferwonder/daily-flywheel --agent cursor --global
```

The skill shows up at `~/.cursor/skills/daily-flywheel` (a symlink to the canonical copy by default; add `--copy` if symlinks fail on Windows). Both config files below go in that directory.

**2. Fill in the vault config**

```bash
cp local.config.example.md local.config.md
```

| Key | What goes in it |
|-----|-----------------|
| `ROOT_DIR` | Parent directory shared by the vaults, used only to expand the two defaults below |
| `DAILY_VAULT` | Vault holding daily notes, tasks, and projects. Everything the skill writes goes here. Required |
| `NOTES_VAULT` | Optional second vault of existing notes, read-only, used only for topic dedup. Blank skips dedup |
| `OWNER` | Value written into the `owner` frontmatter field of generated task files |
| `LANGUAGE` | Chat + generated prose: `zh` \| `en` (default `zh`); strings in `references/i18n.md` |
| `OBJECTIVE_FILE` | Path of the north-star objective note, relative to `DAILY_VAULT`. Created by `df init` if missing. Required |
| `CAPABILITY_FILE` | Path of the capability sub-project note; blank keeps the profile and milestones on the objective note |
| `PUBLISH_SLOTS` | Frontmatter keys that store publish URLs, comma-separated, in the order you want to be asked |
| `EXTRA_ARCHETYPES` | Optional private candidate rows that never enter the open docs |

**3. Fill in the article config** (`df ship` / `df final` need it)

```bash
cp local.article.config.example.md local.article.config.md
```

`audience`, `export_dir`, and `export_slug_pattern` are required; ship policy, style, illustration budget, and per-channel export steps (`publish_export`) are optional.

**4. Run it**

Type `df init` in Cursor.

If the config is missing the skill stops and tells you, rather than guessing a vault path — a wrong guess scatters files into the wrong vault.

**The config holds locations, slot key names, and optional private archetypes — not goal content.** What you are aiming at, how you measure it, where the thresholds sit, and any accounts or numbers involved live only in the objective note inside your vault, read at runtime; per-channel export steps live in `local.article.config.md`. Both config files are gitignored, so a pasted config, a screen-share, or an accidental `git add -f` cannot leak the goal itself. Examples under `references/` are invented placeholders on purpose — do not replace them with your own values, or a fork or PR will carry them out.

### Hacking on it / contributing

Clone it wherever you keep open source projects, then link that clone into Cursor's user-level skills directory. Repo and skill are then the same files — edit, run, commit, no divergence.

```powershell
# Windows, no admin rights needed
git clone https://github.com/Jenniferwonder/daily-flywheel.git
cmd /c mklink /J "$env:USERPROFILE\.cursor\skills\daily-flywheel" "<your clone path>\daily-flywheel"
```

```bash
# macOS / Linux
git clone https://github.com/Jenniferwonder/daily-flywheel.git
ln -s <your clone path>/daily-flywheel ~/.cursor/skills/daily-flywheel
```

## Layout

```
SKILL.md                          routing + global rules
references/
  conventions.md                  the Obsidian vault contract: folder layout, paths,
                                  frontmatter schema, Tasks syntax, hard constraints
                                  (edit this to fit your own vault)
  init.md                         one-time bootstrap
  plan.md                         morning
  ship.md                         evening (article config / dual-write / calibration)
local.config.example.md           vault path template
local.article.config.example.md   style / audience / export / illustration template (private)
```

`SKILL.md` only routes, and loads exactly one reference per phase. That is deliberate context control — no conversation needs all four documents at once. To change behaviour, edit the one reference that owns it.

## More tips

I write about this workflow and other agent-skill experiments in Chinese. Two pieces cover how this skill was designed:

- [Building an AI + Obsidian learning-output workflow, so you never stall on "what should I study today"](https://zhuanlan.zhihu.com/p/2067904165205087916)
- [Letting AI run the article pipeline end to end](https://zhuanlan.zhihu.com/p/2068384023894922886)

If this skill got your daily shipping habit running, a Star ⭐️ helps.

## License

MIT
