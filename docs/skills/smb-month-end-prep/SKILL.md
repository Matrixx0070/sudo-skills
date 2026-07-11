---
name: smb-month-end-prep
version: 1.0.0
description: Walk the owner through month-end close — reconcile books against processor payouts, flag discrepancies, and export a review packet.
author: matrixx0070
tags: [finance, bookkeeping, reconciliation, month-end, accounting, close]
capabilities: []
---

# Month-End Prep

## When to use
Use this at month-end to close the books with confidence. It guides you through reconciling recorded revenue against what payment processors actually deposited, flags mismatches, and assembles a packet for the owner or accountant.

**Not for:** tax estimates or the accountant handoff (use smb-tax-season-organizer); forward cash forecasting (use smb-month-heads-up); making unapproved edits to financial records — every adjustment needs owner sign-off.

## Method
1. **Gather sources.** The month's bookkeeping records plus payout reports from each processor (card, online, marketplace).
2. **Reconcile.** Match recorded income against processor deposits by date and amount. Surface unmatched transactions, unbooked fees, refunds, and chargebacks.
3. **Rank discrepancies.** For each mismatch: likely cause and dollar amount, sorted largest first. Decision point: never silently adjust — a large unexplained gap is a stop-and-ask, not an auto-fix.
4. **Check common gaps.** Uncategorized expenses, missing receipts, duplicate entries, outstanding invoices.
5. **Propose corrections.** Present findings and suggested adjustments. Apply only owner-approved changes.
6. **Export the packet.** Reconciliation summary, flagged items, and a corrections log. State where it was saved. Books are the owner's to sign off.

## Example
March recorded card revenue $24,000; Stripe deposited $22,910. Reconcile: gross $24,000 minus $690 processor fees (not booked) minus two refunds ($400) = $22,910 — matches, so the "gap" is just unbooked fees. Flag: fees $690, action "book as expense." Separately, a $180 charge appears twice — duplicate entry, remove one. Gaps: 3 expenses uncategorized, 1 receipt missing. Packet exported; owner approves the two adjustments before they're applied.

## Pitfalls
- Treating processor fees or refunds as "missing money" instead of expected deductions from gross.
- Silently adjusting entries to force a match — that hides the real error and breaks the audit trail.
- Reconciling only the biggest account and skipping the marketplace payouts where small fees pile up.
- Exporting the packet before the owner has approved corrections, so the numbers ship half-baked.

## Output format
- **Reconciliation summary:** recorded vs deposited | net difference.
- **Discrepancy list (ranked):** item | amount | likely cause | suggested action.
- **Gaps checklist:** uncategorized | missing receipts | duplicates | outstanding invoices.
- **"Approve the adjustments to apply"** gate.
- **Exported packet:** reconciliation + flagged items + corrections log, with save location.
