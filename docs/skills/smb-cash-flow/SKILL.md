---
name: smb-cash-flow
version: 1.0.0
description: Produce a 30/60/90-day cash-flow forecast from AR and AP with confidence bands.
author: matrixx0070
tags: [small-business, cash-flow, forecast, ar, ap]
---

# Cash Flow Forecast

## When to use
Use this when the owner needs to know whether cash will cover commitments over the next quarter — before taking on an expense, hiring, or a large purchase, or when a lender or partner asks for a forward view.

## METHOD
1. **Set starting cash and horizon.** State today's bank balance and forecast the next 30, 60, and 90 days.
2. **Schedule inflows from AR.** List open receivables by expected pay date; adjust each date by the customer's historical days-to-pay, not the invoice term.
3. **Schedule outflows from AP.** List payables, payroll, rent, loan payments, taxes, and recurring subscriptions by due date.
4. **Roll the balance forward.** Compute projected ending cash at each week and at the 30/60/90 marks.
5. **Apply confidence bands.** Give a base case, plus low (late payers slip, no new sales) and high (on-time collections) cases as a range.
6. **Flag shortfalls.** Identify any week the balance dips below the owner's minimum buffer and how large the gap is.

Treat this as decision support; the owner approves any financing, delayed payment, or spending decision it informs.

## OUTPUT FORMAT
- **Starting cash / forecast date.**
- **Forecast table:** week, inflows, outflows, ending balance (base).
- **30 / 60 / 90 summary:** base, low, high.
- **Shortfall alerts:** week, gap size, driver.
- **Assumptions:** days-to-pay used, excluded items.
- **Recommended actions (for owner approval).**
