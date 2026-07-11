---
name: legal-compliance-check
version: 1.0.0
description: Check a proposed action against applicable laws, regulations, and internal policies, then return required approvals and a proceed/hold/escalate verdict.
author: matrixx0070
tags: [legal, compliance, regulatory, approvals, risk, escalation]
capabilities: []
---

## When to use
Use this before doing something with legal exposure — launching a feature, running a promotion, entering a market, processing personal data, sending a mass communication, or making a commitment. It tells you which rules apply, which sign-offs you need, and whether to proceed.

**Not for:** confirming a decision already made (this informs it beforehand), interpreting a genuinely novel or contested regulation (escalate to counsel), or reviewing a contract clause-by-clause (use `legal-review-contract`).

## Method
1. **State the action precisely.** What, by whom, where (jurisdictions), affecting whom, and when. Vague inputs produce useless verdicts.
2. **Map applicable regimes.** List every law, regulation, and internal policy that plausibly governs it — privacy, consumer protection, employment, IP, export, financial, sector-specific — noting jurisdiction per regime.
3. **Test conformance per regime.** State the requirement and mark it compliant / conditional / non-compliant / unclear.
4. **List conditions for the conditionals.** Specify what must be true (consent, disclosure, license, record-keeping) to make each compliant.
5. **Determine required approvals.** Who must sign off (legal, privacy, security, finance) and in what order.
6. **Render the verdict.** *Decision point:* any non-compliant or unclear item, or missing required approval → **hold** or **escalate**; all-compliant-or-conditional-with-owned-conditions → **proceed-with-conditions**; fully clear → **proceed**.

## Example
Action: send a win-back email to lapsed EU customers next Tuesday. Regimes: GDPR (consent/legitimate interest — conditional: needs LIA on file), ePrivacy (conditional: prior opt-in for marketing), internal data-retention policy (compliant). Verdict: proceed-with-conditions. Conditions: attach completed LIA (owner: DPO), confirm suppression of opted-out contacts (owner: CRM lead). Approvals: privacy → marketing lead. Escalate: none.

## Pitfalls
- **A fuzzy action statement.** "Launch marketing" can't be tested; "email 40k EU opt-ins on 7/15" can.
- **Skipping internal policy.** Something legal under statute can still violate a stricter company rule.
- **Treating "unclear" as "compliant."** Unclear is a hold trigger, not a pass.
- **Listing approvals without order.** Parallel sign-offs that should be sequential cause re-work.

## Output format
```
Proposed action + jurisdictions:
Verdict: proceed | proceed-with-conditions | hold | escalate
Regime table:
  | Regime | Requirement | Status | Note |
Conditions to satisfy: <condition> — owner: <name>
Required approvals: <role> (order N)
Residual risk:
Escalation flags:
```
