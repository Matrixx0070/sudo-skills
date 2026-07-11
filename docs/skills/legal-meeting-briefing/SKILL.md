---
name: legal-meeting-briefing
version: 1.0.0
description: Prepare an attendee for a legally-relevant meeting and capture the decisions, commitments, and action items that come out of it.
author: matrixx0070
tags: [legal, meeting, briefing, action-items, preparation, negotiation]
capabilities: []
---

## When to use
Use this before a meeting with legal stakes — a negotiation, a regulator call, a board matter, a dispute discussion, a vendor sign-off — and again after it to capture what was decided. The attendee walks in prepared and walks out with tracked commitments.

**Not for:** routine internal meetings with no legal exposure, drafting the agreement itself (use `legal-review-contract`), or giving the attendee legal advice on positions (attorney-set red lines only).

## Method
1. **State purpose and desired outcome.** What decision or agreement should exist when the meeting ends.
2. **Profile the parties.** Who attends, their interests, likely positions. Note privilege or confidentiality boundaries.
3. **Assemble the record.** Relevant contracts, prior correspondence, open issues, and each item's status. Flag anything still under attorney review.
4. **Prepare positions.** For each contested point: our position, acceptable range, fallback, walk-away. Mark red lines. *Decision point:* red lines and settlement authority are set by counsel, not the attendee — confirm them in advance.
5. **List questions to ask** and commitments to avoid making without counsel.
6. **Capture outcomes.** During/after, record decisions, who committed to what, deadlines, and items deferred to counsel.
7. **Log action items** with owner, due date, and status.

## Example
Meeting: renewal negotiation with a key vendor. Desired outcome: agreed price and a mutual liability cap. Parties: vendor CSM (wants multi-year lock-in) + our procurement. Positions — price: target 5% cut, range 0-8%, walk-away above list; liability: red line = must be mutual and ≥ 12 months fees (counsel-set). Question to ask: "Will you accept a 30-day termination-for-convenience?" Defer: any indemnity change → counsel. Post-meeting decision: 4% cut agreed, cap deferred to legal. Action item: send redline of cap clause (owner: procurement, by Wed).

## Pitfalls
- **Walking in without a walk-away.** Without a defined floor, the attendee concedes under pressure.
- **Committing on the spot to counsel-only terms.** Indemnity, liability, and IP get deferred, not agreed live.
- **No post-meeting capture.** Verbal commitments evaporate; write them down while fresh.
- **Action items with no owner or date.** Follow-through dies in the gap.

## Output format
```
Meeting / purpose / desired outcome:
Attendees & interests:
Key documents & status:
Positions:
  | Point | Our stance | Range | Red line |
Questions to ask:
Commitments to defer to counsel:
Decisions made (post-meeting):
Action items:
  | Item | Owner | Due | Status |
```
