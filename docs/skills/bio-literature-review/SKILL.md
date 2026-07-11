---
name: bio-literature-review
version: 1.0.0
description: Run a structured life-sciences literature search and synthesize findings into a cited, evidence-graded review.
author: matrixx0070
tags: [biology, literature, pubmed, biorxiv, review, evidence-grading]
capabilities: []
---

## When to use

Use this when the user needs a defensible summary of what is known about a gene, pathway, disease mechanism, modality, or method, with traceable citations rather than unsourced prose. Reach for it before target work, grant writing, or experiment design.

**Not for:** ranking drug targets (use bio-target-prioritization), choosing what to work on (use bio-problem-selection), or answering a single factual lookup where one authoritative reference already settles it.

## Method

1. Frame the question in PICO terms: population/system, intervention/perturbation, comparator, outcome. State species scope and time window.
2. Build a query set: MeSH terms, free-text synonyms, HGNC gene aliases, and preprint spellings. **Decision:** if aliases are ambiguous (e.g. a symbol reused across species), split into separate queries rather than OR-ing them.
3. Search PubMed/PMC for peer-reviewed work and bioRxiv/medRxiv for preprints. Tag preprints as unreviewed at capture time.
4. Screen by title/abstract, then full text. Record inclusion/exclusion counts so the search is reproducible.
5. Extract per paper into an evidence table: design, model system, sample size, effect direction/magnitude, key caveats.
6. Grade each claim. **Decision:** strong = multiple independent in vivo/clinical; moderate = single robust study or consistent in vitro; weak = preprint, correlational, or contested. If two strong papers disagree, log a contradiction — do not average them away.
7. Synthesize: consensus, open controversies, and gaps that motivate new work.

## Example

Question: "Does TREM2 loss-of-function increase Alzheimer's risk?" You query `TREM2 AND (Alzheimer OR "amyloid") AND (variant OR knockout)`, screen 60 hits to 14, and build the table. Human genetics (R47H GWAS/Mendelian, multiple cohorts) grades **strong**; mouse amyloid-clearance studies grade **moderate** and split on direction depending on disease stage. Output flags the stage-dependence as an open controversy rather than a settled effect.

## Pitfalls

- Citing an abstract you never opened — confabulated PMIDs are the top failure. Verify every identifier resolves.
- Treating a preprint as equivalent to peer-reviewed evidence.
- Missing papers because you searched the current gene symbol only and skipped historical aliases.
- Burying a contradiction inside "studies suggest" instead of naming both sides.

## Output format

```
# <Question> — Evidence Review
Executive summary: <one paragraph>

## Evidence table
| Claim | Grade (strong/mod/weak) | Key refs (PMID/DOI) | Caveat |

## Synthesis (by sub-question)
- <consensus / controversy per group>

## Contradictions & gaps
- <conflicting findings, missing studies>

## References
1. Author, Year. Title. PMID/DOI. [preprint if applicable]
```
Never invent a citation. If a claim is unsupported, say so and mark it UNVERIFIED.
