---
name: pf-big-purchase
version: 1.0.0
description: Decide on a big purchase (rent vs buy, cash vs finance) using a structured cost-and-fit framework.
author: matrixx0070
tags: [big-purchase, rent-vs-buy, financing, affordability, personal-finance]
capabilities: []
---

## When to use

Use this when the owner faces a large decision — home, car, major appliance — and needs a framework to compare rent vs buy, or cash vs financing, without emotion driving the call. Good for pressure-testing affordability before committing.

**Not for:** predicting home/market prices, choosing a specific lender or mortgage product, or approving the purchase. You frame the trade-offs; the owner decides and signs.

This skill provides education and structure, not individualized financial advice. For mortgages, large loans, or anything irreversible, recommend a licensed advisor or mortgage professional.

## Method

1. Define the item, total price, and how long the owner realistically expects to keep/use it.
2. Compute true cost of ownership: purchase price + financing interest + maintenance/insurance/fees + opportunity cost of the down payment. For renting: rent + expected increases over the same period.
3. Decision point — **rent vs buy**: if the horizon is short (<3-5 yr) or the owner values mobility, renting usually wins; longer horizons and stability favor buying. Compare total costs over the *same* period.
4. Affordability gate: does the monthly payment fit the budget without cutting savings below target? If it forces savings to zero, it fails the gate.
5. Decision point — **cash vs finance**: compare the loan APR to what the cash could earn safely. High APR favors paying cash/larger down payment; low APR may favor keeping cash invested — if the owner has the discipline.
6. Reserve check: does the owner keep their emergency fund intact after the down payment? If not, defer.
7. Score fit vs cost and state a clear recommendation with the deciding factor.

## Example

Car, $30,000, keep 8 years. Buy financed at 7% APR: interest ~$5,600 + insurance/maintenance. Cash available but that would drain the emergency fund → finance, but with a larger down payment to cut interest. Monthly payment $520 fits budget without touching savings. Recommendation: buy, finance partially, keep 3-month reserve. Deciding factor: long horizon + reserve preservation.

## Pitfalls

- Comparing monthly rent to a mortgage payment alone — ignores maintenance, taxes, insurance, and opportunity cost.
- Draining the emergency fund for a down payment; one shock then forces high-interest debt.
- Stretching to the maximum a lender approves. Approval is not affordability.
- Anchoring on sticker price and ignoring multi-year total cost of ownership.

## Output format

```
BIG-PURCHASE DECISION — [owner] — [item]
Price: $[x]   Horizon: [x] yrs

RENT/KEEP-CASH vs BUY/FINANCE (same period)
Option A total cost: $[x]
Option B total cost: $[x]

AFFORDABILITY GATE: payment $[x]/mo — [fits | fails] (savings target intact? [y/n])
RESERVE CHECK: emergency fund after purchase — [intact | breached]
CASH vs FINANCE: APR [x]% vs safe yield [x]% -> [pay cash | finance]

RECOMMENDATION: [buy/rent/defer] — deciding factor: [x]
Confirm large loans with a licensed professional before signing.
```
