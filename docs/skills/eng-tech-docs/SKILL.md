---
name: eng-tech-docs
version: 1.0.0
description: Write or maintain technical documentation — READMEs, runbooks, API references, and architecture docs — that readers can actually act on.
author: matrixx0070
tags: [documentation, readme, runbook, api-docs, technical-writing]
capabilities: []
---

When to use: creating or updating any doc humans rely on to run, integrate with, or understand a system. Good docs answer a reader's next question before they ask it.

METHOD
1. Identify the reader and their goal: a new contributor getting set up, an on-call engineer mid-incident, or an integrator calling your API. Write for that one job.
2. Lead with the outcome. Put the "what this is and why you'd use it" in the first three lines. Bury nothing important below the fold.
3. Make it runnable. Every setup or usage step must be copy-pasteable and verified against a clean environment — no implied prerequisites.
4. Match the form to the type:
   - README: purpose, quickstart, config, common tasks, troubleshooting, links.
   - Runbook: alert/symptom, diagnosis steps, remediation commands, escalation, rollback.
   - API doc: endpoint, params, auth, request/response examples, error codes, rate limits.
   - Architecture: context diagram, components, data flow, key decisions (link ADRs).
5. Show real examples with real (sanitized) values, not `<placeholder>` soup.
6. State what's out of scope and add a "last verified" date. Docs that lie are worse than none.

OUTPUT FORMAT
- Doc type and intended reader
- The document itself in Markdown, with clear headings
- Runnable examples with expected output
- Troubleshooting / FAQ section where relevant
- "Last verified" note and links to related docs
