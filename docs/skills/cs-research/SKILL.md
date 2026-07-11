---
name: cs-research
version: 1.0.0
description: Research a customer question across product docs, past tickets, and release notes, answering with clear source attribution.
author: matrixx0070
tags: [customer-support, research, knowledge-base, attribution, accuracy]
capabilities: []
---

When to use: a customer asks something you cannot answer from memory — behavior of a feature, whether a limit exists, if a bug is known, or what changed in a release. Use this to build a correct, cited answer instead of guessing.

METHOD
1. Restate the question precisely, including the customer's plan, version, and platform. A "does X work" answer often depends on these — pin them before searching.
2. Search authoritative sources in order: official docs and help center, changelog/release notes, engineering tickets and known-issue lists, then prior resolved support tickets. Prefer newest and most authoritative.
3. Cross-check every claim against at least two sources where possible. If sources conflict, note the conflict and favor the one closest to current product state (dated release notes over old docs).
4. Distinguish documented behavior from observed/anecdotal behavior. Label each finding with its source and date.
5. Flag gaps honestly: if no source confirms it, say "unconfirmed — needs eng verification" rather than inferring.
6. Draft the answer for the customer's level, then attach the internal source trail so a teammate can verify.

OUTPUT FORMAT
- Question (restated with context)
- Answer (concise, customer-ready)
- Confidence: High / Medium / Low
- Sources: each claim → `source (title, date/link)`
- Conflicts or gaps (if any)
- Recommended next step if unconfirmed
