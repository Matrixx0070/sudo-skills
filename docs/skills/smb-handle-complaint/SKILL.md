---
name: smb-handle-complaint
version: 1.0.0
description: Handle a single customer complaint end-to-end — context, root cause, an owner-approved remedy, a drafted response, and an operational fix.
author: matrixx0070
tags: [small-business, complaints, customer-service, retention, operations]
---

# Handle a Complaint

## When to use
Use this when a customer raises a complaint and the owner wants to respond well, keep the relationship, and stop the same problem recurring — not just fire off an apology.

**Not for:** aggregating many complaints into themes (use smb-customer-pulse) or drafting reusable templates across issues (use smb-customer-pulse-check). This handles one case, deeply.

## Method
1. **Capture the complaint.** State what the customer said, the channel, the order/account, and the outcome they want.
2. **Pull context.** Note the customer's history — tenure, spend, prior issues — and what actually happened on your side.
3. **Diagnose root cause.** Separate the symptom from the underlying cause (process gap, product defect, miscommunication, one-off).
4. **Decide the remedy.** Propose the resolution — apology, fix, refund, replacement, credit, or goodwill gesture. Decision point: size it to both the severity and the customer's lifetime value; a loyal high-spender warrants more than a first-time buyer with a minor gripe.
5. **Draft the response.** Write a message that acknowledges, takes responsibility where due, states the remedy and timeline, and stays warm and specific.
6. **Prescribe the operational fix.** Recommend the change that prevents recurrence, with an owner.

Any refund, credit, compensation, or customer-facing reply requires owner approval before it goes out or money moves — present them as proposals.

## Example
Complaint (email): "My monthly delivery arrived broken again." Context: 3-year customer, ~$1,200/yr, second breakage in two months. Root cause: new packaging insert too thin. Proposed remedy: replace free + one month credit ($40) — pending approval. Draft response opens: "You've been with us three years and this is twice now — that's on us." Operational fix: revert to the thicker insert; owner = ops lead.

## Pitfalls
- **Apology without a fix.** "Sorry for the inconvenience" with no remedy or root cause loses the customer anyway.
- **One-size remedy.** Over-compensating a minor issue trains bad behavior; under-compensating a loyal customer loses them.
- **Sending before approval.** Every reply and any money movement waits for the owner's yes.
- **Skipping prevention.** If you don't name the operational fix, the same complaint returns.

## Output format
```
Complaint: <what> | channel <..> | desired outcome <..>
Customer context: tenure, value, history
Root cause: ___
Proposed remedy: <action> — cost/credit $__ (pending owner approval)
Draft response: "<ready to send on approval>"
Operational fix: <change> — owner <who> — prevents <what>
```
