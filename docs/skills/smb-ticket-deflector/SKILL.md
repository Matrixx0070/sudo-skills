---
name: smb-ticket-deflector
version: 1.0.0
description: Read a forwarded customer email or ticket, pull order, refund, and history, and draft a tone-matched reply — refunds only with owner approval.
author: matrixx0070
tags: [support, customer, tickets, refund, replies]
capabilities: []
---

When to use: Run this when the owner forwards a customer email or support ticket and wants a fast, accurate, on-brand reply drafted. It saves the owner from writing every response while keeping them in control of anything that costs money.

METHOD
1. Read the forwarded message. Identify the customer, the request or complaint, and the sentiment.
2. Look up context from connected systems: order details, payment and refund status, shipping, and prior interactions with this customer.
3. Determine the right resolution: answer, fix, apology, refund, replacement, or escalation. If the customer is upset, prioritize acknowledging it.
4. Draft a reply that matches the business's tone — warm, plain, and specific to the order. Include concrete next steps and timelines.
5. If the resolution involves a refund, credit, discount, or any spend, present it as a proposal and wait for the owner to approve before sending.
6. For non-monetary informational replies, still show the draft for a quick owner glance before it goes out.

OUTPUT FORMAT
- Customer + issue summary with pulled order/refund/history facts.
- Recommended resolution and whether it costs money.
- The drafted reply, ready to send.
- Explicit approval gate on any refund or spend; nothing reaches the customer without owner sign-off.
