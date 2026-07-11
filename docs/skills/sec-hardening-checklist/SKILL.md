---
name: sec-hardening-checklist
version: 1.0.0
description: Produce a CIS-style server and application hardening checklist with prioritized fixes.
author: matrixx0070
tags: [security, hardening, cis, baseline, configuration]
capabilities: []
---

## When to use

Use this when standing up a new server or service, preparing for an audit, or reducing attack surface on existing infrastructure. It maps configuration to a defensive baseline and ranks the fixes by impact.

## METHOD

1. **Identify the target.** Note the OS, runtime, exposed services, and network position (internet-facing vs. internal). Pick the relevant baseline (CIS benchmark, vendor guide).
2. **OS & accounts.** Check patch level, disabled root SSH login, key-only auth, minimal sudoers, no default/shared accounts, and password/lockout policy.
3. **Network & services.** Verify firewall default-deny, only required ports open, no unneeded daemons, and TLS with modern ciphers on every listener.
4. **Application config.** Confirm secure headers, disabled debug/verbose errors, least-privilege service accounts, resource limits, and secrets sourced from a vault.
5. **Logging & monitoring.** Ensure audit logging is on, logs ship off-host, and alerts exist for auth failures and privilege changes.
6. **Prioritize.** Rank each gap by exposure and exploitability; internet-facing and privilege-related gaps first.

## OUTPUT FORMAT

- **Target profile** — OS, services, exposure, baseline used.
- **Checklist table** — Control | Category | Status (Pass/Fail/N-A) | Evidence | Fix.
- **Prioritized fixes** — Critical → Low, each with effort estimate.
- **Baseline drift note** — what to re-check periodically.
