# local.config

Copy this file to `local.config.md` in the same directory and fill in your own paths. `local.config.md` is gitignored and never committed.

The skill reads these four keys at the start of every mode. It will refuse to run rather than guess a vault path.

```yaml
# Parent directory shared by your vaults. Used to expand the two below.
# Only needed if DAILY_VAULT / NOTES_VAULT are left as defaults.
ROOT_DIR: D:\YourFolder

# Vault holding daily notes, tasks, and projects.
# Everything the skill writes goes here. Required.
# Defaults to {{ROOT_DIR}}\Daily
DAILY_VAULT: D:\YourFolder\Daily

# Optional second vault of existing notes. Read-only.
# Used only to avoid recommending a topic you have already written about.
# Leave blank to skip dedup scanning entirely.
NOTES_VAULT: D:\YourFolder\Notes

# Written into the `owner` frontmatter field of generated task files.
OWNER: YourName
```

## Notes

`DAILY_VAULT` and `NOTES_VAULT` accept absolute paths and do not have to share a parent. `ROOT_DIR` exists only as a convenience for the common case where they do.

If your vault layout differs from the one described in `references/conventions.md` — different folder names, a different frontmatter schema, different `type` values — edit `conventions.md` directly. It is the structural contract, and it is meant to be forked. The four keys above cover locations, not layout.
