---
name: hr-interview-prep
version: 1.0.0
description: Build a structured, bias-resistant interview loop — competencies mapped to interviewers, calibrated questions, and 1/3/5 scorecards.
author: matrixx0070
tags: [interviewing, hiring, competencies, scorecards, structured-interview, calibration]
capabilities: []
---

## When to use

Reach for this when preparing an interview loop, standardizing questions across panelists, or designing a scorecard so decisions are evidence-based and comparable across candidates.

**Not for:** tracking candidates through stages (use hr-recruiting-pipeline), writing the offer (use hr-draft-offer), or after-hire ramp planning (use hr-onboarding).

## Method

1. **Derive competencies from the job** — pick 4-6 must-haves (technical + behavioral) tied to real responsibilities, not generic traits.
2. **Distribute across the loop** — assign each interviewer 1-2 competencies for complete, non-redundant coverage; name each interview type (screen, technical, behavioral, values, hiring-manager). Decision point: if a must-have competency has no owner, add a slot or reassign before finalizing.
3. **Write questions** — for each competency give a behavioral prompt (STAR "Tell me about a time…"), a situational prompt, and 2-3 probing follow-ups that reach depth.
4. **Define the rubric** — describe what a 1 (below), 3 (meets), and 5 (exceeds) answer looks like, with concrete observable signals for each.
5. **Build the scorecard** — competency → rating → evidence-notes field, ending in a recommendation (Strong Yes / Yes / No / Strong No) with required written justification.
6. **Add guardrails** — an interviewer briefing, a list of legally off-limits topics, and a debrief that shares evidence before scores. Decision point: run debrief evidence-first to reduce anchoring; if scores were shared early, re-poll after evidence.

## Example

Role: Customer Success Manager. Competency "de-escalation." Behavioral: "Tell me about a time a key account threatened to churn — what did you do?" Follow-ups: What was the root cause? What did you commit to and did you deliver? How did the relationship end up? Rubric — 1: blames the customer, no ownership; 3: describes a structured save with a clear plan; 5: shows the save plus a systemic fix that prevented recurrence. Owner: the hiring-manager interview. Scorecard captures quote-level evidence, then a rating and a written recommendation.

## Pitfalls

- Vague competencies ("culture fit", "smart") that invite bias and can't be scored consistently.
- Every interviewer asking the same questions — redundant coverage, blind spots elsewhere.
- Rubrics with adjectives ("strong", "weak") instead of observable behaviors.
- Scores collected before evidence in the debrief, anchoring the panel to the loudest voice.

## Output format

```
Role + competency map:
  competency | interviewer | interview type
Question bank (per competency):
  behavioral | situational | follow-ups
Scoring rubric (per competency): 1 anchor / 3 anchor / 5 anchor
Scorecard template: competency → rating → evidence → recommendation (SY/Y/N/SN) + justification
Debrief agenda: evidence-first order, roles, bias reminders
```
