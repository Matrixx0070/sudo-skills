---
name: smb-contract-review
version: 1.0.0
description: Lightweight NDA, MSA, and vendor-contract first pass that flags non-standard terms in plain English and outputs a redline — not legal advice.
author: matrixx0070
tags: [legal, contracts, review, risk, operations]
capabilities: []
---

# Contract Review

## When to use
Use this for a fast first pass on an NDA, MSA, or vendor agreement before it reaches a lawyer or your signature. It catches unusual, one-sided, or risky terms and explains them plainly.

**Not for:** legal advice, litigation, regulated or high-value deals where counsel is required, or anything you're about to sign without review. It flags and redlines; it does not approve, sign, or replace a lawyer.

## Method
1. Read the full document and identify its type and the parties.
2. Check the standard risk areas: liability caps, indemnification, termination, auto-renewal, payment terms, IP ownership, confidentiality scope, non-compete, governing law, and data handling.
3. Flag each clause that is missing, non-standard, or unfavorable. Decision point: rate severity high/medium/low by real-world exposure — an uncapped indemnity is high; an odd notice address is low.
4. Propose specific redline edits or alternative language for the worst terms.
5. State clearly this is a preliminary review, not legal advice, and recommend a lawyer for high-severity items. The owner decides what to accept, negotiate, or escalate — nothing is signed here.

## Example
Vendor MSA, overall risk: High. Findings include: liability cap absent (High — vendor's exposure is unlimited against you); auto-renews for 12 months with 90-day notice (Medium — easy to miss the window). Redline for the cap: "Each party's total liability shall not exceed the fees paid in the 12 months preceding the claim." Recommend a lawyer for: the indemnification and IP-assignment clauses.

## Pitfalls
- **Presenting flags as legal advice.** Always mark it preliminary and route high-severity items to counsel.
- **Rating by clause name, not exposure.** Severity is about what it costs you if invoked, not how unusual the wording is.
- **Missing what's absent.** The dangerous term is often the missing liability cap, not the one that's written.
- **Vague redlines.** "Make this fairer" is useless; give exact before/after language.

## Output format
```
Summary: <contract type> — overall risk <High/Med/Low>
Findings:
| Clause | Severity | Plain-English concern | Suggested change |
Redlines:
  <clause>: BEFORE "..." / AFTER "..."
Recommend a lawyer for:
  - <high-severity items>
Reminder: preliminary review, not legal advice; owner approves any signature.
```
