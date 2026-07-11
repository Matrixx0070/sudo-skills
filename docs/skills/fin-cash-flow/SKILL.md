---
name: fin-cash-flow
version: 1.0.0
description: Build a rolling 30/60/90-day cash forecast from AR/AP aging and fixed outflows, flag floor breaches, and model liquidity levers.
author: matrixx0070
tags: [finance, cash-flow, forecast, treasury, liquidity, 13-week]
---

# Cash Flow Forecast

## When to use
Use this to project short-term liquidity, answer "will we make payroll / cover this quarter," or build a rolling 30/60/90-day cash forecast from receivables, payables, and known fixed outflows.

**Not for:** the historical indirect-method cash flow *statement* in a reporting package (fin-financial-statements), or actual-vs-plan variance on cash (fin-variance-analysis). This is forward-looking liquidity planning.

## Method
1. **Set the starting position.** Record today's cash balance, the forecast start date, and any minimum-cash covenant or comfort floor.
2. **Project inflows.** From AR aging, schedule expected collections by expected pay date. Decision point: apply collection-probability haircuts by aging bucket (current ~95%, 30–60 ~80%, 90+ ~50%) — do not forecast overdue invoices at face value. Add other known inflows (financing, deposits).
3. **Project outflows.** From AP aging and payment terms, schedule disbursements; add recurring fixed outflows (payroll, rent, debt service, taxes) on their due dates.
4. **Bucket into 30/60/90.** Roll inflows and outflows into three periods; compute net cash flow and a running ending balance per bucket.
5. **Flag risk.** Decision point: mark any period where ending balance breaches the floor or goes negative; record shortfall size and the exact date it hits.
6. **Model levers.** Show the effect of accelerating collections, delaying payables, or drawing a credit line.
7. **Recommend actions.** Prioritize the levers that close the gap with the least disruption.

## Example
Start cash $220k, floor $150k. Days 0–30: inflows $310k (AR, haircut-adjusted), outflows $360k (incl. $180k payroll) → net −$50k, ending $170k (above floor). Days 31–60: inflows $280k, outflows $340k → net −$60k, ending $110k — **breaches $150k floor on day ~48**, shortfall $40k. Lever: pull a $90k invoice from a current-bucket customer forward 15 days (accelerate collection) → day-48 balance back to $170k. Recommend that plus deferring a $30k non-critical payable one cycle as backup.

## Pitfalls
- **Forecasting overdue AR at face value.** 90+ invoices rarely pay in full or on time — haircut them or you overstate liquidity.
- **Missing fixed, non-invoice outflows.** Payroll, taxes, and debt service don't appear in AP aging; add them explicitly.
- **Netting away timing.** A month that nets positive can still go negative mid-period if a big outflow lands before the inflow — track the running daily/weekly balance, not just the bucket total.
- **Ignoring the floor until it's breached.** Model levers *before* the shortfall date, not after.

## Output format
```
Starting cash: <$> | Start date: <...> | Minimum floor: <$>
Forecast:
  | period (30/60/90) | inflows | outflows | net | ending balance |
Inflow detail: | source/customer | amount | expected date | probability |
Outflow detail: | payee/category | amount | due date |
Risk flags: | period | shortfall $ | date floor breached |
Levers: | action | cash impact | timing |
Recommended actions (prioritized): <...>
```
