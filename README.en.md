# daily-flywheel

[中文](./README.md)

A Cursor Agent Skill. Each morning it tells you what to ship today; each evening it turns what you did into a finished draft and critiques it on the spot. All state is markdown inside your own Obsidian vault — it creates no parallel structure.

## What it fixes

If you have ever built a complete Obsidian setup — Templater daily notes, the Tasks plugin, Dataview rollups, a Kanban board, a project tree — and then stopped opening it one day, this skill was written for you.

That kind of system is excellent at **recording** and completely silent on **deciding**. Every morning it hands you a blank note and leaves the hardest part, figuring out what today should produce, entirely to you. After a few months of that, one morning you don't feel like it, and you never open it again.

So this skill supplies exactly two things:

- **Decision** — given your big goal and the hours you actually have today, 3 to 5 candidate deliverables you can finish today, each labelled with type, difficulty, value, estimated time, and why today
- **Feedback** — a first-reader critique the moment the draft is done. No score, no encouragement. External engagement will be near zero for the first weeks, and motivation cannot hang on it

## Two touchpoints a day

```
morning  df plan   yesterday's close-out -> today's candidates -> pick -> write plan into daily note and task file
evening  df ship   action status -> finished draft -> first-reader critique -> platform export
```

Run `df init` once first: it translates a vague goal into verifiable milestones, runs an evidence-based skill profile interview, and builds the dedup baseline.

## Requirements

Obsidian community plugins, five required, plus core daily notes:

| Plugin | Used for |
|--------|----------|
| `dataview` | Output rollups in the daily note and project rollups |
| `templater-obsidian` | Daily note template |
| `obsidian-tasks-plugin` | Due / Todo / Done blocks |
| `obsidian-kanban` | Task board |
| `periodic-notes` | Weekly and monthly notes |

## Install

**1. Clone it wherever you keep open source projects**

```bash
git clone https://github.com/Jenniferwonder/daily-flywheel.git
```

**2. Link it into Cursor's user-level skills directory**

Cursor loads user-level skills from a fixed location, so point a link at it. Repo and skill are then the same files — edit, run, commit, no divergence.

```powershell
:: Windows, no admin rights needed
mklink /J "%USERPROFILE%\.cursor\skills\daily-flywheel" "<your clone path>\daily-flywheel"
```

```bash
# macOS / Linux
ln -s <your clone path>/daily-flywheel ~/.cursor/skills/daily-flywheel
```

**3. Configure**

```bash
cp local.config.example.md local.config.md
```

Fill in four keys: `ROOT_DIR`, `DAILY_VAULT`, `NOTES_VAULT`, `OWNER`. The file is gitignored.

If the config is missing the skill stops and tells you, rather than guessing a vault path — a wrong guess scatters files into the wrong vault.

**4. Run**

Type `df init` in Cursor.

## Adapting it to your vault

The four config keys cover **locations**, not **layout**.

Folder structure, frontmatter fields, `type` values and Tasks plugin syntax all live in [`references/conventions.md`](./references/conventions.md). It describes one concrete working layout rather than an abstract contract, because a vague contract produces vague files.

**If your vault is organised differently, edit `conventions.md` directly.** It is meant to be forked.

## Layout

```
SKILL.md                      routing + global rules, ~60 lines
references/
  conventions.md              paths, schema, hard constraints (the structural contract)
  init.md                     one-time bootstrap
  plan.md                     morning
  ship.md                     evening
local.config.example.md       config template
```

`SKILL.md` only routes, and loads exactly one reference per phase. That is deliberate context control — no conversation needs all four documents at once.

## Things learned the hard way

All of these are in `conventions.md`. Listed here because they generalise beyond this skill:

- **Templater does not render files written by an agent.** Generated daily notes must be fully rendered, with dates computed and substituted and no placeholder left unexpanded.
- **A running Obsidian instance rewrites your edits.** Linter strips trailing whitespace after empty YAML values, `update-time-on-edit` rewrites `DateModified`. A one-line change can appear as a twenty-line diff. This is normal.
- **Never write a bare template open-marker into a vault file**, not even inside backticks. Observed twice: silently deleted on one write, auto-closed into an empty pair on the next.
- **`draft: true` can be a zero-information field.** It is the default in most templates, so if every file has it, it cannot identify unfinished stubs. Any metadata field with a constant value carries no information — verify a field actually discriminates before relying on it.
- **Vaults on cloud-synced drives are slow.** A depth-2 recursive listing took ~50 seconds during development, which killed the idea of letting the model scan the whole note library. Every scan is scoped and filename-only.

## License

MIT
