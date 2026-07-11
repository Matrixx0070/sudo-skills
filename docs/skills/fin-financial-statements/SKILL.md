---
name: fin-financial-statements
version: 1.0.0
description: Build and tie out the three primary statements (P&L, balance sheet, cash flow) with articulation checks and variance commentary.
author: matrixx0070
tags: [finance, financial-statements, reporting, gaap, ifrs, variance, articulation]
---

# Financial Statements

## When to use
Use this to prepare or review the three primary financial statements for a period, confirm they articulate correctly, or produce a management reporting package with variance commentary.

**Not for:** decomposing a single variance into price/volume/mix drivers (fin-variance-analysis), building a forward cash *forecast* (fin-cash-flow — this uses the historical indirect-method statement), or reconciling underlying accounts (fin-reconciliation).

## Method
1. **Set the reporting basis.** State entity, period, currency, basis (GAAP / IFRS / management), and comparison columns (prior period, prior year, budget).
2. **Build the income statement.** Revenue, COGS, gross profit, operating expenses by category, operating income, other income/expense, taxes, net income; compute margins.
3. **Build the balance sheet.** Assets (current, non-current), liabilities (current, non-current), equity. Decision point: if assets ≠ liabilities + equity, stop — do not proceed to cash flow until it balances.
4. **Build the cash flow statement.** Operating (indirect: net income + non-cash + working-capital changes), investing, financing; sum to net change in cash.
5. **Tie the statements together.** Net income flows to retained earnings; ending cash equals the balance-sheet cash line; PP&E and debt roll forward.
6. **Run variance analysis.** For each material line compute change vs comparison in $ and %; flag anything past the materiality threshold.
7. **Write commentary.** Explain each flagged variance with its driver. Decision point: if a variance is material but you cannot name a driver, treat it as a possible error and re-check the ledger, not a story to invent.

## Example
Q2, GAAP, vs prior quarter. P&L: revenue $4.2M, net income $610k. Balance sheet balances at $18.4M = $11.0M + $7.4M. Cash flow starts from $610k NI, adds $180k depreciation, subtracts $240k AR growth, nets to +$390k operating; ending cash $2.1M — matches the balance-sheet cash line (articulation pass). Variance: opex +$150k (+9%) vs Q1, flagged; driver = two Q2 sales hires. Retained earnings roll: opening $6.79M + $610k = $7.4M — ties.

## Pitfalls
- **Force-balancing with a plug.** A "rounding" line hiding a real $30k gap masks a booking error — find it.
- **Ending cash that doesn't match the balance sheet.** If the cash-flow ending cash ≠ balance-sheet cash, the statements do not articulate; the package is wrong.
- **Copying prior-period commentary.** Stale narratives claim drivers that no longer apply — re-derive from this period's numbers.
- **Flagging every line.** Below-materiality noise buries the two variances leadership actually needs.

## Output format
```
Entity: <...> | Period: <...> | Basis: <...> | Compare: <...>
Income statement: | line | current | compare | $var | %var | margin |
Balance sheet: | ... |  →  A = L + E: <shown> [pass/fail]
Cash flow: operating / investing / financing → net change | ending cash
Articulation: NI→equity [pass/fail] | ending cash = BS cash [pass/fail]
Variances (material): | line | $var | %var | driver |
Commentary: <...>
```
