---
name: pf-budget
version: 1.0.0
description: Build a personal budget from income and expenses using the 50/30/20 rule or a zero-based plan.
author: matrixx0070
tags: [budget, personal-finance, cash-flow, 50-30-20, zero-based]
capabilities: []
---

## When to use

Use this when the owner wants a clear monthly plan for where their money goes — starting a budget, resetting after lifestyle change, or fixing a "money disappears" feeling. Works for irregular income too (budget from a conservative baseline month).

**Not for:** investment selection, tax filing, debt-strategy sequencing (see pf-debt-payoff), or telling the owner what they *should* value. You structure their choices; you do not moralize spending.

This skill provides education and structure, not individualized financial advice. For decisions with real stakes, recommend a licensed financial planner.

## Method

1. Gather net (take-home) monthly income. Decision point — is income irregular? Use the lowest of the last 3 months as the planning baseline.
2. List fixed expenses (rent, utilities, insurance, minimum debt payments) and variable expenses (food, transport, fun).
3. Decision point — pick a method: **50/30/20** (50% needs, 30% wants, 20% savings/debt) for simplicity, or **zero-based** (every dollar assigned until income minus outflows = 0) for tight control or irregular income.
4. Categorize each expense as need, want, or savings/debt. Sum each bucket.
5. Compare actual buckets to targets. Flag any bucket over target with the gap amount.
6. Decision point — is the plan negative (outflows > income)? Cut from wants first, then renegotiate fixed costs; never zero out savings entirely.
7. Set one automation: move the savings amount out on payday before it can be spent.

## Example

Net income $4,000. 50/30/20 targets: needs $2,000, wants $1,200, savings/debt $800. Actual: needs $2,300 (rent-heavy, +$300 over), wants $1,400 (+$200 over), savings $300 (-$500 short). Fix: trim wants by $200 (dining), redirect to savings → savings $500. Needs stay high; flag rent as >30% of income and revisit at lease renewal.

## Pitfalls

- Budgeting from gross income instead of take-home — you plan money you never receive.
- Forgetting irregular annual costs (insurance, gifts, car registration). Divide them by 12 and reserve monthly.
- Setting wants to $0. Unrealistic budgets get abandoned; leave breathing room.
- Never reviewing. A budget is a monthly loop, not a one-time document.

## Output format

```
PERSONAL BUDGET — [owner] — [month]
Method: [50/30/20 | zero-based]

NET INCOME: $[x]

NEEDS      $[actual] / target $[t]   [OK | OVER +$x]
WANTS      $[actual] / target $[t]   [OK | OVER +$x]
SAVINGS    $[actual] / target $[t]   [OK | SHORT -$x]

ADJUSTMENTS
- [move $x from [cat] to [cat] — reason]

AUTOMATION: transfer $[savings] on payday.
Next: track for one month, then we reconcile actuals.
```
