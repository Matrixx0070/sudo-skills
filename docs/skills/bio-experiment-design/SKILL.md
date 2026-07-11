---
name: bio-experiment-design
version: 1.0.0
description: Design a rigorous preclinical experiment with hypothesis, controls, power analysis, and pre-registered readouts.
author: matrixx0070
tags: [experiment-design, preclinical, statistics, power, controls]
capabilities: []
---

When to use: the user is planning a wet-lab or in vivo study and needs a statistically sound, reproducible design before spending reagents or animals. Use this to prevent underpowered, confounded, or unblinded experiments.

METHOD
1. State one falsifiable hypothesis and the primary readout that would confirm or refute it. Separate primary from exploratory endpoints.
2. Define the experimental system: model, genotype/strain, passage, age/sex, and the perturbation with dose and timing.
3. Specify controls: negative (vehicle/scramble), positive (known effector), and technical (batch, isotype). Address every plausible confounder.
4. Power the study: state expected effect size and variance (from pilot or literature), choose alpha and power (typically 0.05 / 0.80), and compute n per group. Show the calculation and the test that will be used.
5. Build in rigor: randomization scheme, blinding of treatment and analysis, and pre-specified inclusion/exclusion criteria.
6. Plan analysis before data collection: the statistical test, multiple-comparison correction, and how outliers are handled.

OUTPUT FORMAT
- Hypothesis and primary readout (one sentence each).
- Design table: Group | Perturbation | n | Control role.
- Power analysis: effect size, alpha, power, test, resulting n, and assumptions.
- Rigor checklist: randomization, blinding, replicates (biological vs technical), stopping rules.
- Pre-registered analysis plan and known limitations. If effect size is a guess, label it UNVERIFIED.
