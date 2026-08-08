<h1 align="center">Daily Flywheel - Obsidian AI 智能学习产出工作流</h1>

<p align="center">
  <b>让 Obsidian 不只记录学习，而是每天推动你完成一个可发布的成果</b>
</p>

<p align="center"><a href="./README.en.md">English</a></p>

你已经有日记、任务、项目和知识库，却还是每天纠结「今天学什么、做什么、写什么」？问题不在记录工具，而在缺少从**长期目标 → 今日行动 → 成果发布 → 反馈改进**的完整闭环。

Daily Flywheel 是一个 Cursor Agent Skill。你告诉它大目标和今天能投入多久，它会给出当天做得完的内容产出候选；你选定一个，晚上先出初稿，手改后再可选点评、定稿配图与校准。**所有状态继续留在你自己的 Obsidian vault，不迁移数据，也不新建一套平行系统。**

![Daily Flywheel：从长期目标、每日计划和今日产出，到成稿发布与反馈校准的 Obsidian AI 工作流](https://files.mdnice.com/user/41327/bbcd45e1-29d6-4d34-b9c0-66c7b5b4daaf.jpg)

## 六条命令，跑起每日产出飞轮

| 阶段 | 输入 | 得到什么 |
|------|------|----------|
| `df init` | 你的长期目标与现有能力 | 可验收的结果阶梯、能力里程碑和选题基线 |
| `df review` | 昨日行动与各平台当前计数 | 任务复盘、`reviewed` 戳记、大目标 Snapshot/阶梯勾选；可选周焦点微调 |
| `df plan` | 今天可支配的时间（须已 `df review`） | 3–5 个做得完的 **文章/脚本** 候选，写入日记和任务 |
| `df ship` | 今天实际完成的工作 | 冻结 v1 + 导出路径待改稿（不点评、不配图） |
| `df comment` | 手改后的终稿（可选） | 四行第一读者点评；任务写入 `commented` 日期 |
| `df final` | 确认终稿 | 文章：配图+图床回贴+校准+发布交接；脚本：跳过配图 |

## 立即安装

```bash
npx skills add Jenniferwonder/daily-flywheel --agent cursor --global
```

安装后复制两份示例配置，填入你的 vault 路径和文章偏好，再在 Cursor 中输入 `df init`。完整字段见[安装与配置](#安装与配置)。

## 为什么值得安装

- **每天直接产出，不再面对空白日记。** 候选受长期目标和真实时间预算约束，超时的任务不会混进来。
- **复用现有 Obsidian 系统。** 日记、任务、项目、周月复盘仍是普通 markdown，不把知识锁进另一款应用。
- **从计划一直走到发布。** 它不止列待办，还负责成稿、点评、配图、发布链接回写与后续反馈收集。
- **越用越贴近你的写法。** 首稿与终稿的差异会沉淀为私有改稿规则，后续草稿逐步减少重复手改。
- **真实目标和渠道配置只留本地。** 目标、数字、账号与导出步骤不会写进开源仓库。
- **中英双语 UI。** 在 `local.config.md` 设 `LANGUAGE: zh` 或 `en`；对话与生成散文跟偏好走，vault 结构字段保持稳定（见 `references/i18n.md`）。

## 功能一览

| 功能 | 做什么 | 写到哪 |
|------|--------|--------|
| 昨日复盘 | 收链接与反馈、写任务 Review、刷新 Snapshot、自动勾阶梯；触发时提议优化方向 | 任务 + 大目标笔记（vault 内） |
| 今日决策 | 按**最新**大目标与当天时间，给 3–5 个文章/脚本候选 | 今日日记 `## Actions` + 任务文件 |
| 目标级联 | 年 → 月 → 周 → 日单源下推；任务须带 `goalDim` / `goalStep` / `deliverable` | 大目标笔记 / 月记 / 周记 |
| 成稿双写 | `df ship`：任务冻结 v1，导出路径供手改 | 任务 `## Outcomes` + 导出目录 |
| 第一读者点评 | 可选 `df comment`；先确认终稿；写入 `commented` | 聊天 + 任务 frontmatter |
| 定稿收尾 | `df final`：配图/图床/校准/发布交接（脚本跳过配图） | 导出稿 + `local.article.memory.md` |
| 日记聚合 | Review 区用 Dataview 拉任务字段，避免多处抄写 | 日记模板 |
| 选题去重 | 只读文件名和 frontmatter | 能力笔记 Covered Topics |
| 能力画像 | 每天补 1–2 个带证据的能力问题 | 能力笔记 Skill Profile |

## 使用指南

### `df init` — 只跑一次

把模糊的大目标翻译成可验收的东西：结果阶梯（数得出来的那些）写进大目标笔记，能力里程碑写进能力子工程笔记；再做一次带证据的技能画像访谈，建立选题去重基线。

它按 [`references/conventions.md`](./references/conventions.md) 描述的目录结构和 frontmatter schema 写文件。**如果你的 vault 结构不一样，先改 `conventions.md` 再跑 `df init`。**

### `df review` — 每天早上先跑

```
扫发布链接 → 收计数与反馈 → 写任务 Review + reviewed → Snapshot/勾阶梯 →（触发时）确认后改周焦点
```

真实目标数字只写在你 vault 的大目标笔记里，不会进入开源 skill 仓库。

### `df plan` — 复盘之后

```
检查 reviewed →（周日/月末周月复盘）→ 读最新大目标 → 今日候选 → 写入日记与任务
```

昨日未 `reviewed` 会硬挡。可支配时间是**硬上限**。默认推文章或视频脚本。

### `df ship` → 手改 →（可选）`df comment` → `df final`

```
ship：勾待办 + 双写 v1/待改稿
comment：确认终稿后四行点评，写 commented
final：再确认终稿 → 配图+OSS（文章）→ 校准 → 发布交接
```

缺 `local.article.config.md` 时文章 ship/final 会直接拒绝，而不是退化成无约束草稿。

## 依赖

Obsidian 社区插件，5 个必需，加核心的 daily notes：

| 插件 | 用途 |
|------|------|
| `dataview` | 日记里的产出汇总与项目 rollup |
| `templater-obsidian` | 日记模板 |
| `obsidian-tasks-plugin` | 待办的 Due / Todo / Done 区块 |
| `obsidian-kanban` | 任务看板 |
| `periodic-notes` | 周报月报 |

## 安装与配置

**1. 安装技能**（已经执行过上面的命令可跳过）

```bash
npx skills add Jenniferwonder/daily-flywheel --agent cursor --global
```

技能会挂在 `~/.cursor/skills/daily-flywheel`（默认是指向本地副本的符号链接，Windows 上创建失败就加 `--copy`），下面两份配置填在这个目录里。

**2. 填 vault 配置**

```bash
cp local.config.example.md local.config.md
```

| 键 | 填什么 |
|----|--------|
| `ROOT_DIR` | vault 的共同父目录，只用于展开下面两个的默认值 |
| `DAILY_VAULT` | 放日记、任务、项目的 vault，技能写入的文件全在这里。必填 |
| `NOTES_VAULT` | 已有笔记的第二个 vault，只读，仅用于选题去重。留空即跳过去重 |
| `OWNER` | 写进生成任务文件 `owner` 字段的名字 |
| `LANGUAGE` | 对话与生成散文语言：`zh` \| `en`（默认 `zh`）；文案见 `references/i18n.md` |
| `OBJECTIVE_FILE` | 大目标笔记路径（相对 `DAILY_VAULT`），`df init` 会在缺失时创建。必填 |
| `CAPABILITY_FILE` | 能力子工程笔记路径，留空则画像和里程碑都留在大目标笔记里 |
| `PUBLISH_SLOTS` | 任务 frontmatter 里存发布链接的字段名，逗号分隔，按你希望被询问的顺序 |
| `EXTRA_ARCHETYPES` | 可选，只给自己用的候选类型，不进开源文档 |

**3. 填文章配置**（`df ship` / `df final` 需要）

```bash
cp local.article.config.example.md local.article.config.md
```

必填 `audience`、`export_dir`、`export_slug_pattern`；其余（成稿策略、风格、配图预算、各渠道导出步骤 `publish_export`）按需填。

**4. 跑起来**

在 Cursor 里输入 `df init`。

读不到配置时技能会停下来提示你，不会去猜路径 —— 猜错会把文件写进错误的 vault。

**配置只放位置、字段名和可选私有候选类型，不放目标内容。** 你在追什么、怎么衡量、门槛定在哪、涉及哪些账号与数字，只写在 vault 里那篇大目标笔记，技能运行时去读；各渠道怎么导出写在 `local.article.config.md`。两份配置都已在 `.gitignore` 里。所以贴配置求助、录屏、误用 `git add -f`，都带不出目标本身。`references/` 里的例子全是编造的占位值，别替换成自己的真实数据，否则 fork 或提 PR 会一起带出去。

### 想改源码 / 参与贡献

克隆到你放开源项目的地方，再用目录链接指到 Cursor 的用户级技能目录。这样仓库和技能是同一份文件，改完直接提交，不会分叉。

```powershell
# Windows，不需要管理员权限
git clone https://github.com/Jenniferwonder/daily-flywheel.git
cmd /c mklink /J "$env:USERPROFILE\.cursor\skills\daily-flywheel" "<你克隆的路径>\daily-flywheel"
```

```bash
# macOS / Linux
git clone https://github.com/Jenniferwonder/daily-flywheel.git
ln -s <你克隆的路径>/daily-flywheel ~/.cursor/skills/daily-flywheel
```

## 结构

```
SKILL.md                            路由 + 全局规则
references/
  conventions.md                    Obsidian vault 的目录结构、路径、frontmatter
                                    schema、Tasks 语法与硬约束（结构契约，改这里适配你的 vault）
  init.md                           一次性引导
  plan.md                           早上
  ship.md                           晚上（含文章配置 / 双写 / 校准）
local.config.example.md             vault 路径模板
local.article.config.example.md     文章风格 / 读者 / 导出 / 配图模板（私有）
```

`SKILL.md` 只做路由，按阶段只加载一个 reference。这是刻意的上下文控制：一次对话不需要把四份文档全读进去。想改行为就改对应那一份。

## 更多 skill 使用技巧

想看更多 skill 的用法与我的踩坑记录，欢迎关注公众号 [瞻思于学](https://mp.weixin.qq.com/s/mg0mI3uHPAENDrHtZqUuxA)，各平台同名。这个技能本身的设计过程我写过两篇：

- [用 AI + Obsidian 搭一套智能化学习产出工作流，再也不用纠结今天学什么了](https://mp.weixin.qq.com/s/mg0mI3uHPAENDrHtZqUuxA)
- [让 AI 优化文章创作流：写文章不用愁了](https://mp.weixin.qq.com/s/vmtMSp3LVyIxeSs9humJaQ)

如果这个技能帮你把日更跑起来了，给个 Star ⭐️ 支持一下。

## License

MIT
