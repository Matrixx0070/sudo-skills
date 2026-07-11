---
name: smb-close-month
version: 1.0.0
description: Run a small-business month-end close — reconcile books against processors and bank, propose adjustments, and produce a plain-English P&L narrative.
author: matrixx0070
tags: [small-business, month-end, close, reconciliation, p&l]
---

# Close the Month

## When to use
Use this at month-end to close the books cleanly: match recorded revenue and fees against payment processors and bank deposits, catch missing entries, and explain the month's P&L in plain language.

**Not for:** forward forecasting (use smb-cash-flow) or a live status read (use smb-business-pulse). This closes a completed period and never posts to the books without sign-off.

## Method
1. **Set the period.** State the month, the ledger source, and the processors and accounts in scope (bank, Stripe/Square/PayPal, card).
2. **Reconcile deposits.** Match each processor payout and bank deposit to recorded revenue. Surface unmatched items and processor fees not yet booked.
3. **Reconcile expenses.** Tie card and bank charges to recorded bills. Flag duplicates, personal charges, and uncategorized spend.
4. **Book adjustments.** List accruals, deferrals, and corrections, each with amount and reason. Decision point: propose only — do not post without owner or accountant sign-off.
5. **Build the P&L.** Summarize revenue, COGS, gross margin, operating expenses, and net income vs prior month and vs budget.
6. **Write the narrative.** Explain the three biggest drivers of the change in plain English.

Anything that changes the books is a proposal for the owner (or their accountant) to approve.

## Example
June, QuickBooks + Stripe + bank. Stripe payout $8,420 matched revenue but $310 in fees weren't booked — proposed adjustment. Two $49 charges to the same SaaS vendor on the same day flagged as a likely duplicate. Net income $12,100, up $2,300 vs May, driven by higher repeat orders, lower ad spend, and the un-booked Stripe fees now corrected. Awaiting sign-off on 3 adjustments.

## Pitfalls
- **Posting adjustments directly.** Always propose; the owner or accountant approves every book change.
- **Ignoring processor fees.** Gross payouts booked as revenue overstate income — reconcile net of fees.
- **Force-matching to clear the list.** An unmatched item is a signal, not a nuisance; leave it flagged.
- **A P&L with no story.** Numbers without the top-3 drivers leave the owner guessing.

## Output format
```
Period: <month> | Accounts: <list>
Reconciliation (per account):
  matched $__ | unmatched <n> | fees to book $__
Adjustments proposed (pending approval):
  - <item> — $__ — <reason>
P&L: revenue $__ | COGS $__ | gross $__ | opex $__ | net $__
       vs prior <±> | vs budget <±>
Narrative: top 3 drivers
Open items / sign-off gate
```
