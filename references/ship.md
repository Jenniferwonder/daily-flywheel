# Mode: ship (evening)

Turns the day's work into a finished deliverable and gives it a real reading. Read today's daily note and today's task file. Nothing else.

## Step 1 — Collect status

One question, accepting a loose answer:

```
今天做到哪了？一句话就行 —— 做完了 / 做了一半卡在哪 / 换方向了 / 没动。
```

Then mark the checkboxes in both the task file and the daily note: `✅ YYYY-MM-DD` on what got done, untouched items left as-is. Do not delete unfinished items; they are evidence for tomorrow's estimate calibration.

Record actual elapsed time against the estimate in the task's `## Review`. That comparison is the single most useful number in the whole system for the first week — it is what makes tomorrow's plan realistic.

## Step 2 — Decide what is actually publishable

Branch on the honest answer, and say which branch you took:

- **做完了** — write the deliverable as planned.
- **做了一半** — do not write an article that pretends otherwise. Two options, offer both: ship the finished slice as a smaller piece, or write the 卡住的地方 as a debugging post. A genuine "我卡在这里，这是我排查的四步" post is often better content than a smooth success story, and it is publishable tonight.
- **换方向了** — write about what got abandoned and why. The reasoning is the content.
- **没动** — do not generate anything. Record it, ask the one useful question (是时间不够、方向不对、还是不想动), put the answer in `ToImprove::`, and stop. A fabricated article on a day with no work poisons the whole loop.

Never generate a deliverable that is not backed by something that actually happened today.

## Step 3 — Write the draft

Goes into the task file's `## Outcomes`.

For an **open source** deliverable, `## Outcomes` records the repo or commit link, what was built, and the one design decision worth explaining. A README that lets a stranger run it counts as the deliverable; a companion post is optional and should be offered, not assumed.

For an **article** deliverable, write it in markdown, first person, 1500 to 2500 characters of substance, readable in one sitting.

Structure:

- Open on something concrete — a specific error, a specific decision, a specific number. Never open on 背景铺垫.
- Middle carries the process and the trade-offs, with evidence: code, numbers, a real failure.
- Close on one sentence worth quoting, plus what comes next.

Hard rules for the prose, because this is the only long generation of the day and the failure mode is fluent emptiness:

- No 随着…的发展 / 在当今…时代 / 众所周知 openings.
- Every claim carries code, a number, or a specific lived detail. A paragraph that would survive being written by someone who did not do the work gets cut.
- No heading scaffolding with nothing under it. Fewer sections, more substance per section.
- Keep the user's actual voice and the actual mess. The stumbles are the differentiator; a polished account of a smooth process is indistinguishable from every other post on the topic.

Show the draft in chat and let the user edit before anything else happens.

## Step 4 — First-reader critique

This step exists to fix 学了很久得不到反馈没有动力. It is the only feedback available on day one, so it has to be worth reading. Four lines, no score, no encouragement for its own sake:

1. **最强的地方** — point at a specific paragraph and say what makes it work.
2. **最可能弃读的地方** — where a reader bails, and why.
3. **一个改进点** — concrete enough to apply right now, not "可以更深入".
4. **谁会觉得这篇有用** — the specific reader this lands for.

Honest and specific beats kind. Empty praise is detectable, and once the user notices it, every future critique is worthless. If the piece is weak, say it is weak and say what would fix it.

Offer to apply the improvement point, then stop critiquing. One round.

## Step 5 — Export

Phase 0 does not auto-publish. Convert and hand over.

- **微信** — WeChat strips markdown, so it needs a converter. If the third-party `baoyu-post-to-wechat` skill is installed, use its converter:

```powershell
npx -y bun "<baoyu-post-to-wechat>\scripts\md-to-wechat.ts" "<markdown_file>" --help
```

  Run with `--help` first to confirm the current flags, write the draft to a temp markdown file, convert, and tell the user where the output is. If that skill is not installed, skip this and export plain markdown like the platforms below.

- **知乎 / 掘金** — standard markdown pastes in directly. Save the draft to a file and give the path.

- **GitHub** — for open source deliverables, the README is the deliverable; make sure the run steps are reproducible by someone who is not the author.

## Step 6 — Write back

In the task file:

- `status: 🟢Done` if the deliverable exists, otherwise leave `🟡Doing`
- `DateDone` today when done
- `DateModified` today
- Leave `wechat` / `zhihu` / `juejin` / `bilibili` empty

In the daily note, fill `## Actions` completion state and leave `## Review` for tomorrow morning's close-out.

## Step 7 — Hand off the third touch

Close with one line, not a summary:

> 发出去之后回来把链接填进 task 的 `wechat` / `zhihu` 字段，明早 `df plan` 我会来收反馈数字。

Do not restate the article, the plan, or the critique. The user just read all three.
