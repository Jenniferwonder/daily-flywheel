# Mode: final (illustrate, calibrate, hand off)

Locks the working copy as final, then (for articles) illustrates + uploads images, calibrates v1→final rules, and hands off publish slots. Run after human edits (and optionally after `df comment`).

User-facing strings: `references/i18n.md` keys under `## comment / final`.

## Step −1 — Resolve target day

Same rule as `df ship` (`conventions.md` **Target day**): `df final [date]`; default calendar today. Announce `shared.target_announce`. Stop on `shared.target_missing`.

Read:

1. `local.config.md` (including optional `OSS_*`)
2. `local.article.config.md` — **required** when `deliverable: article` (or path is `pub-*`)
3. `local.article.memory.md` if present (most recent 7 rules)
4. **Target day's** daily note + main task file
5. Export-path working file and frozen task `## Outcomes` v1

## Step 0 — Resolve deliverable type

1. Prefer task frontmatter `deliverable`: `article` | `script` | `other`
2. Else infer from export path / slug: `pub-` → article, `script-` → script
3. If still unclear, ask one line and write `deliverable` onto the task before continuing

If type is `other` (or no pub/script artifact exists): **stop**. No illustrate, no calibrate-as-article. Point them to tomorrow's `df review`.

## Step 1 — Final-draft gate (always)

Ask `final.q_is_final` for `LANGUAGE`, then wait.

- **no** → stop everything (no images, no OSS, no memory write). Write `final.pending_marker` under task `## Review`. Show `final.not_final_stop`. Re-run after edits. If `df comment` earlier said yes, **this answer wins**.
- **yes** → continue.

## Step 2 — Illustrate + OSS (articles only)

Skip this entire step when `deliverable: script`.

Skip if config sets `cover: false` and `max_inline_images: 0`.

Budget: `illustrate_timebox_min` (default 45). Say the budget out loud.

Order:

1. **Cover** via `baoyu-cover-image` when `cover: true` → `images_dir_pattern`
2. **Inline images** via `baoyu-article-illustrator`, capped at `max_inline_images`
3. When `illustrate_confirm: false`, invoke baoyu skills with skip-confirm wording so their confirmation gate does not burn the timebox
4. On timebox breach: drop remaining inline images first, **keep the cover**, link what exists into the export-path markdown

### Step 2b — OSS upload + rewrite

If `local.config.md` has non-empty `OSS_BUCKET` and `OSS_ACCESS_KEY_ID`:

```bash
python "{{SKILL_DIR}}/scripts/oss_upload_images.py" "{{export-path-article.md}}"
```

`{{SKILL_DIR}}` is this skill's directory. Script must leave no local `imgs/` refs in the export-path body/cover.

If OSS keys are missing: one line that hosting was skipped; do not invent credentials; do not commit secrets.

## Step 3 — Calibrate (article and script)

1. Diff frozen `## Outcomes` v1 against the export-path file (script: same if v1 exists; if Outcomes has no prose body, skip with one line).
2. Derive **at most 5** executable rewrite rules (not an essay). Rules must stay abstract — **no private goal totals, account names, or ladder thresholds** in `local.article.memory.md`.
3. Append to `local.article.memory.md` with today's date; keep only the most recent 7 usable rules.
4. Tell the user they may edit or delete rules in that gitignored file.

## Step 4 — Publish handoff

Phase 0 does not auto-publish.

- Point at the export-path working markdown (post-OSS links for articles)
- For each key in `PUBLISH_SLOTS`, follow `publish_export` in `local.article.config.md`; skip missing entries in one line
- Do not demand publish URLs tonight; tomorrow `df review` syncs YAML → task

Append under task `## Outcomes` (do not overwrite v1 body):

- `终稿路径: <export path>`
- `配图目录: <images dir>` when relevant

Set `status: 🟢Done` / `DateDone` when the deliverable path exists; else leave `🟡Doing`.

Close with `final.closer` for `LANGUAGE`.
