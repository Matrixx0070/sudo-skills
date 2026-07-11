---
name: legal-vendor-check
version: 1.0.0
description: Reconcile the agreements that should exist for a vendor against what actually does across systems, and produce a gap analysis with a coverage verdict.
author: matrixx0070
tags: [legal, vendor, contracts, gap-analysis, compliance]
capabilities: []
---

## When to use
Use this before onboarding, renewing, or auditing a vendor, or when someone asks "are we covered with this vendor." It reconciles what agreements should exist against what actually does, and surfaces gaps that create legal or compliance exposure.

**Not for:** reviewing the terms inside a specific contract (use `legal-review-contract`), rating a single risk in depth (use `legal-risk-assessment`), or negotiating with the vendor. This is a coverage inventory, not a term-quality review.

## Method
1. **Define the vendor and relationship.** What they provide, data they touch, spend level, criticality.
2. **List agreements that should exist** for this relationship type: master agreement / order form, DPA (if personal data), security addendum, BAA (if applicable), SOW, plus required certifications or insurance. *Decision point:* if they touch personal or regulated data with no DPA/BAA, that's an automatic high-severity gap.
3. **Pull actual status from each system** available (contract repository, procurement, finance, security records). Per document: present? executed? current version? expiry date?
4. **Reconcile.** Match expected vs. found; mark present / missing / expired / superseded / unsigned.
5. **Analyze gaps.** For each missing or expired item, state the exposure (unprotected data, uncapped liability, compliance failure) and severity.
6. **Check dates.** Flag anything expiring within the renewal window and any auto-renewal triggers.
7. **Recommend actions** to close each gap, with owner and deadline.

## Example
Vendor: cloud analytics provider, processes customer PII, $120k/yr, business-critical. Expected: MSA, DPA, security addendum, SOC 2 cert. Found: MSA (executed, current), security addendum (executed), SOC 2 (expired 3 months ago), DPA (missing). Verdict: gaps. Gap analysis: DPA missing → PII processed with no data-protection terms, severity Critical; SOC 2 expired → unverified security posture, severity High. Actions: obtain and execute DPA (owner: privacy, by month-end), request renewed SOC 2 (owner: security, 2 weeks).

## Pitfalls
- **Checking one system.** The DPA may live in procurement while the MSA is in the repository; miss a source, miss a document.
- **Marking "present" without checking executed/current.** An unsigned or superseded draft is not coverage.
- **Ignoring expiry dates.** A current-looking agreement that lapses next month is a pending gap.
- **Missing the data-driven gaps.** No DPA/BAA where personal or health data flows is the exposure that matters most.

## Output format
```
Vendor / service / criticality / data touched:
Coverage verdict: covered | gaps | not covered
Agreement table:
  | Document | Expected | Found | Status | Expiry |
Gap analysis:
  | Item | Exposure | Severity |
Expiring / auto-renew alerts:
Actions to close gaps:
  | Action | Owner | Deadline |
```
