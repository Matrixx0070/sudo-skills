---
name: data-write-query
version: 1.0.0
description: Turn a natural-language data need into optimized, dialect-specific SQL you can run immediately.
author: matrixx0070
tags: [sql, nl2sql, query, warehouse, optimization]
capabilities: []
---

# data-write-query

When to use: someone describes what they want in plain English ("top 10 customers by revenue this quarter, excluding refunds") and needs runnable SQL back. This is the translation skill: intent in, correct dialect-specific query out.

## METHOD

1. **Extract the spec** from the request: the metric, the grain of the output, filters, grouping, sort, limit, and time window. Restate it so the requester can catch a misread before running anything.
2. **Map to schema.** Identify the tables and columns that hold each piece. Confirm keys and each table's grain. If the schema is unknown, state the assumed table/column names clearly so they are easy to correct.
3. **Resolve ambiguity with explicit defaults.** "This quarter" → calendar vs fiscal? "Revenue" → gross vs net of refunds? Pick the common-sense default, label it an assumption, and encode it visibly in the SQL.
4. **Write for the target dialect** (BigQuery, Snowflake, Redshift, Postgres, DuckDB). Use CTEs per step, filter before aggregating, and guard against join fan-out on non-unique keys.
5. **Optimize** while writing: prune partitions, avoid `SELECT *`, use window functions instead of self-joins, and pre-aggregate before joining wide tables.
6. **Predict the output shape** (columns and a sample row) so the requester knows what to expect.

## OUTPUT FORMAT

- **Interpreted need** — the spec in one or two lines.
- **SQL** — final query, dialect labeled, commented, formatted.
- **Assumptions** — every default chosen (definitions, calendar, table/column names).
- **Expected output** — columns and one illustrative row.
- **Adjustments** — the one-line changes to swap common alternatives (fiscal calendar, gross revenue).

Make the assumptions impossible to miss — a wrong metric definition silently returns a plausible but wrong number.
