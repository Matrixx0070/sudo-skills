---
name: eng-code-review
version: 1.0.0
description: Review a diff or pull request for correctness, security, and performance with specific, actionable, severity-ranked findings.
author: matrixx0070
tags: [code-review, security, performance, correctness, quality]
capabilities: []
---

When to use: any time you are handed a diff, PR, or patch to assess before merge. Review the change, not the whole codebase, but read enough surrounding context to judge impact.

METHOD
1. Understand intent first. Read the description and the diff; restate what the change is supposed to do. If intent is unclear, that is your first finding.
2. Correctness: trace edge cases — empty/null inputs, off-by-one, timezone/locale, concurrency and race conditions, error paths, partial failure, idempotency.
3. Security: check for injection (SQL/command/template), missing authz checks, unvalidated input, secrets in code, unsafe deserialization, SSRF, and leaky error messages.
4. Performance: hunt N+1 queries, unbounded loops/allocations, missing indexes, synchronous work in hot paths, and chatty network calls.
5. Design & maintainability: naming, duplication, dead code, test coverage of the new logic, and backward compatibility.
6. Rank each finding Critical / Major / Minor / Nit. Quote the file and line, explain the risk, and propose a concrete fix.

Be direct but not exhaustive-for-its-own-sake — prioritize findings that would cause bugs, breaches, or outages.

OUTPUT FORMAT
- Summary (1-2 lines: intent + overall verdict)
- Verdict: Approve / Approve-with-nits / Request-changes / Block
- Findings (grouped by severity): `path:line` — issue — why it matters — suggested fix
- Questions for author (if any)
