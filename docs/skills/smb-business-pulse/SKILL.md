---
name: smb-business-pulse
version: 1.0.0
description: Build a one-page cross-functional snapshot of cash, sales, pipeline, and the watch-list so an owner can read the whole business at a glance.
author: matrixx0070
tags: [small-business, dashboard, cash, sales, pipeline, owner-report]
---

# Business Pulse

## When to use
Use this when the owner wants a single-glance read on how the business is doing right now — before a call, at the start of a day, or when something feels off and they need one page tying finance, sales, and operations together.

**Not for:** forward forecasting (use smb-cash-flow), month-end reconciliation (use smb-close-month), or the weekly retrospective (use smb-friday-brief). This is a live cross-section, not a closed period.

## Method
1. **Set the as-of date and comparison.** State the snapshot date and the prior period you compare against. Decision point: pick last week for an operational read, last month or same-period-last-year for a trend read.
2. **Pull cash.** Report cash on hand, net change since the last snapshot, and weeks of runway at current burn (use trailing burn, not one day's outflow).
3. **Pull sales.** Show revenue period-to-date vs target and vs prior period, plus the new vs repeat mix.
4. **Pull pipeline.** Summarize open opportunities by stage, weighted value, and expected close this period.
5. **Build the watch-list.** Flag anything off-trend: overdue AR, thin margins, slipping deals, staffing or supply risk. Decision point: keep only items actionable this week — park the rest.
6. **Rank actions.** Convert the watch-list into the top 3 things the owner should act on.

This is an internal read only. Do not send anything to customers or move money — get owner approval before acting on any item.

## Example
As-of Fri vs prior Fri. Cash $48,200 (down $6,100), 5.1 weeks runway. Sales MTD $71k vs $90k target (79%), 62% repeat. Pipeline: 4 deals in Proposal, weighted $22k, two expected to close this month. Watch-list: a $9k invoice 40 days overdue; ad spend up 30% with flat leads. Top 3: chase the $9k, pause the underperforming ad set, confirm the two Proposal closes.

## Pitfalls
- **Padding the watch-list.** Ten flags with no ranking is noise; force it down to the top 3 actions.
- **Stale comparisons.** Comparing to an atypical prior period (a holiday week) hides the real trend — note anomalies.
- **Runway from a single balance.** Weeks-of-runway off one day's cash misleads; base it on trailing burn.
- **Silently guessing missing numbers.** If a source is unavailable, mark the line UNKNOWN rather than estimating.

## Output format
```
As-of: <date> | vs <comparison period>
Cash: on hand $__ | net change $__ | runway __ wks
Sales: PTD $__ vs target $__ vs prior $__ | new/repeat __%/__%
Pipeline:
  <stage> — <count> deals — weighted $__ — exp. close $__
Watch-list:
  - <flag> — <one-line why>
Top 3 actions (owner approval required to act):
  1. ___  2. ___  3. ___
```
