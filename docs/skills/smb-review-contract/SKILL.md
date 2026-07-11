---
name: smb-review-contract
version: 1.0.0
description: Review a contract in plain English, flag red flags by severity, and return a marked-up redline with suggested edits.
author: matrixx0070
tags: [contract, legal, review, redline, risk, negotiation]
capabilities: []
---

# Review Contract

## When to use
Run this when the owner receives a contract, lease, vendor agreement, or client SOW and wants to understand it and negotiate before signing.

**Not for:** legal advice or high-stakes deals on its own — this is a plain-English review; recommend a lawyer when the stakes are high. Not for signing or sending anything on the owner's behalf.

## Method
1. **Read the whole document.** Identify the parties, the deal, term length, renewal, and termination mechanics.
2. **Explain in plain English.** What the owner is agreeing to, what they get, and what they owe.
3. **Scan for risk clauses.** Auto-renewal, unilateral changes, liability/indemnification, exclusivity, non-compete, payment terms, late fees, IP ownership, dispute venue.
4. **Rate each red flag.** Severity High/Medium/Low, a one-line "why it matters," and a suggested fix. Decision point: if any High-severity clause is present (uncapped liability, broad IP assignment, auto-renew with a long notice window), say plainly that a lawyer should see it before signing.
5. **Produce a redline.** Original text with proposed edits marked and short margin comments.
6. **Hand back the decision.** The owner decides what to accept, push back on, or walk away from. Nothing is signed or sent on their behalf without approval.

## Example
A SaaS vendor agreement: 12-month term, **auto-renews for 12 months unless cancelled 90 days out** (High — long lock-in, easy to miss; fix: 30-day notice, month-to-month after year one). Liability capped at fees paid (Medium — acceptable). **Vendor may change pricing "at any time" (High** — fix: cap increases at 5%/year with 60-day notice). Plain-English summary: you commit for a year, hard to exit, and price can jump. Redline marks the two High clauses with suggested language; note recommends a lawyer given the auto-renew lock-in.

## Pitfalls
- Summarizing only the friendly clauses and glossing over indemnification or IP ownership buried at the back.
- Rating everything "Medium" — severity has to discriminate or it's noise.
- Flagging a problem with no suggested fix, leaving the owner nothing to negotiate with.
- Presenting the review as legal advice; always steer high-stakes deals to a licensed lawyer.

## Output format
- **Plain-English summary** (5-8 sentences).
- **Red-flag table:** clause | severity | why it matters | suggested change.
- **Redline block:** tracked edits + margin comments.
- **Closing note:** recommend professional legal review when stakes are high; nothing signed or sent without owner approval.
