---
name: cs-ticket-triage
version: 1.0.0
description: Triage an incoming support ticket — assign priority P1-P4, route it, and check for duplicates and known issues.
author: matrixx0070
tags: [customer-support, triage, prioritization, routing, sla]
capabilities: []
---

When to use: a new ticket arrives and must be sorted before work begins. Use this to set the right priority, send it to the right team, and avoid re-solving something already tracked.

METHOD
1. Extract the essentials: what broke, for whom (plan tier, account value), scope (one user vs. many), and business impact. Note anything time-sensitive (deadline, event, renewal).
2. Assign priority by impact × reach:
   - P1: outage, data loss, security, or many/high-value accounts blocked — respond now.
   - P2: major feature broken for one account or degraded for many, no workaround.
   - P3: broken with a workaround, or single-user non-critical.
   - P4: cosmetic, minor, or feature request.
3. Check for duplicates: search open tickets and known-issue lists for the same symptom. If found, link and merge rather than open a parallel thread.
4. Check known issues / recent releases — if it matches a tracked bug, tag it and attach the customer to that issue for updates.
5. Route to the owning team (support tier, billing, eng, security) with a one-line reason. State the applicable SLA and first-response deadline.
6. If information is missing to triage confidently, list the exact questions to ask the customer.

OUTPUT FORMAT
- Priority: P1-P4 + one-line justification
- Category + route (team/queue)
- Duplicate / known-issue: link or "none found"
- SLA / first-response deadline
- Missing info to request (if any)
