# Mode: comment (optional first-reader pass)

One round of first-reader critique on the **hand-edited working copy**. Optional: `df final` does **not** require this mode. When this mode completes successfully, stamp the task.

User-facing strings: `references/i18n.md` (`final.q_is_final`, `comment.labels`, `final.not_final_stop`).

## Step −1 — Resolve target day

Same rule as `df ship` (`conventions.md` **Target day**): `df comment [date]`; default calendar today. Announce `shared.target_announce`. Stop on `shared.target_missing`.

Read:

1. `local.config.md`
2. **Target day's** daily note → main task link
3. That task file (`deliverable`, `## Outcomes` v1, export path notes)
4. The **export-path** working markdown (body — required for critique)

Skip entirely when `deliverable` is not `article` or `script` (and path is not `pub-*` / `script-*`). Tell the user `df ship` was enough for that day.

## Step 1 — Final-draft gate

Ask `final.q_is_final` for `LANGUAGE`, then wait.

- **no** → stop. Do **not** set `commented`. Show `final.not_final_stop`. Re-run after edits (or go to `df final`, which asks again).
- **yes** → continue.

## Step 2 — Four-line critique

No score, no empty praise. Use `comment.labels` for `LANGUAGE`.

Offer to apply **only that single improvement** to the export-path file. Never edit frozen `## Outcomes` v1. Critique prose in `LANGUAGE`.

Append a short pointer under task `## Review` (`comment: 已评 YYYY-MM-DD`) without pasting the whole critique essay if the Review section is already long — chat holds the four lines.

## Step 3 — Stamp

Set task frontmatter:

```yaml
commented: YYYY-MM-DD
```

Use **calendar today** (execution day), not the target day. This field is a record only; it does not unlock `df final`.
