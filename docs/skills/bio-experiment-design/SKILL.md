---
name: bio-experiment-design
version: 1.0.0
description: Design a rigorous preclinical experiment with a falsifiable hypothesis, controls, power analysis, and a pre-registered analysis plan.
author: matrixx0070
tags: [experiment-design, preclinical, statistics, power, controls, pre-registration]
capabilities: []
---

## When to use

Use this when the user is planning a wet-lab or in vivo study and needs a statistically sound, reproducible design before spending reagents or animals. It exists to prevent underpowered, confounded, or unblinded experiments.

**Not for:** analyzing data you already collected, choosing which target to test (use bio-target-prioritization), or running a computational pipeline (use bio-pipeline-runner).

## Method

1. State one falsifiable hypothesis and the primary readout that confirms or refutes it. Separate primary from exploratory endpoints — you power on the primary only.
2. Define the system: model, genotype/strain, passage, age/sex, and the perturbation with dose and timing.
3. Specify controls: negative (vehicle/scramble), positive (known effector), technical (batch, isotype). Address every plausible confounder.
4. Power the study: state expected effect size and variance from pilot or literature, choose alpha and power (typically 0.05 / 0.80), compute n per group, and name the test. **Decision:** if no pilot effect size exists, run a small pilot or state the minimum detectable effect at feasible n — do not invent a number.
5. Build in rigor: randomization scheme, blinding of treatment and analysis, pre-specified inclusion/exclusion.
6. **Decision:** pre-register the analysis before collecting data — the test, multiple-comparison correction, and outlier rule. If you change it later, that becomes exploratory, not confirmatory.

## Example

Hypothesis: "Compound X reduces tumor volume vs vehicle at day 21." Pilot gives effect size d≈0.9, SD known. Power at 0.05/0.80 → n=11 per group; round to 12 for attrition. Groups: vehicle (negative), X, and paclitaxel (positive control). Mice randomized by cage, tumor measurement blinded to arm, animals below engraftment threshold excluded pre-treatment. Primary test: Mann–Whitney on day-21 volume; exploratory time-course reported without inference.

## Pitfalls

- Powering on a wished-for effect size instead of a measured one — the commonest source of underpowered studies.
- Omitting a positive control, so a null result can't distinguish "no effect" from "assay didn't work."
- Deciding the statistical test after seeing the data (HARKing / p-hacking).
- Confusing technical replicates with biological replicates when counting n.

## Output format

```
# Experiment Design — <title>
Hypothesis: <one sentence, falsifiable>
Primary readout: <one sentence>

## Design table
| Group | Perturbation | n | Control role |

## Power analysis
effect size=_, alpha=_, power=_, test=_, n/group=_, assumptions=_

## Rigor checklist
randomization / blinding / bio vs tech replicates / stopping rules

## Pre-registered analysis plan
test, correction, outlier handling, limitations
```
If effect size is a guess, label it UNVERIFIED.
