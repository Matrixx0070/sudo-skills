---
name: legal-brief
version: 1.0.0
description: Produce a decision-ready legal briefing — daily digest, topic research, or incident write-up — scoped to what a non-lawyer stakeholder needs to decide or act on.
author: matrixx0070
tags: [legal, briefing, research, summary, risk, escalation]
capabilities: []
---

## When to use
Use this when a non-lawyer needs legal context fast enough to act: a daily digest of active matters, a focused briefing on one topic (a new regulation, a contract type, a jurisdiction), or a write-up of an incident. Your output is a summary that drives a decision, not a law-review memo.

**Not for:** giving legal advice or opinions on liability (escalate to counsel), drafting the actual filing or contract (use `legal-review-contract` / `legal-response`), or rating a single risk in depth (use `legal-risk-assessment`).

## Method
1. **Fix mode and audience.** Daily / Topic / Incident, and who reads it (exec, PM, ops). *Decision point:* if the audience is a lawyer, drop the plain-language layer and cite primary sources instead.
2. **Gather sources with dates.** Active matters, statutes/regs, contracts, prior guidance, incident facts. Record each source's date — stale law is a trap.
3. **Extract only what the reader can act on.** Pull facts, deadlines, obligations, and risks that touch their decisions; discard background.
4. **Separate law from opinion.** Tag every point [requirement] (settled), [interpretation] (judgment call), or [open] (unresolved). *Decision point:* if the decision hinges on an [interpretation] or [open] item, route it to counsel before the reader acts.
5. **Surface deadlines and owners.** Every filing date, response window, or renewal trigger gets a named owner.
6. **Flag escalation.** List anything needing licensed-attorney review before action.

## Example
PM asks: "Can we launch the referral promo in the EU next week?" Topic brief, PM audience. Bottom line: "Launchable in 3 of 4 target countries; Germany needs a disclosure change; France is an open question." Key points: [requirement] GDPR consent for referral emails; [interpretation] German UWG may treat the reward as an unfair inducement; [open] French DGCCRF stance unconfirmed. Deadline: legal sign-off by Thu (owner: Priya). Escalate: German UWG interpretation to counsel.

## Pitfalls
- **Burying the decision under background.** The reader wants the answer first; context second.
- **Mixing settled law with your guess.** An untagged interpretation reads as fact and gets acted on as one.
- **Undated sources.** A regulation summary without an "as of" date silently rots.
- **Owner-less deadlines.** "File by the 15th" with no name means nobody files.

## Output format
```
Mode / Audience / Date:
Bottom line: <2-3 sentences>
Key points:
  - [requirement|interpretation|open] <point>
Deadlines & owners:
  | Item | Date | Owner |
Risks (ranked): <risk> — exposure: <impact>
Escalate to counsel: <items needing attorney review>
Sources: <source — as of DATE>
```
