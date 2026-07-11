---
name: smb-customer-pulse
version: 1.0.0
description: Aggregate disputes, tickets, and reviews into weighted themes with trend and revenue-at-risk, then recommend the three highest-leverage fixes.
author: matrixx0070
tags: [small-business, customers, feedback, reviews, support]
---

# Customer Pulse

## When to use
Use this when the owner wants to understand what customers are actually experiencing across scattered channels — support tickets, chargebacks/disputes, and public reviews — and turn the noise into a short list of fixes.

**Not for:** handling a single complaint end-to-end (use smb-handle-complaint) or drafting per-customer reply templates (use smb-customer-pulse-check). This is portfolio-level analysis, not a response tool.

## Method
1. **Set window and sources.** State the period and channels included (tickets, disputes, reviews, survey/NPS if any).
2. **Normalize the inputs.** For each item capture channel, date, sentiment, and the underlying issue in a common form.
3. **Cluster into themes.** Group by root issue (product, delivery, billing, support responsiveness, expectations). Decision point: weight by severity and frequency together — one chargeback can outweigh ten mild grumbles.
4. **Trend it.** Compare theme volume against the prior window to show what's rising or cooling.
5. **Quantify impact.** Estimate revenue at risk per theme (dispute amounts, churn signals, review-score effect).
6. **Pick three actions.** Recommend the three highest-leverage fixes, each with the theme it addresses and expected effect.

Do not reply to reviewers, issue refunds, or change policy on your own; present analysis and proposed actions for owner approval, since these touch customers and money.

## Example
30-day window, 42 items (tickets, disputes, Google reviews). Top theme: "late delivery" — 14 items, rising from 6 last month, ~$2,100 revenue at risk (2 disputes + 3 one-star reviews). Representative quote: "Third time my order came a week late." Do these 3: (1) audit the courier SLA, (2) add proactive delay notifications, (3) offer store credit to the 5 affected customers — owner to approve credits.

## Pitfalls
- **Counting frequency only.** A rare but high-dollar dispute can matter more than a common minor gripe — weight severity.
- **Cherry-picking quotes.** Pick a representative quote per theme, not the most dramatic one.
- **Acting unilaterally.** Refunds, replies, and policy changes are owner decisions, not this skill's.
- **No trend baseline.** A theme count means little without the prior window to compare against.

## Output format
```
Window: <period> | Sources: <list> | Volume: <n>
Themes:
| Theme | Count | Severity | Trend vs prior | Rev at risk |
Representative quotes:
  - <theme>: "<quote>"
Do these 3 things:
  1. Action — theme addressed — expected effect
Items needing owner decision (refunds, replies, policy):
```
