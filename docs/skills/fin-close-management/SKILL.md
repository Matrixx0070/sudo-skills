---
name: fin-close-management
version: 1.0.0
description: Run a month-end close with sequenced tasks, dependencies, ownership, and real-time status tracking.
author: matrixx0070
tags: [finance, close, accounting, month-end, checklist]
---

# Close Management

## When to use
Use this to plan or run a period-end close (month, quarter, year), to unblock a stalled close, or to build a repeatable close calendar that shortens days-to-close.

## METHOD
1. **Define the period and target.** State the close period, the day-1 date, and the committed close deadline (e.g., business day 5).
2. **Inventory tasks by workstream.** Group into subledger cutoff (AR, AP, payroll), accruals and deferrals, reconciliations, intercompany, fixed assets, revenue, then consolidation and reporting.
3. **Map dependencies.** Order tasks so upstream feeds finish first: subledgers close before reconciliations; reconciliations before variance review; variance review before reporting.
4. **Assign owner and due day.** Give every task a single owner and a target business day; flag the critical path.
5. **Track status live.** Mark each task not started / in progress / blocked / complete with a timestamp; surface blockers immediately with the owner and the dependency causing them.
6. **Gate the close.** Do not advance to reporting until all reconciliations are signed off and material variances are explained.
7. **Capture retro items.** Note what ran late and the fix for next cycle.

## OUTPUT FORMAT
- **Period / day-1 / close deadline.**
- **Progress summary:** tasks complete vs total, on-track / at-risk verdict, days remaining.
- **Task register table:** ID, task, workstream, owner, due day, status, dependency.
- **Critical path:** ordered blocking tasks.
- **Blockers:** task, owner, cause, needed action.
- **Sign-off gate status.**
- **Retro / process-improvement notes.**
