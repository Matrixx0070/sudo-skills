---
name: sec-incident-response
version: 1.0.0
description: Drive a security incident through contain, eradicate, recover, and postmortem phases.
author: matrixx0070
tags: [security, incident-response, forensics, postmortem, containment]
capabilities: []
---

## When to use

Use this when a security incident is suspected or confirmed — breach, malware, credential compromise, data exposure, or active intrusion. It structures a calm, evidence-preserving defensive response.

## METHOD

1. **Triage & declare.** Confirm the incident is real, classify severity, assign an incident lead, and open a timestamped log. Record scope: what systems, data, and accounts are involved.
2. **Preserve evidence.** Before changing anything, capture volatile state (logs, memory, connections, disk snapshots). Do not tip off an active attacker prematurely.
3. **Contain.** Isolate affected hosts, revoke compromised credentials and sessions, block malicious IPs/domains, and disable exploited paths. Prefer reversible short-term containment first.
4. **Eradicate.** Remove malware, close the entry vector, patch the exploited weakness, and rotate all potentially exposed secrets.
5. **Recover.** Restore from known-good backups, rebuild rather than clean when in doubt, monitor closely for reinfection, and confirm service integrity before reopening.
6. **Postmortem.** Write a blameless timeline, root cause, impact, what worked, and concrete action items with owners and dates.

## OUTPUT FORMAT

- **Incident summary** — severity, scope, current status.
- **Timeline** — timestamped events and actions taken.
- **Phase checklist** — Contain / Eradicate / Recover items with status.
- **IOCs** — indicators of compromise observed.
- **Postmortem** — root cause, impact, action items (owner + due date).
