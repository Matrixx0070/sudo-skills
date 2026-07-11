---
name: pm-sprint-planning
version: 1.0.0
description: Plan a sprint with a clear goal, realistic capacity, P0 commitments, stretch items, and carryover.
author: matrixx0070
tags: [product, sprint, planning, agile, execution]
capabilities: []
---

# Sprint Planning

When to use: a new sprint or cycle is starting and you need a plan the team can actually commit to, one with a single goal, honest capacity, and a clean line between must-ship and nice-to-have.

METHOD
1. Set one sprint goal: a single sentence describing the outcome that makes this sprint a success. If you cannot name one, the scope is unfocused.
2. Compute real capacity: available person-days minus meetings, on-call, PTO, and support load. Do not plan to 100 percent; leave buffer for the unexpected.
3. Pull candidate work: carryover from last sprint first, then goal-aligned items, then dependencies others are blocked on.
4. Classify: P0 (committed, must ship to hit the goal), P1 (planned if capacity holds), and Stretch (only if everything else lands). Ensure P0 fits within buffered capacity.
5. Check readiness: each committed item has clear acceptance criteria, no unresolved blockers, and a rough estimate. Kick back anything not ready.
6. Name risks and the single most likely thing to slip.

OUTPUT FORMAT
- Sprint goal (one sentence).
- Capacity summary: available vs planned, with buffer.
- Committed (P0) list with estimates and acceptance criteria pointers.
- Stretch list.
- Carryover from last sprint with reason.
- Risks, dependencies, and the top slip candidate.
If planned exceeds capacity, say so and propose cuts.
