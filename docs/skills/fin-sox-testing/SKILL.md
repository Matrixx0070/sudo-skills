---
name: fin-sox-testing
version: 1.0.0
description: Execute a SOX control test end to end — document design, prove population completeness, pull a reproducible sample, and conclude on effectiveness.
author: matrixx0070
tags: [finance, sox, controls, testing, workpapers, design-effectiveness]
---

# SOX Testing

## When to use
Use this to run a SOX control test from design through conclusion — document design and implementation (D&I), prove the population, pull a defensible sample, run attributes, and write the workpaper.

**Not for:** the audit-facing re-performance workpaper handoff (fin-audit-support overlaps — use *this* when you own the test design and D&I; use that when supporting an external auditor's re-performance). Not for account tie-outs (fin-reconciliation).

## Method
1. **Document design first.** Record the control objective, the risk it addresses, who performs it, how often, and whether it is manual or automated. Decision point: if the control as designed cannot prevent/detect the risk, stop — report a *design* deficiency; operating tests are moot.
2. **Confirm the population.** Obtain the complete period population, reconcile its count to a system total, and state the source so completeness is provable.
3. **Set sample size.** Frequency minimums: daily ~25, weekly ~5, monthly ~2, quarterly/annual 1–2. Decision point: scale up for higher risk or after any mid-period control change (test both sides of the change).
4. **Select reproducibly.** Random or interval selection; document method and seed so a reviewer re-derives the exact sample.
5. **Define test attributes.** List the specific checks per item (approval present, amount matches, timely, authorized signer) *before* touching a sample.
6. **Execute and log.** For each item record evidence inspected and pass/fail per attribute.
7. **Assess and conclude.** Classify any deviation (deficiency / significant deficiency / material weakness) and state operating effectiveness.

## Example
Control PO-03: all POs over $10k approved by a manager before issue. Design: preventive, addresses unauthorized commitments — adequate. Population: 640 POs, tied to the procurement system PO register total. Monthly-ish volume but daily activity → sample 25, interval selection (every 25th, seed logged). Attributes: (a) approval present, (b) approver in authority matrix, (c) approved before PO date. Result: 24 pass; item 19 approved *after* issue date — timing deviation, control deficiency, isolated (1/25), remediation: system block on unapproved issue. Conclusion: operating effectively with one deficiency noted.

## Pitfalls
- **Skipping design assessment.** A well-executed test of a badly designed control proves nothing — D&I comes first.
- **Population you can't tie to a system total.** Without a completeness tie-out the sample is unfounded.
- **Defining attributes after seeing the sample.** That invites cherry-picked criteria — lock attributes before selection.
- **Ignoring a mid-period control change.** One sample spanning a change hides which version failed; split it.

## Output format
```
Control: <ID> | Objective: <...> | Owner: <...> | Freq: <...> | Type: manual/auto
Design assessment: adequate / inadequate — <why>
Population: source <...> | count <n> | tied to <system total> [pass/fail]
Sample: size <n> | method <random/interval + seed> | reproducible: yes
Attributes (locked pre-selection): <a, b, c>
Workpaper:
  | item | attr a | attr b | attr c | evidence | result |
Deviations: | count | severity | root cause |
Operating effectiveness: effective / deficient | follow-ups: <...>
```
