# Mode: ship (evening)

Turns the day's work into a finished deliverable and gives it a real reading.

Read, in this order:

1. `local.config.md` (vault paths)
2. `local.article.config.md` — **required for any article deliverable**
3. `local.article.memory.md` if it exists (learned edit rules)
4. Today's daily note and today's task file

Do not read further back.

## Step 0 — Load article config (articles only)

Skip this step for a pure open-source deliverable with no companion article.

If `local.article.config.md` is missing, or any of `audience` / `export_dir` /
`export_slug_pattern` is empty:

1. Stop. Do not draft.
2. Tell the user to copy `local.article.config.example.md` → `local.article.config.md`
   and fill the required keys.
3. Exit ship.

Resolve:

| Key | Role |
|-----|------|
| `ship_policy` | `quality` \| `time` \| `hybrid` (default `hybrid`) |
| `style_path` / `style` | Voice constraints |
| `audience` | Reader brief injected into the draft prompt |
| `export_dir` + `export_slug_pattern` | Working markdown path (edit target) |
| `images_dir_pattern` | Cover + inline image directory |
| `cover` / `max_inline_images` / `illustrate_confirm` / `illustrate_timebox_min` | Illustration budget |
| `publish_export` | Per-slot export / handoff text; keys must match `PUBLISH_SLOTS` |

Also load `PUBLISH_SLOTS` from `local.config.md` — those are the only frontmatter
keys used for publish URLs. If the key is missing, stop and ask the user to add it.

Confirm `{slug}` with the user in one short line if ambiguous (derive from the
task filename by default, stripping the `cpe-` / `te-` / `pm-` prefix).

If `local.article.memory.md` exists, load the **most recent 7** executable rules
and treat them as hard constraints alongside style/audience.

### `ship_policy` when time is short

- **hybrid** (default): shorten before shipping; if still below bar, fall through
  to the "做了一半" branches in Step 2 (slice or stuck post). Never pad a long
  weak draft.
- **quality**: same shortening rule; if a short piece still fails the bar, mark
  the day unfinished and do not publish.
- **time**: must produce something linkable; enforce only the minimum bar from
  config/memory (concrete number or decision required).

Principle locked in config intent: **do not sacrifice quality to fill time —
compress length instead.**

## Step 1 — Collect status

One question, accepting a loose answer:

```
今天做到哪了？一句话就行 —— 做完了 / 做了一半卡在哪 / 换方向了 / 没动。
```

Then mark the checkboxes in both the task file and the daily note:
`✅ YYYY-MM-DD` on what got done, untouched items left as-is. Do not delete
unfinished items; they are evidence for tomorrow's estimate calibration.

Record actual elapsed time against the estimate in the task's `## Review`.

## Step 2 — Decide what is actually publishable

Branch on the honest answer, and say which branch you took:

- **做完了** — write the deliverable as planned.
- **做了一半** — do not write an article that pretends otherwise. Two options,
  offer both: ship the finished slice as a smaller piece, or write the
  卡住的地方 as a debugging post.
- **换方向了** — write about what got abandoned and why.
- **没动** — do not generate anything. Record it, ask the one useful question
  (是时间不够、方向不对、还是不想动), put the answer in `ToImprove::`, and stop.

Never generate a deliverable that is not backed by something that actually
happened today.

## Step 3 — Write the draft (dual-write)

### Open source (no article)

`## Outcomes` records the repo or commit link, what was built, and the one
design decision worth explaining. README that a stranger can run counts.

### Article

Write markdown, first person, sized to the time left under `ship_policy`
(prefer 1500–2500 characters of substance when time allows; shorter is fine).

Inject into the generation constraints:

- `audience`
- `style_path` contents or `style`
- the recent memory rules

Structure:

- Open on something concrete — a specific error, decision, or number. Never
  open on 背景铺垫.
- Middle carries process and trade-offs with evidence.
- Close on one sentence worth quoting, plus what comes next.

Hard rules:

- No 随着…的发展 / 在当今…时代 / 众所周知 openings.
- Every claim carries code, a number, or a lived detail.
- No empty heading scaffolding.
- Keep the user's voice and mess.

**Dual-write (same bytes, once):**

1. Task file `## Outcomes` — this copy is **v1 and frozen**. Do not edit it
   again after the first write (except appending a "终稿路径 / 发布链接" note
   later). It is the calibration baseline.
2. Resolved export path
   (`export_dir` + `export_slug_pattern`) — **the only working copy**. Create
   parent directories as needed. All critique fixes and human edits happen here.

Show the draft in chat. Tell the user the export path is the edit target.

## Step 4 — First-reader critique (one round, export path only)

Four lines, no score, no empty praise:

1. **最强的地方**
2. **最可能弃读的地方**
3. **一个改进点**
4. **谁会觉得这篇有用**

Offer to apply the single improvement point **only to the export-path file**.
Do not modify the frozen `## Outcomes` v1. Then stop critiquing.

## Step 5 — Cover + inline illustrations (timeboxed)

Skip if the deliverable is not an article, or config sets `cover: false` and
`max_inline_images: 0`.

Budget: `illustrate_timebox_min` (default 45). Say the budget out loud before
starting.

Order:

1. **Cover** via `baoyu-cover-image` when `cover: true`. Output under
   `images_dir_pattern`.
2. **Inline images** via `baoyu-article-illustrator`, capped at
   `max_inline_images` (default 4). Prefer the export-path article as input.

When `illustrate_confirm: false`, invoke baoyu skills with explicit skip-confirm
wording (e.g. 按默认出图 / 跳过确认 / 直接生成) so their default confirmation
gate does not burn the timebox.

On timebox breach: **drop remaining inline images first, keep the cover**,
link whatever exists into the export-path markdown, and continue. Do not start
hand-tuning individual images inside ship.

## Step 6 — Export for publish slots

Phase 0 does not auto-publish. Hand over files.

- **工作稿** — the export-path markdown (already final edit target).
- **Each key in `PUBLISH_SLOTS`** — read the matching bullet under
  `publish_export` in `local.article.config.md` and follow it. If a slot has no
  entry, say so in one line and skip rather than inventing a converter.
- **GitHub** — for open source, README is the deliverable.

## Step 7 — Write back task + daily

In the task file:

- `status: 🟢Done` if the deliverable exists, otherwise leave `🟡Doing`
- `DateDone` / `DateModified` today when done
- Under `## Outcomes`, append (do not overwrite v1 body):

  - `终稿路径: <export path>`
  - `配图目录: <images dir>` when relevant

In the daily note, mark action completion. Leave `## Review` for tomorrow's
`df plan` close-out.

## Step 8 — Calibrate + publish links (one question block)

Ask in a single block:

```
1. 导出路径里的 md 已是终稿了吗？（是 → 我现在做 v1↔终稿校准；否 → 明早 df plan 再收）
2. 各发布槽的链接？（按 PUBLISH_SLOTS 逐个问；没有的写「未发」）
```

### Calibration (when answer 1 is 是)

1. Diff frozen `## Outcomes` v1 against the export-path file.
2. Derive **at most 5** executable rewrite rules (not a prose essay). Examples:
   「开头禁止背景铺垫」「配图默认 ≤4」「删空话段」。
3. Append them to `local.article.memory.md` with today's date. Keep the file's
   usable window to the **most recent 7 rules** (archive or drop older ones).
4. Tell the user they can hand-edit or delete rules in that file.

If answer 1 is 否, write a one-line deferral into the task `## Review`
(`校准: 待收`) and move on. `df plan` will ask again tomorrow.

### Publish links (always attempt)

Write whatever URLs the user provides into the task frontmatter keys listed by
`PUBLISH_SLOTS`. Also append a compact `发布链接` bullet list under `## Outcomes`
(below the frozen v1, next to `终稿路径`) so Dataview/task review and human
scanning share one place. **Do not leave published articles linkless in the task
file** — that breaks the next morning's feedback collection and the weekly retro.

If the user has not published yet, leave the fields empty and close with:

> 发出去之后把链接填进 task 的 PUBLISH_SLOTS 各字段（或回一句让我写入），明早 `df plan` 收反馈数字；若终稿今晚才定，校准也一并在那时收。

Do not restate the article, the plan, or the critique.
