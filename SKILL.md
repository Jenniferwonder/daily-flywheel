---
name: daily-flywheel
description: >-
  Daily output flywheel for an Obsidian vault: reviews yesterday against the
  north-star objective, plans a finishable content deliverable for today, ships
  a v1 draft, optionally critiques the hand-edited final, then illustrates /
  calibrates / hands off publish. Use when the user invokes daily-flywheel, df,
  df plan, df review, df ship, df comment, df final, 飞轮, 日更, or asks what to
  produce today / to close out yesterday / to ship or finalize the day's output.
---

# Daily Output Flywheel

This skill assumes the user already owns a working Obsidian setup: Templater daily notes, the Tasks plugin, Dataview rollups, a Kanban board, and a `type` based project tree. That kind of system is very good at recording and completely silent on deciding. It is common for one to be built carefully and then abandoned within months.

The stall it is built to fix has four symptoms: no way to slice a big goal into something finishable today, no way to size that to the hours actually available, no confidence about what a deliverable could even be, and no feedback after months of study. Three are decomposition problems and the fourth is a feedback problem. None is a recording problem.

So this skill supplies **decision** (what to produce today, sized to today), **feedback** (review + optional critique), and **finalize** (illustrate / calibrate / handoff). Everything else reuses what already exists.

## Configuration — read this before anything else

Every path, goal filename, and platform name in this skill is a placeholder. Resolve them by reading `local.config.md` in this skill's own directory:

| Key | Meaning |
|-----|---------|
| `ROOT_DIR` | Parent directory shared by the vaults, used to expand the two below |
| `DAILY_VAULT` | Vault holding daily notes, tasks, and projects. Everything this skill writes goes here. Defaults to `{{ROOT_DIR}}/Daily` |
| `NOTES_VAULT` | Optional second vault of existing notes, read-only, used only for dedup. Defaults to `{{ROOT_DIR}}/Notes` |
| `OWNER` | Value written into the `owner` frontmatter field |
| `LANGUAGE` | UI language for chat + generated prose: `zh` \| `en` (default `zh`). See `references/i18n.md` |
| `OBJECTIVE_FILE` | Path, relative to `DAILY_VAULT`, of the north-star objective note holding the goal, its milestones, and the year/month/week focus |
| `CAPABILITY_FILE` | Optional path of the capability sub-project note (skill profile, engineering milestones). Blank keeps everything on `OBJECTIVE_FILE` |
| `PUBLISH_SLOTS` | Comma-separated frontmatter keys that store publish URLs on task / article notes |
| `EXTRA_ARCHETYPES` | Optional private rows for the `df plan` candidate table; leave blank to skip |

If `local.config.md` does not exist, stop and tell the user to copy `local.config.example.md` to `local.config.md` and fill it in. Do not guess a vault path, and do not proceed with placeholders unresolved — writing to a guessed path scatters files into the wrong vault.

If `NOTES_VAULT` is absent or points nowhere, skip dedup scanning rather than failing.

`local.config.md` holds **locations, publish-slot key names, optional private archetypes, and optional OSS keys**. The goal itself — dimensions, thresholds, baseline numbers, accounts, Latest Snapshot — lives **only** in the objective note inside the vault (plus other vault task/daily files). Per-channel export steps live in `local.article.config.md` under `publish_export`. **Never copy goal content, ladder numbers, account names, or channel-specific tactics into this repository**, not even into passing prose, commit messages, or examples. When a reference file needs an example, it uses a placeholder or an obviously invented value.

### Article config

Article drafts (`df ship`) and article finalize (`df final`) require `local.article.config.md` (gitignored). Copy from `local.article.config.example.md`. Learned edit rules from v1→final diffs live in `local.article.memory.md` (also gitignored). Memory rules must stay abstract — never store private goal totals there.

If the article config is missing when an article deliverable needs it, refuse to draft/finalize — do not silently fall back to an unconfigured write.

## Routing

Always read `references/conventions.md` first — it holds every path, schema, and hard constraint. Resolve `LANGUAGE` from `local.config.md` (default `zh`) and skim `references/i18n.md` for that language's user-facing strings. Then read **exactly one** mode reference. Never read all mode refs.

| Trigger | Mode | Reference |
|---------|------|-----------|
| `df init`, first ever run, or `{{OBJECTIVE_FILE}}` is missing | Bootstrap north-star + capability sub-project | `references/init.md` |
| `df review`, "复盘昨天", morning before plan when yesterday is open | Sync publish links; capture feedback; write task Review + `reviewed`; refresh Latest Snapshot; auto-check ladders; optional focus tweak | `references/review.md` |
| `df plan`, morning, "今天做什么" | Hard-gate on yesterday `reviewed`; ISO Sunday / month-end week/month gates; candidates from **latest** objective; prefer article/script | `references/plan.md` |
| `df ship`, evening, "写出来", "收工" | Action status + dual-write v1 draft + editable export copy only | `references/ship.md` |
| `df comment`, "点评" | Optional; confirm 终稿; four-line critique; set `commented` | `references/comment.md` |
| `df final`, "定稿", "配图", "校准" | Confirm 终稿; article: illustrate + OSS; calibrate; publish handoff. script: skip illustrate/OSS | `references/final.md` |

If the mode is ambiguous:

1. Explicit `df review` / `comment` / `final` / `plan` / `ship` wins.
2. Else if today's `## Actions` is empty → `plan` (after reminding about `review` if the gate would fail).
3. Else if today's task has no `## Outcomes` v1 → `ship`.
4. Else ask whether they want `comment` or `final`.

Typical day: `review` → `plan` → work → `ship` → hand-edit → optional `comment` → `final` → publish → next morning `review`.

## Rules that apply to every mode

1. **One question turn.** Collect all inputs for a phase in a single numbered question block and wait for one reply. Ritual overhead is what kills daily systems; do not spread questions across turns.
1b. **Respect `LANGUAGE`.** All chat with the user (questions, candidate tables, closers, gate messages) uses `references/i18n.md` for the active `LANGUAGE`. Accept answers in either language. Vault **schema** keys stay as in `conventions.md` (not translated). Draft bodies use `draft_language` from article config if set, else `LANGUAGE`.
2. **Never write Templater syntax** into agent-written daily/task notes. Templater does not render those. Do not write a bare template open-marker into a vault file even as prose or inside backticks. Describe it in words instead. Editing the vault's Templater *template* files is allowed when the user asked for template updates.
3. **A live Obsidian instance will rewrite what you write.** Linter strips trailing whitespace after empty YAML values and `update-time-on-edit` rewrites `DateModified`. Expect a diff larger than your edit, and never treat that as corruption.
4. **Never scan a vault recursively without a narrow path filter.** Use the exact scoped commands in `conventions.md`.
5. **Read filenames and frontmatter, never note bodies**, unless the mode requires a named file (export draft, task Outcomes, objective ladders, etc.).
6. **Never invent industry trends or news.** Justification for "why today" must cite the user's own state from the objective / profile / yesterday's files.
7. **Respect the time budget as a hard ceiling.**
8. **Structured output only.** Candidate lists, plans, and reviews are tables or short bullets. Long prose is the article/script in `ship` (and image prompts inside `final`).
9. **Edit in place, additively.** Preserve existing content; fill empty sections rather than rewriting files.
10. **Feedback numbers are recorded, not trend-analyzed, for the first 7 days.** Auto-checking a ladder when a threshold is met is allowed. Optimization proposals in `df review` may use controllable process signals from day one; engagement *trends* unlock on day 8+.
11. **Privacy.** Goal text, ladder thresholds, baselines, Latest Snapshot totals, and account names stay in the vault / gitignored configs. Open-source skill files and public README examples use placeholders only.
