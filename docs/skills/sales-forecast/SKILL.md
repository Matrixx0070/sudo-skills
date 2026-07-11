---
name: sales-forecast
version: 1.0.0
description: Build a weighted sales forecast with best/likely/worst cases, commit vs. upside, and gap-to-target.
author: matrixx0070
tags: [sales, forecast, pipeline, revenue]
capabilities: []
---

# Sales Forecast

## When to use
Use this at forecast time when you have a set of open deals and need a defensible number for the period — with the reasoning a manager can challenge and the gaps you must close to hit quota.

## METHOD
1. **Set the frame.** Confirm the period, the quota/target, and any already-closed-won bookings.
2. **Normalize each deal.** For every open deal capture amount, stage, close date, and a probability — using stage defaults adjusted for real signals (engagement, next step set, champion strength).
3. **Categorize.** Sort deals into Commit (high confidence, will close), Best Case/Upside (possible but not banked), and Pipeline (early, this-period unlikely).
4. **Compute scenarios.** Worst = closed-won + only rock-solid commits. Likely = commit + probability-weighted best case. Best = commit + full best case.
5. **Weight the total.** Sum amount × probability for the weighted forecast.
6. **Gap analysis.** Compare each scenario to target; state the shortfall and what must convert to close it.
7. **Flag risk.** Call out deals with slipping dates, no next step, or single-threaded contacts that inflate the number.

## OUTPUT FORMAT
- **Period and target:** one line.
- **Scenario summary:** worst / likely / best with dollar figures.
- **Commit vs. upside:** two totals with the deals in each.
- **Weighted forecast:** the probability-weighted number.
- **Gap to target:** amount and what must close.
- **At-risk deals:** deal — risk — impact on forecast.
- **Assumptions:** probabilities and defaults used.
