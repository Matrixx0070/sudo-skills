---
name: smb-customer-pulse-check
version: 1.0.0
description: Synthesize disputes, tickets, and reviews into a top-3 fixable-issues list, each with root cause and a ready-to-edit response template — never auto-sent.
author: matrixx0070
tags: [customer-success, support, reviews, analytics, retention]
capabilities: []
---

# Customer Pulse Check

## When to use
Use this when customer feedback is scattered across support tickets, payment disputes, and online reviews and you want the signal: what's actually hurting customers and what to say about it.

**Not for:** deep portfolio analysis with trend and revenue-at-risk (use smb-customer-pulse) or resolving one specific complaint (use smb-handle-complaint). This surfaces the top three fixable issues and drafts reply templates.

## Method
1. Gather recent disputes, support tickets, and reviews across your channels.
2. Cluster the feedback by theme (shipping, product defect, billing, response time) and count how often each appears.
3. Rank themes by frequency and severity to find the top three that are genuinely fixable. Decision point: exclude one-off complaints and things outside your control — focus on patterns you can act on.
4. For each issue, note the likely root cause and a concrete operational fix.
5. Draft a response template the owner can adapt for affected customers. Present everything for approval. Do not send any reply or post any public response — the owner approves all customer-facing messages.

## Example
Pulse summary: 28 items, sentiment trending down. Top issue: billing confusion — 9 mentions, medium-high severity. Example: "Got charged twice and no one replied for days." Root cause: no auto-confirmation on the retry path. Fix: add a payment-confirmation email + a same-day billing-reply SLA. Template: "Hi {name}, you're right — we double-charged you and were too slow to respond. The duplicate is refunded and here's what we changed... " — owner edits before it goes out.

## Pitfalls
- **Fixing one-offs.** A single angry review isn't a pattern; require repetition before it makes the top 3.
- **Templates that dodge fault.** A response that won't own a real error reads as corporate and worsens churn.
- **Skipping root cause.** A reply without an operational fix means the same complaints return next month.
- **Auto-sending.** Every customer-facing message waits for owner approval or edits.

## Output format
```
Pulse summary: volume <n> | sentiment trend <up/flat/down>
Top 3 issues:
  1. <theme> — frequency <n> — severity <H/M/L>
     Example quote: "..."
     Root cause: ___
     Suggested fix: ___
     Response template: "<ready-to-edit draft>"
"Approve or edit these templates before anything goes to a customer."
```
