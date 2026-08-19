---
name: daily-flywheel
description: >-
  Daily output flywheel for an Obsidian vault: reviews yesterday against the
  north-star objective, plans a finishable content deliverable for today, ships
  a v1 draft, optionally critiques the hand-edited final, then illustrates /
  calibrates / hands off publish. Use when the user invokes daily-flywheel, df,
  df plan, df review, df ship, df comment, df final, df study, 飞轮, 日更, or
  asks what to produce today / to close out yesterday / to ship or finalize the
  day's output / to learn a book chapter or resource with questions (学习某章 /
  带问题读 / 读书笔记).
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
| `HOT_TOPICS_FILE` | Optional gitignored markdown of last-7-day sourced topics for `df plan`. Defaults to `local.hot-topics.md` in this skill directory |
| `CODESPACE_DIR` | Local clone root for third-party repos. **Always** clone here (never elsewhere). |
| `TRENDRADAR_DIR` | Path of the [TrendRadar](https://github.com/sansan0/TrendRadar) clone. Defaults to `{{CODESPACE_DIR}}/TrendRadar`. Used by `df plan` hot-topic refresh. |
| `STUDY_CARDS_DIR` | Optional. Write-allowed dir for study cards + theme note (sole exception to read-only `NOTES_VAULT`). Blank disables `df study`. |
| `STUDY_DECK_PREFIX` | Optional. Anki deck prefix for study cards, e.g. `AI-Engineering`. |
| `STUDY_TYPES` | Optional. Comma list of supported learning kinds: `book, tutorial, codebase, video`. Extend by editing this key. |
| `SCRIPT_STYLE_PATH` | Optional. Distilled **video** house style for `df ship` when `deliverable: script`. Absolute path. Blank → script ship refuses. Never read this on article days. |
| `SCRIPT_CRAFT_PATH` | Optional. Gitignored script outline bars (`script-craft.md` in this directory by default). Copy `script-craft.example.md`. Never commit the working file; never fall back to `article-craft.md`. |
| `SCRIPT_PACK_DIR` | Optional. Root folder for video packs when `deliverable: script`. Set only in gitignored `local.config.md`. Never write the resolved OS path into this repository, examples, or chat. |
| `SCRIPT_PACK_SAMPLE` | Optional. Folder name (not a path) of the sample pack to copy. Default layout: `YYMMDD-slug/` with `{id}-project.md`, `{id}-script.md`, later `{id}-script-final.md` / shot-list / editing / publishing checklists. |

If `local.config.md` does not exist, stop and tell the user to copy `local.config.example.md` to `local.config.md` and fill it in. Do not guess a vault path, and do not proceed with placeholders unresolved — writing to a guessed path scatters files into the wrong vault.

If `NOTES_VAULT` is absent or points nowhere, skip dedup scanning rather than failing.

`local.config.md` holds **locations, publish-slot key names, optional private archetypes, and optional OSS keys**. The goal itself — dimensions, thresholds, baseline numbers, accounts, Latest Snapshot — lives **only** in the objective note inside the vault (plus other vault task/daily files). Per-channel export steps live in `local.article.config.md` under `publish_export`. **Never copy goal content, ladder numbers, account names, or channel-specific tactics into this repository**, not even into passing prose, commit messages, or examples. When a reference file needs an example, it uses a placeholder or an obviously invented value.

### Article config

Article drafts (`df ship`) and article finalize (`df final`) require `local.article.config.md` (gitignored). Copy from `local.article.config.example.md`. Distilled house style lives in `local.article.style.md` (copy `local.article.style.example.md`); `df ship` reads that file instead of long sample essays. Learned edit rules from v1→final diffs live in `local.article.memory.md` (also gitignored; incremental, no 7-rule cap). `df ship` priority: house style → comment/scorecard bars → memory. Memory rules must stay abstract — never store private goal totals there. Plan-time hot topics live in `HOT_TOPICS_FILE` (gitignored).

If the article config is missing when an article deliverable needs it, refuse to draft/finalize — do not silently fall back to an unconfigured write.

Script drafts (`deliverable: script`) read `SCRIPT_STYLE_PATH` + `SCRIPT_CRAFT_PATH` only. They must **not** open `local.article.style.md`, `article-craft.md`, or `local.article.memory.md`. If either script path is missing, refuse to draft.

Script and related files always land in a new pack under `SCRIPT_PACK_DIR`, copying the filename set of `SCRIPT_PACK_SAMPLE`. Do **not** write scripts into the notes-vault `insights-to-share` tree. Do **not** paste absolute disk paths into committed skill files, examples, or user-facing chat — say `SCRIPT_PACK_DIR/<folder>` or the vault-relative pack name.

## Routing

Always read `references/conventions.md` first — it holds every path, schema, and hard constraint. Resolve `LANGUAGE` from `local.config.md` (default `zh`) and skim `references/i18n.md` for that language's user-facing strings. Then read **exactly one** mode reference. Never read all mode refs. `df plan` / `df ship` / `df comment` may also read `references/article-craft.md` (abstract slots only).

| Trigger | Mode | Reference |
|---------|------|-----------|
| `df init`, first ever run, or `{{OBJECTIVE_FILE}}` is missing | Bootstrap north-star + capability sub-project | `references/init.md` |
| `df review`, "复盘昨天", morning before plan when yesterday is open | Sync publish links; capture feedback; write task Review + `reviewed`; refresh Latest Snapshot; auto-check ladders; optional focus tweak | `references/review.md` |
| `df plan`, morning, "今天做什么" | Hard-gate on yesterday `reviewed`; ISO Sunday / month-end week/month gates; candidates from **latest** objective + URL-backed hot topics; prefer article/script | `references/plan.md` |
| `df ship` [`date`], evening, "写出来", "收工" | **Manual only**; target-day status + topic/outline-gated dual-write v1 (funnel skeleton; style abstract + memory) | `references/ship.md` |
| `df comment` [`date`], "点评" | Optional; same target-day rule; confirm 终稿; advisory scorecard + critique; set `commented` | `references/comment.md` |
| `df final` [`date`], "定稿", "配图", "校准" | Optional; same target-day rule; illustrate/OSS/calibrate/handoff | `references/final.md` |
| `df study <资源> [--type book|codebase|video|tutorial]`, "学习", "带问题读", "读某章" | Optional question-driven reading loop routed by resource type: questions (all upfront) → answers/reflection → evaluation → Anki-ready cards → article feed | `references/study.md` |

**Target day** (ship/comment/final only): `YYYY-MM-DD` / `today`/`昨天`/`yesterday`/`今天`; omit = calendar today. See `conventions.md`. Stamps (`✅`, `DateDone`, `commented`) use calendar today; files read/written are the target day's.

If the mode is ambiguous:

1. Explicit `df review` / `comment` / `final` / `plan` / `ship` wins (parse any date arg for the last three).
2. Else if today's `## Actions` is empty → `plan` (after reminding about `review` if the gate would fail).
3. Else if today's task has no `## Outcomes` v1 → `ship`.
4. Else ask whether they want `comment` or `final`.

Typical day: `review` → `plan` → work → `ship` → hand-edit → optional `comment` → `final` → publish → next morning `review`. Study day: `review` → `plan` → study (questions given upfront → read → answers) → confirm cards → next morning `review`. Backfill: `df ship yesterday` then `df comment yesterday` / `df final yesterday`.

## Rules that apply to every mode

1. **One question turn.** Collect all inputs for a phase in a single numbered question block and wait for one reply. Ritual overhead is what kills daily systems; do not spread questions across turns.
1b. **Respect `LANGUAGE`.** All chat with the user (questions, candidate tables, closers, gate messages) uses `references/i18n.md` for the active `LANGUAGE`. Accept answers in either language. Vault **schema** keys stay as in `conventions.md` (not translated). Draft bodies use `draft_language` from article config if set, else `LANGUAGE`.
2. **Never write Templater syntax** into agent-written daily/task notes. Templater does not render those. Do not write a bare template open-marker into a vault file even as prose or inside backticks. Describe it in words instead. Editing the vault's Templater *template* files is allowed when the user asked for template updates.
3. **A live Obsidian instance will rewrite what you write.** Linter strips trailing whitespace after empty YAML values and `update-time-on-edit` rewrites `DateModified`. Expect a diff larger than your edit, and never treat that as corruption.
4. **Never scan a vault recursively without a narrow path filter.** Use the exact scoped commands in `conventions.md`.
5. **Read filenames and frontmatter, never note bodies**, unless the mode requires a named file (export draft, task Outcomes, objective ladders, etc.).
6. **Never invent industry trends or news.** Hot-topic refresh (`df plan`; `df ship` must not open a second scrape) is **AI-themed only**. Prefer **TrendRadar** (MCP or `scripts/trendradar_hot_topics.py`) for zhihu / douyin / bilibili; WebSearch is fallback (and for x / youtube / google). Queries include `AI` / `人工智能` (or a named AI product); general trending tabs do not count. **Hot topics angle today's work; they are never the deliverable.** An article/script must be evidenced by a named action from today's task (or work already done today). A news recap of `HOT_TOPICS_FILE` with no lived step is invalid even if every row has a URL. Why-today cites the objective / profile / yesterday **and** today's action; a URL-backed AI row is optional seasoning. If a source was not fetched or had no AI hit, write `未取到` — do not fabricate titles or links. Clone TrendRadar only into `CODESPACE_DIR` from `local.config.md`.
7. **Respect the time budget as a hard ceiling.**
8. **Structured output only.** Candidate lists, plans, and reviews are tables or short bullets. Long prose is the article/script in `ship` (and image prompts inside `final`).
9. **Edit in place, additively.** Preserve existing content; fill empty sections rather than rewriting files.
10. **Feedback numbers are recorded, not trend-analyzed, for the first 7 days.** Auto-checking a ladder when a threshold is met is allowed. Optimization proposals in `df review` may use controllable process signals from day one; engagement *trends* unlock on day 8+.
11. **Privacy.** Goal text, ladder thresholds, baselines, Latest Snapshot totals, and account names stay in the vault / gitignored configs. Open-source skill files and public README examples use placeholders only.
12. **Study is optional and card-writing is gated.** `df study` runs only on request. Cards are drafted, confirmed with the user, then written to `STUDY_CARDS_DIR` (the only write exception to read-only `NOTES_VAULT`). Cards are internal review material — no goal numbers, no counters. Articles must rephrase card content; citation goes at the end, never inline pasted cards.
13. **Articles are manual-ship and topic-gated.** `df ship` runs only on explicit user request — no mode auto-triggers article generation. Before drafting an article body: brainstorm the topic (use the `brainstorming` skill when available) → confirm; build the outline (use the `writing-assistant` skill when available) → confirm; only then write v1. Both gates are hard; no multi-draft fishing.
