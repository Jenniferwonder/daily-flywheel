# Mode: plan (morning)

Decides today. Does **not** close yesterday — that is `df review`. Job: hand the user a finishable deliverable sized to today's hours, aligned to the **latest** objective note.

User-facing strings: `references/i18n.md` keys under `## plan` for `LANGUAGE`. Article-candidate craft: `references/article-craft.md`.

Read the north-star objective first: `{{DAILY_VAULT}}\{{OBJECTIVE_FILE}}` — Purpose, `## 维度字典`, ladders, `## Latest Snapshot`, `## This Year` / `## This Month` / `## This Week`, Baseline. Then capability sub-project `{{CAPABILITY_FILE}}` for Skill Profile, Open Questions, Covered Topics. If the north-star file is missing, run `init` instead. Read today's daily note if it exists. On ISO Sunday also skim this week's daily `## Actions` / task Outcomes (scoped). On calendar month-end skim this month's week Review headers if they exist.

**Privacy:** never copy objective thresholds, counters, or account details into this repository.

## Step 0 — Yesterday-reviewed hard gate

Before any candidate work:

1. Open **yesterday's** daily note. Resolve main task from `## Actions` (`- 任务：[[...]]`).
2. **No yesterday daily / no main task link** (e.g. day one): skip gate; continue.
3. If main task exists and frontmatter `reviewed` is empty: **STOP**. Do not write today's Actions, do not present candidates. Show `plan.gate_need_review` for `LANGUAGE`. **No skip escape.**
4. If `reviewed` is a date: continue.

## Step 0b — Weekly / monthly review gates

Same as before; runs after Step 0. Weekly first, then monthly when both fire.

### When today is an ISO Sunday — weekly review + next-week plan

1. Path: `Daily\YYYY\YYYY-Qn\YYYY-MM\YYYY-Www\YYYY-Www.md`  
   Template shape: `Templates\Tp-Daily\tp-Weekly.md` — fully rendered, no Templater markers.
2. Draft from this week's daily Actions, task Outcomes / Reviews, objective ladders + Latest Snapshot + This Month/Year, capability progress. Fill 成就 / 离大目标 / Next Week plan; fill 分项快照 from Latest Snapshot (not invented numbers).
3. One confirmation block (max 3): use `plan.week_confirm` for `LANGUAGE`, then wait.
4. Write/update week note; **overwrite** objective `## This Week` with the agreed focus.
5. Continue to Step 0c, then Step 1.

### When today is a calendar month-end — monthly review + next-month plan

1. Path: `Daily\YYYY\YYYY-Qn\YYYY-MM\YYYY-MM.md` — template `tp-Monthly.md`, fully rendered.
2. Draft from week Reviews, Outcomes, objective ladders + This Year + prior This Month; 月末分项快照 from Latest Snapshot vs Baseline.
3. One confirmation block (max 3): use `plan.month_confirm` for `LANGUAGE`, then wait.
4. Write/update month note; **overwrite** objective `## This Month`.
5. Continue to Step 0c, then Step 1. Merge W/M questions into one turn when both fire.

If neither gate applies, skip Step 0b.

## Step 0c — Focus cascade sync (silent, every morning)

1. Compare objective `DateModified` to today's month note and week note.
2. Create a missing note if needed (Focus mirror + snapshot skeleton; leave Review/Plan for review day).
3. Refresh a stale Focus mirror from `## This Month` / `## This Week` (objective wins; never merge).
4. Leave Baseline immutable; net growth uses Baseline + Latest Snapshot.
5. Report in one line only when a mirror actually changed.

## Step 1 — One question block

Ask once (`plan.q_block` for `LANGUAGE`), then wait. On Sunday/month-end, finish Step 0b confirmations **before** this block.

Include hot-topics refresh as item 3 (`plan.q_hot`). If `HOT_TOPICS_FILE` is missing or `updated` is older than 7 days, say so in the question (`plan.hot_stale`).

No yesterday-completion / feedback questions here — those belong to `df review`.

## Step 2 — Update the profile

Fold the reply to question 2 into the capability Skill Profile; move answered items out of Open Questions. Evidence must name a specific artifact, failure, or trade-off.

## Step 3 — Dedup scan + hot topics

Scoped scans from `conventions.md`. Refresh Covered Topics when new notes appeared. Already-written topics are not candidates unless the angle is genuinely new.

**Hot topics** (after Step 1 reply), path from `HOT_TOPICS_FILE` (default `local.hot-topics.md` in the skill directory):

1. User said **yes**, or file missing / `updated` >7 days **and** user did not say **no**: WebSearch AI topics for the last ~7 days on douyin / zhihu / x / youtube. Write only URL-backed rows. Source with no hit → `未取到`. Never invent titles or links. Set `updated` to calendar today.
2. User said **no**: read the existing file as-is. If missing or stale, candidates may still run but Why-today must say `无可用热点，只服务本周格子` (or the `en` equivalent).
3. Do not copy hot-topic titles into this repository.

## Step 4 — Build candidates

Produce 3 to 5 candidates. **Re-read the objective note immediately before building** so Snapshot, ladder checks, and any `df review` edits to This Week are included. Apply the **three-way filter** in `article-craft.md` (who × situation × information increment vs Covered Topics). Drop slogan rows.

### Deliverable bias (hard preference)

Default every day toward a shippable **`article` (`pub-*`) or `script` (`script-*`)**. Pure engineering may appear only as a **slice inside** that content day, not as the sole daily outcome. Open-source-only rows are allowed only when they clearly unblock a named `goalStep` **and** the user overrides after seeing content-first candidates.

When writing the task (Step 6), set frontmatter `deliverable: article | script | other`.

### Deliverable archetypes

**Article**

| Archetype | Typical time |
|-----------|--------------|
| 选型对比：两三个方案的取舍表 + 结论 | 60-90 min |
| 踩坑复盘：一个具体报错，从现象到根因到修法 | 60-90 min |
| 工作流拆解：把自己的一个 AI 用法写成可复制流程 | 60-90 min |
| 概念拆解：一个类比讲清一个抽象概念 | 60-90 min |
| 最小可运行示例：30 行代码讲透一个机制 | 90-120 min |
| 系列连载的下一集 | 视上一集而定 |
| 源码走读：一条调用链 | 2-3 h |

**Script (short video)**

| Archetype | Typical time |
|-----------|--------------|
| 文章 → 短视频成稿包：标题/口播/分镜/导流 | 60-90 min |
| 仿写样本脚本（先有风格总结） | 60-90 min |

**Open source** (secondary; see bias above)

| Archetype | Typical time |
|-----------|--------------|
| 一个 skill / prompt / 配置资产开源 | 60-90 min |
| 清单或 awesome 仓库 | 60-90 min |
| 给现有项目提一个有内容的 issue 或小 PR | 1-2 h |
| 最小 demo 仓库，README 可复现 | 2-3 h |
| 一个能自己天天用的小 CLI | 2-3 h |

**Extra archetypes** — if `EXTRA_ARCHETYPES` in `local.config.md` is non-empty, append those rows. Private; never commit into this repository.

### Candidate table

Use header row `plan.candidate_headers` and difficulty labels `plan.difficulty` for `LANGUAGE`.

Rules:

- Est. time ≤ hours from Step 1; else omit or slice.
- Difficulty: at least one Comfort / 舒适区 row.
- `goalDim` + `goalStep` mandatory; `goalStep` copied verbatim from the objective.
- Reject slogan candidates.
- Why-today: `## This Week` + **one URL-backed hot-topics row** (or explicit no-hot-topic fallback). Then Month/Year, profile gaps, time ceiling. Never invent industry trends.
- At least one candidate advances `## This Week` when that section is non-empty.
- Candidate **cell text** (titles, why-today) in `LANGUAGE`.

Present the table, wait for a choice (or user-named alternative with goalDim + goalStep).

## Step 5 — Resources and prior art

2–4 precise resources + 1–2 success cases for `## Reference`. Do not fabricate URLs.

## Step 6 — Write the plan

Create `Tasks\New\Backlog\<prefix>-<slug>.md`:

- `goalDim` + `goalStep` hard gate
- `deliverable: article | script | other`
- `reviewed` / `commented` left empty
- `## Purpose` / `## Reference` / `## Actions`
- `status: 🟡Doing`, `DateStarted` today
- Budget writing (or script packaging) as its own checkbox (~¼ of time)

Action items need `🛫 YYYY-MM-DD`.

Write today's daily note `## Actions` as **aggregation headers only** (fully rendered): 今日产出, task link, `维度::` / `目标格::`, objective / week / month links, time budget, optional 备注. Optionally one line: 待办只在任务卡. **Never** copy task `## Actions` checkboxes into the daily note — Tasks Todo/Done queries aggregate them. Do **not** write yesterday's Review.

Chat: deliverable, budget, ladder cell, first action. Nothing else.

## Day 7 checkpoint

On the seventh day since the capability note's `DateStarted`, run before Step 1. Read 7 dailies + 7 tasks.

Report: 闭环完成率 / 哪几步真用上了（include review/comment/final) / 手工痛点 / 估时准确度 / 反馈趋势（now unlocked）/ 阶梯移动（from objective, do not paste private totals into the skill repo).

Ask: 继续 Phase 0、砍步骤、还是 Phase 1 — recommend Phase 1 only if a manual pain appears on ≥4 of 7 days.
