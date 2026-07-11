---
name: fin-journal-entry
version: 1.0.0
description: Draft balanced, review-ready journal entries (accruals, depreciation, rev-rec, reclasses) with calculation, support, and reversal.
author: matrixx0070
tags: [finance, accounting, journal-entry, accruals, depreciation, revenue-recognition]
---

# Journal Entry

## When to use
Use this to draft a journal entry that passes review the first time — accruals, prepaid amortization, depreciation, revenue recognition, or reclasses — with the debits, credits, calculation, and support an approver needs.

**Not for:** correcting entries that fall out of a reconciliation (fin-reconciliation proposes those), or sequencing when entries post during close (fin-close-management). This is the *content* of one entry.

## Method
1. **Identify transaction and type.** State what happened, the entry type (accrual, deferral, depreciation, rev-rec, reclass), and the period it belongs to.
2. **Apply the treatment.** Cite the driver: matching principle for accruals, straight-line (or chosen method) for depreciation, ASC 606 five-step for revenue.
3. **Compute the amount.** Show the calculation step by step (e.g., (cost − salvage) / useful life; contract value × % complete or ratable portion).
4. **Build the entry.** List each account with number, debit or credit, and amount. Decision point: debits must equal credits — if they don't, do not post; find the missing leg.
5. **Attach support.** Reference the invoice, contract, schedule, or accrual worksheet backing each line.
6. **Plan the reversal.** Decision point: if it is an accrual or deferral, set the reversal date and mechanism now — an unreversed accrual double-counts next period.
7. **Self-check.** Confirm it balances, hits the correct period, and uses valid active accounts.

## Example
Accrue December consulting: work done, invoice not received, belongs to December (matching). Estimate from the SOW: $12,000/month, 80% complete = $9,600.
```
Dr 6200 Consulting expense   9,600
   Cr 2100 Accrued liabilities   9,600
```
Debits = credits = $9,600. Support: SOW #C-4471, PM completion note. Reversal: Jan 1, auto-reverse (invoice will post against 2100). Reviewer note: estimate; true-up on receipt.

## Pitfalls
- **Entry that doesn't balance.** A one-sided or mistyped amount is the most common review kick-back — total both columns before submitting.
- **Wrong period.** Booking December work in January defeats the accrual's purpose and distorts both months.
- **Missing reversal on an accrual.** It silently double-counts when the actual invoice posts.
- **No support reference.** "Accrual, $9,600" with no SOW or worksheet is unauditable — the approver cannot verify the number.

## Output format
```
Description: <...> | Type: <accrual/...> | Period: <...> | Posting date: <...>
Rationale: <principle / ASC standard>
Calculation: <shown step by step>
Entry:
  | account | acct # | debit | credit |
  Totals:            | <sum> | <sum> |  → equal? [yes/no]
Support: <invoice / contract / schedule refs>
Reversal: <date + mechanism, or N/A>
Reviewer notes: <...>
```
