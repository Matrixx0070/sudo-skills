---
name: pros-cons
version: 1.0.0
description: Structure a decision into weighted pros and cons with a recommendation - steelmanning both sides and separating reversible from irreversible consequences.
triggers:
  - pros and cons
  - help me decide
  - weigh this decision
  - should I
  - tradeoffs of
capabilities: []
inputs:
  - name: decision
    required: true
    description: The decision or options being weighed.
  - name: context
    required: false
    description: Constraints that matter (budget, deadline, risk tolerance, who is affected).
---

# Pros / Cons

## Purpose
Turn "should I...?" into a decision the person can defend: both sides argued properly, consequences sized, and a recommendation they are free to reject.

## Hard rules
1. **Steelman both sides.** The strongest argument FOR and the strongest argument AGAINST must both appear, stated as their best advocate would put them - not a strawman padded with filler points.
2. **Size the consequences.** Mark each point high/medium/low impact. Ten trivial pros do not beat one high-impact con; never present counts as the verdict.
3. **Flag irreversibility.** Any consequence that cannot be undone (data loss, burned relationship, signed contract, public statement) gets an explicit "one-way door" marker and extra weight.
4. **Surface the missing fact.** If one unknown would settle the decision, name it before recommending - sometimes the right answer is "find X out first".
5. **Recommend, do not hedge.** End with a clear recommendation and its single biggest risk. "It depends" without saying on WHAT is banned.

## Workflow
1. Restate the decision in one sentence, including the do-nothing option if it exists.
2. List pros and cons, each tagged (high/med/low) and marked ⛔ if a one-way door.
3. Note the decisive unknown, if any.
4. Recommendation: one option, why in two lines, biggest risk in one.

## Output format
```
**Decision:** ...

**For** ...
**Against** ...

**Decisive unknown:** <or "none">
**Recommendation:** <option> — <why>. Biggest risk: <one line>.
```

## Example
**Input:** "should we rewrite the billing service in Go or keep patching the Node one"

**Output (abridged):**
**Decision:** Rewrite billing in Go now, or keep patching Node (do-nothing is viable).

**For rewrite:** (high) chronic memory leaks have caused 3 billing incidents this quarter; (med) team already runs 4 Go services.
**Against:** (high, ⛔) 2-3 months where bugs land in TWO codebases during migration; (med) the leak might be fixable in days if profiled properly - nobody has actually tried.

**Decisive unknown:** whether the leak is fixable cheaply - one profiling day answers it.
**Recommendation:** Spend 2 days profiling before deciding. Biggest risk: the leak looks fixable, gets patched, and the underlying architecture debt resurfaces in 6 months.
