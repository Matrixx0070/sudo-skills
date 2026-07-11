---
name: ops-capacity-plan
version: 1.0.0
description: Build a resource capacity plan from workload analysis and a utilization forecast.
author: matrixx0070
tags: [operations, capacity, forecasting, planning, resources]
capabilities: []
---

# Capacity Plan

## When to use
Use this when you must decide whether current resources (people, compute, budget, throughput) will meet projected demand, or when planning hiring, procurement, or scaling ahead of a known growth curve or seasonal peak.

## METHOD
1. **Define the resource and unit.** Name what you are sizing (engineers, CPU cores, support tickets/day) and the measurable unit of capacity per resource.
2. **Baseline current state.** Record total capacity, current demand, and utilization % (demand ÷ capacity). Flag anything already above 80%.
3. **Gather the demand drivers.** Identify what moves the workload (users, transactions, releases) and pull 3-6 periods of history.
4. **Forecast demand.** Project each driver forward using growth rate, seasonality, and known events. State the model and its assumptions.
5. **Compute the gap.** For each future period, calculate required capacity vs. available, applying a target headroom buffer (default 20%).
6. **Recommend actions.** For each gap, propose add/reallocate/defer with lead time and cost, and mark the trigger threshold that forces the action.

## OUTPUT FORMAT
- **Summary:** resource, horizon, headline verdict (adequate / gap in period X).
- **Baseline table:** capacity, demand, utilization %.
- **Forecast table:** period, projected demand, required capacity, available, surplus/deficit, utilization %.
- **Assumptions:** growth rate, buffer, model used.
- **Recommendations:** action, timing, cost, trigger threshold.
- **Risks:** what breaks the forecast.
