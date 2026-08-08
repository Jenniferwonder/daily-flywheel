# local.config

Copy this file to `local.config.md` in the same directory and fill in your own
paths. `local.config.md` is gitignored and never committed.

The skill reads these keys at the start of every mode. It will refuse to run
rather than guess a vault path.

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

# UI + vault prose language for agent chat and generated note prose: zh | en
# Default zh. Vault schema keys (## Actions, ## Review, frontmatter names) stay fixed.
# Article/script draft language can override via local.article.config `draft_language`.
LANGUAGE: zh

# North-star objective note: your goal, its checkable milestones, and the
# rolling This Year / This Month / This Week focus.
# Path relative to DAILY_VAULT. Created by `df init` if missing. Required.
OBJECTIVE_FILE: Projects\Scope\my-north-star.md

# Optional capability sub-project note: skill profile, engineering milestones,
# covered topics, open questions. Leave blank to keep all of it on OBJECTIVE_FILE.
CAPABILITY_FILE: Projects\Scope\Skills\my-capability-project.md

# Frontmatter keys on task / article notes that store publish URLs.
# Comma-separated, in the order you want to be asked. Required for link sync.
# Use whatever names match your vault schema — the skill never hardcodes them.
PUBLISH_SLOTS: pub_a, pub_b, pub_c

# Optional. Extra rows for the df plan candidate table, beyond the generic
# article / open-source archetypes in references/plan.md.
# Leave blank (or omit) to skip. Put personal / channel-specific tactics here
# so they never enter the open repository.
EXTRA_ARCHETYPES: |

# Optional. Aliyun OSS image upload for `scripts/oss_upload_images.py` and df final.
# Leave blank to skip automated image hosting. Never commit real secrets.
OSS_ENDPOINT: oss-cn-example.aliyuncs.com
OSS_BUCKET: your-bucket
OSS_PREFIX: articles/
OSS_ACCESS_KEY_ID: ""
OSS_ACCESS_KEY_SECRET: ""
OSS_PUBLIC_BASE: https://your-bucket.oss-cn-example.aliyuncs.com
```

## Notes

`DAILY_VAULT` and `NOTES_VAULT` accept absolute paths and do not have to share a
parent. `ROOT_DIR` exists only as a convenience for the common case where they do.

**This file holds locations, publish-slot key names, and optional private
archetypes — not goal content.** What you are aiming at, how you measure it,
thresholds, counters, and any figures live only in the objective note inside
your vault. Keeping them out of this file (and out of `references/`) means a
screen-share, a support paste, or an accidental `git add -f` cannot leak them.

Reference files use invented placeholders on purpose. Do not replace them with
your own values, or a fork or PR will carry them out.

If your vault layout differs from the one described in
`references/conventions.md` — different folder names, a different frontmatter
schema, different `type` values — edit `conventions.md` directly. It is the
structural contract, and it is meant to be forked.
