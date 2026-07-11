---
name: do-incident-runbook
version: 1.0.0
description: Produce a clear on-call runbook mapping symptoms to checks and mitigations so responders act fast.
author: matrixx0070
tags: [incident, oncall, runbook, sre, reliability]
capabilities: []
---

# do-incident-runbook

**When to use:** You need an on-call runbook for a service, are turning tribal knowledge into a document a tired responder can follow at 3am, or are capturing what to do when a specific alert fires.

**METHOD:**
1. State the service's purpose, owners, dependencies, and criticality up front, plus links to dashboards, logs, and the deploy history.
2. For each known failure mode, write a symptom → diagnosis → mitigation entry: the alert or user report, the exact commands/queries to confirm the cause, and the ordered steps to mitigate.
3. Lead with mitigation over root-cause: how to restore service now (roll back, scale out, failover, drain, feature-flag off), then how to investigate after.
4. Include escalation: when to page the next tier, who owns each dependency, and the severity ladder with response-time expectations.
5. Add safety rails — commands that are destructive, changes that need a second approver, and rollback steps for each mitigation.
6. Keep it current: reference the last incident, note gaps, and prompt the reader to update the runbook after use.

**OUTPUT FORMAT:**
- A header block (service, owners, deps, dashboards, severity ladder).
- A symptom/check/mitigation table or numbered entries per failure mode.
- An escalation path and a post-incident update checklist.
