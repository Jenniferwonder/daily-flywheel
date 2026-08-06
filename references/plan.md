# Mode: plan (morning)

Closes out yesterday and decides today. This is the mode that fixes the stall, so its job is narrow: hand the user a deliverable they can finish today and a plan sized to the hours they actually have.

Read the north-star objective first: `{{DAILY_VAULT}}\{{OBJECTIVE_FILE}}` — Purpose, `## 维度字典`, every result ladder it declares, `## This Year`, `## This Month`, `## This Week`, Baseline table. Then read the capability sub-project `{{DAILY_VAULT}}\{{CAPABILITY_FILE}}` for Skill Profile, Open Questions, Covered Topics, engineering milestones. If the north-star file is missing, run `init` instead. Then read yesterday's daily note and yesterday's task file. On ISO Sunday also read this week's daily `## Actions` / task Outcomes (scoped, not the whole vault). On calendar month-end also skim this month's week notes' Review headers if they exist. Do not read further back except on the Day 7 checkpoint.

## Step 0 — Review yesterday + sync publish links (before asking anything)

Do this **before** Step 0b / 0c / 1. It is silent bookkeeping, not a question turn.

1. **Review yesterday's completion** from the daily note `## Actions` checkboxes and the linked task file: how many items done, whether `status` / `DateDone` match, whether `## Outcomes` exists. Note gaps for Step 2; do not re-ask what the files already answer.
2. **Locate yesterday's article(s)** under `{{NOTES_VAULT}}\ai\insights-to-share\`:
   - Prefer the export path recorded in the task `## Outcomes` (`终稿路径` / `pub-*`).
   - Else a shallow listing of `insights-to-share\pub-*\*.md` only (filenames, not recursive vault scan); match by `DateStarted` = yesterday or by slug mentioned in yesterday's task.
3. **Read only the article frontmatter** for every key in `PUBLISH_SLOTS` from `local.config.md` (and `cover` if useful). Do not read the article body unless matching failed.
4. **If any publish URL is non-empty** and the corresponding task YAML field is empty or still a non-URL placeholder (account name only):
   - Write the URLs into the matching task frontmatter keys from `PUBLISH_SLOTS`.
   - Append or refresh **成果落点** under yesterday's daily `## Review` (成稿路径 + 各发布链接).
   - Optionally refresh a local publish index note when the user maintains one.
5. **If URLs are still empty** in the article YAML, leave a one-line note in the task `## Review` (`发布链接: 文章 frontmatter 仍空`) and include the ask in Step 1 item 5 — do not invent links.

This step exists because publish often happens after `df ship`; morning `df plan` is the reliable sweep that keeps diary + task + article YAML aligned.

## Step 0b — Weekly / monthly review gates

Run after Step 0. Either gate may fire on the same morning; do weekly first, then monthly.

### When today is an ISO Sunday — weekly review + next-week plan

1. Resolve paths from today's date (ISO week, week folder under Monday's month):
   `Daily\YYYY\YYYY-Qn\YYYY-MM\YYYY-Www\YYYY-Www.md`
   Template shape: `Templates\Tp-Daily\tp-Weekly.md` — **agent must write a fully rendered note** (all dates literal). Never leave Templater markers in the written file.
2. Draft from files only: this week's daily `## Actions` / Reviews, linked task `## Outcomes`, the objective's ladders + `## This Month` / `## This Year`, capability progress on the sub-project. Fill:
   - Review · 成就（产出了什么 / 改进了什么）
   - Review · 离大目标更近了吗 — must cite ladder cells, and fill 分项快照 with this week's counter values and net change against the immutable baseline
   - Plan · Next Week（重点产出 / 要改进什么 / 为什么）
3. Ask **one** confirmation block (max 3 items), then wait:
   ```
   W1. 本周成就有无漏记？（补一条或「无」）
   W2. 下周重点产出选哪 1–2 个？（可改我的草稿；每条须点名 goalDim + goalStep）
   W3. 下周改进项有否决的吗？本周的计数指标现在能给数字吗？
   ```
4. Write/update the week note; **overwrite** the objective's `## This Week` with the agreed next-week focus (dates + 1–2 deliverables + goalDim/goalStep + why).
5. Continue to Step 0c so the refreshed focus propagates, then Step 1.

### When today is a calendar month-end — monthly review + next-month plan

1. Path: `Daily\YYYY\YYYY-Qn\YYYY-MM\YYYY-MM.md`
   Template shape: `Templates\Tp-Daily\tp-Monthly.md` — fully rendered, no Templater markers.
2. Draft from this month's week Reviews, daily/task Outcomes, the objective's ladders + `## This Year` + prior `## This Month`. Fill 月末分项快照 with net growth against the baseline.
3. Ask **one** confirmation block (max 3 items):
   ```
   M1. 本月成就有无漏记？结果阶梯有无新勾选？
   M2. 下月 1–3 个焦点选哪些？（至少 1 条落在结果阶梯，且带可验收数字）
   M3. 下月改进项有否决的吗？是否仍服务 This Year？
   ```
4. Write/update the month note; **overwrite** the objective's `## This Month` with next month's focus.
5. Continue to Step 0c, then Step 1. If both Sunday and month-end hit, merge W/M confirmations into one question turn (W* then M*), write week+month files, then continue.

If neither gate applies, skip Step 0b.

## Step 0c — Focus cascade sync (silent, every morning)

The objective also changes on days that are neither Sunday nor month-end. Without this step those edits never reach the notes the user actually opens, and the year → month → week → day chain silently breaks.

1. Compare the objective note's `DateModified` against today's month note and week note (paths in `conventions.md`).
2. **Create a missing note** — mid-period is fine: fill the `## Focus` mirror and the snapshot skeleton, leave `## Review` / `## Plan` for the review day.
3. **Refresh a stale mirror** by overwriting the `## Focus` table from `## This Month` / `## This Week`, keeping each row's `goalDim` + `goalStep`, and updating that section's 最后同步 date. Never merge — the objective wins.
4. Leave baseline rows untouched; net growth is always computed against the objective's immutable baseline.
5. Say nothing unless a mirror actually changed; then report it in one line alongside Step 2's summary.

## Step 1 — One question block

Ask everything at once, numbered, then wait for a single reply. On Sunday/month-end, run Step 0b confirmations **before** this block.

```
1. 今天有多少可支配时间？（决定今天能做什么，我会按这个硬卡上限）
2. 昨天那个成果做完了吗？实际花了多久？（Step 0 已从文件读过的，只求确认或补差）
3. 昨天发出去的东西有反馈数字吗？（点赞/评论/转发/关注，没有就跳过）
4. <从能力子工程的 Open Questions 里取 1-2 个能力问题，要证据>
5. （仅当昨天 task ## Review 含「校准: 待收」，或 Step 0 发现发布链接仍空时）导出路径终稿定了吗？/ 发布链接补哪几个？
```

Day one has no items 2 and 3 — drop them rather than asking the user to type "无".
Drop item 5 when there is no deferred calibration **and** Step 0 already synced all links.

Never split this across turns. If the reply is partial, work with what came back and note the gap; do not re-interrogate.

## Step 2 — Close out yesterday

Write into yesterday's daily note `## Review` and yesterday's task file `## Review`.

For the first 7 days, review **only controllable items**:

- 完成率: 计划的动作做完了几项
- 耗时偏差: 实际 vs 预估，以及偏差的原因
- 一句话自评: 用户自己的判断
- `ToImprove::` 一条，必须是明天能立刻执行的，不是"要更专注"这类

Do not analyze like counts. Record the numbers into the task's `## Review` verbatim and move on. Say so out loud once if the user seems to expect analysis:

> 反馈数字我先记着不分析 —— 一天一篇、样本这么小的时候，点赞波动说明不了任何事，硬分析只会得到一堆听着有道理的废话。攒够 7 天我再做跨篇趋势。

Once 7 or more days of feedback exist, add a trend pass: which deliverable types drew more response, which titles, which publish times. Still label it as weak evidence.

## Step 3 — Update the profile

Fold the reply to question 4 into the capability note's Skill Profile table, and move the answered items out of Open Questions. Apply the calibration rules from `init.md`: evidence that names a specific artifact, failure, or trade-off supports the level; a restated concept does not.

Also fold in yesterday's outcome as evidence — actually shipping something is stronger evidence than any self-report, and should raise the relevant level.

## Step 4 — Dedup scan

Run the scoped scans from `conventions.md`. Compare against `Covered Topics` in the capability note and refresh it if new notes appeared. A topic already written is not a candidate unless the angle is genuinely new, and then the candidate must say what is new.

## Step 5 — Build candidates

Produce 3 to 5 candidates. This step exists because the user's stated blocker is 不确定能有哪些学习成果产出 — so the candidates must be concrete enough to start immediately, not categories.

### Deliverable archetypes

Draw from these rather than inventing a shape each time. Times assume the writing is included.

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

**Open source**

| Archetype | Typical time |
|-----------|--------------|
| 一个 skill / prompt / 配置资产开源 | 60-90 min |
| 清单或 awesome 仓库 | 60-90 min |
| 给现有项目提一个有内容的 issue 或小 PR | 1-2 h |
| 最小 demo 仓库，README 可复现 | 2-3 h |
| 一个能自己天天用的小 CLI | 2-3 h |

**Extra archetypes** — if `EXTRA_ARCHETYPES` in `local.config.md` is non-empty, append those rows to the pool. They are private and never belong in this repository. If the key is blank or missing, skip this pool.

### Candidate table

| 成果 | 类型 | goalDim | goalStep | 难度 | 预期耗时 | 为什么是今天 |
|------|------|---------|----------|------|----------|--------------|

Rules for the table:

- **预期耗时 must fit inside the hours reported in step 1.** Anything over is not listed. If a good idea is too big, list the first slice of it as its own finishable deliverable and say what the slice is.
- **难度** relative to the user's current profile levels, not in the abstract: 舒适区 / 够一够 / 有风险。At least one candidate should be 舒适区 so a low-energy day still ships.
- **`goalDim` + `goalStep` are mandatory columns.** `goalStep` must be copied verbatim from a ladder cell or a `## This Month` item in the objective note. A candidate that cannot name one is not a candidate — drop it rather than inventing a cell.
- **Reject slogan candidates**: anything justified only by a vague phrase with no ladder cell (no number, date, or named artifact). Capability work qualifies only when the row says which ladder cell it unblocks.
- **为什么是今天** may cite only the user's own state — **优先** `## This Week`，其次 `## This Month` / `## This Year`、画像缺口、昨天的自然下一步、残稿收尾、今天时间硬上限。Never cite industry trends or news; there is no live data behind such a claim.
- At least one candidate must advance `## This Week` when that section is non-empty. If a candidate ignores the week focus, say why it still wins today (e.g. it unblocks the week).

Present the table, then wait for the user to choose. They may also reject all of them and name their own — that is a fine outcome, go to step 6 with their idea, but still make them name `goalDim` + `goalStep`.

## Step 6 — Resources and prior art

For the chosen deliverable, gather what goes into the task's `## Reference`:

- 2 to 4 high-quality resources: official docs sections, a specific repo, a specific paper or talk. Name them precisely — `owner/repo`, doc section title, paper title and authors.
- 1 to 2 成功案例: an existing article or project that did this well, and one sentence on what makes it good, so there is a bar to aim at.

**Do not fabricate URLs.** Name the resource precisely and let the user find it, or offer a web search if they want live links. A wrong link costs more time than no link.

## Step 7 — Write the plan

Create the task file at `Tasks\New\Backlog\<prefix>-<slug>.md` per `conventions.md`:

- frontmatter `goalDim` + `goalStep` — **hard gate, refuse to write the file without both**; `goalStep` must be a real ladder cell, not a restatement of the task
- `## Purpose` — the deliverable in one sentence, the "why today" line, and one line naming which 大目标维度 this serves and how it will be verified. Reference the objective by wiki-link, do not restate its numbers here
- `## Reference` — step 6
- `## Actions` — the checkbox plan
- `status: 🟡Doing`, `DateStarted` today

The action plan must budget the writing, not just the doing. A day that spends all its hours building and none writing produces nothing publishable, which is exactly the failure that drained motivation before. Reserve roughly a quarter of the time for turning it into the deliverable, and make that a checkbox of its own.

Every item gets a start date so the daily note's Todo block picks it up:

```markdown
- [ ] 把三种分块策略各跑一遍，记录 chunk 数和检索命中 🛫 2026-03-05
- [ ] 整理成对比表 🛫 2026-03-05
- [ ] 写成文章草稿 🛫 2026-03-05
```

Then write today's daily note at
`Daily\YYYY\YYYY-Qn\YYYY-MM\YYYY-Www\YYYY-MM-DD.md`
(create quarter / month / ISO-week folders as needed; week hangs under Monday's month) — fully rendered, no `<%` anywhere. Put in `## Actions`:

- a link to today's task file
- `维度::` and `目标格::` lines mirroring the task's `goalDim` / `goalStep`
- links to the objective, this week's note, this month's note
- today's time budget
- the same checkboxes

Finally, tell the user in chat: the deliverable, the time budget, which ladder cell it moves, and the first action to start with. Nothing else — they have already read the table.

The user can edit any of these files by hand, add their own tasks, or throw the plan out. That is the point of keeping everything in markdown — do not treat the generated plan as authoritative on the next run, always re-read the files.

## Day 7 checkpoint

On the seventh day since the capability note's `DateStarted`, run this before step 1. It is the only day that reads the full week — 7 daily notes and 7 task files.

The purpose is to decide whether Phase 1 (a Python service) is justified, and the default answer is no. Building the tool is the most seductive way to avoid using it.

Report, in this order:

1. **闭环完成率** — 7 天里有几天真的产出了可贴链接的东西. Fewer than 5 means the flywheel itself is the problem; fix it before anything else.
2. **哪几步真用上了** — for each step in this mode plus `ship`, mark 用了 / 走过场 / 没碰. Steps nobody used are dead weight and should be cut from the reference file, not ported to Python.
3. **手工痛点排序** — what the user retyped, re-explained, or worked around most. This is the only valid input to what Phase 1 should automate first.
4. **估时准确度** — actual vs estimated across 7 days, and whether the bias is consistent.
5. **反馈趋势** — now unlocked. Which deliverable types and titles drew response. Still label it weak evidence at n=7.
6. **阶梯移动** — which ladder cells moved in 7 days, and net change against the baseline. If no result dimension moved at all, that is the finding, not the tooling.

Then ask the one decision question: 继续跑 Phase 0、砍掉某几步继续跑、还是开始写 Phase 1。Do not recommend Phase 1 unless a specific manual pain shows up on at least 4 of the 7 days.
