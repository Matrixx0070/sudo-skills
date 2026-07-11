---
name: smb-ticket-deflector
version: 1.0.0
description: Read a forwarded customer email or ticket, pull order/refund/history context, and draft a tone-matched reply — refunds only with owner approval.
author: matrixx0070
tags: [support, customer, tickets, refund, replies, tone]
capabilities: []
---

# Ticket Deflector

## When to use
Run this when the owner forwards a customer email or support ticket and wants a fast, accurate, on-brand reply drafted. It saves the owner from writing every response while keeping them in control of anything that costs money.

**Not for:** sending replies autonomously (every draft gets an owner glance first); anything that spends money without approval; multi-message campaigns (use smb-run-campaign).

## Method
1. **Read the message.** Identify the customer, the request or complaint, and the sentiment.
2. **Pull context.** From connected systems: order details, payment/refund status, shipping, prior interactions with this customer.
3. **Determine the resolution.** Answer, fix, apology, refund, replacement, or escalation. Decision point: if the customer is upset, acknowledge that first; if facts are missing, ask internally rather than guessing in the reply.
4. **Draft a tone-matched reply.** Warm, plain, specific to the order, with concrete next steps and timelines.
5. **Gate anything that costs money.** If the resolution involves a refund, credit, discount, or spend, present it as a proposal and wait for owner approval before sending.
6. **Show every draft.** Even non-monetary informational replies get a quick owner glance before they go out.

## Example
Customer: "Order #5521 arrived cracked, this is ridiculous." Sentiment: angry. Context: delivered 2 days ago, one prior clean order, $58 paid. Resolution: apologize + free replacement (no refund needed) — costs a replacement unit, so gate it. Draft: "Hi Dana, I'm so sorry your order arrived damaged — that's on us. I've queued a free replacement shipping today, tracking to follow. Nothing needed on your end." Present the replacement cost for owner approval before sending.

## Pitfalls
- Sending a refund, credit, or replacement without the owner's approval — the money gate is non-negotiable.
- Replying with generic canned language instead of matching the business's actual voice.
- Answering before pulling order/refund history, so the reply contradicts the record.
- Matching an angry customer's heat instead of acknowledging the frustration and de-escalating.

## Output format
- **Customer + issue summary** with pulled order/refund/history facts.
- **Recommended resolution** and whether it costs money.
- **Drafted reply,** ready to send.
- **Approval gate:** explicit sign-off on any refund or spend; nothing reaches the customer without owner approval.
