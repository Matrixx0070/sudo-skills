---
name: sec-secrets-scan
version: 1.0.0
description: Scan a repository and logs for leaked secrets and produce a credential rotation runbook.
author: matrixx0070
tags: [security, secrets, credentials, rotation, dlp]
capabilities: []
---

## When to use

Use this when onboarding a repo, after a suspected leak, before open-sourcing code, or on a recurring cadence. It detects exposed credentials so they can be revoked and rotated defensively.

## METHOD

1. **Define targets.** Enumerate what to scan: working tree, full git history, CI logs, application logs, and config/env files.
2. **Pattern scan.** Search for high-entropy strings and known token shapes: AWS keys (AKIA...), private keys (BEGIN ... PRIVATE KEY), JWTs, `Bearer` tokens, DB connection strings, and `password=`/`api_key=` assignments.
3. **History sweep.** Scan committed history, not just HEAD — secrets often live in old commits. Note that deleting a file does not remove it from history.
4. **Triage findings.** Classify each hit as true positive, test/placeholder, or false positive. Record where it is exposed and its blast radius.
5. **Rotation runbook.** For each confirmed secret: revoke the credential at the provider, issue a replacement, update the secret store, redeploy, then purge history if warranted.
6. **Prevent recurrence.** Recommend pre-commit secret scanning, `.gitignore` hardening, and a secrets manager.

## OUTPUT FORMAT

- **Scan scope** — targets covered.
- **Findings table** — Secret type | Location (file:line / commit / log) | Confidence | Blast radius.
- **Rotation runbook** — per secret: revoke → reissue → update store → redeploy → verify.
- **Prevention** — tooling and policy recommendations.
