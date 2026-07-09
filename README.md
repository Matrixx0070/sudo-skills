# sudo-skills

The official skill registry for [SUDO-AI](https://github.com/Matrixx0070/sudo-ai) — community-authored `SKILL.md` behavior packs your agent can discover and install.

**Registry endpoint:** `https://sudoapi.shop/index.json` (served from `docs/` via GitHub Pages)
**Directory UI:** https://sudoapi.shop

## Install a skill

From any SUDO-AI chat channel:

```
install the eli5 skill from the registry
```

or explicitly via the agent tools:

```
skill.search { query: "email" }
skill.install { name: "email-polish", dryRun: false }
```

Every install is verified against the SHA-256 pin in `index.json` and then passes through SUDO-AI's Skill Workshop security gate (prompt-injection scan, capability policy, protected-path check) before anything is written. Installed skills take effect on the next daemon restart and can be removed with `skill.rollback`.

## Repository layout

```
docs/               <- everything servable (GitHub Pages root, CNAME sudoapi.shop)
  index.json        <- THE registry index (name, version, path, sha256, capabilities)
  index.html        <- browsable directory
  skills/
    <name>/SKILL.md <- one directory per skill, single-file skills only (v1)
```

## Skill format (v1)

A skill is one `SKILL.md`: YAML frontmatter + markdown body.

```markdown
---
name: my-skill            # kebab-case, must match the directory name
version: 1.0.0            # semver
description: One line describing what it does.
triggers:                 # phrases that should activate it
  - do the thing
capabilities: []          # subset of: fs.read, fs.write, net.fetch, db.read
inputs:
  - name: text
    required: true
    description: What the skill operates on.
---

# My Skill
Instructions the agent follows when the skill triggers...
```

Rules v1 enforces:

- Single `SKILL.md` per skill (no scripts, no binaries, no extra files).
- `capabilities` must stay within SUDO-AI's workspace tier — `shell.exec` and friends are rejected by the Workshop gate at install time regardless of what the index claims.
- `sha256` in `index.json` must match the file exactly; clients refuse mismatches.

## Contributing

Open a PR that adds `docs/skills/<name>/SKILL.md` and an `index.json` entry (see [CONTRIBUTING.md](CONTRIBUTING.md)). Every submission is human-reviewed before merge; the checksum pins the reviewed content.
