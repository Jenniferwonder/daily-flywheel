# Mode: init

One-time bootstrap. Produces the objective file that `plan` reads every morning.

Gate: if `{{DAILY_VAULT}}\Projects\Scope\TechSkills\AI\ai-agent-flywheel.md` already exists, do not re-run. Say it exists, show the current goal and milestones, and ask whether to refresh the goal, add to the skill profile, or exit.

## Step 1 — Make the goal judgeable

Ask the user for their big goal. Most people state something like this example:

> 掌握践行能让 AI 价值最大化的学习工作流，掌握 AI Agent 工程实践能力，每日输出相关学习成果

That example is two goals plus a constraint, and neither goal has a finish line. "掌握某种工作流" cannot be checked off — which is exactly why systems like this stall: with no way to tell whether a day moved the needle, every day feels equally arbitrary. Expect the user's first answer to have the same shape and treat fixing it as the real work of this step.

Translate it into 3 to 5 milestones that a stranger could verify from the outside. A milestone qualifies only if you could point at an artifact and say "done". Examples of the required shape:

- Bad: 深入理解 Agent 架构
- Good: 开源一个能跑通 plan → tool call → 自我修正循环的最小 Agent，README 里有可复现的运行步骤
- Bad: 掌握 RAG
- Good: 写完一个 4 篇的 RAG 系列，最后一篇是自己踩过的 3 个坑

Confirm the milestones with the user before writing anything. Keep the user's own wording where it is already concrete.

## Step 2 — Optional goal optimization across models

Offer once, then move on:

> 要不要让另一个模型也优化一遍这个目标做对比？切换 Cursor 顶部的模型（KIMI / DeepSeek / OpenAI）后重跑 `df init`，我会只重做这一段并把两版并排给你。不需要就跳过。

Do not fan out to multiple models yourself — that doubles cost for a decision that changes roughly once a week. If the user does rerun under a different model, output both versions side by side and let them pick; do not merge automatically.

## Step 3 — Skill profile interview

Ask 5 to 8 questions in **one** numbered block, then wait for a single reply. Derive the questions from the milestones just agreed, not from a fixed list.

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

Run the scoped scans from `conventions.md` and record, in the objective file, a compact list of topics already covered — filenames only, grouped, no bodies. This is what stops `plan` from recommending a topic written in May.

Keep it to a list of topic keywords, not raw paths. Note the last-covered date only where it is obvious from the filename.

## Step 5 — Write the objective file

Path and frontmatter are specified in `conventions.md`. Body:

```markdown
# ai-agent-flywheel

## Purpose
<the goal in the user's own words, one paragraph>

## Milestones
- [ ] <verifiable milestone> 
- [ ] <verifiable milestone>

## Skill Profile
_最后更新: YYYY-MM-DD_

| 能力 | 自评 | 校准 | 证据 |
|------|------|------|------|
| 工具调用与错误恢复 | L3 | L2 | 只跟着文档跑过，没处理过失败重试 |

## Covered Topics
_去重基线，扫描自 NOTES_VAULT，YYYY-MM-DD_
- RAG: 分块、检索、评估
- Prompt engineering: ...

## Open Questions
_画像里还没问到的能力，plan 每天补 1-2 个_
- ...

## Actions

## Review
```

`Open Questions` is what makes the progressive interview work: `init` deliberately leaves gaps, and `plan` pulls one or two from here each morning instead of running a 30-minute onboarding that blocks day one.

After writing, confirm in chat with the goal, the milestones, and the three weakest capabilities — those are where the first few days' deliverables will come from. Then tell the user to run `df plan` to start day one.
