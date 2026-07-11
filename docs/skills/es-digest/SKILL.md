---
name: es-digest
version: 1.0.0
description: Produce a daily or weekly digest of activity across all connected sources — mentions, action items, and decisions.
author: matrixx0070
tags: [enterprise-search, digest, action-items, decisions, summary]
capabilities: []
---

# Enterprise Search Digest

## When to use
Use this to catch someone up on what happened across their tools over a period — start of day, Monday-morning, or after time away. It scans every connected source for the window and returns what needs attention, not raw activity.

## METHOD
1. **Set the window and owner.** Confirm the period (default: since last digest, else last 24h/7d) and whose perspective — the "you" whose mentions and action items matter.
2. **Sweep sources.** Pull activity in the window from chat, email, storage, and trackers. Scope to items involving the owner or their teams/projects.
3. **Classify each item.** Sort into: direct mentions/requests, action items (something the owner must do), decisions made, and notable FYI activity. Drop pure noise.
4. **Extract action items.** For each, capture the task, who asked, the source link, and any due date. Flag anything overdue or blocking others.
5. **Capture decisions.** Note what was decided, by whom, and the thread — so the owner isn't relitigating settled calls.
6. **Prioritize.** Rank by urgency and whether the owner is the bottleneck. Lead with what breaks if ignored.

## OUTPUT FORMAT
- **Period:** window covered + sources scanned.
- **Needs you now:** top items with a mention or action, each linked, most urgent first.
- **Action items:** checklist — task, from, due, link.
- **Decisions:** bullets — what, who, link.
- **FYI:** brief notable activity worth knowing, not acting on.
- **Quiet:** sources with nothing relevant, named in one line.
