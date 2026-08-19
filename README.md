<h1 align="center">Daily Flywheel - Obsidian AI 智能学习产出工作流</h1>

<p align="center">
  <b>让 Obsidian 不只记录学习，而是每天推动你完成一个可发布的成果</b>
</p>

<p align="center"><a href="./README.en.md">English</a></p>

你已经有日记、任务、项目和知识库，却还是每天纠结「今天学什么、做什么、写什么」？问题不在记录工具，而在缺少从**长期目标 → 今日行动 → 成果发布 → 反馈改进**的完整闭环。

Daily Flywheel 是一个 AI Agent Skill。你告诉它大目标和今天能投入多久，它会给出当天做得完的内容产出候选；你选定一个，晚上先出初稿，手改后再可选点评、定稿配图与校准。**所有状态继续留在你自己的 Obsidian vault，不迁移数据，也不新建一套平行系统。**

![](https://files.mdnice.com/user/41327/bbcd45e1-29d6-4d34-b9c0-66c7b5b4daaf.jpg)

## 七条命令，跑起每日产出飞轮

| 阶段 | 输入 | 得到什么 |
|------|------|----------|
| `df init` | 你的长期目标与现有能力 | 可验收的结果阶梯、能力里程碑和选题基线 |
| `df review` | 昨日行动与各平台当前计数 | 任务复盘、`reviewed` 戳记、大目标 Snapshot/阶梯勾选；可选周焦点微调 |
| `df plan` | 今天的时间（须已 `df review`）；可选更新热点 | 3–5 个文章/脚本候选（对齐大目标 + 热点笔记） |
| `df study` | 学习资源 + 类型（book/codebase/video/tutorial，可推断） | 题单（读前一次给全）→ 回答感悟 → 逐题评价建议 → Anki 卡片（确认后写入）→ 供料文章 |
| `df ship` | 今天实际完成的工作 | 冻结 v1 + 导出路径待改稿（漏斗骨架；读风格摘要+校准） |
| `df comment` | 手改后的终稿（可选） | 清单打分（不拦 final）+ 四行点评 |
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
- **学习也能变成产出。** 可选 `df study`：给定一本书 / 代码仓库 / 视频 / 教程，读前一次给全高价值问题，回答后逐题点评，知识点沉淀为 Anki 兼容卡片并回链主题笔记，直接为系列文章供料。
- **越用越贴近你的写法。** 首稿与终稿的差异会沉淀为私有改稿规则，后续草稿逐步减少重复手改。
- **真实目标和渠道配置只留本地。** 目标、数字、账号与导出步骤不会写进开源仓库。
- **中英双语 UI。** 在 `local.config.md` 设 `LANGUAGE: zh` 或 `en`；对话与生成散文跟偏好走，vault 结构字段保持稳定（见 `references/i18n.md`）。

## 功能一览

| 功能 | 做什么 | 写到哪 |
|------|--------|--------|
| 目标级联 | 年 → 月 → 周 → 日单源下推；任务须带 `goalDim` / `goalStep` / `deliverable` | 大目标笔记 / 月记 / 周记 |
| 昨日复盘 | 收链接与反馈、写任务 Review、刷新 Snapshot、自动勾阶梯；触发时提议优化方向 | 任务 + 大目标笔记（vault 内） |
| 今日决策 | 按**最新**大目标、当天时间与 URL 热点笔记，三维过滤出 3–5 个文章/脚本候选 | 今日日记 `## Actions` + 任务文件 |
| 问答式学习 | 可选 `df study`：按资源类型路由（书/代码/视频/教程）；问题覆盖全章 → 评价 → Anki 兼容卡片（内部复习） | 知识库 `STUDY_CARDS_DIR`（卡片）+ 任务卡（题单/回答/评价） |
| 成稿双写 | `df ship`：任务冻结 v1，导出路径供手改 | 任务 `## Outcomes` + 导出目录 |
| 第一读者点评 | 可选 `df comment`；清单打分（不拦 final）+ 四行点评；写入 `commented` | 聊天 + 任务 frontmatter |
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
检查 reviewed →（周日/月末周月复盘）→ 读最新大目标 → 可选刷新热点笔记 → 三维过滤出候选 → 写入日记与任务
```

昨日未 `reviewed` 会硬挡。可支配时间是**硬上限**。默认推文章或视频脚本。候选必须同时服务本周格子和（有 URL 的）热点笔记；搜不到的源写「未取到」，不编造热点。

### `df study` — 可选：问答驱动的阅读学习

输入一个学习资源和它的类型。不给类型时按资源推断：`.pdf`/`.epub` → book、含 `.git` 的目录 → codebase、视频文件/链接 → video、`.md`/`.html`/文档链接 → tutorial。流程按类型路由：

| 类型 | 提取 | 单位 | 出处 | 实践切片 | deck 路由 |
|------|------|------|------|----------|-----------|
| book | `pdftotext` 页范围 | 章/节 | 小节 + 印刷页 | 跑书中示例 / 小探针 | `PREFIX::Ch-XX` |
| codebase | 定向读仓库区域 | 模块 / 功能 / diff | 文件 + 行号 | 复现 / 修改 / 基准 | `PREFIX::Module-XX` |
| video | 字幕 / 带时间戳分段浏览 | 片段（时间区间） | 片段 + 时间戳 | 跟做一遍 | `PREFIX::Part-XX` |
| tutorial | 读文档小节 | 课 / 节 | 小节 + 行/URL | 跟做并记偏差 | `PREFIX::Lesson-XX` |

读前一次给全覆盖该单位**全部重要概念**的高价值问题（题数不设上限，以覆盖为准；长单位切成多个 cycle）；你带问题读、回答 + 感悟；我逐题点评并给下一步建议；确认后把知识点写成 Anki 兼容卡片（每章一文件、每知识点一卡，deck 路由行 + `### 知识点` 卡头），并回链知识库主题笔记。卡片只做内部复习；系列文章正文必须转述，文末可注明参考了哪份卡片。

### `df ship` → 手改 →（可选）`df comment` → `df final`

```
ship：**只手动触发**；正文前必经定题（brainstorm，可借 brainstorming skill）→ 大纲确认（可借 writing-assistant skill）→ 才双写 v1（漏斗骨架；读风格摘要+校准，不重读长范文）
comment：确认终稿后清单打分（不拦 final）+ 四行点评，写 commented
final：再确认终稿 → 配图+OSS（文章）→ 校准 → 发布交接
```

缺 `local.article.config.md` 时文章 ship/final 会直接拒绝，而不是退化成无约束草稿。脚本日缺 `SCRIPT_STYLE_PATH` 或 `script-craft.md` 同样拒绝，且不会去读文章文风。

## 依赖

Obsidian 社区插件，5 个必需，加核心的 daily notes：

| 插件 | 用途 |
|------|------|
| `dataview` | 日记里的产出汇总与项目 rollup |
| `templater-obsidian` | 日记模板 |
| `obsidian-tasks-plugin` | 待办的 Due / Todo / Done 区块 |
| `obsidian-kanban` | 任务看板 |
| `periodic-notes` | 周报月报 |
| `obsidian-to-anki-plugin` | （可选，`df study`）把知识点卡片导出到 Anki；不装则卡片只留在 Obsidian |

## 安装与配置

**1. 安装技能**（已经执行过上面的命令可跳过）

```bash
npx skills add Jenniferwonder/daily-flywheel --agent cursor --global
```

技能会挂在 `~/.cursor/skills/daily-flywheel`（默认是指向本地副本的符号链接，Windows 上创建失败就加 `--copy`），vault / 文章配置填在这个目录里。

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
| `HOT_TOPICS_FILE` | 近 7 天带 URL 的热点笔记（gitignore）。默认 `local.hot-topics.md` |
| `EXTRA_ARCHETYPES` | 可选，只给自己用的候选类型，不进开源文档 |
| `STUDY_CARDS_DIR` | 可选。`df study` 卡片与主题笔记目录（唯一写允许的 `NOTES_VAULT` 例外）；留空禁用 study |
| `STUDY_DECK_PREFIX` | 可选。Anki deck 前缀，如 `AI-Engineering` |
| `STUDY_TYPES` | 可选。支持的学习类型：`book, tutorial, codebase, video`，可扩展 |

**3. 填文章配置**（`df ship` / `df final` 需要）

```bash
cp local.article.config.example.md local.article.config.md
```

必填 `audience`、`export_dir`、`export_slug_pattern`；其余（成稿策略、人设/禁区/术语、配图预算、各渠道导出步骤 `publish_export`）按需填。风格摘要另拷一份：

```bash
cp local.article.style.example.md local.article.style.md
cp local.hot-topics.example.md local.hot-topics.md
cp script-craft.example.md script-craft.md
```

**4. 跑起来**

在 Cursor 里输入 `df init`。

读不到配置时技能会停下来提示你，不会去猜路径 —— 猜错会把文件写进错误的 vault。

**配置只放位置、字段名和可选私有候选类型，不放目标内容。** 你在追什么、怎么衡量、门槛定在哪、涉及哪些账号与数字，只写在 vault 里那篇大目标笔记，技能运行时去读；各渠道怎么导出写在 `local.article.config.md`。vault / 文章 / 风格摘要 / 热点笔记都已在 `.gitignore` 里。所以贴配置求助、录屏、误用 `git add -f`，都带不出目标本身。`references/` 里的例子全是编造的占位值，别替换成自己的真实数据，否则 fork 或提 PR 会一起带出去。

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
  conventions.md                    Obsidian vault 结构契约（路径 / frontmatter / Tasks）
  i18n.md                           中英用户可见文案（LANGUAGE）
  init.md                           一次性引导
  review.md                         昨日复盘
  plan.md                           今日计划（三维过滤 + 热点笔记）
  study.md                          可选问答式学习（按资源类型路由 + 卡片模板）
  ship.md                           初稿双写（漏斗骨架；风格摘要 + 校准）
  comment.md                        可选点评（清单打分不拦 final）
  final.md                          定稿配图 / 校准 / 发布交接
  article-craft.md                  选题/漏斗/打分抽象槽位（仅文章日）
local.config.example.md             vault 路径模板
local.article.config.example.md     人设 / 读者 / 导出 / 配图模板（私有）
local.article.style.example.md      抽出来的文章风格摘要模板（私有）
script-craft.example.md             脚本大纲闸模板（工作副本 `script-craft.md` 不入库）
local.hot-topics.example.md         近 7 天热点笔记模板（私有）
scripts/                            OSS 图床上传（df final）
```

`SKILL.md` 只做路由，按阶段只加载一个 mode reference。这是刻意的上下文控制：一次对话不需要把全部文档读进去。想改行为就改对应那一份。

## 更多 skill 使用技巧

想看更多 skill 的最新功能玩法、更新动态和保姆级教程，欢迎关注公众号 [瞻思于学](https://mp.weixin.qq.com/s/mg0mI3uHPAENDrHtZqUuxA)，各平台同名。daily-flywheel skill 的设计过程与使用方法，详见我的公众号 AI 工作流系列文章：

1. [用 AI + Obsidian 搭一套智能化学习产出工作流，再也不用纠结今天学什么了](https://mp.weixin.qq.com/s/mg0mI3uHPAENDrHtZqUuxA)
2. [让 AI 优化文章创作流：写文章不用愁了](https://mp.weixin.qq.com/s/vmtMSp3LVyIxeSs9humJaQ)
3. [用 Obsidian + AI 将大目标拆到每天：确保实现可量化的行动价值](https://mp.weixin.qq.com/s/8oYScF_kbPZ-1Xo3dyyZsA)
4. [想用 AI 做技术视频：脚本有了，为什么还是拍不出来](https://mp.weixin.qq.com/s/NS3pvbtY8JgMB82S_MTTVw)
5. [用 AI 做视频超全总结：我成功制作并发布了一条 AI 主题视频](https://mp.weixin.qq.com/s/aZVIEWDokvvzrm-xdvnKPA)
6. [AI 创作工作流优化：让选题接上热点，标题击中卖点](https://mp.weixin.qq.com/s/mkDQzzgeJ4EaN9AAyi5j-g)
7. [AI 高效阅读法：把经典著作变成你的个人知识体系，实现系统学习](https://mp.weixin.qq.com/s/ScXRaI5tkS1DdCq4mRufQw)

如果这个技能帮你把日更跑起来了，给个 Star ⭐️ 支持一下。

## License

MIT
