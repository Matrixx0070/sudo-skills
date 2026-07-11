---
name: eng-testing-strategy
version: 1.0.0
description: Design a test strategy that matches test types to risk, defines meaningful coverage, and keeps the suite fast and trustworthy.
author: matrixx0070
tags: [testing, test-strategy, coverage, quality, ci]
capabilities: []
---

When to use: when planning how to test a new feature, service, or system — or when an existing suite is slow, flaky, or gives false confidence. Coverage percentage is a means, not the goal; the goal is catching regressions cheaply.

METHOD
1. Map the risk. List what breaking would hurt most: core business logic, money paths, auth, data integrity, external contracts. Test heaviest where risk is highest.
2. Choose the mix along the pyramid. Unit tests for logic and edge cases (fast, many); integration tests for component seams and real dependencies; end-to-end for critical user journeys only (few, high-value). Justify the ratio.
3. Cover the right cases: happy path, boundaries, error/failure paths, and known past bugs (regression tests). Include at least one adversarial/invalid-input case per surface.
4. Decide isolation. What gets mocked vs. run for real? Mock external systems and nondeterminism; avoid mocking your own logic into meaninglessness — mocks must mirror real contracts.
5. Design for trust and speed. Tests must be deterministic (no time/order/network flakiness), independent, and fast enough to run on every commit. Name flaky tests as defects.
6. Define the gate: what must be green before merge, and what runs nightly or pre-release.

OUTPUT FORMAT
- Risk Map (what to protect, ranked)
- Test Mix (unit / integration / e2e with rationale and rough counts)
- Coverage Plan (cases per critical area, including failure paths)
- Mocking & Isolation policy
- CI Gate (blocking vs. non-blocking suites)
- Gaps & Risks accepted
