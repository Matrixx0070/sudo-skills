---
name: data-validate
version: 1.0.0
description: QA a completed analysis for methodology, accuracy, and bias before it is shared with stakeholders.
author: matrixx0070
tags: [validation, qa, accuracy, bias, review]
capabilities: []
---

# data-validate

When to use: an analysis is finished and about to be shared, shipped, or acted on. Run this as the last gate. The goal is to catch the error before the stakeholder does — wrong numbers erode trust permanently.

## METHOD

1. **Reproduce the headline number.** Re-derive the top figure independently from source. If it does not match, stop and reconcile before anything else.
2. **Audit the methodology.** Check the grain, the metric definition, the time window, and the filter logic. Confirm joins did not fan out and that aggregations use the right denominator.
3. **Spot-check rows.** Trace 3-5 individual records end to end from raw source to final output. Sample edge cases: nulls, zeros, extremes, boundary dates.
4. **Reconcile totals** against a known external anchor (a prior report, a system total). Explain any variance.
5. **Hunt for bias**: survivorship (dropped rows), selection (filtered population no longer representative), timezone/date-boundary shifts, and denominator errors. Verify the sample supports the claim's generality.
6. **Pressure-test the conclusion.** Does the data actually support it, or is causation claimed from correlation? Are confidence limits honored?
7. **Check the presentation**: chart axes, units, labels, and rounding are not misleading.

## OUTPUT FORMAT

- **Verdict** — pass / pass-with-fixes / do-not-ship.
- **Checks run** — table of check, result, and evidence.
- **Issues found** — ranked by severity, each with location and fix.
- **Reconciliation** — headline number re-derived and matched (or the variance explained).

Be adversarial toward the analysis, including your own. Report an issue even when it undermines the desired conclusion. Never sign off on an unreconciled headline number.
