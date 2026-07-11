---
name: sec-access-review
version: 1.0.0
description: Run a periodic access review for least-privilege, stale accounts, and role drift.
author: matrixx0070
tags: [security, iam, access-review, least-privilege, governance]
capabilities: []
---

## When to use

Use this on a recurring cadence (quarterly is common), during audits, or after reorgs and offboarding waves. It enforces least privilege and removes access that is no longer justified.

## METHOD

1. **Gather inventory.** Collect all identities (users, service accounts, API keys) and their granted roles/permissions across systems. Include group and inherited access.
2. **Establish expected access.** For each identity, determine the role its job actually requires. Note owners and last-login/last-used timestamps.
3. **Find stale accounts.** Flag disabled-but-not-removed users, accounts with no activity past a threshold, orphaned service accounts, and unused API keys.
4. **Detect over-provisioning.** Compare granted vs. required permissions. Flag admin rights, wildcard grants, and standing access that could be just-in-time.
5. **Detect role drift.** Identify permissions accumulated across role changes that were never revoked, and separation-of-duties conflicts.
6. **Remediate.** Recommend revoke, downgrade, or convert-to-JIT for each finding, and require owner attestation for retained access.

## OUTPUT FORMAT

- **Review scope** — systems and identity count reviewed.
- **Findings table** — Identity | System | Current access | Justified? | Last used | Recommended action.
- **Remediation list** — revoke / downgrade / attest, with owners.
- **Trends** — drift or offboarding gaps to fix in process.
