---
name: fin-reconciliation
version: 1.0.0
description: Reconcile GL balances to subledgers, bank statements, or third-party records and clear differences.
author: matrixx0070
tags: [finance, reconciliation, accounting, gl, bank-rec]
---

# Reconciliation

## When to use
Use this to reconcile a general-ledger account to a supporting source — bank statement, subledger (AR/AP), or a third-party report — to explain a difference, or to produce a signed reconciliation for the close.

## METHOD
1. **Define the reconciliation.** Name the GL account, the supporting source, the as-of date, and both starting balances.
2. **Compute the raw difference.** Subtract source from GL; if zero, note it and sign off.
3. **Identify reconciling items.** Work the usual categories: timing differences (outstanding checks, deposits in transit, unposted receipts), errors, omissions, and items recorded on only one side.
4. **Quantify and categorize each item.** For every reconciling item, capture amount, direction, category, and root cause.
5. **Prove the tie-out.** Adjusted GL (GL ± its items) must equal adjusted source (source ± its items); show the bridge.
6. **Resolve.** Propose the correcting journal entry or action for each item that requires one; flag aged or unexplained items.
7. **Sign off.** State reconciled / not reconciled with any residual unexplained amount.

## OUTPUT FORMAT
- **Account / source / as-of date.**
- **Balances:** GL, source, raw difference.
- **Reconciling-items table:** item, amount, side, category, root cause, action.
- **Bridge:** adjusted GL = adjusted source (shown, pass/fail).
- **Correcting entries proposed.**
- **Aged / unexplained items flagged.**
- **Conclusion and sign-off.**
