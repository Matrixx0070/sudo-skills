---
name: ops-change-request
version: 1.0.0
description: Draft a change management request with impact analysis and a rollback plan.
author: matrixx0070
tags: [operations, change-management, risk, rollback, itil]
capabilities: []
---

# Change Request

## When to use
Use this before making any production, infrastructure, or process change that could affect users, data, or dependent teams, and when a change advisory board or approver needs a structured record to review.

## METHOD
1. **Describe the change.** State what changes, why now, and the desired end state in one paragraph. Classify as standard, normal, or emergency.
2. **Scope the blast radius.** List affected systems, services, teams, and users. Note upstream and downstream dependencies.
3. **Analyze impact.** Assess effect on availability, performance, security, and cost. Rate risk (low/med/high) and likelihood × impact.
4. **Plan the implementation.** Write ordered steps with owners, the maintenance window, and required approvals.
5. **Define validation.** Specify the exact checks (metrics, smoke tests, user paths) that confirm success post-change.
6. **Write the rollback.** Give the concrete reversal steps, the decision trigger to invoke them, the point of no return, and the max acceptable recovery time.
7. **Communicate.** Note who is informed before, during, and after.

## OUTPUT FORMAT
- **Change ID / title / type / requested-by / date.**
- **Description & justification.**
- **Impact analysis:** systems, dependencies, risk rating.
- **Implementation plan:** numbered steps, owners, window.
- **Validation criteria:** pass/fail checks.
- **Rollback plan:** steps, trigger, point of no return, RTO.
- **Approvals:** required sign-offs.
- **Communication plan.**
