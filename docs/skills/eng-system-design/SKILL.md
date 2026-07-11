---
name: eng-system-design
version: 1.0.0
description: Design a service, API, or data model with clear boundaries, explicit interfaces, and a scaling and failure story.
author: matrixx0070
tags: [system-design, api-design, data-modeling, scaling, architecture]
capabilities: []
---

When to use: whenever you must design a new service, a significant API, or a data model — or evaluate one someone else proposed. Anchor everything in real requirements, not resume-driven complexity.

METHOD
1. Requirements first. List functional needs and non-functional targets: expected QPS, data volume, read/write ratio, latency budget (p50/p99), consistency needs, and availability target. Estimate the numbers; do not hand-wave.
2. Define boundaries. Decide what this component owns and what it delegates. Draw the seams so responsibilities don't leak across them.
3. Design the interface. Specify the API contract — resources/operations, request/response shapes, idempotency, pagination, versioning, and error semantics — before internals.
4. Model the data. Choose the store to fit access patterns, not fashion. Define the schema, keys/indexes, and how it grows. Note where you trade normalization for read speed.
5. Address scale and failure. Identify bottlenecks; plan caching, partitioning, async/queue work, and backpressure. State what happens when each dependency is slow or down.
6. Note trade-offs explicitly and call out the parts you are least sure about.

OUTPUT FORMAT
- Requirements (functional + non-functional with numbers)
- Component & Boundary overview (text diagram)
- API Contract (operations, shapes, errors, versioning)
- Data Model (schema, keys, indexes, growth)
- Scaling & Failure plan (bottlenecks, caching, partitioning, degradation)
- Trade-offs & Open Questions
