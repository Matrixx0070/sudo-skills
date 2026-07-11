---
name: smb-invoice-chase
version: 1.0.0
description: Draft overdue-invoice reminders tuned to each customer's payment history and the right tone, with a cadence plan — every message owner-approved before send.
author: matrixx0070
tags: [small-business, ar, collections, invoicing, customers]
---

# Invoice Chase

## When to use
Use this when receivables are aging and the owner needs reminder messages that recover cash without damaging good relationships — tuned to how late each customer is and how they've paid before.

**Not for:** forecasting when cash will land (use smb-cash-flow) or sending anything automatically. This drafts reminders; the owner approves every one.

## Method
1. **Pull the aging list.** List overdue invoices with customer, amount, invoice date, due date, and days overdue.
2. **Read payment history.** For each customer, note typical days-to-pay, prior late episodes, and lifetime value.
3. **Segment by tone.** Decision point: sort into gentle nudge (first reminder, usually reliable), firm follow-up (repeatedly late or well past due), and escalation candidate (severely overdue or unresponsive).
4. **Draft the message.** Write each reminder with the invoice number, amount, due date, a clear pay link/next step, and tone matched to the segment — warm for good customers, firmer for chronic late payers.
5. **Set the cadence.** Recommend when to send the next touch if unpaid.
6. **Flag escalations.** Identify accounts that may need a call, payment plan, or hold.

Do not send anything directly. Present drafts for the owner to review, edit, and approve — every customer-facing message and any escalation is owner-approved.

## Example
Aging: 1-30 → 4 invoices ($6.2k); 31-60 → 2 ($3.1k); 60+ → 1 ($9k). Riverside Co. (INV-1043, $1,200, 12 days over) usually pays on time → gentle nudge: "Just a quick heads-up, INV-1043 slipped past due — pay link here, no worries if it's already on the way." Delta LLC ($9k, 63 days, third late episode) → firm + flag for a call and a possible payment plan.

## Pitfalls
- **Same tone for everyone.** Dunning a reliable customer over a 5-day slip damages a good relationship.
- **Missing the pay link/next step.** A reminder with no clear way to pay just adds friction.
- **Auto-sending.** Every message and any escalation waits for owner approval.
- **Ignoring history.** A chronic late payer needs a firmer path (call, plan, hold), not a fourth polite nudge.

## Output format
```
Aging summary: 1-30 <n>/$__ | 31-60 <n>/$__ | 60+ <n>/$__
Per invoice:
| Customer | Amount | Days over | Segment | History note |
Draft messages (one per invoice, ready to send on approval):
  <customer>: "<draft>"
Cadence plan: next touch timing if unpaid
Escalations flagged for owner: <account — why>
```
