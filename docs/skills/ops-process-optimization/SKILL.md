---
name: ops-process-optimization
version: 1.0.0
description: Analyze a slow or bottlenecked process and propose measurable improvements.
author: matrixx0070
tags: [operations, process, optimization, lean, bottleneck]
capabilities: []
---

# Process Optimization

## When to use
Use this when a process is too slow, error-prone, costly, or inconsistent, and you need to find the constraint and propose changes that move a metric — not just reorganize the diagram.

## METHOD
1. **Quantify the current state.** Measure the baseline: cycle time, throughput, error rate, cost per unit, and lead vs. process time. Without numbers, stop and collect them.
2. **Map the value stream.** Break the process into steps and tag each as value-add, necessary non-value-add, or waste.
3. **Find the bottleneck.** Identify the constraint (longest queue or slowest step) and the waste types present (waiting, rework, handoffs, over-processing).
4. **Root-cause it.** Apply 5 Whys or a cause categorization to the constraint; separate symptoms from causes.
5. **Design improvements.** Propose changes (eliminate, automate, parallelize, reorder, standardize). Estimate the metric impact of each.
6. **Prioritize.** Rank by impact vs. effort; pick the smallest change that relieves the constraint first.
7. **Define measurement.** State how you will confirm the improvement and guard against regression.

## OUTPUT FORMAT
- **Baseline metrics table:** metric, current value.
- **Value-stream map:** step, time, classification.
- **Bottleneck & root cause.**
- **Improvement backlog:** change, expected impact, effort, priority.
- **Projected after-state:** metric, target value.
- **Verification plan.**
