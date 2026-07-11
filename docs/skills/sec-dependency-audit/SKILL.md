---
name: sec-dependency-audit
version: 1.0.0
description: Audit project dependencies for known CVEs and produce a prioritized remediation plan.
author: matrixx0070
tags: [security, dependencies, cve, sca, supply-chain]
capabilities: []
---

## When to use

Use this before a release, during supply-chain reviews, or on a recurring schedule to catch vulnerable and abandoned packages. It is defensive: you identify and remediate known weaknesses in third-party code.

## METHOD

1. **Inventory dependencies.** Collect direct and transitive packages from lockfiles (package-lock, pnpm-lock, poetry.lock, go.sum). Note versions and whether each is direct or transitive.
2. **Run the ecosystem auditor.** Use the native tool (`npm audit`, `pnpm audit`, `pip-audit`, `osv-scanner`) and read the raw output. Cite counts by severity — do not estimate.
3. **Map CVEs.** For each advisory record the CVE/GHSA id, affected package, vulnerable range, fixed version, and CVSS severity. Distinguish reachable vs. transitive-only.
4. **Assess exploitability.** Note whether the vulnerable code path is actually used and whether a fix exists. Flag packages that are unmaintained or have no patch.
5. **Plan remediation.** For each: upgrade to the fixed version, apply an override/resolution for transitive pins, or document a compensating control if no fix exists.
6. **Prevent drift.** Recommend automated dependency updates and CI audit gating.

## OUTPUT FORMAT

- **Scan summary** — tool used, total advisories by severity (cite output).
- **CVE table** — CVE/GHSA | Package | Current | Fixed | Severity | Direct/Transitive | Action.
- **Remediation plan** — ordered by severity then effort.
- **Residual/no-fix items** — with compensating controls.
