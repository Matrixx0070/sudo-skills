---
name: cs-escalation
version: 1.0.0
description: Package a customer escalation for engineering, product, or leadership with complete, decision-ready context.
author: matrixx0070
tags: [customer-support, escalation, triage, communication, handoff]
capabilities: []
---

When to use: a ticket exceeds frontline scope — a confirmed bug, a data-loss risk, a churn-threatening account, a legal/security concern, or a repeated issue that needs an owner outside support. Use this to hand off cleanly so the receiving team can act without a second round of questions.

METHOD
1. Classify the escalation type (Bug / Outage / Data / Security / Billing / Churn-risk / Feature-gap) and pick the target team. State why it leaves support scope in one line.
2. Establish impact: how many users/accounts, revenue at stake, plan tier, and whether it is spreading. Quantify — "1 enterprise account, $48k ARR, renewal in 3 weeks" beats "important customer."
3. Reconstruct the timeline: when it started, what the customer did, what support already tried, and the current state. Link the ticket and any logs, screenshots, or repro steps.
4. Separate facts from hypotheses. Mark each line [confirmed] or [suspected]. Never present a guess as a diagnosis.
5. State the specific ask and urgency: what you need the team to do, by when, and what unblocks the customer in the meantime (workaround given? credit offered?).
6. Name an owner and next check-in time so the escalation cannot stall silently.

OUTPUT FORMAT
- Title: [SEVERITY] one-line summary
- Impact: users / revenue / tier / renewal
- Timeline: dated bullets
- Facts vs. hypotheses (tagged)
- The ask + deadline
- Links: ticket, logs, repro
- Owner + next check-in
