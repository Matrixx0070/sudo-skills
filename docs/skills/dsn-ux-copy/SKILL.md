---
name: dsn-ux-copy
version: 1.0.0
description: Write and review interface microcopy - errors, empty states, buttons, labels, and CTAs - that is clear, concise, human, and consistent with the product's voice.
author: matrixx0070
tags: [design, ux-writing, microcopy, content, cta]
capabilities: []
---

# UX Copy

## When to use
Reach for this when a screen needs its words - button labels, error messages, empty states, tooltips, confirmations, CTAs - or when existing copy is confusing, robotic, or blames the user. Works for drafting from scratch or reviewing what exists.

## Method
1. **Locate the moment.** Name where the user is, what they just did, what they need next, and how they likely feel. Copy serves that moment, not the system's internals.
2. **Lead with the user's goal.** Say what to do or what happened in plain language. Cut hedges, jargon, and filler; front-load the important word.
3. **Errors: cause + fix, never blame.** Explain what went wrong and how to resolve it. Ban "invalid input" and "an error occurred"; name the fix instead.
4. **Empty states earn their space.** Explain what belongs here and give one clear next action - never a blank void.
5. **CTAs describe the outcome.** Prefer "Send invite" over "Submit"; make the verb match what happens.
6. **Voice and consistency.** Match the product's tone; use one term per concept everywhere; keep tense, capitalization, and punctuation uniform.
7. **Check length** against real layouts and edge cases.

## Output format
```
# UX Copy: <surface>
**Context:** where / what just happened / what's next
**Copy:** element — recommended text (+ character count if constrained)
**Errors:** condition — message (cause + fix)
**Rationale:** why this wording, voice notes
**Rejected alternatives:** option — why not
```
Every string is testable against clarity, brevity, and voice; flag anything that needs product truth to confirm.
