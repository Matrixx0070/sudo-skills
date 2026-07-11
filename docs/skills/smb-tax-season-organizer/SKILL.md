---
name: smb-tax-season-organizer
version: 1.0.0
description: Organize tax-season materials for a quarterly estimate or year-end 1099 and produce an accountant handoff packet.
author: matrixx0070
tags: [tax, organization, quarterly, 1099, accountant, handoff]
capabilities: []
---

# Tax Season Organizer

## When to use
Run this ahead of a quarterly estimated-tax deadline or at year-end 1099 time, when the owner needs their numbers and documents gathered into something an accountant can use.

**Not for:** filing or tax advice (this organizes; the accountant advises and files); sending the packet externally without owner approval; bookkeeping cleanup (use smb-month-end-prep).

## Method
1. **Confirm the mode.** Quarterly estimate or year-end 1099 packet, and the tax period.
2. **Pull income and expense totals.** From connected accounting or bank data, categorized by common tax buckets. Flag gaps and uncategorized items for the owner to resolve.
3. **For quarterly mode.** Summarize period income, deductible expenses, and a rough estimate range, clearly labeled as an estimate to confirm with the accountant.
4. **For 1099 mode.** List contractors paid over the reporting threshold; check for missing W-9 details (name, TIN, address). Decision point: flag incomplete records for collection rather than filing partial data.
5. **Assemble the handoff packet.** Organized summary, supporting-document checklist, and open questions.
6. **Deliver for review.** To the owner first; the owner approves any external send to the accountant.

## Example
Year-end 1099 mode. Contractors over threshold: Jordan Lee $8,400 (W-9 complete), Sam Diaz $2,100 (missing TIN — flag to collect), Riya Patel $640 (under $600? no, over — include). Income/expense summary attached by category. "Needs your attention": Sam's TIN, 3 uncategorized expenses. Packet outline + document checklist assembled; delivered to the owner to review before it goes to the accountant.

## Pitfalls
- Filing or preparing 1099s with a missing TIN instead of flagging it for the owner to collect.
- Presenting the estimate range as a final figure — it's for accountant confirmation only.
- Miscategorizing expenses into wrong tax buckets, which the accountant then has to unwind.
- Sending the packet to the accountant before the owner has reviewed and approved it.

## Output format
- **Mode + period header.**
- **Categorized income/expense summary** (or contractor table for 1099).
- **"Missing or needs your attention"** list.
- **Handoff packet outline** + document checklist.
- **Disclaimer:** figures are for accountant review, not filed advice; owner approves any external send.
