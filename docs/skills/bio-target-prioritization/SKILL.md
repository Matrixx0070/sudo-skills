---
name: bio-target-prioritization
version: 1.0.0
description: Rank candidate drug targets by genetic evidence, tractability, safety, and novelty into a transparent, weighted, sensitivity-tested shortlist.
author: matrixx0070
tags: [drug-discovery, target-id, tractability, genetics, prioritization, scoring]
capabilities: []
---

## When to use

Use this when the user has a set of candidate genes or proteins for a disease and needs a transparent, weighted ranking to decide which to pursue. Apply before committing screening or chemistry resources.

**Not for:** summarizing the evidence base for one gene (use bio-literature-review), deciding whether a whole program is worth starting (use bio-problem-selection), or designing the validation assay itself (use bio-experiment-design).

## Method

1. Assemble the candidate set and fix the disease context: indication, mechanism hypothesis, patient population.
2. Score each target across weighted dimensions:
   - Genetic/causal evidence — GWAS, Mendelian, Open Targets association, direction of effect.
   - Biological rationale — pathway centrality, tissue expression (GTEx/HPA), model validation.
   - Tractability — small-molecule pockets, antibody accessibility (surface/secreted), existing chemical matter, structures.
   - Safety liabilities — essentiality (DepMap), broad expression, known on-target tox, knockout phenotypes.
   - Novelty & competition — patent/clinical landscape, precedented vs first-in-class.
3. Normalize each dimension to 0–1. Apply explicit, user-tunable weights and show the arithmetic.
4. **Decision:** run a sensitivity check. If the ranking flips under a plausible ±20% weight change, report it as unstable rather than as a firm order.
5. **Decision:** flag any target that ranks only via a single dimension; a lone high genetics score with zero tractability is a research target, not a drug target.
6. Recommend a top tier with go/no-go rationale and the single biggest de-risking experiment per target.

## Example

Five candidates for a fibrosis program. Target A scores genetics 0.9 but tractability 0.1 (intrinsically disordered, no pocket) — flagged single-dimension, demoted to tool-compound track. Target C scores 0.6/0.7/0.8/0.7/0.5; weighted total 0.66 tops the list and survives the sensitivity sweep. The de-risking experiment for C: a knockdown in primary lung fibroblasts measuring collagen deposition.

## Pitfalls

- Hiding the weights so the ranking looks objective when it encodes your priors.
- Scoring novelty as "high" without actually checking the clinical/patent landscape.
- Ignoring DepMap essentiality — a pan-essential gene is a toxicity trap.
- Reporting a single ordered list with no sensitivity note, implying false precision.

## Output format

```
# Target Prioritization — <Indication>
Weights: genetics=_, biology=_, tractability=_, safety=_, novelty=_

## Scoring table
| Target | Genetics | Biology | Tractability | Safety | Novelty | Weighted |

## Ranked shortlist
1. <Target> — <two-line rationale> | de-risking exp: <one line>

## Risk flags & missing data
- <target>: <single-dimension flag / key gap>

Sensitivity: <stable | flips under weight change X>
```
Cite sources; mark low-confidence scores UNVERIFIED.
