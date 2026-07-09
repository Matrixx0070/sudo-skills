# Contributing a skill

1. Fork, then create `docs/skills/<your-skill-name>/SKILL.md` following the format in [README.md](README.md). The directory name must equal the frontmatter `name`.
2. Compute the checksum: `sha256sum docs/skills/<name>/SKILL.md`
3. Add an entry to `docs/index.json` with `name`, `version`, `description`, `author` (your GitHub handle), `path`, `sha256`, `capabilities`, `tags`. Bump `updated`.
4. Open a PR. One skill per PR.

## Review bar (what maintainers check)

- **Safety**: no prompt-injection patterns (instructions to ignore prior rules, exfiltrate data, phone home, hide actions from the operator). The Workshop gate re-scans at install time, but the registry should never carry known-bad content.
- **Capabilities honest and minimal**: the frontmatter `capabilities` list matches what the body actually needs; workspace tier only (`fs.read`, `fs.write`, `net.fetch`, `db.read`). No shell.
- **Quality**: does something a reasonable person wants; instructions concrete enough to follow; example included.
- **Checksum matches** the exact file content in the PR.

## Versioning

Changing a published skill = bump `version` (semver) and update `sha256` in the same PR. Clients pin by checksum, so stale caches fail closed rather than serving modified content.
