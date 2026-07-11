---
name: fin-audit-support
version: 1.0.0
description: Support ICFR audits by scoping a key control, selecting a defensible sample, and producing workpapers an auditor can re-perform unaided.
author: matrixx0070
tags: [finance, audit, sox-404, icfr, internal-controls, workpapers, compliance]
---

# Audit Support

## When to use
Use this when you support an internal or external audit of internal control over financial reporting (ICFR), test a SOX 404 key control, or prepare workpapers an auditor can re-perform without asking you a single question.

**Not for:** initial control *design* documentation (use fin-sox-testing for D&I), account-level tie-outs (fin-reconciliation), or financial-statement preparation (fin-financial-statements). This assumes the control already exists and needs testing evidence.

## Method
1. **Scope the control.** Record control ID, the assertion it addresses (existence, completeness, accuracy, valuation, cutoff), the risk it mitigates, and whether it is preventive or detective.
2. **Pick the testing approach.** Choose inquiry, observation, inspection, or re-performance. Decision point: re-performance is strongest — use it for high-risk controls; inquiry alone is *never* sufficient for a conclusion.
3. **Set sample size by frequency.** Daily ~25, weekly ~5, monthly ~2, quarterly ~2, annual 1. Decision point: if the control is high-risk, was changed mid-period, or relies on an automated step that could have broken, increase the sample and split it before/after the change.
4. **Select the sample.** Use random or systematic (interval) selection from the *full* population. Document population source, total count, and method so it is reproducible.
5. **Execute.** For each item capture the attribute tested, the evidence inspected, and pass/fail with a specific reason.
6. **Evaluate exceptions.** Decision point: classify each as deficiency, significant deficiency, or material weakness, and judge isolated vs systemic — one exception in a control-change window is systemic, not isolated.
7. **Conclude.** State operating effectiveness and note any compensating controls.

## Example
Control APR-07: two-signature approval on wires over $50k, preventive, addresses *authorization*. It fires ~daily, so you pull 25 of 312 wires by interval selection (every 12th, seed documented). Attributes: (a) both signatures present, (b) signer within authority matrix, (c) approval dated before release. Item 14 shows one signature only — a control deficiency. It is isolated (1/25), no dollar impact (wire was valid), compensating detective bank-recon caught nothing amiss. Conclusion: operating effectively with one noted deficiency, remediation logged.

## Pitfalls
- **Sampling from an incomplete population.** If you cannot tie the population to a system total, your sample proves nothing — completeness first.
- **Treating inquiry as evidence.** "They told me they check it" is not a test result. Inspect artifacts.
- **Auto-classifying one exception as isolated.** Frequency and root cause decide severity, not the count.
- **Non-reproducible selection.** No seed, no interval, no source = the auditor re-derives a different sample and rejects yours.

## Output format
```
Control: <ID> | Assertion: <...> | Risk: <...> | Type: prev/det | Freq: <...>
Approach: <inquiry/obs/insp/re-perf> — rationale: <...>
Population: source <...> | total <n> | tied to <system total>
Sample: size <n> | method <random/interval, seed> | reproducible: yes
Test of detail:
  | item | attribute | evidence | result | note |
Exceptions: | desc | severity | isolated/systemic | root cause |
Conclusion: effective / deficient | compensating controls: <...>
Open items: <...>
```
