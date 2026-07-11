---
name: legal-risk-assessment
version: 1.0.0
description: Size one legal risk by severity and likelihood, place it on a matrix, apply escalation criteria, and assign owned mitigations.
author: matrixx0070
tags: [legal, risk, assessment, matrix, escalation, mitigation]
capabilities: []
---

## When to use
Use this to size a specific legal risk — a contract term, a compliance gap, a potential dispute, a data exposure, an IP conflict — so stakeholders agree on how serious it is and who must act. It turns vague worry into a rated, owned item.

**Not for:** assessing many risks at once (run this per risk), a full contract review (use `legal-review-contract`), or deciding whether an action is lawful in the first place (use `legal-compliance-check`).

## Method
1. **Describe the risk as a scenario.** "If X happens, then Y consequence." One risk per assessment.
2. **Rate severity (1-5).** Weigh financial exposure, regulatory penalty, litigation, reputational and operational harm. State the driver of the score.
3. **Rate likelihood (1-5).** Base it on evidence and precedent, not gut feel. Note the basis.
4. **Plot severity × likelihood** and derive a tier: Low / Medium / High / Critical.
5. **Apply escalation criteria.** *Decision points:* Critical or any severity 5 → immediate counsel + leadership; High → counsel within the week; Medium → owner + tracked; Low → monitor.
6. **Define mitigation.** For each material risk, give an action that lowers severity or likelihood, with owner and date.
7. **Set a review trigger.** The event or date that forces re-assessment.

## Example
Scenario: "If the auto-renewal in the SaaS contract fires unnoticed, we're locked into another 12 months at $180k with no exit." Severity: 4 (financial lock-in, no operational harm). Likelihood: 3 (no calendar reminder exists; renewal is 60 days out). Tier: High → counsel within the week. Mitigation: file a 45-day-prior cancellation reminder and send notice of non-renewal (owner: Procurement, by next Friday). Residual: Low once notice is sent. Review trigger: renewal date, or any renegotiation.

## Pitfalls
- **Scoring on gut feel.** Likelihood without an evidence basis invites endless debate; cite precedent or data.
- **Bundling multiple risks.** One assessment per scenario, or the tier becomes meaningless.
- **Mitigations without an owner or date.** An unowned action is a wish, not a control.
- **No review trigger.** Risk ratings go stale; name the event that forces a re-look.

## Output format
```
Risk scenario: If <X>, then <Y>.
Severity: <1-5> — driver:
Likelihood: <1-5> — basis:
Tier: Low | Medium | High | Critical
Escalation: <who> by <when>
Mitigations: <action> — owner: <name> — by: <date>
Residual risk (post-mitigation):
Review trigger:
```
