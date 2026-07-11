---
name: bio-target-prioritization
version: 1.0.0
description: Rank candidate drug targets by genetic evidence, tractability, safety, and novelty into a scored shortlist.
author: matrixx0070
tags: [drug-discovery, target-id, tractability, genetics, prioritization]
capabilities: []
---

When to use: the user has a list of candidate genes or proteins for a disease and needs a transparent, weighted ranking to decide which to pursue. Use before committing screening or chemistry resources.

METHOD
1. Assemble the candidate set and the disease context (indication, mechanism hypothesis, patient population).
2. Score each target across weighted dimensions:
   - Genetic/causal evidence: GWAS, Mendelian, Open Targets association, direction of effect.
   - Biological rationale: pathway centrality, expression in relevant tissue (GTEx/HPA), model-system validation.
   - Tractability: small-molecule pockets, antibody accessibility (surface/secreted), existing chemical matter, structural data.
   - Safety liabilities: essentiality (DepMap), broad expression, known on-target toxicity, knockout phenotypes.
   - Novelty & competition: patent/clinical landscape, precedented vs first-in-class.
3. Normalize each dimension to a 0-1 scale; apply explicit weights the user can tune. Show the arithmetic.
4. Run a sensitivity check: does the ranking survive reasonable weight changes? Flag targets that only rank via one dimension.
5. Recommend a top tier with go/no-go rationale and the single biggest de-risking experiment for each.

OUTPUT FORMAT
- Scoring table: Target | Genetics | Biology | Tractability | Safety | Novelty | Weighted score.
- Ranked shortlist with a two-line rationale per target.
- Risk flags and the key missing data per target.
- Stated weights and sensitivity note. Cite sources; mark low-confidence scores UNVERIFIED.
