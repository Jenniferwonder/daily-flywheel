---
name: daily-flywheel
description: >-
  Daily output flywheel for an Obsidian vault: decides what learning
  deliverable to produce today, sizes it to the time available, writes the plan
  into the existing daily note and task files, then turns the day's work into a
  finished article and critiques it. Use when the user invokes daily-flywheel,
  df, 飞轮, 日更, asks what to produce today, wants a daily learning plan tied to
  a big goal, or wants to ship and review the day's output.
---

# Daily Output Flywheel

This skill assumes the user already owns a working Obsidian setup: Templater daily notes, the Tasks plugin, Dataview rollups, a Kanban board, and a `type` based project tree. That kind of system is very good at recording and completely silent on deciding. It is common for one to be built carefully and then abandoned within months.

The stall it is built to fix has four symptoms: no way to slice a big goal into something finishable today, no way to size that to the hours actually available, no confidence about what a deliverable could even be, and no feedback after months of study. Three are decomposition problems and the fourth is a feedback problem. None is a recording problem.

So this skill supplies exactly two things: **decision** (what to produce today, sized to today) and **feedback** (a real critique the same day, not dependent on an audience). Everything else reuses what already exists.

## Configuration — read this before anything else

Every path, goal filename, and platform name in this skill is a placeholder. Resolve them by reading `local.config.md` in this skill's own directory:

| Key | Meaning |
|-----|---------|
| `ROOT_DIR` | Parent directory shared by the vaults, used to expand the two below |
| `DAILY_VAULT` | Vault holding daily notes, tasks, and projects. Everything this skill writes goes here. Defaults to `{{ROOT_DIR}}/Daily` |
| `NOTES_VAULT` | Optional second vault of existing notes, read-only, used only for dedup. Defaults to `{{ROOT_DIR}}/Notes` |
| `OWNER` | Value written into the `owner` frontmatter field |
| `OBJECTIVE_FILE` | Path, relative to `DAILY_VAULT`, of the north-star objective note holding the goal, its milestones, and the year/month/week focus |
| `CAPABILITY_FILE` | Optional path of the capability sub-project note (skill profile, engineering milestones). Blank keeps everything on `OBJECTIVE_FILE` |
| `PUBLISH_SLOTS` | Comma-separated frontmatter keys that store publish URLs on task / article notes |
| `EXTRA_ARCHETYPES` | Optional private rows for the `df plan` candidate table; leave blank to skip |

If `local.config.md` does not exist, stop and tell the user to copy `local.config.example.md` to `local.config.md` and fill it in. Do not guess a vault path, and do not proceed with placeholders unresolved — writing to a guessed path scatters files into the wrong vault.

If `NOTES_VAULT` is absent or points nowhere, skip dedup scanning rather than failing.

`local.config.md` holds **locations, publish-slot key names, and optional private archetypes**. The goal itself — its dimensions, thresholds, baseline numbers, and the accounts involved — lives in the objective note inside the vault and is read from there at runtime. Per-channel export steps live in `local.article.config.md` under `publish_export`. **Never copy goal content or channel-specific tactics into this repository**, not even into passing prose or an example. When a reference file needs an example, it uses a placeholder or an obviously invented value.

### Article config (ship only)

Article drafts also require `local.article.config.md` (gitignored). Copy from
`local.article.config.example.md`. It holds style, audience, export paths, and
illustration budget. Learned edit rules from v1→final diffs live in
`local.article.memory.md` (also gitignored). See `references/ship.md` Step 0.

If the article config is missing during `df ship` for an article deliverable,
refuse to draft — do not silently fall back to an unconfigured write.

## Routing

Always read `references/conventions.md` first — it holds every path, schema, and hard constraint. Then read exactly one mode reference. Never read all of them.

| Trigger | Mode | Reference |
|---------|------|-----------|
| `df init`, first ever run, or `{{OBJECTIVE_FILE}}` is missing | Bootstrap north-star + capability sub-project | `references/init.md` |
| `df plan`, morning, "今天做什么" | Review yesterday + sync publish links; on ISO Sunday / month-end run week/month review+plan; daily candidates aligned to the objective's This Year/Month/Week and its result ladders | `references/plan.md` |
| `df ship`, evening, "写出来", "收工" | Action status + configured draft (dual-write) + critique + illustrate + calibrate + publish links | `references/ship.md` |

If the mode is ambiguous, check whether today's daily note already has a filled `## Actions` section: empty means `plan`, filled means `ship`.

## Rules that apply to every mode

1. **One question turn.** Collect all inputs for a phase in a single numbered question block and wait for one reply. Ritual overhead is what kills daily systems; do not spread questions across turns.
2. **Never write Templater syntax.** Templater does not render agent-written files, so every template expression must be resolved to a literal value before writing. A daily note containing an unexpanded placeholder is a defect. Separately, do not write a bare template open-marker into a vault file even as prose or inside backticks: a live Obsidian instance rewrites it (observed twice — once deleted, once auto-closed into an empty pair). The exact plugin responsible was not isolated; Linter and Templater are both candidates. Describe it in words instead. The skill's own files sit outside the vault and are unaffected.
3. **A live Obsidian instance will rewrite what you write.** Linter strips trailing whitespace after empty YAML values and `update-time-on-edit` rewrites `DateModified`. Expect a diff larger than your edit, and never treat that as corruption.
4. **Never scan a vault recursively without a narrow path filter.** Vaults on network or cloud-synced drives are slow — a depth-2 recursive listing took ~50 seconds during development. Use the exact scoped commands in `conventions.md`.
5. **Read filenames and frontmatter, never note bodies**, unless the user names a specific file.
6. **Never invent industry trends or news.** Justification for "why today" must cite the user's own state: a gap in the skill profile, an unfinished stub, an unfinished series, yesterday's result. The model has no live trend data and must not pretend otherwise.
7. **Respect the time budget as a hard ceiling.** A deliverable estimated above the hours the user reported today is not a candidate. Cut scope until it fits.
8. **Structured output only.** Candidate lists, plans, and reviews are tables or short bullets. The only long prose generated all day is the article in `ship`.
9. **Edit in place, additively.** These files are the user's own notes and may have been hand-edited. Preserve existing content; fill empty sections rather than rewriting files.
10. **Feedback numbers are recorded, not analyzed, for the first 7 days.** Early like counts are statistical noise, and a fake analysis of them will burn the user's trust. Trend analysis unlocks once 7 days of data exist.
