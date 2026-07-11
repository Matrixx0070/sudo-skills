---
name: fin-sox-testing
version: 1.0.0
description: Design SOX sample selections, build testing workpapers, and document control assessments.
author: matrixx0070
tags: [finance, sox, controls, testing, workpapers]
---

# SOX Testing

## When to use
Use this to execute a SOX control test end to end — pull a defensible sample, run the test attributes, and write the workpaper — or to assess whether a control is designed and operating effectively.

## METHOD
1. **Document design first.** Record the control objective, the risk it addresses, who performs it, how often, and whether it is manual or automated (D&I: design and implementation).
2. **Confirm the population.** Obtain the complete population for the period, reconcile its count to a system total, and state the source so completeness is provable.
3. **Set sample size.** Use frequency-based minimums (daily ~25, weekly ~5, monthly ~2, quarterly/annual 1-2); scale up for higher risk or after a control change.
4. **Select reproducibly.** Apply random or interval selection; document the method and any seed so a reviewer can re-derive the exact sample.
5. **Define test attributes.** List the specific checks per item (approval present, amount matches, timely, authorized signer) before touching a sample.
6. **Execute and log.** For each item record evidence inspected and pass/fail per attribute.
7. **Assess and conclude.** Classify any deviation (deficiency / significant deficiency / material weakness) and state operating effectiveness.

## OUTPUT FORMAT
- **Control ID / objective / owner / frequency / type.**
- **Design assessment:** adequate / inadequate.
- **Population:** source, count, completeness tie-out.
- **Sample:** size, selection method, reproducibility note.
- **Testing workpaper table:** item, attributes, evidence, result.
- **Deviations:** count, severity, root cause.
- **Operating-effectiveness conclusion and follow-ups.**
