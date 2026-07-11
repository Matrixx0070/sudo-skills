---
name: smb-crm-cleanup
version: 1.0.0
description: Scan the CRM for stale deals, duplicate contacts, and missing fields, propose fixes, and apply only what the owner approves.
author: matrixx0070
tags: [crm, data-quality, operations, cleanup, sales]
capabilities: []
---

# CRM Cleanup

## When to use
Use this when the CRM has drifted — old deals lingering in the pipeline, the same contact entered twice, records missing emails or owners. It produces a cleanup plan and executes only the changes the owner signs off on.

**Not for:** routine ongoing upkeep from email/calendar (use smb-crm-maintenance) or building a daily call list (use smb-call-list). This is a periodic deep clean, not a daily sync.

## Method
1. Scan all contacts and deals. Detect duplicates (matching name, email, or phone), stale deals (no activity past a threshold you state), and records missing key fields (email, owner, stage, value).
2. Group findings by type and estimate cleanup impact (how many records, what it unblocks).
3. For duplicates, propose which record to keep and which to merge. Decision point: keep the record with the most complete history and recent activity; show exactly what data survives.
4. For stale deals, propose a status change (close-lost, revive, or nurture) with reasoning — never auto-close.
5. Present the full plan. Apply only approved changes, then confirm what was updated. Deletions and merges always require explicit approval.

## Example
Findings: 6 duplicate contacts, 11 stale deals (>60 days no activity), 9 records missing an owner. Duplicate example: "J. Smith" (2 records) → keep the one with 4 logged calls and the recent email, merge in the other's phone number. Stale example: $3k deal, last touch 74 days ago → propose close-lost. Nothing changes until the owner replies with which items to apply.

## Pitfalls
- **Auto-merging on a name match.** Two different people share names; require email or phone corroboration before merging.
- **Auto-closing stale deals.** A quiet deal may be mid-negotiation offline — propose, don't close.
- **Losing data in a merge.** Always show which fields survive so nothing important is silently dropped.
- **Bulk-applying without a change log.** After execution, return exactly what changed so it's auditable.

## Output format
```
Findings: <n> duplicates | <n> stale | <n> missing fields
Duplicates:
  - keep <record A> / merge <record B> — survives: <fields>
Stale deals:
  - <deal> — last activity <date> — propose <close-lost/revive/nurture>
Missing fields:
  - <record> — missing <field>
"Reply with the items to apply (or 'all')."
[after approval] Change log: <exactly what was modified>
```
