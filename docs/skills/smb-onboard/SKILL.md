---
name: smb-onboard
version: 1.0.0
description: Onboard a new small-business owner — connect their first two tools, run one recipe, interview them, store context, and set a weekly check-in.
author: matrixx0070
tags: [onboarding, setup, interview, context, check-in, first-run]
capabilities: []
---

# Onboard

## When to use
Run this the first time a small-business owner arrives, or when they want to reset their setup. It gets them from zero to one real result and captures enough context to be useful going forward.

**Not for:** routing an already-onboarded owner to a task (use smb-router); deep analysis in any one area — onboarding produces a taste, not a full report.

## Method
1. **Welcome and orient.** In two sentences: what the toolkit does, and that the owner approves anything touching money or customers.
2. **Connect the first two tools.** Typically accounting or payments, plus a CRM or storefront. Decision point: pick the two that match the owner's biggest headache, not a fixed list. Confirm each connection actually works.
3. **Run one recipe end to end.** For example a sales brief or a month heads-up, so they see a real result in the first session.
4. **Interview the owner.** Business type, what they sell, busy seasons, biggest current headache, goals. Keep it short and conversational.
5. **Store durable context.** Save the answers so later skills personalize. Decision point: read the result and interview back to confirm before storing — don't persist a wrong guess.
6. **Set cadence and hand off.** Agree a weekly check-in day and point them to smb-router for what's next. No spend or customer contact happens during onboarding without approval.

## Example
Bakery owner arrives. Connect Square (payments) and Mailchimp (CRM); both confirm green. Run smb-sales-brief on the last 30 days — croissants top revenue, day-old bread stale. Interview: wholesale + retail, holidays are peak, headache is slow weekday mornings, goal is +15% weekday sales. Store that context. Set Monday check-in; hand off to smb-run-campaign for a weekday-morning promo when ready.

## Pitfalls
- Connecting five tools and finishing none; two working connections beat five half-configured.
- Skipping the live recipe — an owner who hasn't seen one result won't come back.
- Storing interview answers without confirming them, so every later skill inherits a wrong assumption.
- Quietly acting on money or customers "to demonstrate" — the approval rule starts at minute one.

## Output format
- **Connection status:** each of the two tools (connected / failed + reason).
- **First recipe result:** the actual output produced.
- **Business-context summary:** saved, and shown for the owner to correct.
- **Cadence + next steps:** confirmed weekly check-in day + a short "what's next" menu.
- **Approval note:** no spend or customer contact during onboarding without approval.
