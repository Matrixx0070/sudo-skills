---
name: pf-retirement-plan
version: 1.0.0
description: Build a personal retirement savings plan and projection from age, savings rate, and target (educational).
author: matrixx0070
tags: [retirement, savings-rate, compounding, projection, personal-finance]
capabilities: []
---

## When to use

Use this when the owner wants to know if they are on track for retirement — projecting a nest egg from current savings, contribution rate, and time, and translating a target income into a savings goal.

**Not for:** choosing specific funds or accounts (see pf-investment-allocation), guaranteeing returns, or giving withdrawal-tax rulings. Projections are estimates, not promises.

This skill provides education and structure, not individualized financial advice. Retirement outcomes depend on markets, inflation, and personal factors — recommend a licensed financial planner before relying on any projection.

## Method

1. Gather inputs: current age, target retirement age, current retirement savings, monthly contribution, and desired annual retirement income.
2. Estimate the target nest egg. Educational rule of thumb: target ≈ desired annual income × 25 (the 4% rule), adjusted for other income sources like pensions/social security.
3. Project growth: compound current savings + contributions to retirement age. Use a conservative real (after-inflation) return assumption, e.g., 5%, and state it explicitly.
4. Decision point — is the projection below target? Increase contributions, delay retirement, or lower the income target; show the gap in dollars and the extra monthly saving needed to close it.
5. Prioritize order: capture any employer match first (free money), then tax-advantaged accounts, then taxable — but keep this account-type guidance educational.
6. Decision point — is retirement <10 years out? Shift the conversation toward capital preservation and sequence-of-returns risk; defer specifics to a professional.
7. Set a yearly review to update inputs and re-project.

## Example

Age 35, retire at 65, $50,000 saved, $600/mo contributions, wants $40,000/yr income. Target ≈ $1,000,000. At 5% real return, $50k grows to ~$216k and 30 yrs of $600/mo adds ~$478k → ~$694k projected. Gap ≈ $306k. Closing it needs roughly +$380/mo (to ~$980/mo). Action: capture full employer match first, then raise contributions gradually. Review yearly.

## Pitfalls

- Using nominal returns and ignoring inflation — the projected number looks great and buys far less.
- Assuming aggressive returns (10%+) that leave no margin for bad decades.
- Leaving employer match on the table; it is an immediate guaranteed return.
- Treating one projection as destiny. Re-run yearly as income and markets change.

## Output format

```
RETIREMENT PROJECTION (educational) — [owner]
Age [x] -> retire [x]   Assumed real return: [x]% (stated, not guaranteed)

TARGET NEST EGG: $[x]  (desired income $[x]/yr × 25, adj. for [pension/SS])
PROJECTED AT RETIREMENT: $[x]
GAP: $[x]   ->  close with +$[x]/mo OR delay [n] yrs OR lower target

PRIORITY ORDER: 1) employer match  2) tax-advantaged  3) taxable
REVIEW: yearly.

Estimate only — confirm with a licensed financial planner before relying on it.
```
