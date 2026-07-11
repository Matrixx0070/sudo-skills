---
name: eng-debug
version: 1.0.0
description: Diagnose and fix a bug through a disciplined reproduce, isolate, diagnose, fix, verify loop driven by evidence rather than guesswork.
author: matrixx0070
tags: [debugging, troubleshooting, root-cause, stack-trace, fix]
capabilities: []
---

When to use: whenever you are given an error, stack trace, failing test, or "it's broken" report. Resist the urge to change code before you understand the failure.

METHOD
1. Reproduce. Establish exact steps, inputs, environment, and version that trigger the bug. A bug you cannot reproduce, you cannot confirm fixed. Note frequency (always / intermittent).
2. Read the evidence. Parse the full stack trace top to bottom; identify the first frame in your own code. Capture the actual error message verbatim — do not paraphrase it away.
3. Isolate. Narrow the surface: bisect commits, comment out branches, add targeted logging, or minimize the input until the smallest failing case remains.
4. Form one hypothesis at a time. State what you believe is wrong and what output would confirm or refute it. Let the observed output win over your expectation.
5. Diagnose root cause, not symptom. Ask why the bad state arose, not just where it surfaced. Distinguish trigger from underlying defect.
6. Fix minimally, then verify by re-running the original repro. Add a regression test that fails before the fix and passes after.

OUTPUT FORMAT
- Symptom (observed behavior + error text)
- Reproduction (exact steps)
- Root Cause (the actual defect, with file/line)
- Fix (what changed and why)
- Verification (repro re-run result + regression test)
- Prevention (guard, test, or invariant to stop recurrence)
