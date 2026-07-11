---
name: fin-reconciliation
version: 1.0.0
description: Reconcile a GL account to a bank statement, subledger, or third-party source, prove the tie-out bridge, and clear differences.
author: matrixx0070
tags: [finance, reconciliation, gl, bank-rec, subledger, close]
---

# Reconciliation

## When to use
Use this to reconcile a general-ledger account to a supporting source — bank statement, subledger (AR/AP), or third-party report — to explain a difference, or to produce a signed reconciliation for the close.

**Not for:** drafting the correcting entry itself in full detail (hand the item to fin-journal-entry), or explaining an actual-vs-budget variance (fin-variance-analysis). This proves *GL agrees to source*, not plan.

## Method
1. **Define the reconciliation.** Name the GL account, the supporting source, the as-of date, and both starting balances.
2. **Compute the raw difference.** GL − source. Decision point: if zero and both balances are complete, note it and sign off — no reconciling items needed.
3. **Identify reconciling items.** Work the usual categories: timing (outstanding checks, deposits in transit, unposted receipts), errors, omissions, and one-sided items.
4. **Quantify and categorize each item.** Capture amount, direction (which side it adjusts), category, and root cause.
5. **Prove the tie-out.** Adjusted GL (GL ± its items) must equal adjusted source (source ± its items); show the bridge. Decision point: if the bridge doesn't tie, you are missing an item — do not sign off on a residual you can't name.
6. **Resolve.** Propose the correcting entry or action for each item that needs one; flag aged or unexplained items.
7. **Sign off.** State reconciled / not reconciled with any residual unexplained amount.

## Example
Cash account 1000 vs bank statement, 3/31. GL $84,200; bank $86,050; raw diff −$1,850. Items: (a) two outstanding checks −$2,300 (reduce bank), (b) deposit in transit +$500 (add to bank), (c) unrecorded bank fee −$50 (reduce GL). Bridge: adjusted bank = 86,050 − 2,300 + 500 = $84,250; adjusted GL = 84,200 − 50 = $84,150... off by $100 → missing item found: a $100 unposted customer receipt. Corrected, both sides = $84,250. Correcting entry: book fee and receipt to GL. Reconciled, $0 residual.

## Pitfalls
- **Signing off with an unexplained residual.** "Reconciled except $100" is not reconciled — an unnamed gap is a potential error or fraud.
- **Reconciling to an incomplete source.** A bank statement missing the last day understates cash; confirm the source covers the full period.
- **Miscoding item direction.** Adding an outstanding check instead of subtracting flips the bridge and hides the real difference.
- **Letting items age silently.** A reconciling item outstanding three months is usually an error you never booked, not timing.

## Output format
```
Account: <GL#> | Source: <...> | As-of: <date>
Balances: GL <...> | source <...> | raw diff <...>
Reconciling items:
  | item | amount | side (GL/source ±) | category | root cause | action |
Bridge: adjusted GL <...> = adjusted source <...>  [pass/fail]
Correcting entries proposed: <...>
Aged / unexplained flags: <...>
Conclusion: reconciled / not | residual: <$> | sign-off: <who/date>
```
