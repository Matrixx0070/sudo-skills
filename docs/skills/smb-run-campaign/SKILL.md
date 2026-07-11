---
name: smb-run-campaign
version: 1.0.0
description: Run an end-to-end marketing campaign — sales analysis to content brief to assets to CRM send — with an owner-approval gate at every step.
author: matrixx0070
tags: [marketing, campaign, crm, content, sales, gated]
capabilities: []
---

# Run Campaign

## When to use
Run this when the owner wants to launch a promotion, seasonal push, or re-engagement campaign built end to end rather than piece by piece. Every stage is gated: the owner approves before the next begins.

**Not for:** analysis without execution (use smb-sales-brief); sending anything to customers without explicit approval at the send gate — nothing reaches a customer before that click.

## Method
1. **Analyze sales.** Top and bottom sellers, recent trends, customer segments. Recommend a campaign angle and target audience. **Gate: owner approves the angle.**
2. **Content brief.** Offer, message, channel(s), timing, success metric. **Gate: owner approves the brief.**
3. **Assets.** Draft copy, subject lines, captions, image prompts for the approved channels. **Gate: owner reviews and edits.**
4. **Audience.** Pull the recipient segment from the connected CRM; show count and filters. Decision point: if the segment looks unexpectedly large or small, stop and confirm the filters before proceeding. **Gate: owner confirms the list.**
5. **Send.** Schedule or send through the CRM only after final owner approval. **Gate: nothing goes out before that click.**
6. **Report.** Send confirmation and where to watch results.

## Example
Coffee roaster, slow summer. Analyze: cold brew rising, single-origin bags stale; segment = lapsed 90-day buyers. Angle "Summer Cold Brew — 15% off." Owner approves. Brief: email + Instagram, launch Mon, metric = 25 orders. Approved. Assets: subject "Your summer cold brew is here ☕," body draft, IG caption. Owner edits the subject. Audience: 340 lapsed buyers — matches expectation, owner confirms. Send scheduled Mon 8am after final approval. Report: sent, results tracked in the CRM dashboard.

## Pitfalls
- Collapsing the gates — drafting assets or pulling the list before the angle is approved wastes work if direction changes.
- Sending to an unverified segment; a wrong filter can blast the whole list or the wrong people.
- Treating owner edits on assets as optional — the brand voice is theirs.
- Reporting "done" without a success metric or a place to watch results.

## Output format
- **Stage-by-stage output,** each ending with an explicit **"Approve to continue?"** gate.
- **Sequence:** sales analysis → brief → assets → audience count + filters → send confirmation.
- **Approval note:** any step that contacts customers or spends money waits for owner approval.
