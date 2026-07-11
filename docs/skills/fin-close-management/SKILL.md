---
name: fin-close-management
version: 1.0.0
description: Run a sequenced period-end close with dependencies, single-owner tasks, a critical path, and live status to shorten days-to-close.
author: matrixx0070
tags: [finance, close, month-end, accounting, checklist, critical-path]
---

# Close Management

## When to use
Use this to plan or run a period-end close (month, quarter, year), unblock a stalled close, or build a repeatable close calendar that shortens days-to-close.

**Not for:** preparing the statements the close produces (fin-financial-statements), individual account reconciliations (fin-reconciliation), or drafting the entries booked during close (fin-journal-entry). This orchestrates *when and by whom*, not the accounting itself.

## Method
1. **Define period and target.** State the close period, day-1 date, and the committed deadline (e.g., business day 5, "BD5").
2. **Inventory tasks by workstream.** Group into subledger cutoff (AR, AP, payroll), accruals/deferrals, reconciliations, intercompany, fixed assets, revenue, then consolidation and reporting.
3. **Map dependencies.** Order so upstream feeds finish first: subledgers → reconciliations → variance review → reporting. Decision point: if two tasks share no dependency, run them in parallel to compress the calendar.
4. **Assign owner and due day.** Every task gets one owner and a target business day. Flag the critical path — the longest dependency chain that sets the earliest possible close.
5. **Track status live.** Mark each task not started / in progress / blocked / complete with a timestamp. Decision point: the moment a task is blocked, surface the owner and the blocking dependency — do not wait for standup.
6. **Gate the close.** Do not advance to reporting until all reconciliations are signed off and material variances are explained.
7. **Capture retro items.** Note what ran late and the concrete fix for next cycle.

## Example
March close, day-1 = Apr 1, target BD5 = Apr 7. AP cutoff (owner: J, BD1) and payroll accrual (owner: M, BD1) run in parallel. Bank rec (owner: J, BD3) depends on AP cutoff — critical path. At BD3, bank rec is *blocked*: a $40k deposit-in-transit is unposted, dependency = treasury feed. You escalate same-hour; treasury posts BD3 PM; rec clears BD4; reporting starts BD4 on schedule. Retro: automate the treasury feed to remove the recurring BD3 stall.

## Pitfalls
- **No single owner.** "The team" owns nothing; blocked tasks sit until someone notices.
- **Ignoring the critical path.** Racing non-blocking tasks feels productive but the close is only as fast as its longest chain.
- **Opening reporting before reconciliations sign off.** You will re-issue the package when a rec turns up a difference.
- **Skipping the retro.** The same task slips every month until you record and fix the cause.

## Output format
```
Period: <...> | Day-1: <date> | Deadline: BD<n>
Progress: <complete>/<total> tasks | verdict: on-track / at-risk | days left: <n>
Task register:
  | ID | task | workstream | owner | due BD | status | dependency |
Critical path: <task → task → task>
Blockers: | task | owner | cause | needed action |
Sign-off gate: reconciliations <n/n> | material variances explained: y/n
Retro: <what slipped → fix>
```
