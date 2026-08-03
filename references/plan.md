# Mode: plan (morning)

Closes out yesterday and decides today. This is the mode that fixes the stall, so its job is narrow: hand the user a deliverable they can finish today and a plan sized to the hours they actually have.

Read the objective file first: `{{DAILY_VAULT}}\Projects\Scope\TechSkills\AI\ai-agent-flywheel.md`. If it is missing, run `init` instead. Then read yesterday's daily note and yesterday's task file — those two files plus the objective are the entire context. Do not read further back except on the Day 7 checkpoint defined at the end of this file.

## Step 1 — One question block

Ask everything at once, numbered, then wait for a single reply.

```
1. 今天有多少可支配时间？（决定今天能做什么，我会按这个硬卡上限）
2. 昨天那个成果做完了吗？实际花了多久？
3. 昨天发出去的东西有反馈数字吗？（点赞/评论/转发/关注，没有就跳过）
4. <从 objective 的 Open Questions 里取 1-2 个能力问题，要证据>
```

Day one has no items 2 and 3 — drop them rather than asking the user to type "无".

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

Fold the reply to question 4 into the objective file's Skill Profile table, and move the answered items out of Open Questions. Apply the calibration rules from `init.md`: evidence that names a specific artifact, failure, or trade-off supports the level; a restated concept does not.

Also fold in yesterday's outcome as evidence — actually shipping something is stronger evidence than any self-report, and should raise the relevant level.

## Step 4 — Dedup scan

Run the scoped scans from `conventions.md`. Compare against `Covered Topics` in the objective file and refresh it if new notes appeared. A topic already written is not a candidate unless the angle is genuinely new, and then the candidate must say what is new.

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

### Candidate table

| 成果 | 类型 | 难度 | 价值 | 预期耗时 | 为什么是今天 |
|------|------|------|------|----------|--------------|

Rules for the table:

- **预期耗时 must fit inside the hours reported in step 1.** Anything over is not listed. If a good idea is too big, list the first slice of it as its own finishable deliverable and say what the slice is.
- **难度** relative to the user's current profile levels, not in the abstract: 舒适区 / 够一够 / 有风险。At least one candidate should be 舒适区 so a low-energy day still ships.
- **价值** is justified by one of: 直接推进某个里程碑 / 把画像里某个低等级能力推上去 / 是连载的下一集，有复利 / 产出物本身能被反复复用。Say which.
- **为什么是今天** may cite only the user's own state — 画像缺口、昨天的自然下一步、某个停着的残稿今天能收尾、里程碑还差这块、今天时间少所以只有这个能真做完。Never cite industry trends or news; there is no live data behind such a claim.

Present the table, then wait for the user to choose. They may also reject all of them and name their own — that is a fine outcome, go to step 6 with their idea.

## Step 6 — Resources and prior art

For the chosen deliverable, gather what goes into the task's `## Reference`:

- 2 to 4 high-quality resources: official docs sections, a specific repo, a specific paper or talk. Name them precisely — `owner/repo`, doc section title, paper title and authors.
- 1 to 2 成功案例: an existing article or project that did this well, and one sentence on what makes it good, so there is a bar to aim at.

**Do not fabricate URLs.** Name the resource precisely and let the user find it, or offer a web search if they want live links. A wrong link costs more time than no link.

## Step 7 — Write the plan

Create the task file at `Tasks\New\Backlog\<prefix>-<slug>.md` per `conventions.md`:

- `## Purpose` — the deliverable in one sentence plus the "why today" line from the table
- `## Reference` — step 6
- `## Actions` — the checkbox plan
- `status: 🟡Doing`, `DateStarted` today

The action plan must budget the writing, not just the doing. A day that spends all its hours building and none writing produces nothing publishable, which is exactly the failure that drained motivation before. Reserve roughly a quarter of the time for turning it into the deliverable, and make that a checkbox of its own.

Every item gets a start date so the daily note's Todo block picks it up:

```markdown
- [ ] 把三种分块策略各跑一遍，记录 chunk 数和检索命中 🛫 2026-08-03
- [ ] 整理成对比表 🛫 2026-08-03
- [ ] 写成文章草稿 🛫 2026-08-03
```

Then write today's daily note at `Daily\YYYY-MM-DD.md` — fully rendered, no `<%` anywhere. Put in `## Actions`:

- a link to today's task file
- today's time budget
- the same checkboxes

Finally, tell the user in chat: the deliverable, the time budget, the first action to start with, and nothing else. They have already read the table; do not restate it.

The user can edit any of these files by hand, add their own tasks, or throw the plan out. That is the point of keeping everything in markdown — do not treat the generated plan as authoritative on the next run, always re-read the files.

## Day 7 checkpoint

On the seventh day since the objective file's `DateStarted`, run this before step 1. It is the only day that reads the full week — 7 daily notes and 7 task files.

The purpose is to decide whether Phase 1 (a Python service) is justified, and the default answer is no. Building the tool is the most seductive way to avoid using it.

Report, in this order:

1. **闭环完成率** — 7 天里有几天真的产出了可贴链接的东西. Fewer than 5 means the flywheel itself is the problem; fix it before anything else.
2. **哪几步真用上了** — for each of the 7 steps in this mode plus the 7 in `ship`, mark 用了 / 走过场 / 没碰. Steps nobody used are dead weight and should be cut from the reference file, not ported to Python.
3. **手工痛点排序** — what the user retyped, re-explained, or worked around most. This is the only valid input to what Phase 1 should automate first.
4. **估时准确度** — actual vs estimated across 7 days, and whether the bias is consistent.
5. **反馈趋势** — now unlocked. Which deliverable types and titles drew response. Still label it weak evidence at n=7.

Then ask the one decision question: 继续跑 Phase 0、砍掉某几步继续跑、还是开始写 Phase 1。Do not recommend Phase 1 unless a specific manual pain shows up on at least 4 of the 7 days.
