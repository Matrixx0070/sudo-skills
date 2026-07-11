---
name: smb-plan-payroll
version: 1.0.0
description: Forecast cash to the next payroll date, judge coverage, and rank collectible invoices so payroll can run with confidence.
author: matrixx0070
tags: [small-business, payroll, cash, collections, planning, coverage]
capabilities: []
---

# Plan Payroll

## When to use
Use this in the days before a payroll run when the owner needs certainty that cash will cover it — and, if it's tight, a prioritized list of collections and levers that would close the gap.

**Not for:** general 30-day cash outlook (use smb-month-heads-up); running payroll or actually chasing invoices — this produces a plan the owner approves and acts on.

## Method
1. **Set the payroll target.** Payroll date and total due, including employer taxes and any contractor payments.
2. **Project cash to that date.** Start from today's balance, add expected inflows (AR by realistic pay date), subtract non-payroll obligations due before then.
3. **Compute coverage.** Compare projected available cash on payroll date vs the amount due; state surplus or gap and the buffer left. Decision point: if the buffer is thin (say under one week of expenses), treat it as "at-risk," not "go."
4. **Rank collectible invoices.** If tight, sort overdue invoices by (likelihood-to-collect-fast × amount) to show which follow-ups most improve coverage.
5. **List other levers.** Delay discretionary AP, draw on a line of credit, owner contribution — each with an amount.
6. **Give a clear call.** Go / at-risk, in plain words. Do not chase invoices, delay payments, or draw credit yourself — payroll and money decisions are the owner's to approve.

## Example
Payroll $14,000 due Friday. Today $9,500; expected inflow retainer $4,000 (Thu); rent $2,800 due Wed. Projected available Friday = $10,700 → gap of $3,300, buffer negative. Ranked collections: Invoice #188 $5,000 (30 days over, customer reliable — high collect-fast), #191 $2,200 (slow payer — low). Levers: delay $1,500 supplier AP to next week; $2,000 credit line. Call: at-risk — chasing #188 alone closes the gap.

## Pitfalls
- Booking AR on due date instead of a realistic pay date, so coverage looks better than it is.
- Forgetting employer payroll taxes or contractor payments in the amount due.
- Calling "go" on a razor-thin buffer that one late payment would wipe out.
- Acting on collections or credit draws directly — present the plan, let the owner pull the levers.

## Output format
- **Payroll date / amount due** (incl. taxes + contractors).
- **Cash projection to date:** starting | inflows | outflows | available.
- **Coverage verdict:** surplus/gap | buffer | go / at-risk.
- **Ranked collection targets:** invoice | amount | collect-fast likelihood.
- **Other levers:** option | amount.
- **Recommendation (for owner approval).**
