---
name: legal-review-contract
version: 1.0.0
description: Review a contract against a negotiation playbook, flag deviations from preferred and fallback positions, and produce redline-ready comments with a sign/negotiate/reject verdict.
author: matrixx0070
tags: [legal, contract, review, redline, playbook, escalation]
capabilities: []
---

## When to use
Use this to review an incoming or draft contract — MSA, SOW, DPA, license, vendor or partner agreement — against a defined playbook of acceptable terms. It finds where the document departs from what your organization will accept and prepares the redline.

**Not for:** contracts with no playbook or a novel structure (escalate to counsel), drafting a contract from scratch, or a one-line clause question (use `legal-response`). Final legal sign-off on execution-ready contracts stays with an attorney.

## Method
1. **Identify contract type and load the playbook.** Preferred, fallback, and walk-away position for each key clause. *Decision point:* no playbook exists → escalate to counsel rather than guess.
2. **Read for the critical clauses.** Liability caps and exclusions, indemnity, IP ownership and license grant, confidentiality, data protection, term and termination, payment, warranty, governing law, assignment, auto-renewal.
3. **Compare each clause to the playbook.** Mark: acceptable / within-fallback / beyond-fallback / missing / one-sided.
4. **Assess each deviation.** State the risk it creates and its business impact.
5. **Draft the redline.** For every problem clause, give the specific proposed edit plus a one-line rationale for the counterparty.
6. **Prioritize.** Separate deal-breakers (must fix) from negotiables (nice to fix).
7. **Flag counsel items.** Anything novel or beyond fallback goes to an attorney before signature.

## Example
Contract: vendor MSA. Liability clause caps vendor at 3 months' fees and excludes all indirect damages including a data-breach carve-out. Playbook: cap ≥ 12 months' fees, breach must be super-cap. Status: beyond-fallback. Risk: a breach of our customer data could leave us bearing seven-figure exposure against a capped vendor. Redline: "Liability cap raised to 12 months' fees; data-breach and confidentiality violations excluded from the cap." Rationale: "Aligns risk with the sensitivity of data processed." Priority: deal-breaker. Escalate: yes — cap structure beyond fallback.

## Pitfalls
- **Reviewing without a playbook.** "Looks fine" is not a standard; every clause needs a benchmark.
- **Flagging problems without proposed text.** A comment the counterparty can't paste in stalls the deal.
- **Missing what's absent.** A missing indemnity or DPA is a deviation too — check for silence, not just bad language.
- **Treating every deviation as a deal-breaker.** Mixing must-fix with nice-to-fix buries the real blockers.

## Output format
```
Contract / parties / type / playbook:
Summary verdict: sign | negotiate | reject
Clause table:
  | Clause | Playbook position | Contract says | Status | Risk |
Redlines:
  | Clause | Proposed edit | Rationale |
Deal-breakers vs. negotiables:
Escalate to counsel: <items beyond fallback / novel>
```
