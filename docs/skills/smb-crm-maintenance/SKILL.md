---
name: smb-crm-maintenance
version: 1.0.0
description: Keep the CRM current from email and calendar context — create and update contacts and deals, log notes, and flag stale records.
author: matrixx0070
tags: [crm, automation, sales, productivity, operations]
capabilities: []
---

## When to use

Use this as a routine (daily or weekly) to keep the CRM honest without manual data entry. It reads recent email and calendar activity and proposes the updates that keep records accurate.

## METHOD

1. Review recent email threads and calendar events since the last run.
2. Detect new people worth adding as contacts, and existing contacts or deals that changed (meetings held, replies received, stage movement).
3. Draft the updates: new contacts, deal field changes, and short activity notes summarizing each interaction — grounded only in what the source shows.
4. Flag deals that have gone quiet and may need owner attention.
5. Present all proposed changes for approval before writing to the CRM. Do not send any email or contact a customer; this skill only maintains records.

## OUTPUT FORMAT

A grouped preview: New contacts, Deal updates, Notes to log, and Stale flags — each with the source that justifies it. End with "Approve these updates and I'll sync them to the CRM." After the owner confirms, apply them and return a concise confirmation of what synced.
