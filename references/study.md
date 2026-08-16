# Mode: study (optional question-driven reading loop)

Turns a learning unit (book chapter, tutorial section, codebase area, video) into
a question-driven study cycle whose cards feed the content pipeline. Optional:
runs only when the user asks (学习 / 读 X 章 / 带问题读 / `df study`). Extensible
via `STUDY_TYPES` (default `book`; add `tutorial`, `codebase`, `video`).

## Config (`local.config.md`)

| Key | Meaning |
|-----|---------|
| `STUDY_CARDS_DIR` | Directory holding theme note + cards. Write-allowed (the only exception to read-only `NOTES_VAULT`). Blank disables study. |
| `STUDY_DECK_PREFIX` | Anki deck route prefix, e.g. `AI-Engineering` → cards route `AI-Engineering::Ch-02`. |
| `STUDY_TYPES` | Comma list of supported learning kinds: `book, tutorial, codebase, video`. Append new kinds here. |

## Resource routing (by type)

`df study <resource> [--type <kind>]`. Omit `--type` → infer from the resource:
`.pdf` / `.epub` → book · repo dir (has `.git`) → codebase · `.mp4` / `.mov` /
video URL → video · `.md` / `.html` / docs URL → tutorial · otherwise ask one
question (`study.type_prompt`).

| Type | Input | Extract | Unit (long → cycles) | Source tag | Question lean | Practice slice | Deck route |
|------|-------|---------|----------------------|------------|---------------|----------------|------------|
| book | PDF / ePub | `pdftotext` page range (verify page offset first) | chapter / section | section + print page | concepts + why + apply | run a book example or a small probe | `<PREFIX>::Ch-XX` |
| codebase | repo dir | scoped read (no recursive full scan) | module / feature / diff | file + line range | mechanism + trade-offs + fix | reproduce / modify / benchmark | `<PREFIX>::Module-XX` |
| video | file / URL | transcript; else chaptered manual skim with timestamps | segment (time range) | segment + timestamp | procedure + why + pitfalls | redo the steps | `<PREFIX>::Part-XX` |
| tutorial | docs dir / URL / html | read the section | lesson / section | section + line/URL | steps + when-to-use | follow steps, note deviations | `<PREFIX>::Lesson-XX` |

New kinds: append to `STUDY_TYPES` in `local.config.md` and add a row here; the
rest of the cycle stays type-agnostic.

## Cycle (per learning unit)

Long units split into multiple cycles; each cycle covers a contiguous slice and
produces its own cards.

1. **Pick unit.** Chapter / section / module / segment. If the unit is long
   (roughly >30 min of work), split into 2+ cycles.
2. **Read the source before writing questions.** Dispatch by the resource's type
   (table above): extract the unit's content, map headings + source tags.
3. **Question set (all upfront).** Cover **all** key concepts of the unit; no
   fixed cap — quality and coverage decide the count. Mix: basic concept checks
   (as many as needed) + why/mechanism + connect to the user's practice +
   critique/apply. Every question must be answerable from this unit and tagged
   with that type's source-tag format (table above). Add reading hints (range /
   focus / skip). Give the whole set in one block before the user reads.
4. **User answers + reflection.** One block; user answers all questions and adds
   a 感悟 line.
5. **Evaluate.** Per question (2–3 lines): 对 / 偏差 / 补充. Overall: depth and
   what connects to existing practice. Next: 1–2 concrete suggestions (re-read a
   passage / run a small probe / fix a misconception / which points can feed an
   article). Update capability Open Questions when a new gap appears.
6. **Cards (after confirmation).** One file per unit under
   `STUDY_CARDS_DIR/cards`, one card per knowledge point, Obsidian_to_Anki
   compatible. Deck route per type (table above); book default
   `<PREFIX>::Ch-XX`. See template. Cards are internal review material — no goal
   numbers, no counters.
7. **Article handoff.** Cards + Q&A are the material for a later `df ship`.
   `df ship` is **manual-only** and topic/outline-gated (see
   `references/ship.md`) — study never auto-triggers an article. Article body
   must rephrase — never paste card content verbatim; the article may end with
   a note citing the card note it drew on.

## Card template (Obsidian_to_Anki)

File: `<STUDY_CARDS_DIR>/cards/<unit-slug>.md` — one file per unit, one
`### heading` card per knowledge point.

```markdown
---
title: <unit-slug>
type: D
tags:
  - <DECK_TAG>
DateStarted: YYYY-MM-DD
DateModified: YYYY-MM-DD
status: 🟡Doing
draft: true
---

<STUDY_DECK_PREFIX>::Ch-XX

# <Unit title>

### <问题式知识点，如「为什么 RAG 能减少幻觉？」>
💡 提示：<可选一句话>
- 一句话答案
- 机制 / 例子（2–4 行）
- 我的理解 / 联系实践：
- 出处：<节> p.<页> · 关联：[[主题笔记]] · [[其他卡]]

### <下一张卡>
```

Rules:
- Deck route line at top: `<STUDY_DECK_PREFIX>::<type-suffix>` (book: `Ch-XX`;
  codebase: `Module-XX`; video: `Part-XX`; tutorial: `Lesson-XX`).
- `### heading` = card front (Basic regexp `^#{3}\s(.+)`); content below = back.
- Card front must be a question answerable from memory.
- One knowledge point per card (atomic); no compound cards.
- `<!--ID-->` is written by Obsidian_to_Anki on sync — never hand-write IDs.

## Theme note

`<STUDY_CARDS_DIR>/<theme>.md` — knowledge entry: resource info, unit map,
learning-progress table, Dataview aggregation of cards. Cards double-link back.

## Task + daily integration

- Study day = a `te-` task (`goalDim: capability`, `goalStep` = named unit).
  Questions in task Purpose; answers + 感悟 in Outcomes; evaluation in Review;
  cards in `STUDY_CARDS_DIR` (after confirmation).
- Cards are written only after the user confirms the drafted set.
- Long unit: each cycle is its own `te-` task (e.g. `te-aie-ch02-1`, `te-aie-ch02-2`).
