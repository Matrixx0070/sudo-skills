---
name: bio-problem-selection
version: 1.0.0
description: Select, ideate, and de-risk life-sciences research problems by importance, tractability, and neglectedness.
author: matrixx0070
tags: [research-strategy, ideation, de-risking, prioritization, planning]
capabilities: []
---

When to use: the user is choosing what to work on next, generating project ideas, or unsticking a stalled program and wants a structured judgment rather than gut feel. Use at project inception or at a go/kill decision point.

METHOD
1. Clarify the goal and constraints: scientific aim, timeline, budget, platform, and what "success" concretely produces.
2. Generate a candidate set widely before judging — combine unmet needs, new tools/datasets, and adjacent-field transfers. Aim for breadth first.
3. Score each candidate on Importance (impact if true), Tractability (can we make progress with our tools now), and Neglectedness (crowding/competition). Add a personal-fit/capability multiplier.
4. Identify each candidate's crux: the single assumption that, if false, kills it. Rank by how cheaply that crux can be tested.
5. For a stuck project, diagnose the failure mode — wrong hypothesis, wrong model system, underpowered, or execution/tooling — and propose the smallest experiment that discriminates between them.
6. Recommend: pursue, park, or kill, each with the next de-risking step and a kill criterion.

OUTPUT FORMAT
- Candidate table: Idea | Importance | Tractability | Neglectedness | Fit | Crux.
- Top pick(s) with the cheapest crux-testing experiment and expected information gain.
- For stuck projects: diagnosed failure mode and the discriminating next step.
- Explicit kill criteria per recommendation. Flag assumptions as ASSUMED and any untested claim as UNVERIFIED.
