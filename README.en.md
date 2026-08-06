<h1 align="center">Daily Flywheel - AI Goal-Oriented Learning Workflow for Obsidian</h1>

<p align="center">
  <b>Turn Obsidian from a place that records learning into a system that ships something every day</b>
</p>

<p align="center"><a href="./README.md">中文</a></p>

You already have daily notes, tasks, projects, and a knowledge base — yet every morning still starts with “What should I learn, make, or write today?” The missing piece is not another recording tool. It is a loop from **long-term goal → today's action → published result → feedback**.

Daily Flywheel is a Cursor Agent Skill. Give it your goal and today's available hours; it proposes deliverables that fit. Pick one, and that evening it helps turn the work into a draft, critique, illustrations, and publish-link sync. **Everything remains ordinary markdown in your own Obsidian vault — no migration and no parallel system.**

## Three commands to run the flywheel

| Phase | Input | What you get |
|-------|-------|--------------|
| `df init` | Your long-term goal and current capabilities | Verifiable result ladders, capability milestones, and a topic baseline |
| `df plan` | The hours you actually have today | 3–5 finishable candidates plus a plan written into the daily note and task file |
| `df ship` | What you actually completed | Draft, first-reader critique, illustrations, editing rules, and publish-link sync |

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

## Features at a glance

| Feature | What it does | Where it lands |
|---------|--------------|----------------|
| Today's decision | Given your big goal and the hours you actually have, 3–5 candidate deliverables you can finish today, each labelled with type, difficulty, value, estimated time, and why today | Today's daily note `## Actions` + the task file it creates |
| Goal cascade | Year → month → week → day pushed down from a single source; weekly and monthly notes only mirror it. A task that can't name which rung of the goal it moves doesn't get created | Objective note / monthly / weekly notes |
| Dual-write draft | Writes the first draft from your private article config: v1 frozen in the task file, the export path holding the copy you actually edit | Task `## Outcomes` + export directory |
| First-reader critique | Critiques the draft the moment it's done. No score, no encouragement | Task `## Review` |
| Timeboxed illustration | Cover and inline images within a fixed budget; on timeout it drops inline images and keeps the cover | Article `imgs/` directory |
| Edit calibration | Diffs v1 against the version you hand-edited, distills ≤5 actionable rewrite rules and keeps them rolling, so later drafts need less fixing | `local.article.memory.md` |
| Publish sync | Publish URLs written back to task frontmatter; engagement collected in one place next morning. Recorded but not analyzed for the first 7 days | Task frontmatter + daily note |
| Topic dedup | Builds a "what I've already written" baseline from filenames and frontmatter only, and stops recommending it | Capability note Covered Topics |
| Skill profile | 1–2 evidence-based capability questions a day; answers recalibrate levels, and later candidates target the gaps | Capability note Skill Profile |

## How to use it

### `df init` — once, ever

Translates a vague goal into something verifiable: countable result ladders go on the objective note, capability milestones on the capability sub-project note. Then it runs an evidence-based skill profile interview and builds the dedup baseline.

It writes files against the folder layout and frontmatter schema described in [`references/conventions.md`](./references/conventions.md). **If your vault is organised differently, edit `conventions.md` before running `df init`.**

### `df plan` — every morning

```
yesterday's close-out -> review -> today's candidates -> you pick -> write into daily note and task file
```

All questions arrive in one numbered block and you answer once. On ISO Sunday and at month-end it also runs the weekly / monthly review and writes the focus back. The hours you report are a **hard ceiling** — anything estimated above them never reaches the candidate table.

### `df ship` — every evening

```
action status -> dual-write draft -> first-reader critique -> timeboxed illustration -> calibrate edit rules -> publish links
```

Without `local.article.config.md` it refuses to draft, rather than degrading into an unconstrained draft you then rescue by hand.

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
| `OBJECTIVE_FILE` | Path of the north-star objective note, relative to `DAILY_VAULT`. Created by `df init` if missing. Required |
| `CAPABILITY_FILE` | Path of the capability sub-project note; blank keeps the profile and milestones on the objective note |
| `PUBLISH_SLOTS` | Frontmatter keys that store publish URLs, comma-separated, in the order you want to be asked |
| `EXTRA_ARCHETYPES` | Optional private candidate rows that never enter the open docs |

**3. Fill in the article config** (only `df ship` needs it)

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
