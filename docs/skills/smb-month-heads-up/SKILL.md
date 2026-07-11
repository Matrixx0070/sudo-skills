---
name: smb-month-heads-up
version: 1.0.0
description: On the 25th, produce a next-30-day cash-flow outlook that flags the items needing owner attention before month-end.
author: matrixx0070
tags: [cash-flow, forecast, monthly, finance, planning, runway]
capabilities: []
---

# Month Heads-Up

## When to use
Run this near the 25th, or whenever the owner wants a forward look at cash before the month closes. It answers "what's coming, and what do I need to touch before the 1st?"

**Not for:** reconciling past books (use smb-month-end-prep); payroll-specific coverage (use smb-plan-payroll); actually sending reminders or moving money — this is a plan the owner acts on.

## Method
1. **Set the starting balance.** Pull current cash from connected accounting/bank data. Decision point: if nothing is connected, ask the owner for a starting balance rather than guessing.
2. **List inflows (next 30 days).** Open invoices with due dates, recurring revenue, scheduled deposits. Flag anything overdue.
3. **List outflows.** Payroll, rent, loan payments, subscriptions, taxes, known one-offs.
4. **Build a running daily balance.** Mark any day the projected balance dips below the owner's comfort floor. Decision point: if a floor breach appears, trace it to the specific bill or timing that causes it.
5. **Surface attention items.** Invoices to chase, bills to time differently, low-balance days, decisions due before the 1st — each with a suggested action and deadline.
6. **Present the outlook.** The owner approves before any invoice reminder, payment, or transfer goes out.

## Example
Start $12,000 on the 25th. Inflows: Invoice #204 $6,000 (due 2nd), retainer $3,000 (1st). Outflows: payroll $9,500 (1st), rent $2,800 (1st), SaaS $600 (3rd). Running balance dips to $2,700 on the 1st before #204 lands on the 2nd — below the owner's $4,000 floor. Attention: nudge #204 to pay by the 31st (closes the dip), or delay the $600 SaaS charge two days. Headline: projected EOM ~$8,100, low point $2,700 on the 1st.

## Pitfalls
- Assuming invoices pay on their due date; use a realistic pay date and flag chronic late payers.
- Reporting only the end-of-month balance and hiding a mid-month dip below the floor.
- Sending a reminder or moving money without owner approval — this skill plans, it doesn't act.
- Omitting irregular outflows (quarterly taxes, annual renewals) that blindside the forecast.

## Output format
- **Headline:** projected end-of-month balance + lowest point (and which day).
- **Daily table:** date | inflows | outflows | running balance (floor breaches marked).
- **"Needs your attention":** item | suggested action | deadline.
- **Approval note:** nothing that moves money or contacts a customer goes out without explicit owner approval.
