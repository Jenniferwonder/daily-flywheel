# daily-flywheel

[English](./README.en.md)

一个 Cursor Agent Skill：每天早上告诉你今天该产出什么，晚上把你做的事变成成稿并当场给出点评。全部状态是你 Obsidian vault 里的 markdown，不新建任何平行结构。

## 它解决什么

如果你搭过一套完备的 Obsidian 系统 —— Templater 日记模板、Tasks 插件、Dataview 汇总、Kanban 看板、项目树 —— 然后某天停了，再没打开过，那这个技能是为你写的。

那套系统很擅长**记录**，但对**决策**完全沉默。每天早上打开空白日记，「今天该做什么」这个最耗神的部分仍然原封不动留给你。做几个月之后，某天早上不想做了，就再也没打开过。

所以这个技能只补两件事：

- **决策** —— 基于你的大目标和当天可支配时间，给出 3 到 5 个当天能做完的产出候选，每个标注类型、难度、价值、预期耗时，以及为什么是今天
- **反馈** —— 成稿写完当场以第一读者身份给出点评。不打分、不鼓励。外部点赞前两周必然接近零，动力不能挂在上面

## 每天两次触发

```
早上  df plan   收昨天状态 → 复盘 → 今日候选 → 选定 → 写入日记与任务文件
晚上  df ship   收行动状态 → 生成成稿 → 第一读者点评 → 平台格式导出
```

首次使用先跑 `df init`：把模糊的大目标翻译成可验收的里程碑，做一次带证据的技能画像访谈，建立去重基线。

## 依赖

Obsidian 社区插件，5 个必需，加核心的 daily notes：

| 插件 | 用途 |
|------|------|
| `dataview` | 日记里的产出汇总与项目 rollup |
| `templater-obsidian` | 日记模板 |
| `obsidian-tasks-plugin` | 待办的 Due / Todo / Done 区块 |
| `obsidian-kanban` | 任务看板 |
| `periodic-notes` | 周报月报 |

## 安装

**1. 克隆到你存放开源项目的目录**

```powershell
git clone https://github.com/Jenniferwonder/daily-flywheel.git
```

**2. 链接到 Cursor 的用户级技能目录**

Cursor 只从固定位置加载用户级技能，所以用目录 junction 指过去。这样仓库和技能是同一份文件，改完直接就能提交，不会分叉。

```powershell
# Windows，不需要管理员权限
mklink /J "%USERPROFILE%\.cursor\skills\daily-flywheel" "<你克隆的路径>\daily-flywheel"
```

macOS / Linux 用符号链接：

```bash
ln -s <你克隆的路径>/daily-flywheel ~/.cursor/skills/daily-flywheel
```

**3. 填配置**

```powershell
copy local.config.example.md local.config.md
```

打开 `local.config.md` 填四个键：`ROOT_DIR`、`DAILY_VAULT`、`NOTES_VAULT`、`OWNER`。这个文件已在 `.gitignore` 里，不会被提交。

技能读不到配置会直接停下来提示你，不会去猜路径 —— 猜错会把文件写进错误的 vault。

**4. 跑起来**

在 Cursor 里输入 `df init`。

## 适配你自己的 vault

四个配置键只管**位置**，不管**布局**。

具体的目录结构、frontmatter 字段、`type` 取值、Tasks 插件语法全部写在 [`references/conventions.md`](./references/conventions.md) 里。它描述的是一套具体可用的布局而不是抽象契约 —— 契约写得含糊，生成的文件也会含糊。

**如果你的 vault 结构不一样，直接改 `conventions.md`。** 它就是设计成给人 fork 的。

## 结构

```
SKILL.md                      路由 + 全局规则，约 60 行
references/
  conventions.md              路径、schema、硬约束（结构契约）
  init.md                     一次性引导
  plan.md                     早上
  ship.md                     晚上
local.config.example.md       配置模板
```

`SKILL.md` 只做路由，按阶段只加载一个 reference。这是刻意的上下文控制：一次对话不需要把四份文档全读进去。

## 开发中踩到的几个坑

这些都写进了 `conventions.md`，单独列出来是因为它们不止对这个技能成立：

- **Templater 不会为 agent 写入的文件渲染。** 生成的日记必须是已渲染的成品，日期算好填死，不能留任何未展开的占位符。
- **开着的 Obsidian 会回写你的编辑。** Linter 削掉空 YAML 值后的尾随空格，`update-time-on-edit` 刷新 `DateModified`，一行改动可能显示成二十行 diff。这是正常的。
- **别把裸的模板开标记写进 vault 文件**，哪怕包在反引号里。实测两次被改写：一次直接吞掉，一次自动补成空标记对。
- **`draft: true` 可能是零信息量字段。** 它是多数模板的默认值，如果每个文件都是 `true`，它就不能用来找残稿。任何一个恒定不变的元数据字段都不携带信息 —— 依赖某个字段做判断前先验证它真的有区分度。
- **云同步盘上的 vault 很慢。** 开发时一次深度 2 的递归列目录跑了约 50 秒，这直接毙掉了「让 AI 扫一遍整个笔记库」的设计。所有扫描都限定范围且只取文件名。

## License

MIT
