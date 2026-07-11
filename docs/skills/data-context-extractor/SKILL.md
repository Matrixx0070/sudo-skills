---
name: data-context-extractor
version: 1.0.0
description: Bootstrap a company-specific data skill by extracting an analyst's tribal knowledge into a reusable reference.
author: matrixx0070
tags: [onboarding, metadata, tribal-knowledge, documentation, semantics]
capabilities: []
---

# data-context-extractor

When to use: you are working with a new company's data warehouse and generic SQL keeps producing plausible-but-wrong answers because the real definitions live in analysts' heads. Use this to capture that tribal knowledge once and turn it into a durable, reusable context file other skills can consult.

## METHOD

1. **Inventory the landscape.** List the core tables, their grain, freshness/refresh cadence, and which are canonical vs deprecated. Flag the "do not use" tables that look tempting.
2. **Extract metric definitions.** For each key metric (revenue, active user, churn), capture the exact business definition, the source column(s), the filters applied, and the gotchas (refunds excluded? test accounts filtered? which timezone?).
3. **Map the join graph.** Record the correct keys between core tables and where fan-out risk lives. Note keys that look joinable but are not.
4. **Capture conventions.** Fiscal vs calendar periods, standard segment definitions, status-code meanings, and the enum/category vocabulary.
5. **Record known traps.** Duplicate-prone tables, late-arriving data, backfilled history, and columns whose meaning changed on a known date.
6. **Interview by proxy.** When facts are missing, list the exact questions to ask an analyst rather than guessing.

## OUTPUT FORMAT

Write a structured reference (Markdown) with these sections:

- **Tables** — name, grain, freshness, canonical/deprecated.
- **Metrics** — definition, source, filters, gotchas, verified example.
- **Joins** — key pairs, fan-out warnings.
- **Conventions** — calendars, segments, status codes, enums.
- **Traps** — dated caveats and data-quality landmines.
- **Open questions** — what still needs an analyst's confirmation.

Mark every entry as verified or assumed. This file is only trustworthy if its confidence is honest — never present an assumed definition as confirmed.
