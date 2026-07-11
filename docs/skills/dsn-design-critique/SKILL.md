---
name: dsn-design-critique
version: 1.0.0
description: Give structured, actionable design feedback on a screen or flow - usability, visual hierarchy, and consistency - anchored to goals and heuristics rather than taste.
author: matrixx0070
tags: [design, critique, usability, heuristics, review]
capabilities: []
---

# Design Critique

## When to use
Reach for this when a designer wants feedback before handoff, when a flow "feels off" but no one can say why, or when you need a review that separates real problems from personal preference. Works on a single screen, a full flow, or a component.

## Method
1. **Anchor to intent.** State the user's goal and the primary action for this screen. Every critique judges against that goal, not against your taste.
2. **Hierarchy.** Ask what the eye hits first, second, third. Does that order match importance? Flag competing focal points, weak primary CTAs, and content buried below the fold.
3. **Usability heuristics.** Walk Nielsen's ten: system status, match to real world, user control, consistency, error prevention, recognition over recall, flexibility, minimalist design, error recovery, help. Name the heuristic each issue violates.
4. **Consistency.** Check spacing, type scale, color roles, component variants, and terminology against the rest of the product. Note one-off patterns that should reuse an existing one.
5. **Separate signal from taste.** Mark each item Blocker / Improvement / Nit, and keep opinions labeled as opinions.
6. **Lead with what works** so it survives the next iteration.

## Output format
```
# Critique: <screen> — goal: <user goal>
**What works:** ...
**Blockers (breaks the task):** issue — heuristic — suggested fix
**Improvements:** ...
**Nits (taste, optional):** ...
```
Every finding gets a concrete suggestion, not just a complaint.
