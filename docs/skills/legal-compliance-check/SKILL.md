---
name: legal-compliance-check
version: 1.0.0
description: Check a proposed action against applicable laws, regulations, and internal policies, and return required approvals plus a risk verdict.
author: matrixx0070
tags: [legal, compliance, regulatory, approvals, risk]
capabilities: []
---

## When to use
Use this before doing something with legal exposure — launching a feature, running a promotion, entering a market, processing personal data, sending a mass communication, or signing a commitment. It tells you what rules apply, what sign-offs you need, and whether to proceed.

## METHOD
1. **State the proposed action precisely.** What, by whom, where (jurisdictions), affecting whom, and when.
2. **Map applicable regimes.** Identify the laws, regulations, and internal policies that plausibly govern it (privacy, consumer protection, employment, IP, export, financial, sector-specific). Note jurisdiction per regime.
3. **Test conformance.** For each regime, state the requirement and whether the action meets it: compliant / conditional / non-compliant / unclear.
4. **List conditions and controls.** For conditional items, specify what must be true (consent, disclosure, license, record-keeping) to make it compliant.
5. **Determine required approvals.** Who must sign off (legal, privacy, security, finance) before proceeding.
6. **Render a verdict.** Proceed / proceed-with-conditions / hold / escalate to counsel.

## OUTPUT FORMAT
- **Proposed action** and jurisdictions.
- **Verdict:** proceed / conditions / hold / escalate.
- **Regime table:** regime, requirement, status, note.
- **Conditions to satisfy:** actionable, with owners.
- **Required approvals:** roles and order.
- **Residual risk** and escalation flags.
