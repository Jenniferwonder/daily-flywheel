<h1 align="center">Daily Flywheel - AI Goal-Oriented Learning Workflow for Obsidian</h1>

<p align="center">
  <b>Turn Obsidian from a place that records learning into a system that ships something every day</b>
</p>

<p align="center"><a href="./README.md">中文</a></p>

You already have daily notes, tasks, projects, and a knowledge base — yet every morning still starts with “What should I learn, make, or write today?” The missing piece is not another recording tool. It is a loop from **long-term goal → today's action → published result → feedback**.

Daily Flywheel is an AI Agent Skill. Give it your goal and today's available hours; it proposes finishable **article/script** candidates. Pick one, ship a v1 draft, hand-edit, optionally critique, then finalize (illustrate / calibrate / hand off). **Everything remains ordinary markdown in your own Obsidian vault — no migration and no parallel system.**

## Seven commands to run the flywheel

| Phase | Input | What you get |
|-------|-------|--------------|
| `df init` | Your long-term goal and current capabilities | Verifiable result ladders, capability milestones, and a topic baseline |
| `df review` | Yesterday's work + current counters | Task retro + `reviewed`, objective Snapshot/ladder ticks; optional week-focus tweak |
| `df plan` | Today's hours (requires yesterday `reviewed`); optional hot-topic refresh | 3–5 article/script candidates (objective + sourced hot topics) |
| `df study` | Learning resource + type (book/codebase/video/tutorial; inferred when omitted) | Question set (all upfront) → answers/reflection → per-question evaluation → Anki cards (after confirmation) → article feed |
| `df ship` | What you actually completed | Frozen v1 + editable export draft (funnel skeleton; style abstract + memory) |
| `df comment` | Hand-edited final (optional) | Advisory checklist score + four-line critique; stamps `commented` |
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
- **Turn learning into output.** Optional `df study`: point it at a book / codebase / video / tutorial; high-value questions arrive upfront, answers are evaluated, and knowledge points become Anki-compatible cards linked from the theme note — feeding the article pipeline.
- **Make later drafts sound more like you.** Differences between the first and final drafts become private editing rules, reducing repeated manual fixes over time.
- **Keep real goals and channel setup local.** Goals, numbers, accounts, and export steps never enter the open repository.
- **Bilingual UI.** Set `LANGUAGE: zh` or `en` in `local.config.md`; chat and generated prose follow it. Vault schema keys stay stable (see `references/i18n.md`).

## Features at a glance

| Feature | What it does | Where it lands |
|---------|--------------|----------------|
| Goal cascade | Year → month → week → day; tasks need `goalDim` / `goalStep` / `deliverable` | Objective / month / week notes |
| Yesterday review | Sync links, capture counters/feedback, task Review, Snapshot + auto ladder ticks; propose focus tweaks when triggered | Task + objective note (vault only) |
| Today's decision | From the **latest** objective, hours, and URL-backed hot topics, 3–5 article/script candidates (three-way filter) | Daily `## Actions` + task file |
| Question-driven study | Optional `df study`: routes by resource type (book/codebase/video/tutorial); questions cover the whole unit → evaluation → Anki-compatible cards (internal review) | `STUDY_CARDS_DIR` cards + task (questions/answers/evaluation) |
| Dual-write draft | `df ship`: freeze v1 in the task; export path for hand-edits | Task `## Outcomes` + export dir |
| First-reader critique | Optional `df comment` after confirming final; advisory score + four-line critique; stamps `commented` | Chat + task frontmatter |
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
require reviewed -> (Sunday/month-end gates) -> read latest objective -> optional hot-topic refresh -> three-way filter -> write daily + task
```

Hard-stops if yesterday is not `reviewed`. Hours are a **hard ceiling**. Defaults to article/script days. Candidates must serve This Week **and** a URL-backed hot-topics row when one exists; missing sources are marked `not found` — never invented.

### `df study` — optional: question-driven reading loop

Give it a learning resource and its type. When the type is omitted it is inferred: `.pdf`/`.epub` → book, a repo dir with `.git` → codebase, a video file/URL → video, `.md`/`.html`/docs URL → tutorial. The flow routes by type:

| Type | Extract | Unit | Source tag | Practice slice | Deck route |
|------|---------|------|------------|----------------|------------|
| book | `pdftotext` page range | chapter / section | section + print page | run a book example / small probe | `PREFIX::Ch-XX` |
| codebase | scoped repo read | module / feature / diff | file + line | reproduce / modify / benchmark | `PREFIX::Module-XX` |
| video | transcript / chaptered skim | segment (time range) | segment + timestamp | redo the steps | `PREFIX::Part-XX` |
| tutorial | read the docs section | lesson / section | section + line/URL | follow steps, note deviations | `PREFIX::Lesson-XX` |

All high-value questions covering **every key concept** of the unit are given upfront (no fixed cap — coverage decides; long units split into multiple cycles). You read with the questions, answer all, and add a reflection; the agent evaluates each answer and suggests next steps; after confirmation, knowledge points become Anki-compatible cards (one file per unit, one card per knowledge point, deck-route line + `### knowledge point` front), linked back from the theme note. Cards are internal review material; series articles must rephrase card content, citing the card note only at the end.

### `df ship` → hand-edit → (optional) `df comment` → `df final`

```
ship: **manual trigger only**; topic brainstorm (brainstorming skill when available) → outline confirmation (writing-assistant skill when available) → then dual-write v1 (funnel skeleton; style abstract + memory, no long sample essays)
comment: confirm final → advisory checklist score + four-line critique → commented date
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
| `obsidian-to-anki-plugin` | (optional, `df study`) exports knowledge-point cards to Anki; without it cards stay in Obsidian only |

## Install and configure

**1. Install the skill** (skip if you already ran the command above)

```bash
npx skills add Jenniferwonder/daily-flywheel --agent cursor --global
```

The skill shows up at `~/.cursor/skills/daily-flywheel` (a symlink to the canonical copy by default; add `--copy` if symlinks fail on Windows). Vault and article configs go in that directory.

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
| `HOT_TOPICS_FILE` | Last-7-day URL-backed topics note (gitignored). Defaults to `local.hot-topics.md` |
| `EXTRA_ARCHETYPES` | Optional private candidate rows that never enter the open docs |
| `STUDY_CARDS_DIR` | Optional. `df study` cards + theme-note directory (the only write-allowed `NOTES_VAULT` exception); blank disables study |
| `STUDY_DECK_PREFIX` | Optional. Anki deck prefix, e.g. `AI-Engineering` |
| `STUDY_TYPES` | Optional. Supported learning kinds: `book, tutorial, codebase, video`; extensible |

**3. Fill in the article config** (`df ship` / `df final` need it)

```bash
cp local.article.config.example.md local.article.config.md
```

`audience`, `export_dir`, and `export_slug_pattern` are required; ship policy, voice/taboos/terms, illustration budget, and per-channel export steps (`publish_export`) are optional. Also copy the style abstract and hot-topics templates:

```bash
cp local.article.style.example.md local.article.style.md
cp local.hot-topics.example.md local.hot-topics.md
cp script-craft.example.md script-craft.md
```

**4. Run it**

Type `df init` in Cursor.

If the config is missing the skill stops and tells you, rather than guessing a vault path — a wrong guess scatters files into the wrong vault.

**The config holds locations, slot key names, and optional private archetypes — not goal content.** What you are aiming at, how you measure it, where the thresholds sit, and any accounts or numbers involved live only in the objective note inside your vault, read at runtime; per-channel export steps live in `local.article.config.md`. Vault, article, style, and hot-topics files are gitignored, so a pasted config, a screen-share, or an accidental `git add -f` cannot leak the goal itself. Examples under `references/` are invented placeholders on purpose — do not replace them with your own values, or a fork or PR will carry them out.

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
  i18n.md                         bilingual user-facing strings (LANGUAGE)
  init.md                         one-time bootstrap
  review.md                       yesterday review
  plan.md                         morning (three-way filter + hot-topics note)
  study.md                        optional question-driven study (resource-type routing + card template)
  ship.md                         evening (funnel skeleton; style abstract + memory)
  comment.md                      optional critique (advisory scorecard; does not block final)
  final.md                        illustrate / calibrate / publish handoff
  article-craft.md                abstract slots for topic / funnel / score (articles only)
local.config.example.md           vault path template
local.article.config.example.md   voice / audience / export / illustration template (private)
local.article.style.example.md    distilled house-style template (private)
script-craft.example.md           script outline-gate template (working `script-craft.md` is gitignored)
local.hot-topics.example.md       last-7-day hot-topics template (private)
scripts/                          OSS image upload (df final)
```

`SKILL.md` only routes, and loads exactly one mode reference per phase. That is deliberate context control — no conversation needs every reference at once. To change behaviour, edit the one file that owns it.

## More tips

For updates, new feature walkthroughs, and step-by-step tutorials, I write in Chinese. The daily-flywheel skill's design notes and how-to live in my WeChat AI workflow series (Zhihu mirrors, publish order):

1. [Building an AI + Obsidian learning-output workflow, so you never stall on "what should I study today"](https://zhuanlan.zhihu.com/p/2067904165205087916)
2. [Letting AI run the article pipeline end to end](https://zhuanlan.zhihu.com/p/2068384023894922886)
3. [Breaking a north-star goal down to a daily, countable action](https://zhuanlan.zhihu.com/p/2068951424130606543)
4. [Script in hand, still can't shoot: first day of AI tech-video production](https://zhuanlan.zhihu.com/p/2069437689905017138)
5. [Full recap: I shipped my first AI-topic video](https://zhuanlan.zhihu.com/p/2071322742285195193)
6. [Tuning the writing workflow: hot topics in planning, titles that hit](https://zhuanlan.zhihu.com/p/2071915456995258401)
7. [An AI reading method: turn a classic into a personal knowledge system](https://zhuanlan.zhihu.com/p/2072801961523599091)

If this skill got your daily shipping habit running, a Star ⭐️ helps.

## License

MIT
