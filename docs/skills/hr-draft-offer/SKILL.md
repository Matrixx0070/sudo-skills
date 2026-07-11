---
name: hr-draft-offer
version: 1.0.0
description: Draft a clear, complete, ready-to-send offer letter with compensation, terms, and contingencies — flagging every unconfirmed figure.
author: matrixx0070
tags: [offer-letter, compensation, hiring, onboarding, terms, contingencies]
capabilities: []
---

## When to use

Reach for this when a candidate has verbally accepted or a hiring manager has approved an offer and you need a written letter ready to send. Produce a professional, accurate document that mirrors the approved requisition exactly.

**Not for:** deciding the numbers or benchmarking pay (use hr-comp-analysis), planning the new hire's ramp (use hr-onboarding), or giving binding legal advice — route jurisdiction-specific clauses to counsel.

## Method

1. **Collect inputs** — candidate name, role title, level, manager, team, start date, employment type (full-time/part-time/contract), work location/remote status, reporting line.
2. **Assemble compensation** — base salary (and pay period), sign-on bonus (with clawback window if any), target annual bonus, equity grant (type, amount, vesting, cliff), benefits summary.
3. **State conditions** — at-will language (jurisdiction-appropriate), background check, work authorization/I-9 or local equivalent, offer expiration date.
4. **Add key terms** — relocation, confidentiality/IP assignment, PTO policy, probation period if applicable. Decision point: include only terms the requisition or policy supports; do not invent.
5. **Set tone** — warm, welcoming opener; precise on every number; clean acceptance instructions (signature + date + deadline).
6. **Verify before delivery** — cross-check every figure and date against the approved req. Decision point: any value you cannot confirm gets a visible `[CONFIRM]` marker, and any legal-sensitive clause routes to counsel before sending.

Never invent numbers, dates, or legal terms. When in doubt, mark it and escalate.

## Example

Candidate Priya Shah, Product Manager (L4), start 2026-08-04, full-time, hybrid (SF). Base $165,000/yr paid semi-monthly; sign-on $15,000 (12-month clawback); target bonus 12%; 12,000 RSUs vesting 4yr with 1-yr cliff. Contingent on background check and I-9. Offer expires 2026-07-25. Placeholder left: `[CONFIRM manager name]` because the req listed "TBD — Growth PM lead." That marker plus a reviewer note ("route clawback clause to legal — CA") ships with the draft.

## Pitfalls

- Copying comp numbers from an earlier draft or memory instead of the signed-off requisition.
- Omitting the offer expiration date, leaving the offer open-ended.
- Using generic at-will boilerplate in a jurisdiction where it is unenforceable (e.g., outside the US).
- Sending before legal/finance review on equity, clawback, or relocation clauses.

## Output format

```
--- OFFER LETTER (ready to send) ---
Greeting
Position: <title>, <level> — reporting to <manager>, <team>
Start date | Employment type | Location/remote
Compensation: base, pay period, sign-on (+clawback), target bonus
Equity: type, amount, vesting, cliff
Benefits: summary
Contingencies: background check, work authorization, offer expiration
At-will / terms: confidentiality/IP, PTO, probation
Acceptance block: signature ___ date ___ deadline ___
---
Placeholder list: [CONFIRM ...] items needing sign-off
Reviewer notes: clauses to route to legal/finance
```
