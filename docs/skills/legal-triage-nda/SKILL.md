---
name: legal-triage-nda
version: 1.0.0
description: Triage an incoming NDA against standard terms and classify it GREEN, YELLOW, or RED with a recommended action and specific edits.
author: matrixx0070
tags: [legal, nda, triage, confidentiality, review, escalation]
capabilities: []
---

## When to use
Use this when an NDA arrives and someone needs a fast, consistent read: sign as-is, negotiate lightly, or send to counsel. It applies a standard rubric so NDAs don't silently pile up or get signed with hidden traps.

**Not for:** NDAs bundled inside a larger agreement (review the whole via `legal-review-contract`), high-stakes M&A or litigation confidentiality (escalate), or drafting an NDA from scratch. This triages incoming standalone NDAs only.

## Method
1. **Capture the basics.** Parties, one-way vs. mutual, purpose, and which disclosure direction matters to us.
2. **Check core terms** against standard: definition of confidential information, permitted use, exclusions (public, independently developed, already known), term and survival, return/destruction, governing law.
3. **Scan for red flags:** non-competes or non-solicits hidden inside, IP assignment, indemnification, unlimited/perpetual duration, unusually broad "confidential" definitions, one-sided obligations on us, residuals clauses, foreign jurisdiction.
4. **Classify.** *Decision points:* GREEN = standard, mutual, reasonable term → sign as-is. YELLOW = minor deviations fixable with playbook edits → negotiate. RED = any red-flag term, IP/indemnity/non-compete, or high-stakes counterparty → escalate to counsel.
5. **Recommend action** matching the color, with specific edits for YELLOW.
6. **Note the deadline** and who owns the next step.

## Example
Incoming: one-way NDA, we are the receiving party, purpose "evaluate a partnership." Core terms mostly standard, but two issues: term survives 7 years (standard is 3-5) and it includes an IP-assignment clause granting them rights to anything we create during discussions. Red flag: IP assignment. Classification: RED. Recommended action: escalate to counsel; do not sign. Owner: deal lead, deadline: before next partner call Thursday.

## Pitfalls
- **Skimming for the confidentiality clause only.** The trap is usually a smuggled non-compete or IP-assignment term elsewhere.
- **Calling a one-sided NDA GREEN.** If all obligations fall on us, it isn't standard — that's at least YELLOW.
- **Negotiating a RED item yourself.** IP, indemnity, and non-competes go to counsel, not playbook edits.
- **No deadline.** An untriaged NDA that "we'll get to" blocks the deal it gates.

## Output format
```
Parties / type (one-way|mutual) / purpose:
Classification: GREEN | YELLOW | RED
Term check table:
  | Term | Standard | This NDA | OK? |
Red flags (if any):
Recommended action: sign | negotiate (edits: ...) | escalate to counsel
Owner & deadline:
```
