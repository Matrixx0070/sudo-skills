---
name: fin-variance-analysis
version: 1.0.0
description: Decompose an actual-vs-plan gap into price, volume, mix, and rate drivers that sum to the total, with a waterfall and action-oriented narrative.
author: matrixx0070
tags: [finance, variance, fpa, budget, bridge, waterfall]
---

# Variance Analysis

## When to use
Use this to explain why actuals differ from budget, forecast, or prior period — for a P&L line, a department, or a KPI — turning a raw dollar gap into named, quantified drivers leadership can act on.

**Not for:** the statement-level "material line changed" flagging inside a reporting package (fin-financial-statements does that lightly), or reconciling GL to a source (fin-reconciliation). This is the *why* behind one variance, decomposed.

## Method
1. **Frame the comparison.** State the metric, actual, baseline (budget / forecast / prior), and total variance in $ and %; note favorable (F) or unfavorable (U).
2. **Set materiality.** Define the $ and/or % threshold below which you do not decompose.
3. **Decompose into drivers.** Use the right bridge: price × volume for revenue, rate × hours for labor, volume × mix for product lines, plus one-time/timing items. Decision point: the drivers *must* sum back to the total variance — if they don't, a driver is missing or double-counted.
4. **Quantify each driver.** Compute each in isolation, holding the others constant.
5. **Attribute causes.** Give each driver a business reason (new pricing, demand shift, headcount ramp, timing of spend).
6. **Build the waterfall.** Bridge baseline → each driver (up/down bars) → actual so the decomposition is visible and ties.
7. **Write the narrative and flag risk.** Decision point: label each driver persistent vs one-time — persistent drivers change the forecast; one-time do not.

## Example
Revenue: actual $4.6M vs budget $4.0M, +$600k (+15%, F). Decompose price × volume: volume +8,000 units × $50 budget price = +$400k; price +$2.50 × 84,000 actual units = +$210k; mix shift to lower-price SKU = −$10k. Sum: +$600k — ties. Causes: volume from a new enterprise deal (persistent), price from the January list increase (persistent), mix from SMB promo (one-time). Narrative: raise the forward forecast for volume and price; do not extrapolate the promo mix.

## Pitfalls
- **Drivers that don't sum to the total.** A bridge that leaves an unexplained plug is not a decomposition — find the missing driver.
- **Double-counting price and volume.** Applying both at actual quantities overstates; hold one constant per driver.
- **Naming a number, not a cause.** "Volume +$400k" without the enterprise deal behind it gives leadership nothing to act on.
- **Treating one-time items as run-rate.** Extrapolating a promo or true-up corrupts the next forecast.

## Output format
```
Metric: <...> | Actual: <...> | Baseline: <budget/fcst/prior> | Total var: <$> (<%>) [F/U]
Materiality: <$ / %>
Drivers:
  | driver | $ impact | % of total | cause | persistent? |
  Sum of drivers = total variance? [yes/no]
Waterfall: baseline → <driver bars> → actual  (ties: [yes/no])
Narrative: <plain language>
Risks / watch items: <...> | recommended actions: <...>
```
