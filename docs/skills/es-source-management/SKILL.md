---
name: es-source-management
version: 1.0.0
description: Manage connected search sources — detect what's connected, guide connecting new ones, and set priority order.
author: matrixx0070
tags: [enterprise-search, connectors, sources, configuration, onboarding]
capabilities: []
---

# Enterprise Search Source Management

## When to use
Use this when search coverage feels incomplete, before first real use, or when someone asks "what can you search?" or "why didn't you find X?" It audits connected sources, guides connecting missing ones, and orders sources so the highest-signal ones lead.

## METHOD
1. **Inventory.** List every source category — chat, email, storage, trackers — and mark each connected, available-but-unconnected, or unsupported.
2. **Detect gaps.** For an unconnected source that clearly holds relevant content, call it out explicitly rather than silently searching around it. A missing source is the top cause of a "not found."
3. **Guide connection.** For each source the user wants, give the concrete path (which connector, which scopes/permissions, where in settings). Never ask for tokens or codes in-session — point to the authorization flow.
4. **Verify authorization.** Confirm each connected source actually returns results with a trivial probe; flag any that authenticate but return empty.
5. **Set priority order.** Rank sources by signal density and trust for this user's work, so ranked search and digests weight them correctly.
6. **Note scope and limits.** Record what each source does and does not cover (date range, folders, private vs. shared) so results are honestly bounded.

## OUTPUT FORMAT
- **Connected:** sources live now, with priority rank.
- **Available to connect:** each with a one-line "connect via" instruction.
- **Unsupported / blocked:** sources that can't be searched and why.
- **Recommended priority:** ordered list with rationale.
- **Coverage caveats:** known blind spots the user should expect.
