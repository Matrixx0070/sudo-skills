---
name: ops-runbook
version: 1.0.0
description: Create or update an operational runbook for a recurring or on-call task.
author: matrixx0070
tags: [operations, runbook, on-call, procedure, incident]
capabilities: []
---

# Runbook

## When to use
Use this to write a step-by-step operational runbook for a recurring task or incident response, so any qualified operator — including on-call under pressure — can execute it correctly without tribal knowledge.

## METHOD
1. **Define the task and trigger.** State what the runbook covers, when it runs (schedule, alert, or condition), and the expected outcome.
2. **List prerequisites.** Access, credentials, tools, and preconditions that must be true before starting.
3. **State safety and impact.** Note what this affects, who to notify, and any destructive steps.
4. **Write the procedure.** Give numbered, copy-pasteable steps. Each step: the action, the expected result, and how to tell it worked.
5. **Add verification.** Specify the checks that confirm the task succeeded end to end.
6. **Cover failure paths.** For likely failure points, give symptoms and the recovery or rollback action; include an escalation contact.
7. **Record metadata.** Owner, last-tested date, and review cadence — a runbook untested in 90 days is suspect.

## OUTPUT FORMAT
- **Title / purpose / trigger / severity.**
- **Prerequisites:** access, tools, preconditions.
- **Impact & notifications.**
- **Procedure:** numbered steps with expected result per step.
- **Verification:** success checks.
- **Troubleshooting:** symptom → action table.
- **Escalation:** who, when, how.
- **Metadata:** owner, last tested, review cadence.
