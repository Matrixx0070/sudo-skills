---
name: smb-month-heads-up
version: 1.0.0
description: On the 25th, produce a next-30-day cash-flow outlook that flags the items needing owner attention before month-end.
author: matrixx0070
tags: [cash-flow, forecast, monthly, finance, planning]
capabilities: []
---

When to use: Run this near the 25th of any month, or whenever the owner wants a forward look at cash before the month closes. It answers "what's coming, and what do I need to touch before the 1st?"

METHOD
1. Pull the current cash position from connected accounting or bank data. If none is connected, ask the owner for a starting balance.
2. List expected inflows for the next 30 days: open invoices with due dates, recurring revenue, scheduled deposits. Flag anything overdue.
3. List expected outflows: payroll, rent, loan payments, subscriptions, taxes, known one-offs.
4. Compute a running daily balance and mark any day the projected balance dips below the owner's comfort floor.
5. Surface attention items: invoices to chase, bills to time, low-balance days, decisions due before month-end.
6. Present the outlook. The owner approves before any invoice reminder, payment, or transfer is sent.

OUTPUT FORMAT
- Headline: projected end-of-month balance and lowest point.
- Table: date, inflows, outflows, running balance.
- "Needs your attention" bullet list, each with a suggested action and deadline.
- Nothing that moves money or contacts a customer goes out without explicit owner approval.
