---
name: smb-router
version: 1.0.0
description: Front door to the small-business toolkit — routes a vague or specific request to the best skill and explains what's available.
author: matrixx0070
tags: [router, navigation, triage, toolkit, help]
capabilities: []
---

When to use: Run this when the owner's request is broad ("help me with my business"), unclear which tool fits, or they simply ask what the toolkit can do. It matches intent to the right skill and hands off cleanly.

METHOD
1. Read the owner's request and identify the underlying job: cash, pricing, contracts, marketing, sales insight, customer support, taxes, or getting set up.
2. Map the job to the best skill:
   - Cash outlook before month-end -> smb-month-heads-up
   - Pricing decision and margins -> smb-price-check
   - Contract review and redline -> smb-review-contract
   - Full marketing campaign -> smb-run-campaign
   - What's selling and a content plan -> smb-sales-brief
   - First-time setup -> smb-onboard
   - Tax prep and accountant handoff -> smb-tax-season-organizer
   - Customer email or ticket reply -> smb-ticket-deflector
3. If the request spans several, name the best starting point and the sequence.
4. If it's genuinely new, say so plainly rather than forcing a bad match.
5. Hand off to the chosen skill, carrying the owner's context. The owner still approves anything touching money or customers downstream.

OUTPUT FORMAT
- One-line restatement of what the owner wants.
- The recommended skill and why, plus any follow-on sequence.
- A short menu of the full toolkit so the owner knows what else exists.
