---
name: smb-friday-brief
version: 1.0.0
description: A read-only Friday end-of-week pulse — revenue vs prior week, top sellers, and the wins and watches to carry into next week.
author: matrixx0070
tags: [reporting, analytics, revenue, weekly, operations]
capabilities: []
---

# Friday Brief

## When to use
Use this at the end of the week for a tight, honest read on how the business did — what moved, what sold, what to watch going into next week. Read-only reporting; it changes nothing.

**Not for:** a live cross-functional snapshot (use smb-business-pulse), forward cash forecasting (use smb-cash-flow), or taking any action. This reports the week just ended.

## Method
1. Pull this week's sales, revenue, and order data, plus the prior week for comparison.
2. Compute revenue vs prior week (absolute and percent) and note the drivers behind any swing.
3. Identify the top-selling products or services and any notable drop-offs.
4. Surface wins (deals closed, milestones, standout days) and watches (slipping deals, refund spikes, inventory or cash concerns). Decision point: a watch is something that needs attention next week, not just a bad number.
5. Keep it scannable and factual. Cite the numbers; if data is incomplete, say so rather than estimating. This is a report only — no actions are taken.

## Example
Headline: Revenue $18,400 this week, up 12% from $16,450 last week — driven by two large repeat orders on Wednesday. By the numbers: 47 orders (up from 41), AOV $391. Top sellers: Deep Clean package ($6,200), Gift cards ($1,900). Wins: closed the Harbor account ($4k). Watches: refunds up to 4 (from 1) — all tied to the new courier; one $9k invoice now 40 days overdue.

## Pitfalls
- **Estimating missing data.** If Thursday's numbers haven't synced, say so — don't fabricate a total.
- **Reporting swings without drivers.** "Up 12%" is trivia; "up 12% on two repeat orders" is insight.
- **Watches with no teeth.** List only items worth acting on next week, not every minor dip.
- **Turning a report into action.** Suggestions are optional prompts; nothing changes without a separate request.

## Output format
```
Headline: revenue $__ this week vs $__ last (<±>%)
By the numbers: orders, AOV, key figures
Top sellers: <item> $__ [...]
Wins: <bullet> [...]
Watches: <bullet with figure> [...]
Suggested focus for next week (optional): 2-3 prompts
(No changes made without a separate request.)
```
