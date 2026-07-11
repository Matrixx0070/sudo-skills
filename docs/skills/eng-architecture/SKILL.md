---
name: eng-architecture
version: 1.0.0
description: Create or evaluate an Architecture Decision Record (ADR) that captures context, options, trade-offs, and a defensible decision.
author: matrixx0070
tags: [architecture, adr, decisions, trade-offs, design]
capabilities: []
---

When to use: reach for this whenever a choice is expensive to reverse — a datastore, a framework, a service boundary, an auth model, a build vs. buy call. If someone will ask "why did we do it this way?" in six months, write the ADR now.

METHOD
1. State the decision in one sentence, then the forces driving it: constraints, deadlines, team skills, existing systems, non-functional requirements (latency, cost, compliance).
2. Enumerate at least three real options. "Do nothing" and the obvious incumbent both count. Reject strawmen.
3. For each option, list concrete pros, cons, risks, and a rough cost (effort, dollars, operational burden). Quantify where you can.
4. Score options against the forces from step 1. Make the weighting explicit so the reasoning survives disagreement.
5. Pick one. Write down what you are consciously giving up and what would make you reverse the decision.
6. Capture consequences: follow-up work, migration path, new operational duties, and a review date.

When evaluating an existing ADR, check that options are non-trivial, trade-offs are honest, and the decision actually follows from the stated forces.

OUTPUT FORMAT
- Title & Status (Proposed / Accepted / Superseded)
- Context (forces and constraints)
- Options Considered (table: option | pros | cons | cost)
- Decision (chosen option + rationale)
- Trade-offs Accepted (explicit)
- Consequences & Follow-ups
- Revisit Trigger (what invalidates this)
