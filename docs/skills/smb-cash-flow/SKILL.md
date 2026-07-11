---
name: smb-cash-flow
version: 1.0.0
description: Produce a 30/60/90-day cash-flow forecast from AR and AP with base/low/high confidence bands and shortfall alerts.
author: matrixx0070
tags: [small-business, cash-flow, forecast, ar, ap, runway]
---

# Cash Flow Forecast

## When to use
Use this when the owner needs to know whether cash will cover commitments over the next quarter — before an expense, a hire, or a large purchase, or when a lender or partner asks for a forward view.

**Not for:** the live one-glance snapshot (use smb-business-pulse) or historical reconciliation (use smb-close-month). This is forward-looking decision support, not a closed record.

## Method
1. **Set starting cash and horizon.** State today's bank balance and forecast the next 30, 60, and 90 days, weekly.
2. **Schedule inflows from AR.** List open receivables by expected pay date. Decision point: adjust each date by the customer's historical days-to-pay, not the invoice term — a net-30 invoice from a customer who always pays in 50 lands in week 7.
3. **Schedule outflows from AP.** List payables, payroll, rent, loan payments, taxes, and recurring subscriptions by due date.
4. **Roll the balance forward.** Compute projected ending cash for each week and at the 30/60/90 marks.
5. **Apply confidence bands.** Give a base case, a low case (late payers slip, no new sales), and a high case (on-time collections) as a range.
6. **Flag shortfalls.** Identify any week the balance dips below the owner's minimum buffer, and how large the gap is.

This is decision support; the owner approves any financing, delayed payment, or spending decision it informs.

## Example
Start $32k. Week 5 (base): inflows $18k, outflows $27k → ending $23k. Low case dips to $9k in week 6 — below the $15k buffer, a $6k gap driven by a $12k customer who historically pays 20 days late. Recommend: confirm that payment date or line up a short bridge. Owner decides.

## Pitfalls
- **Using invoice terms, not behavior.** Net-30 on paper, net-55 in practice — history is the truth.
- **Forgetting lumpy outflows.** Quarterly taxes, annual insurance, and loan balloons wreck an otherwise fine month.
- **A single point estimate.** Cash is a range; always show low/base/high, not one line.
- **Counting speculative new sales in the base.** Keep unclosed pipeline in the high case only.

## Output format
```
Starting cash: $__ | forecast date: <date>
Weekly (base):
| Week | Inflows | Outflows | Ending |
30/60/90 summary: base $__ | low $__ | high $__
Shortfall alerts: week __ — gap $__ — driver ___
Assumptions: days-to-pay used, items excluded
Recommended actions (owner approval required):
```
