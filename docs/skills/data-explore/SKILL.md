---
name: data-explore
version: 1.0.0
description: Profile an unfamiliar dataset — shape, quality, nulls, distributions, and duplicates — before any analysis.
author: matrixx0070
tags: [profiling, eda, data-quality, exploration, validation]
capabilities: []
---

# data-explore

When to use: you have just been handed a dataset (file, table, query result) and need to understand it before trusting it. Always run this before analysis — skipping profiling is how wrong numbers reach stakeholders.

## METHOD

1. **Shape.** Report rows, columns, and the grain (what one row represents). Confirm the grain explicitly; most errors trace to a wrong grain assumption.
2. **Schema and types.** List each column, its type, and whether the stored type matches the semantic type (dates stored as strings, IDs stored as numbers).
3. **Completeness.** Per column: null count and percentage. Flag columns that are mostly empty and columns that should never be null but are.
4. **Distributions.** Numeric columns: min, max, mean, median, and outlier flags. Categorical columns: cardinality and top values with frequencies. Date columns: range and gaps.
5. **Duplicates.** Check for fully duplicated rows and for duplicates on the presumed key. Report counts.
6. **Integrity.** Spot referential issues (orphan foreign keys), impossible values (negative ages, future dates), and inconsistent categories ("US" vs "USA").
7. **Reconcile** one total against an external known value to confirm the extract is complete.

## OUTPUT FORMAT

- **Overview** — rows, columns, grain, date range.
- **Column profile** — a table: name, type, %null, cardinality/range, notable values.
- **Quality flags** — ranked list of issues (duplicates, nulls, impossible values, inconsistent categories) with counts and severity.
- **Usability verdict** — is it ready for analysis, ready with caveats, or not usable, and what to fix.

State the grain in the first line. Never proceed to analysis silently past a quality flag — surface it.
