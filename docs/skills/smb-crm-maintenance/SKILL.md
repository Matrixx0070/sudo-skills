---
name: smb-crm-maintenance
version: 1.0.0
description: Keep the CRM current from email and calendar context — propose new contacts, deal updates, activity notes, and stale flags for owner approval before writing.
author: matrixx0070
tags: [crm, automation, sales, productivity, operations]
capabilities: []
---

# CRM Maintenance

## When to use
Use this as a routine (daily or weekly) to keep the CRM honest without manual data entry. It reads recent email and calendar activity and proposes the updates that keep records accurate.

**Not for:** a one-time deep clean of duplicates and stale deals (use smb-crm-cleanup) or contacting customers. This maintains records only — it never sends anything.

## Method
1. Review recent email threads and calendar events since the last run.
2. Detect new people worth adding as contacts, and existing contacts or deals that changed (meetings held, replies received, stage movement).
3. Draft the updates: new contacts, deal field changes, and short activity notes. Decision point: ground every note only in what the source shows — no inferred intent ("seems eager to buy") unless the message says so.
4. Flag deals that have gone quiet and may need owner attention.
5. Present all proposed changes for approval before writing to the CRM. Do not send any email or contact a customer; this skill only maintains records.

## Example
Since last run: a new sender, Priya Nair (Acme Co.), emailed a pricing question → propose new contact. The "Westside remodel" deal had a site visit on the calendar Tuesday → propose stage move Qualified → Proposal, plus a note: "Site visit held Tue; discussed timeline." The "Harbor account" deal has had no activity in 21 days → flag as stale. Awaiting approval before syncing.

## Pitfalls
- **Inferring beyond the source.** Log what happened, not what you assume the customer feels.
- **Creating duplicate contacts.** Check for an existing record by email before proposing a new one.
- **Silent stage jumps.** Propose stage changes with the evidence, don't just move them.
- **Writing before approval.** Every CRM write waits for the owner's yes.

## Output format
```
New contacts:
  - <name>, <company> — source: <email/event>
Deal updates:
  - <deal> — <field change> — source: <...>
Notes to log:
  - <deal/contact> — "<note>" — source: <...>
Stale flags:
  - <deal> — quiet <n> days
"Approve these updates and I'll sync them to the CRM."
[after approval] Synced: <concise confirmation>
```
