---
name: fin-cash-flow
version: 1.0.0
description: Build a 30/60/90-day cash-flow forecast from AR and AP with liquidity risk flags.
author: matrixx0070
tags: [finance, cash-flow, forecast, treasury, liquidity]
---

# Cash Flow Forecast

## When to use
Use this to project short-term liquidity, to answer "will we make payroll / cover this quarter," or to build a rolling 30/60/90-day cash forecast from receivables, payables, and known fixed outflows.

## METHOD
1. **Set the starting position.** Record today's cash balance, the forecast start date, and any minimum-cash covenant or comfort floor.
2. **Project inflows.** From the AR aging, schedule expected collections by expected pay date; apply realistic collection-probability haircuts by aging bucket. Add other known inflows (financing, deposits).
3. **Project outflows.** From the AP aging and payment terms, schedule disbursements; add recurring fixed outflows (payroll, rent, debt service, taxes) on their due dates.
4. **Bucket into 30/60/90.** Roll inflows and outflows into three periods; compute net cash flow and running ending balance per bucket.
5. **Flag risk.** Mark any period where ending balance breaches the floor or goes negative; identify the shortfall size and date.
6. **Model levers.** Show the effect of accelerating collections, delaying payables, or drawing a credit line.
7. **Recommend actions.** Prioritize the levers that close the gap with least disruption.

## OUTPUT FORMAT
- **Starting cash / start date / minimum floor.**
- **Forecast table:** period (30/60/90), inflows, outflows, net, ending balance.
- **Inflow detail:** source/customer, amount, expected date, probability.
- **Outflow detail:** payee/category, amount, due date.
- **Risk flags:** period, shortfall, date floor is breached.
- **Scenario levers:** action, cash impact, timing.
- **Recommended actions, prioritized.**
