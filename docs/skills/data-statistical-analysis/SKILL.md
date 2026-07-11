---
name: data-statistical-analysis
version: 1.0.0
description: Run descriptive stats, trend, outlier, correlation, and hypothesis-testing analysis with correct method selection.
author: matrixx0070
tags: [statistics, hypothesis-testing, correlation, trend, outliers]
capabilities: []
---

# data-statistical-analysis

When to use: a question needs statistical rigor — "is this difference real?", "are these correlated?", "is the trend significant?", "which points are outliers?" Use this instead of eyeballing when a decision rides on whether an effect is signal or noise.

## METHOD

1. **Frame the question statistically.** Translate the business ask into a testable form: estimation, comparison, association, or trend. State the population and unit of analysis.
2. **Describe first.** Report n, central tendency (mean/median), spread (SD/IQR), and shape. Visualize the distribution before testing.
3. **Choose the right test by data type and assumptions**:
   - Two-group means → t-test (Welch if variances differ); non-normal/small → Mann-Whitney.
   - >2 groups → ANOVA / Kruskal-Wallis.
   - Categorical association → chi-square / Fisher.
   - Association of numerics → Pearson (linear) or Spearman (monotonic).
   - Trend → regression with significance on the slope.
   Check assumptions (normality, independence, variance) and say which failed.
4. **Report effect size and confidence interval**, not just the p-value. A significant p with a trivial effect is not actionable.
5. **Outliers**: detect (IQR or z-score), investigate cause, and decide keep/exclude with justification — never drop silently.
6. **Correct** for multiple comparisons when running many tests.

## OUTPUT FORMAT

- **Question** — the hypothesis in plain and statistical terms.
- **Descriptives** — n, center, spread, distribution shape.
- **Test** — method chosen and why, plus assumption checks.
- **Result** — statistic, p-value, effect size, and confidence interval.
- **Interpretation** — what it means for the decision, in plain language.
- **Caveats** — sample size, assumptions violated, confounders.

Distinguish statistical from practical significance. State when the sample is too small to conclude anything.
