---
name: dsn-handoff
version: 1.0.0
description: Turn a finished design into a developer-ready handoff spec - tokens, every interactive state, responsive breakpoints, and the edge cases mockups never show.
author: matrixx0070
tags: [design, handoff, tokens, states, engineering]
capabilities: []
---

# Developer Handoff

## When to use
Reach for this the moment a design is approved and about to be built, or when engineers keep asking "what happens when...". A good handoff kills the back-and-forth by answering the questions before they are asked.

## Method
1. **Inventory components.** List each component and variant in the design. Map each to an existing design-system component where one exists; flag genuinely new ones.
2. **Tokens, not pixels.** Specify color, type, spacing, radius, elevation, and motion as named tokens (e.g. `color.text.secondary`, `space.4`). Give raw values only where no token exists yet, and call that gap out.
3. **Every state.** For each interactive element document default, hover, focus, active, disabled, loading, error, empty, and selected. A state you skip is a state that ships broken.
4. **Responsive behavior.** Define breakpoints and what reflows, stacks, hides, or truncates at each. State min/max widths and how text wraps.
5. **Edge cases and data.** Longest/shortest text, zero and overflow counts, missing images, slow network, permission-denied, and RTL if supported.
6. **Interaction and validation.** Trigger, transition, timing, and any validation rules with exact copy.

## Output format
```
# Handoff: <feature>
**Components:** <name> → DS: <existing | NEW>
**Tokens:** element — token/value
**States:** element — default / hover / focus / disabled / loading / error / empty
**Breakpoints:** <bp> — behavior
**Edge cases:** condition — expected behavior
**Interactions:** trigger — result — timing
**Open questions for eng:** ...
```
Leave nothing to guesswork; if a value is undecided, say so explicitly.
