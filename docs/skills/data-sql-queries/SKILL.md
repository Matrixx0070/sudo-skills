---
name: data-sql-queries
version: 1.0.0
description: Write correct, performant SQL across warehouse dialects and optimize slow queries.
author: matrixx0070
tags: [sql, warehouse, optimization, bigquery, snowflake]
capabilities: []
---

# data-sql-queries

When to use: you need production-grade SQL — a new query, a refactor, or a fix for one that is slow, wrong, or expensive — on a warehouse (BigQuery, Snowflake, Redshift, Postgres, DuckDB). Correctness first, then performance.

## METHOD

1. **Confirm the contract**: target dialect, source tables, grain, expected output columns, and how the result will be used. Ambiguity here produces confidently wrong SQL.
2. **Get the grain right.** Know each table's grain before joining. Guard against fan-out: joins on non-unique keys silently multiply rows and inflate SUMs. Verify row counts before and after each join.
3. **Structure for readability** with CTEs, one logical step each. Filter early, aggregate late. Prefer explicit column lists over `SELECT *`.
4. **Match the dialect**: date functions, `QUALIFY` (BigQuery/Snowflake), array/struct handling, and window syntax differ. Do not port syntax blindly.
5. **Optimize**: prune partitions and clustering keys, push filters down, avoid `SELECT *` on wide tables, replace correlated subqueries with joins/windows, and pre-aggregate before joining. On BigQuery, watch bytes scanned; on Snowflake, watch spillage and warehouse size.
6. **Read the plan.** Use `EXPLAIN`/query profile to confirm the fix; cite the before/after cost or runtime rather than asserting it is faster.

## OUTPUT FORMAT

- The final SQL, dialect labeled, formatted and commented at each CTE.
- **Assumptions** — grain, keys, filters, and dialect chosen.
- **Correctness notes** — fan-out checks and edge cases (nulls, ties, timezone).
- **Performance** — what you optimized and the measured or plan-based evidence.

Never claim a query is faster without a plan or timing. If the grain is unclear, state your assumption explicitly.
