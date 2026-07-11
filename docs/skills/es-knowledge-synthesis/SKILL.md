---
name: es-knowledge-synthesis
version: 1.0.0
description: Merge results from multiple sources into one deduplicated answer with per-claim attribution and a confidence rating.
author: matrixx0070
tags: [enterprise-search, synthesis, attribution, deduplication, confidence]
capabilities: []
---

# Enterprise Search Knowledge Synthesis

## When to use
Use this after a cross-source search returns overlapping, partial, or conflicting hits and the user needs an answer — not a link dump. It turns scattered snippets from chat, email, storage, and trackers into a single sourced narrative.

## METHOD
1. **Cluster by claim.** Group hits around the distinct facts they assert, not by which source they came from.
2. **Deduplicate.** Collapse restatements of the same fact into one claim; keep every distinct source pointer so nothing loses its provenance.
3. **Reconcile conflicts.** When sources disagree, prefer the most recent and most authoritative, and surface the disagreement explicitly rather than silently picking one.
4. **Attribute each claim.** Tie every statement in the answer to its source(s): who, where, when. No unsourced assertion enters the answer.
5. **Rate confidence.** Per claim, mark High (multiple independent recent sources agree), Medium (single credible source), or Low (stale, indirect, or contested).
6. **Fill or flag gaps.** State what the sources do not cover instead of interpolating; suggest where the missing piece likely lives.

## OUTPUT FORMAT
- **Answer:** 2-5 sentences synthesizing the settled facts.
- **Supporting claims:** bullets, each `claim — [source, author, date] — confidence`.
- **Conflicts:** any disagreements with both sides and which was preferred and why.
- **Confidence overall:** one line with the driver.
- **Gaps / next lookups:** what's unknown and where to check.
