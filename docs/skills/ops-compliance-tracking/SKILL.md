---
name: ops-compliance-tracking
version: 1.0.0
description: Track compliance and audit readiness against SOC 2, ISO 27001, or GDPR.
author: matrixx0070
tags: [operations, compliance, audit, soc2, gdpr]
capabilities: []
---

# Compliance Tracking

## When to use
Use this to assess readiness for an audit or certification (SOC 2, ISO 27001, GDPR), to maintain a living control inventory, or to prioritize remediation before an auditor arrives.

## METHOD
1. **Select the framework and scope.** Name the standard, the trust criteria or annex/articles in scope, and the systems and data covered.
2. **Enumerate controls.** List each required control with its ID, intent, and the owner accountable for it.
3. **Assess status per control.** Mark implemented / partial / missing, and record the evidence that proves it (policy, log, config, ticket).
4. **Identify gaps.** For every partial or missing control, describe the deficiency and its exposure.
5. **Prioritize remediation.** Rank gaps by risk and auditor visibility; assign owner, target date, and effort.
6. **Verify evidence freshness.** Confirm each artifact is current, retrievable, and dated within the audit window.
7. **Compute readiness.** Report % controls satisfied and a go / not-ready verdict for the audit date.

## OUTPUT FORMAT
- **Framework / scope / audit date.**
- **Readiness score:** % satisfied, verdict.
- **Control register table:** ID, control, owner, status, evidence, last verified.
- **Gap list:** control, deficiency, risk, owner, due date.
- **Remediation roadmap:** prioritized, with dates.
- **Evidence gaps:** artifacts missing or stale.
- **Next actions.**
