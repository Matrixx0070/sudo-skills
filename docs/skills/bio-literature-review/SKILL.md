---
name: bio-literature-review
version: 1.0.0
description: Run a structured life-sciences literature search and synthesize findings into a cited, evidence-graded review.
author: matrixx0070
tags: [biology, literature, pubmed, biorxiv, review]
capabilities: []
---

When to use: the user needs a defensible summary of what is known about a gene, pathway, disease mechanism, modality, or method, and wants traceable citations rather than unsourced prose. Reach for this before target work, grant writing, or experiment design.

METHOD
1. Frame the question in PICO-style terms: population/system, intervention/perturbation, comparator, and outcome. State the time window and species scope.
2. Build a query set: MeSH terms plus free-text synonyms, gene aliases (HGNC), and preprint spellings. Search PubMed/PMC for peer-reviewed work and bioRxiv/medRxiv for preprints; note that preprints are unreviewed.
3. Screen by title/abstract, then full text. Record inclusion/exclusion counts so the search is reproducible.
4. Extract per paper: design, model system, sample size, effect direction/magnitude, and key caveats into an evidence table.
5. Grade each claim: strong (multiple independent in vivo/clinical), moderate (single robust study or consistent in vitro), weak (preprint, correlational, or contested). Flag contradictions explicitly.
6. Synthesize: consensus, open controversies, and gaps that motivate new work.

OUTPUT FORMAT
- One-paragraph executive summary.
- Evidence table: Claim | Evidence grade | Key refs | Caveat.
- Narrative synthesis grouped by sub-question.
- Contradictions & gaps section.
- Numbered reference list with PMIDs/DOIs; mark preprints. Never invent a citation — if a claim is unsupported, say so.
