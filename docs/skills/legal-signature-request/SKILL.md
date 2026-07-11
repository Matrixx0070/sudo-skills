---
name: legal-signature-request
version: 1.0.0
description: Prepare and route a finalized document for e-signature with a pre-send checklist, correct signer order, and post-signature follow-through.
author: matrixx0070
tags: [legal, e-signature, workflow, routing, execution]
capabilities: []
---

## When to use
Use this once a document is final and ready to execute — a contract, NDA, SOW, offer letter, or consent form — to send it for e-signature cleanly on the first try. It prevents the common failures: wrong version, missing signer, bad signing order, unfilled fields.

**Not for:** documents still under negotiation or review (finalize first via `legal-review-contract`), deciding whether terms are acceptable, or anything where required approvals aren't yet recorded. Do not send until it is truly final.

## Method
1. **Confirm it is truly final.** Version matches the approved redline; all internal approvals recorded; no open comments or tracked changes. *Decision point:* any open comment or missing approval → stop, do not send.
2. **Run the pre-send checklist.** Correct legal entity names, dates, dollar amounts, exhibits/attachments included, all placeholders resolved.
3. **Identify every signer and role.** Full name, title, entity, email, and authority to sign. *Decision point:* if a signer lacks signing authority, correct the routing before sending.
4. **Set signing order.** Sequential vs. parallel; note witness or notary requirements. Add CC recipients who need the executed copy.
5. **Place fields.** Signature, date, initials, and any required data fields per signer.
6. **Configure reminders and expiry.** Reminder cadence and a completion deadline.
7. **Plan post-signature steps.** Where the executed copy is stored, who is notified, and any calendared obligations (renewal, milestone).

## Example
Document: mutual NDA v4 (final, matches approved redline). Checklist: entity names correct, effective date blank → set to send date, no placeholders, no tracked changes → pass. Signers: their GC (signs first), our VP Legal (signs second). CC: deal owner. Order: sequential. Reminders: every 3 days, expiry 14 days. Post-signature: store in contract repository under vendor folder, notify deal owner, no calendared obligation (perpetual NDA).

## Pitfalls
- **Sending a near-final draft.** One unresolved tracked change means re-signing the whole thing.
- **Wrong signer authority.** A signature from someone without authority can void the agreement.
- **Parallel order when sequence matters.** Counterparty-then-internal routing gets scrambled.
- **No storage/notification plan.** The executed copy lands in an inbox and is never filed or calendared.

## Output format
```
Document / version / parties:
Pre-send checklist:
  | Item | Pass/Fail |
Signer list:
  | Name | Title | Entity | Email | Order |
CC / storage location / notifications:
Reminders & expiry:
Post-execution actions:
  | Action | Owner | Date |
```
