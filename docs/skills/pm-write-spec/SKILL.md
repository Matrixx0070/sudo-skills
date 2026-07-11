---
name: pm-write-spec
version: 1.0.0
description: Write a PRD or feature spec with clear goals, non-goals, metrics, and acceptance criteria.
author: matrixx0070
tags: [product, spec, prd, requirements, planning]
capabilities: []
---

# Write Spec

When to use: a feature is ready to move from idea to build and you need a document that aligns design, engineering, and stakeholders on what you are building, why, and how you will know it worked.

METHOD
1. State the problem and context: who has this problem, evidence it matters, and why now. Ground it in research or data, not assertion.
2. Define goals and non-goals explicitly. Non-goals prevent scope creep and are as important as goals; name what this deliberately does not do.
3. Specify success metrics: the primary metric that proves the feature worked, plus guardrail metrics that must not regress. Set target and measurement window.
4. Describe the solution: user stories, key flows, and states (empty, error, edge). Enough for engineering to estimate without dictating implementation.
5. Write acceptance criteria as testable statements ("Given/When/Then" or clear pass conditions). These are the definition of done.
6. Cover the rest: dependencies, risks, open questions, rollout and instrumentation plan.

OUTPUT FORMAT
- Summary and problem statement (with evidence).
- Goals / Non-goals.
- Success metrics (primary + guardrails, with targets).
- Solution: user stories, key flows, states.
- Acceptance criteria (testable).
- Dependencies, risks, open questions.
- Rollout and measurement plan.
Keep open questions visible rather than papering over unknowns.
