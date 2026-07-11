---
name: eng-tech-debt
version: 1.0.0
description: Identify, categorize, and prioritize technical debt into a defensible backlog that ties remediation to business and engineering impact.
author: matrixx0070
tags: [tech-debt, refactoring, prioritization, backlog, maintainability]
capabilities: []
---

When to use: when planning maintenance work, justifying refactor time to stakeholders, or auditing a codebase or service for accumulated risk. The aim is a ranked, honest list — not a wish list.

METHOD
1. Inventory the debt. Gather from code smells, TODO/FIXME markers, incident postmortems, slow tests, flaky deploys, and team pain points. Name each item concretely: what is wrong and where.
2. Categorize each item: Design (bad abstractions), Code (duplication, complexity), Test (gaps, flakiness), Infra/Ops (manual toil, fragile deploys), Dependency (outdated/unsupported), or Documentation.
3. Assess impact and cost per item. Impact = how often it hurts and how badly (dev velocity drag, incident risk, security exposure, onboarding friction). Cost = effort to fix. Estimate both, even roughly.
4. Score and rank. Prioritize high-impact, low-cost items first; flag high-impact/high-cost items as projects needing planning. Explicitly park low-impact debt — recording it counts.
5. Distinguish deliberate debt (a conscious shortcut to revisit) from accidental debt (accrued through neglect). Deliberate debt needs a payoff trigger.
6. Recommend a next-quarter slice: a small set of items with the best impact-to-effort ratio.

OUTPUT FORMAT
- Debt Register (table: item | category | location | impact | est. cost | priority)
- Top Priorities (ranked, with one-line justification each)
- Quick Wins (high impact, low effort)
- Deferred / Accept (with reason)
- Recommended next-cycle slice
