# Mode: init

One-time bootstrap. Produces the north-star objective at `{{OBJECTIVE_FILE}}` that `plan` reads every morning, plus the capability sub-project at `{{CAPABILITY_FILE}}` holding the skill profile and engineering milestones.

Gate: if `{{DAILY_VAULT}}\{{OBJECTIVE_FILE}}` already exists, do not re-run. Say it exists, show Purpose + ladders + This Year/Month/Week, and ask whether to refresh the goal, refresh the skill profile on the capability note, or exit. If only a capability-style note exists without a north star, offer to split it (create the north star, slim the capability file) rather than inventing a second unrelated goal.

If `local.config.md` has no `OBJECTIVE_FILE`, ask for the path and tell the user to save it there — do not hardcode a goal filename into any file in this repository.

## Step 1 — Make the goal judgeable

Ask the user for their big goal. Most people state something shaped like this invented example:

> 精通某个技术方向的工程实践，每天输出学习成果，尽快拿到可核对的结果

That mixes capability with outcomes and has no finish line. Split it into **two layers**:

1. **Result ladders** on the objective note. Ask the user which one or two outcomes the goal is actually about, and what counter each is measured in. Each ladder is a set of rising thresholds verifiable from a dashboard, a bill, or a public artifact. Record the dimension names in `## 维度字典` — those names become the allowed `goalDim` values, so nothing in the skill needs to know what they are.
2. **Capability milestones** on the capability note — artifacts: a skill, a demo, a series, a tool the user actually uses daily.

A milestone qualifies only if you could point at an artifact or a number and say "done":

- Bad: 深入理解某个架构
- Good: 开源一个能跑通完整主流程的最小项目，README 里有陌生人可复现的运行步骤
- Bad: 尽快拿到结果（无可核对计数）
- Good: <某可核对计数> 累计 ≥ <N>（分项快照留痕）

### Measure the baseline before writing any counted milestone

For every ladder measured by a counter, ask for the current value of each source that feeds it — including sources built from unrelated past work. Then decide with the user how that inherited stock counts. This matters: an account grown from an earlier, unrelated direction can satisfy the first rungs on day one, which makes the ladder useless as a daily compass and quietly turns the whole plan into theatre.

Default treatment, unless the user picks otherwise:

- Keep the absolute ladder when the stated purpose is an absolute figure, and mark already-passed rungs as **存量继承** with the date and where the stock came from, explicitly not counted as a win.
- Add a parallel **净增 ladder** measured from the baseline date. That one drives daily candidates.
- Record the baseline as an immutable table row; all future net change is computed against it.

### A ladder whose first rung needs a decision is not schedulable yet

If the first rung depends on a choice the user has not made — what to offer, to whom, through what channel — force that decision now, out of assets that already exist. "先调研一下" is not a milestone, and a ladder that starts with research will sit untouched for months.

## Step 2 — Optional goal optimization across models

Offer once, then move on:

> 要不要让另一个模型也优化一遍这个目标做对比？切换 Cursor 顶部的模型（KIMI / DeepSeek / OpenAI）后重跑 `df init`，我会只重做这一段并把两版并排给你。不需要就跳过。

Do not fan out to multiple models yourself — that doubles cost for a decision that changes roughly once a week. If the user does rerun under a different model, output both versions side by side and let them pick; do not merge automatically.

## Step 3 — Skill profile interview

Ask 5 to 8 questions in **one** numbered block, then wait for a single reply. Derive the questions from the capability milestones just agreed, not from a fixed list.

Every question must target one capability the milestones actually require, and must demand evidence. State the rule up front:

> 每题请给一个等级 + 一句证据（你做过/写过/上线过什么）。没有证据的自评我会按 L1 记，因为「知道」和「做过」在选题时是完全不同的两件事。

Levels:

| Level | Meaning |
|-------|---------|
| L0 | 没接触过 |
| L1 | 读过看过，没动手 |
| L2 | 跟着教程做过一遍 |
| L3 | 独立做出过一个完整的东西 |
| L4 | 做过并踩过坑，能讲清取舍 |
| L5 | 生产环境跑过，或有别人在用 |

Calibration rules when scoring the reply:

- Evidence that names a specific artifact, a specific failure, or a specific trade-off supports the claimed level.
- Evidence that only restates the concept ("我了解 RAG 的原理") does not. Record the level one step lower and say so plainly.
- No evidence caps the entry at L1.
- Never silently downgrade. Show the adjustment and the reason in one line each, so the user can push back.

For the default goal, the capabilities worth probing cluster into three groups. Pick from these, phrased as concrete engineering questions rather than "你会不会 X":

- **Agent 工程**: 工具调用与错误恢复、多步规划与状态管理、上下文窗口与记忆、评测与回归、成本与延迟控制
- **AI 工作流**: 把重复工作沉淀成 skill/prompt 资产、让 AI 读大规模代码或笔记而不炸上下文、人机分工边界、验证 AI 输出的手段
- **产出能力**: 写作节奏、开源项目的最小可发布标准、把踩坑过程转成内容的习惯

## Step 4 — Dedup baseline

Run the scoped scans from `conventions.md` and record, in the capability note, a compact list of topics already covered — filenames only, grouped, no bodies. This is what stops `plan` from recommending a topic written in May.

Keep it to topic keywords, not raw paths. Note the last-covered date only where it is obvious from the filename.

## Step 5 — Write the objective files

Paths and frontmatter are in `conventions.md`.

### The north-star note (`{{OBJECTIVE_FILE}}`, `type: O`)

Required sections:

```markdown
# <objective slug>

## Purpose
<the goal in the user's own words, one paragraph>

## 维度字典
<allowed goalDim values: the user's result dimensions + leverage + capability,
 each with the counter or artifact that verifies it>

## 验收口径
### <result dimension 1>
<what is counted, which sources feed it, inherited-stock treatment, how it is recorded>
### <result dimension 2>
<definitions and any prerequisite decision the first rung depends on>

## Milestones
### <dimension 1> · 绝对值
### <dimension 1> · 净增（自 <baseline date> 基线 <N> 起算）
### <dimension 2>
### 能力底座 → 指向能力子工程

## This Year
## This Month
## This Week

## 级联规则
<objective is the single focus source; df plan pushes mirrors down; tasks need goalDim + goalStep>

## Baseline · 分项快照
| 来源 | 计数 | 更新日期 | 备注 |

## Sub-projects
## Actions
## Review
```

Every `This Year` / `This Month` / `This Week` item must carry a number or an artifact someone else could check. An item that would still be green in a month where no result ladder moved at all is a defect — rewrite it.

Write the user's dimension names, counters, thresholds, and baseline **into the note only**. Do not echo any of them back into `local.config.md` or into any file in this repository.

### The capability note (`{{CAPABILITY_FILE}}`, `type: P`)

```markdown
# <capability slug>

## Purpose
能力底座；父目标 [[<objective slug>]]

## Parent
<parent link, no This Year/Month/Week here, constraint: every milestone must name the ladder cell it unblocks>

## Milestones
## Skill Profile
_最后更新: YYYY-MM-DD_

| 能力 | 自评 | 校准 | 证据 |
|------|------|------|------|

## Covered Topics
## Open Questions
## Actions
## Review
```

`Open Questions` stays on the capability file: `init` deliberately leaves gaps, and `plan` pulls one or two each morning instead of a 30-minute onboarding that blocks day one.

After writing, confirm in chat with the ladders, the baseline, This Year focus, and the three weakest capabilities. Then tell the user to run `df plan` to start day one.
