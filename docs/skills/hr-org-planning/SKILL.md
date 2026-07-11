---
name: hr-org-planning
version: 1.0.0
description: Plan headcount, design org structure, and shape team topology against goals and budget — every role tied to an outcome and a cost.
author: matrixx0070
tags: [org-design, headcount, workforce-planning, team-structure, budget, spans-layers]
capabilities: []
---

## When to use

Reach for this when building a hiring plan for a quarter or year, restructuring a team, or pressure-testing whether the org can deliver its roadmap. Tie every proposed role to a business outcome and a fully-loaded cost.

**Not for:** benchmarking a single role's pay (use hr-comp-analysis), reporting current workforce metrics (use hr-people-report), or managing live candidates (use hr-recruiting-pipeline).

## Method

1. **Anchor to goals** — list the objectives the org must deliver and the capabilities each requires. Gaps between required and current capability drive the plan.
2. **Baseline current state** — map existing roles, levels, reporting lines, and spans of control; flag over/under-loaded managers and single points of failure.
3. **Size headcount** — for each capability gap specify role, level, count, quarter of hire, and rationale. Decision point: separate backfills from net-new growth; they compete differently for budget.
4. **Design structure** — propose reporting lines and team boundaries; target healthy spans (~5-8 reports) and clear ownership with minimal cross-team dependency.
5. **Sequence and budget** — order hires by priority and dependency, estimate fully-loaded cost per role, and total against budget. Account for ramp lag before productivity.
6. **Stress-test** — check attrition assumptions, key-person risk, funnel diversity, and what breaks if budget is cut 20%. Decision point: if the plan can't survive the cut scenario, re-sequence to protect the highest-leverage hires.

## Example

Goal: ship a self-serve billing product in H2. Capability gaps: payments backend (none today), billing PM, and support coverage. Plan — 2× Backend Eng (L4/L5, Q3, net-new, ~$260k loaded each), 1× PM (L4, Q3, net-new, ~$230k), 1× Support (L2, Q4, net-new, ~$110k). Total ~$860k loaded. Current billing team span = 9 under one EM → split into two pods. Cut-20% scenario: drop the L4 backer and slip the L2 to next year; PM + one senior eng are the irreducible core.

## Pitfalls

- Proposing roles without a named outcome — headcount that can't be defended when budget tightens.
- Ignoring ramp lag and booking a Q3 hire as fully productive in Q3.
- Spans that balloon past ~8 (manager overload) or shrink below ~3 (too many layers).
- Costing salary only, omitting benefits, tax, equipment, and overhead in the "fully-loaded" figure.

## Output format

```
Goals → capabilities → gaps table
Current-state snapshot: role | level | reports-to | span
Headcount plan: role | level | count | quarter | backfill/new | rationale | loaded cost
Proposed org chart: reporting lines + team boundaries
Sequenced roadmap: priority order + budget total
Risks & trade-offs (incl. -20% cut scenario)
```
