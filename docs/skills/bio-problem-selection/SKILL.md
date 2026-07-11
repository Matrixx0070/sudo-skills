---
name: bio-problem-selection
version: 1.0.0
description: Select, ideate, and de-risk life-sciences research problems by importance, tractability, and neglectedness, ending in a pursue/park/kill call with kill criteria.
author: matrixx0070
tags: [research-strategy, ideation, de-risking, prioritization, planning, go-kill]
capabilities: []
---

## When to use

Use this when the user is choosing what to work on next, generating project ideas, or unsticking a stalled program and wants structured judgment rather than gut feel. Apply at project inception or at a go/kill decision point.

**Not for:** ranking already-chosen drug targets (use bio-target-prioritization), designing the experiment once a project is picked (use bio-experiment-design), or literature synthesis (use bio-literature-review).

## Method

1. Clarify the goal and constraints: scientific aim, timeline, budget, platform, and what "success" concretely produces.
2. Generate candidates widely before judging — combine unmet needs, new tools/datasets, and adjacent-field transfers. Breadth first; do not filter while ideating.
3. Score each on Importance (impact if true), Tractability (progress with current tools), Neglectedness (crowding). Add a personal-fit/capability multiplier.
4. Identify each candidate's crux: the single assumption that, if false, kills it. **Decision:** rank by how cheaply that crux can be tested, not by raw excitement — a cheap crux beats a marginally more important but untestable idea.
5. **Decision (stuck project):** diagnose the failure mode — wrong hypothesis, wrong model system, underpowered, or execution/tooling — and propose the smallest experiment that discriminates between them.
6. Recommend pursue, park, or kill, each with a next de-risking step and an explicit kill criterion.

## Example

A lab weighs three ideas. Idea 1 (high importance, but crux = "the biomarker is stable in serum," testable for $200 in a week) beats Idea 2 (higher importance, crux = a two-year cohort). Idea 3 is a stuck project: the phenotype won't replicate. Diagnosis narrows to model system vs underpowered; the discriminating step is a single high-n replicate in a second cell line before any mechanism work. Recommendation: pursue 1, park 2, run the discriminator on 3 with kill criterion "no effect at n=20."

## Pitfalls

- Scoring importance while ignoring tractability — chasing the most important problem you cannot make progress on.
- Judging ideas during brainstorming, which kills the weird transfer ideas that become the best bets.
- Naming no crux, so the project drifts without a cheap early test.
- Recommending "pursue" with no kill criterion — projects then run on sunk cost forever.

## Output format

```
# Problem Selection — <goal>
Constraints: aim / timeline / budget / platform / success =

## Candidate table
| Idea | Importance | Tractability | Neglectedness | Fit | Crux |

## Top pick(s)
- <idea> — cheapest crux test: <experiment> | expected info gain: <one line>

## Stuck project (if any)
diagnosed failure mode: <...>  discriminating next step: <...>

## Recommendations
<idea>: pursue/park/kill — next de-risk step — KILL IF <criterion>
```
Flag assumptions as ASSUMED and any untested claim as UNVERIFIED.
