---
name: data-analyze
version: 1.0.0
description: Answer any data question, scaling effort from a one-number lookup to a full stakeholder-ready analysis.
author: matrixx0070
tags: [data, analysis, reporting, insights, decision-support]
capabilities: []
---

# data-analyze

When to use: whenever someone asks a question that a dataset can answer — from "what was revenue last month?" to "why did churn spike in Q3 and what should we do?" Right-size the effort: do not build a 5-section report for a single number, and do not answer a strategic question with one unexplained figure.

## METHOD

1. **Classify the ask.** Decide the tier: (a) lookup — one metric; (b) comparison — segment/time deltas; (c) diagnostic — why did X change; (d) stakeholder analysis — decision + recommendation. State the tier you chose.
2. **Restate the question** in precise terms: metric definition, grain, time window, filters, and population. Surface hidden assumptions.
3. **Locate and confirm the source** (table, file, query). Verify the grain and that the numbers reconcile against a known total before analyzing.
4. **Compute** with the smallest correct operation for the tier. Show the query or transformation used.
5. **Interpret**: quantify magnitude, direction, and whether it is meaningful vs noise. For diagnostics, decompose the change (segment, mix, rate).
6. **Recommend** only for tier (d): tie each insight to a concrete action and its expected impact.

## OUTPUT FORMAT

- **Answer** — the direct number/finding in the first line, with units and time window.
- **How** — one-line method and source (so it is reproducible).
- **Context** — comparison, trend, or benchmark that makes the number meaningful.
- **Caveats** — data gaps, definitions, or confidence limits.
- **Recommendation** — only for stakeholder tier; each action tagged with expected impact.

Lead with the answer. Never bury the number under methodology. If the data cannot answer the question, say so explicitly and state what would be needed.
