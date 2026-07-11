---
name: legal-response
version: 1.0.0
description: Draft a response to a routine legal inquiry from an approved template, with escalation checks that route novel or high-risk questions to counsel before any answer goes out.
author: matrixx0070
tags: [legal, response, templates, intake, escalation]
capabilities: []
---

## When to use
Use this to answer routine, recurring legal questions — "can we use this logo," "is this clause standard," "what's our data-retention period," "can I share this with a partner" — where an approved template exists. It resolves the common case fast and routes anything unusual to a licensed attorney.

**Not for:** novel fact patterns, active or threatened litigation, regulator inquiries, personal legal advice, or exposure above your dollar threshold — all of those escalate. Do not improvise a template where none exists.

## Method
1. **Classify the inquiry.** Match it to a known category (IP use, data handling, contract clause, employment, disclosure, third-party sharing). *Decision point:* no category fits → escalate, stop here.
2. **Run escalation checks first, before drafting.** Flag to counsel if the matter involves litigation, a regulator, a novel fact pattern, dollar exposure above threshold, personal legal advice, or a non-standard jurisdiction. Never template these.
3. **Select the approved template** for the category and confirm it is the current version.
4. **Fill it with the specific facts.** Replace every placeholder; never leave generic language that misstates the situation.
5. **Add caveats.** State your assumptions and the boundary of the answer ("this covers X, not Y").
6. **Mark review need.** Note whether attorney review is required before sending.

## Example
Inquiry: "Can we put a customer's logo on our website?" Category: IP use → template exists. Escalation checks: no litigation, standard jurisdiction, low exposure → pass. Draft (from template): "Yes, provided (a) the customer has signed our reference-rights clause or given written consent, and (b) you use the logo per any brand guidelines they supply." Assumptions: US-based customer, marketing use only. Scope limit: does not cover press releases or paid ads. Attorney review: not required. Next step: confirm signed reference clause with account owner.

## Pitfalls
- **Drafting before running escalation checks.** You'll template a matter that needed a lawyer.
- **Leaving placeholders in.** "[CUSTOMER]" or generic boilerplate that no longer fits the facts misleads the requester.
- **Silent scope creep.** Answering the adjacent question you weren't asked, without flagging it.
- **Using a stale template.** Confirm the version — retention periods and clause language change.

## Output format
```
Inquiry (restated) + category:
Escalation check: pass | ESCALATE — reason:
Response draft: <templated, facts filled>
Assumptions & scope limits:
Attorney review: required | not required
Suggested next step for requester:
```
