---
name: incident-postmortem
version: 1.0.0
description: Turn raw incident notes and timelines into a blameless postmortem - impact, timeline, root cause chain, what worked, and action items that would actually prevent recurrence.
triggers:
  - postmortem
  - incident report
  - write up this incident
  - root cause analysis
  - RCA
capabilities: []
inputs:
  - name: notes
    required: true
    description: Raw incident notes - timeline fragments, log excerpts, chat snippets, who did what.
  - name: severity
    required: false
    description: Severity level and user impact if known.
---

# Incident Postmortem

## Purpose
Produce the document that makes the same incident impossible (or at least survivable) next time - without turning anyone into the villain.

## Hard rules
1. **Blameless means systems, not saints.** "The deploy script allowed prod pushes without CI" - never "Alex pushed without checking". People appear in the timeline by role/name for facts, not fault.
2. **Timeline is UTC, factual, gap-honest.** Every entry has a timestamp from the notes. Where the notes have holes, write "gap - unknown what happened between X and Y" rather than smoothing over it.
3. **Root cause is a chain, not a scapegoat.** Ask why at least three times: trigger → why it broke → why it was possible → why it was not caught. A single-line "root cause: bad config" is a failure.
4. **Impact quantified honestly.** Duration, users/requests affected, data lost, money if known. "Some users were affected" is banned; if unknown, write "impact not measured - itself an action item".
5. **Action items must block recurrence, have owners, and be checkable.** "Be more careful" is banned. Each item names what changes in the SYSTEM, who owns it, and how you verify it happened.
6. **Record what went well.** Detection, escalation, or tooling that worked - so it survives the next reorg.

## Workflow
1. Assemble the timeline from every timestamped fragment first; mark gaps.
2. Establish impact window and blast radius.
3. Walk the why-chain to systemic causes.
4. Write action items sorted by prevent > detect > mitigate.
5. Two-line executive summary last, once the facts are settled.

## Output format
```
# Postmortem: <title> (<date>)
**Summary:** ...
**Impact:** ...
**Timeline (UTC):** ...
**Root cause chain:** trigger → ... → systemic cause
**What went well:** ...
**Action items:** - [ ] <systemic change> — owner, verify-by
```

## Example (abridged)
**Root cause chain:** cron restarted the daemon mid-deploy (trigger) → daemon served half-old, half-new code → possible because deploys do not pause the remediation cron → not caught because health checks test liveness, not version consistency.

**Action items:**
- [ ] Deploy script acquires a lock the remediation cron respects — owner: infra, verify: cron logs show skip during next deploy
- [ ] Health check includes build hash; alert on mixed hashes — owner: platform, verify: staged mixed-version test alerts
