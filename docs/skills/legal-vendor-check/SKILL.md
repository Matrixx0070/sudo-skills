---
name: legal-vendor-check
version: 1.0.0
description: Check the contractual status of a vendor relationship across systems and produce a gap analysis of missing or expiring agreements.
author: matrixx0070
tags: [legal, vendor, contracts, gap-analysis, compliance]
capabilities: []
---

## When to use
Use this before onboarding, renewing, or auditing a vendor, or when someone asks "are we covered with this vendor." It reconciles what agreements should exist against what actually does, and surfaces gaps that create legal or compliance exposure.

## METHOD
1. **Define the vendor and relationship.** What they provide, data they touch, spend level, and criticality.
2. **List the agreements that should exist** for this relationship type: master agreement / order form, DPA (if personal data), security addendum, BAA (if applicable), SOW, and any required certifications or insurance.
3. **Pull actual status from each system** available (contract repository, procurement, finance, security review records). For each document record: present? executed? current version? expiry date.
4. **Reconcile.** Match expected vs. found; mark present / missing / expired / superseded / unsigned.
5. **Analyze gaps.** For each missing or expired item, state the exposure (unprotected data, uncapped liability, compliance failure) and severity.
6. **Check dates.** Flag anything expiring within the renewal window and auto-renewal triggers.
7. **Recommend actions** to close each gap, with owner and deadline.

## OUTPUT FORMAT
- **Vendor / service / criticality / data touched.**
- **Coverage verdict:** covered / gaps / not covered.
- **Agreement table:** document, expected, found, status, expiry.
- **Gap analysis:** item, exposure, severity.
- **Expiring / auto-renew alerts.**
- **Actions to close gaps:** owner, deadline.
