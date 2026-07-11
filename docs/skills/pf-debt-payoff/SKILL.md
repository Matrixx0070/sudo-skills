---
name: pf-debt-payoff
version: 1.0.0
description: Plan a debt payoff using the avalanche or snowball method and produce a month-by-month schedule.
author: matrixx0070
tags: [debt, payoff, avalanche, snowball, personal-finance]
capabilities: []
---

## When to use

Use this when the owner has multiple debts (cards, loans, buy-now-pay-later) and wants a concrete plan to clear them. Good for choosing an order, seeing a payoff date, and quantifying interest saved.

**Not for:** budgeting the monthly surplus itself (see pf-budget), bankruptcy or debt-settlement decisions, or negotiating with creditors on the owner's behalf. Those are hard stops requiring the owner and, where stakes are high, a professional.

This skill provides education and structure, not individualized financial or legal advice. For settlement, consolidation, or hardship decisions, recommend a licensed advisor or nonprofit credit counselor.

## Method

1. List every debt: balance, APR, and minimum payment.
2. Determine the monthly amount available above the sum of all minimums (the "attack" amount).
3. Decision point — pick a method: **avalanche** (attack highest APR first) minimizes total interest; **snowball** (attack smallest balance first) maximizes early wins and motivation.
4. Pay all minimums always; direct the full attack amount to the one target debt per the chosen order.
5. When a debt clears, roll its entire payment (minimum + attack) into the next target — the payment size snowballs.
6. Build the schedule month by month until each balance hits zero; record the payoff month and total interest.
7. Decision point — is any APR above ~20% and eligible for a lower-rate transfer or consolidation? Note it as an option to research (do not execute).

## Example

Debts: Card A $2,000 @ 24%, Card B $5,000 @ 18%, min payments $50 + $100. Attack amount $300/mo. Avalanche targets Card A first ($350/mo to A, $100 min to B). Card A clears ~month 6; roll $350 into B → B gets $450/mo, clears ~month 17. Total interest ≈ $1,050. Snowball would also clear A first here (it is both smallest and highest-rate), so the orders coincide.

## Pitfalls

- Skipping a minimum on a non-target debt — triggers fees and credit damage that dwarf the interest saved.
- Choosing avalanche on paper but abandoning it emotionally. If motivation is the real risk, snowball's wins may finish the job faster.
- Adding new debt mid-plan. Pause new borrowing or the schedule never converges.
- Ignoring a 0%-transfer window's expiry — unpaid balances snap back to high APR.

## Output format

```
DEBT PAYOFF PLAN — [owner]
Method: [avalanche | snowball]   Attack: $[x]/mo above minimums

ORDER
1. [debt] — $[bal] @ [APR]% — payoff ~[month]
2. [debt] — $[bal] @ [APR]% — payoff ~[month]

DEBT-FREE DATE: [month/year]
TOTAL INTEREST PAID: ~$[x]

OPTIONS TO RESEARCH
- [balance transfer / consolidation note]

Next: keep minimums automatic; send $[attack] to target #1 each month.
```
