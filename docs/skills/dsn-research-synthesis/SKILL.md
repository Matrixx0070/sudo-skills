---
name: dsn-research-synthesis
version: 1.0.0
description: Turn raw user-research data into themes, evidence-backed insights, and prioritized recommendations - without inventing findings the data does not support.
author: matrixx0070
tags: [design, research, synthesis, insights, ux]
capabilities: []
---

# Research Synthesis

## When to use
Reach for this after interviews, usability sessions, surveys, or support-ticket dumps, when you have a pile of observations and need to know what they mean and what to do. Turns scattered notes into decisions the team can act on.

## Method
1. **Collect the raw signal.** Pull discrete observations - quotes, behaviors, errors, workarounds - each tagged with its source participant. Keep them atomic; one observation per note.
2. **Cluster bottom-up.** Group related observations by affinity into themes. Let the groupings emerge from the data; do not force notes into a theme you hoped to find.
3. **Elevate to insights.** For each theme write an insight: what users need or struggle with and why. An insight explains a pattern, it is not a restated observation.
4. **Weight the evidence.** State how many participants and which sources support each insight. Separate strong signals from single anecdotes; label frequency honestly.
5. **Flag contradictions and gaps.** Note where participants disagreed and what questions remain unanswered.
6. **Recommend.** Convert insights into prioritized, actionable recommendations tied to the evidence - never a recommendation the data cannot back.

## Output format
```
# Research Synthesis: <study> (n=<participants>)
**Top findings:** insight — supported by X/N — representative quote
**Themes:** theme — observations behind it
**Contradictions / open questions:** ...
**Recommendations (prioritized):** action — insight it addresses — confidence
```
Every insight cites its evidence; anything speculative is labeled a hypothesis, not a finding.
