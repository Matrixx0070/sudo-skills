---
name: smb-close-month
version: 1.0.0
description: Run a small-business month-end close, reconciling books against processors and producing a P&L narrative.
author: matrixx0070
tags: [small-business, month-end, close, reconciliation, p&l]
---

# Close the Month

## When to use
Use this at month-end to close the books cleanly: match recorded revenue and fees against payment processors and bank deposits, catch missing entries, and explain the month's P&L in plain language.

## METHOD
1. **Set the period.** State the month, the ledger source, and the processors and accounts in scope (bank, Stripe/Square/PayPal, card).
2. **Reconcile deposits.** Match each processor payout and bank deposit to recorded revenue; surface unmatched items and processor fees not yet booked.
3. **Reconcile expenses.** Tie card and bank charges to recorded bills; flag duplicates, personal charges, and uncategorized spend.
4. **Book adjustments.** List accruals, deferrals, and corrections needed, each with amount and reason — propose, do not post without owner sign-off.
5. **Build the P&L.** Summarize revenue, COGS, gross margin, operating expenses, and net income vs prior month and vs budget.
6. **Write the narrative.** Explain the three biggest drivers of the change in plain English.

Anything that changes the books is a proposal for the owner (or their accountant) to approve.

## OUTPUT FORMAT
- **Period / accounts in scope.**
- **Reconciliation summary:** matched, unmatched, fees to book, per account.
- **Adjustments proposed:** item, amount, reason (pending approval).
- **P&L:** revenue, COGS, gross margin, opex, net income vs prior/budget.
- **Narrative:** top 3 drivers.
- **Open items / sign-off gate.**
