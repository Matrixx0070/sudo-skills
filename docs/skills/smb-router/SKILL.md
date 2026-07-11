---
name: smb-router
version: 1.0.0
description: Front door to the small-business toolkit — routes a vague or specific request to the best skill and explains what's available.
author: matrixx0070
tags: [router, navigation, triage, toolkit, help, dispatch]
capabilities: []
---

# Router

## When to use
Run this when the owner's request is broad ("help me with my business"), it's unclear which tool fits, or they simply ask what the toolkit can do. It matches intent to the right skill and hands off cleanly.

**Not for:** first-time setup (use smb-onboard); doing the work itself — the router points to the right skill, it doesn't run the analysis.

## Method
1. **Identify the underlying job.** Cash, pricing, contracts, marketing, sales insight, customer support, taxes, or getting set up.
2. **Map job to skill:**
   - Cash outlook before month-end → smb-month-heads-up
   - Reconcile/close the books → smb-month-end-prep
   - Payroll coverage → smb-plan-payroll
   - Pricing decision → smb-price-check (or smb-margin-analyzer for deep unit economics)
   - Contract review → smb-review-contract
   - Full marketing campaign → smb-run-campaign
   - What's selling + content plan → smb-sales-brief
   - Quarter-end deck → smb-quarterly-review
   - Weekly pulse → smb-monday-brief
   - Tax prep/handoff → smb-tax-season-organizer
   - Customer reply → smb-ticket-deflector
   - First-time setup → smb-onboard
3. **Handle multi-part requests.** Decision point: if the request spans several skills, name the best starting point and the sequence rather than firing all of them.
4. **Be honest about gaps.** If it's genuinely new, say so plainly rather than forcing a bad match.
5. **Hand off with context.** Carry the owner's context to the chosen skill. The owner still approves anything touching money or customers downstream.

## Example
Owner: "Q4 was rough, help me figure out next year." Restatement: they want a look-back plus a plan. Best start: smb-quarterly-review to tell the Q4 story, then smb-price-check if margin is the issue, then smb-run-campaign to drive new revenue. Route to smb-quarterly-review first; note the sequence so they know the path.

## Pitfalls
- Forcing a request into the nearest skill when the honest answer is "we don't have that yet."
- Firing three skills at once for a multi-part request instead of naming a starting point and sequence.
- Dropping the owner's context on handoff, so the next skill re-asks what they already said.
- Explaining the whole toolkit when they asked one specific thing — lead with the match.

## Output format
- **Restatement:** one line on what the owner wants.
- **Recommended skill + why**, plus any follow-on sequence.
- **Toolkit menu:** short list of the other skills so the owner knows what else exists.
- **Approval note:** the owner still approves anything touching money or customers downstream.
