---
name: hr-recruiting-pipeline
version: 1.0.0
description: Track a recruiting funnel across stages with conversion metrics, bottleneck diagnosis, and a next action for every candidate.
author: matrixx0070
tags: [recruiting, pipeline, ats, funnel-metrics, talent-acquisition, time-to-fill]
capabilities: []
---

## When to use

Reach for this when managing candidates through a hiring funnel, running a pipeline review with a hiring manager, or diagnosing why a req is stalling. Keep the pipeline current, surface bottlenecks, and drive every candidate to a clear next step.

**Not for:** designing the interview loop or scorecards (use hr-interview-prep), writing the offer (use hr-draft-offer), or headcount planning (use hr-org-planning).

## Method

1. **Define stages** — sourced → applied → screen → hiring-manager → onsite/loop → offer → accepted. Confirm entry/exit criteria per stage so status is unambiguous.
2. **Inventory candidates** — list each with current stage, days-in-stage, owner, and next action with a date. Decision point: flag anyone past your stage SLA as at-risk.
3. **Compute funnel health** — stage-to-stage conversion, time-in-stage, and time-to-fill vs. target; compare to benchmark or prior reqs.
4. **Diagnose bottlenecks** — find the stage with worst conversion or longest dwell and name the likely cause (weak top-of-funnel, slow feedback, offer declines). Decision point: a top-of-funnel volume problem and a mid-funnel conversion problem need opposite fixes — don't source more into a stage that's already leaking.
5. **Assign actions** — for every active candidate and every bottleneck, specify owner, action, and due date. Chase pending scorecards and interviewer feedback.
6. **Report status** — pipeline coverage vs. hiring goal (enough candidates to hit the number), risks, and decisions the hiring manager owes you.

## Example

Req: 2× Backend Eng, target time-to-fill 45 days (day 38). Funnel: 60 sourced → 18 screens → 6 HM → 3 onsite → 1 offer. Screen→HM converts 33% (healthy); HM→onsite drops to 50% but the real leak is onsite→offer at 33% with 9-day average dwell — interviewers are late on scorecards. Diagnosis: mid-funnel feedback lag, not top-of-funnel volume. Actions: chase 2 outstanding scorecards (owner: recruiter, due tomorrow); HM to decide on candidate #4 by Friday. Coverage: 3 in loop for 2 seats — thin; add one sourcing pass as insurance.

## Pitfalls

- Stale stages — a candidate marked "onsite" who was actually rejected a week ago, hiding the true leak.
- Sourcing more candidates to fix a mid-funnel conversion problem (pouring into a leaking bucket).
- Tracking activity (calls made) instead of conversion and time-in-stage.
- Candidates with no dated next action — the pipeline silently goes cold.

## Output format

```
Pipeline snapshot: candidate | stage | days-in-stage | owner | next action + date
Funnel metrics: per-stage conversion | time-in-stage | time-to-fill vs target
Bottleneck: stage + likely cause
Action list: owner → action → due
Coverage vs goal + decisions needed from HM
```
