---
name: es-search-strategy
version: 1.0.0
description: Decompose a natural-language question into per-source searches, rank the plan, and resolve ambiguity before querying.
author: matrixx0070
tags: [enterprise-search, query-planning, decomposition, ranking, ambiguity]
capabilities: []
---

# Enterprise Search Strategy

## When to use
Use this before a broad or fuzzy search, when a single query string would miss the answer — the question bundles several sub-questions, spans multiple source types, or is ambiguous about who/when/where. This plans the search; es-search executes it.

## METHOD
1. **Restate the ask.** Write the question in one precise sentence. If a word is ambiguous (a name, a project codename, "the doc"), list the readings.
2. **Resolve ambiguity first.** Pick the most probable reading and label it an assumption; only ask the user back when the readings would send you to entirely different sources.
3. **Decompose.** Split into atomic sub-questions, each answerable from one artifact type.
4. **Map to sources.** For each sub-question, name the best source and the reason. Chat for decisions/discussion, email for external threads, storage for finished docs, trackers for status/ownership.
5. **Craft per-source queries.** Write the actual query string or filters for each — keyword operators for structured sources, natural phrasing for semantic ones. Set a time window per query.
6. **Rank the plan.** Order sub-queries by likelihood of carrying the answer so the highest-yield searches run first and can short-circuit the rest.

## OUTPUT FORMAT
- **Interpreted question:** one line + any assumptions taken.
- **Sub-questions:** numbered, each atomic.
- **Search plan:** table of sub-question → source → query/filters → why.
- **Priority order:** ranked list with a one-line rationale for the top pick.
- **Open ambiguities:** anything that needs the user only if it changes the sources.
