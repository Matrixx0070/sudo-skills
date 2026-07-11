---
name: es-search
version: 1.0.0
description: Search across every connected source in a single query and return one ranked, attributed result set.
author: matrixx0070
tags: [enterprise-search, search, retrieval, federated, cross-source]
capabilities: []
---

# Enterprise Search

## When to use
Use this when someone asks "where is..." or "what did we say about..." and the answer could live in any connected source — chat, email, cloud storage, or issue trackers. One question, one fan-out, one answer, instead of the user hopping tools.

## METHOD
1. **Read the intent.** Extract the core entities, the likely artifact type (message, file, thread, ticket), and any time or person constraints stated or implied.
2. **Enumerate sources.** List which connected sources are live. Skip sources that structurally cannot hold the answer, and say so.
3. **Fan out.** Issue one tailored query per relevant source in parallel — keyword for storage/trackers, semantic phrasing for chat/email. Widen or tighten terms per source rather than reusing one string.
4. **Normalize hits.** Collapse each result to a common shape: title, source, author, timestamp, snippet, link.
5. **Rank globally.** Score by term match, recency, authority of source/author, and how directly the snippet answers the question — not by which source replied first.
6. **Deduplicate.** Fold the same artifact surfaced by multiple sources into one entry noting where it appears.

## OUTPUT FORMAT
- **Answer line:** one sentence if the results settle it; otherwise "top candidates below."
- **Ranked results:** each as `[source] title — author, date` + snippet + link.
- **Coverage:** which sources were searched, which were skipped and why.
- **Refine:** 2-3 suggested narrowing filters (person, date, source) if the set is large.
