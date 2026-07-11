---
name: smb-crm-cleanup
version: 1.0.0
description: Scan the CRM for stale deals, duplicate contacts, and missing fields, then fix only what the owner approves.
author: matrixx0070
tags: [crm, data-quality, operations, cleanup, sales]
capabilities: []
---

## When to use

Use this when the CRM has drifted — old deals lingering in the pipeline, the same contact entered twice, records missing emails or owners. It produces a clean-up plan and executes only the changes the owner signs off on.

## METHOD

1. Scan all contacts and deals. Detect duplicates (matching name, email, or phone), stale deals (no activity past a threshold you state), and records missing key fields like email, owner, stage, or value.
2. Group findings by type and estimate the cleanup impact.
3. For duplicates, propose which record to keep and which to merge, showing what data survives.
4. For stale deals, propose a status change (close-lost, revive, or nurture) with reasoning — never auto-close.
5. Present the full plan. Apply only the approved changes, then confirm what was updated. Deletions and merges always require explicit approval.

## OUTPUT FORMAT

A findings summary with counts per issue type. Then three sections — Duplicates, Stale deals, Missing fields — each listing affected records and the proposed fix. End with "Reply with the items to apply (or 'all')." After execution, return a change log of exactly what was modified.
