---
name: hr-comp-analysis
version: 1.0.0
description: Benchmark a role's pay, place it in a band by level/geo/function, and model base/bonus/equity trade-offs with sourced numbers.
author: matrixx0070
tags: [compensation, benchmarking, equity, pay-bands, total-rewards, compa-ratio]
capabilities: []
---

## When to use

Reach for this when you are sizing an offer, resolving a pay-equity question, setting or auditing a band for a role, or deciding a merit/promotion increase. Ground every number in a named source plus the role's level, location, and function.

**Not for:** drafting the offer letter itself (use hr-draft-offer), broad headcount/budget planning (use hr-org-planning), or workforce metrics reporting (use hr-people-report).

## Method

1. **Define the role precisely** — title, job family, level (IC or manager), primary geo tier, and remote policy. These drive every comparison.
2. **Gather benchmarks** — cite sources (survey data, competing offers, published ranges) with percentiles (25th/50th/75th). Decision point: if data is thin, self-reported, or older than ~12 months, widen your range and lower confidence instead of forcing a point estimate.
3. **Set the band** — pick a target percentile per your comp philosophy, then define min / midpoint / max. Compute compa-ratio = actual ÷ midpoint.
4. **Place the candidate** — map experience and skills to a point in the band. Decision point: if they land below min or above max, state why and whether the band or the placement is wrong.
5. **Model total comp** — break out base, target bonus (% and $), equity (grant value, vesting, strike/FMV if options), and benefits. Show year-1 vs. steady-state.
6. **Check equity** — compare against peers at the same level/geo. Any gap over a few percent needs a documented justification or a correction plan.

State assumptions and confidence explicitly. Never present a single number as fact when the underlying data is a range.

## Example

Senior Backend Engineer (IC, L5), Austin (Tier 2), remote-eligible. Survey 50th = $185k base; you target 60th → ~$195k. Band: min $170k / mid $195k / max $225k. Candidate has 8 yrs, strong distributed-systems signal → place at $205k (compa-ratio 1.05). Total comp year-1: $205k base + 15% target bonus ($30.75k) + $400k RSU over 4yr ($100k/yr) = ~$335k; steady-state ~$336k. Peer check: two L5 peers at $200k/$208k — placement is equitable.

## Pitfalls

- Benchmarking by title alone — a "Senior Engineer" at two firms can be two levels apart. Match on scope, not label.
- Comparing across geos without adjusting for the location tier or the company's remote-pay policy.
- Presenting the 50th percentile as "the market rate" and hiding the spread.
- Modeling equity at grant value without noting vesting schedule, cliff, or dilution/strike reality.

## Output format

```
Role: <title> | Level: <L#> | Geo: <tier> | Source + date: <...>
Market table:
  pctile | base | bonus | equity | total
  25th   | ...  | ...   | ...    | ...
  50th   | ...  | ...   | ...    | ...
  75th   | ...  | ...   | ...    | ...
Recommended band: min <$> / mid <$> / max <$> | target compa-ratio <x>
Placement: <$> at compa-ratio <x> — rationale: <...>
Total-comp model: year-1 <$> | steady-state <$>
Risks / equity flags / assumptions: <...>
```
