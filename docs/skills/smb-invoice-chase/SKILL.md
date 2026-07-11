---
name: smb-invoice-chase
version: 1.0.0
description: Draft overdue-invoice reminders matched to each customer's payment history and the right tone.
author: matrixx0070
tags: [small-business, ar, collections, invoicing, customers]
---

# Invoice Chase

## When to use
Use this when receivables are aging and the owner needs reminder messages that recover cash without damaging good relationships — tuned to how late each customer is and how they've paid before.

## METHOD
1. **Pull the aging list.** List overdue invoices with customer, amount, invoice date, due date, and days overdue.
2. **Read payment history.** For each customer, note typical days-to-pay, prior late episodes, and lifetime value.
3. **Segment by tone.** Sort into gentle nudge (first reminder, usually reliable), firm follow-up (repeatedly late or well past due), and escalation candidate (severely overdue or unresponsive).
4. **Draft the message.** Write each reminder with the invoice number, amount, due date, a clear pay link/next step, and tone matched to the segment — warm for good customers, firmer for chronic late payers.
5. **Set the cadence.** Recommend when to send the next touch if unpaid.
6. **Flag escalations.** Identify accounts that may need a call, payment plan, or hold.

Do not send anything directly. Present drafts for the owner to review, edit, and approve — every customer-facing message and any escalation is owner-approved.

## OUTPUT FORMAT
- **Aging summary:** count and total by bucket (1–30, 31–60, 60+).
- **Per-invoice table:** customer, amount, days overdue, segment, history note.
- **Draft messages:** one per invoice/customer, ready to send on approval.
- **Cadence plan.**
- **Escalations flagged for owner.**
