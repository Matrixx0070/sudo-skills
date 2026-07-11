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

## Reference

### The price / volume / mix bridge (revenue)
Total revenue variance decomposes into three drivers that **must sum to the total**. Let subscript `b` = budget/base, `a` = actual.

- **Volume variance** = (Total units_a − Total units_b) × Budget avg price_b
- **Price variance** = (Price_a − Price_b) × Actual units_a, summed per product
- **Mix variance** = Σ [ (Actual mix% − Budget mix%) × (Budget product price − Budget avg price) ] × Total units_a

Check: Volume + Price + Mix = Actual revenue − Budget revenue. If it doesn't tie, a driver is missing or double-counted. The classic error is applying **both** price and volume at actual quantities — that double-counts the price×volume interaction. Standard convention isolates volume at the *budget* price and price at the *actual* quantity so each interaction is attributed once.

Worked example: Budget 10,000 units @ $50 = $500,000. Actual 11,000 units @ $52 = $572,000. Total var = +$72,000.
- Volume = (11,000 − 10,000) × $50 = **+$50,000**
- Price = ($52 − $50) × 11,000 = **+$22,000**
- Sum = +$72,000 ✓ (single product, so mix = 0).

### Mix vs. volume (multi-product)
When product proportions shift, split "quantity" into pure volume and mix:
- **Pure volume** = change in *total* units, holding budget mix and budget prices constant.
- **Mix** = same total actual units, but reweighted to actual proportions, priced at budget prices, versus budget mix. Selling more of a high-price SKU = favorable mix; shifting to cheap SKUs = unfavorable mix even if total units are flat.

### Cost / spend variances
- **Rate (price) variance** (labor/materials) = (Actual rate − Standard rate) × Actual quantity.
- **Efficiency (usage/volume) variance** = (Actual quantity − Standard quantity for actual output) × Standard rate.
- **Labor:** Rate var = (Act wage − Std wage) × Act hours; Efficiency var = (Act hrs − Std hrs allowed) × Std wage.
- **Materials:** Price var = (Act price − Std price) × Act qty purchased; Usage var = (Act qty used − Std qty allowed) × Std price.
- **Overhead:** Spending variance (actual vs. budgeted at actual activity) and volume variance (budgeted vs. applied). Total = spending + volume.

### Sign and labeling conventions
- **Revenue / margin:** Actual > Budget = **Favorable (F)**; Actual < Budget = **Unfavorable (U)**.
- **Cost / expense:** Actual < Budget = **Favorable**; Actual > Budget = **Unfavorable**. (A negative dollar variance is *not* automatically bad — direction depends on whether the line is revenue or cost.)
- Always tag each driver **persistent** (changes the forward forecast — new pricing, structural demand, headcount ramp) vs **one-time** (does not — a promo, a true-up, a timing shift). Extrapolating a one-time item corrupts the next forecast.

### Waterfall (bridge) construction
Order bars: Baseline → volume → price → mix → rate → efficiency → one-time/timing → Actual. Each bar is signed; the running total after the last bar must equal Actual. The waterfall is the visual proof that the decomposition is complete and ties. Common thresholds for decomposing: only bridge lines exceeding materiality (e.g., ≥5% and ≥ a dollar floor) — decompose the two or three drivers leadership can act on, not every line.
