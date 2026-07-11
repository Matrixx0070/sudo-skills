---
name: dsn-accessibility-review
version: 1.0.0
description: Audit a screen, flow, or component against WCAG 2.1 AA - contrast, keyboard operability, target sizes, and screen-reader semantics - and return prioritized, fixable findings.
author: matrixx0070
tags: [design, accessibility, wcag, audit, a11y]
capabilities: []
---

# Accessibility Review

## When to use
Reach for this before shipping any UI, when a design or build needs to clear WCAG 2.1 AA, or when someone reports that a control is unreachable, illegible, or invisible to assistive tech. Works on mockups, live pages, or component specs.

## Method
1. **Scope the surface.** List every interactive element, text block, image, and state (hover, focus, error, disabled, loading). You cannot audit what you have not enumerated.
2. **Contrast.** Check text against its actual background: 4.5:1 for body, 3:1 for large text (>=24px, or >=19px bold) and for UI/graphical boundaries. Report measured ratios, never "looks fine".
3. **Keyboard.** Trace Tab order; confirm every action is reachable and operable without a mouse, focus is always visible, order matches visual flow, and no focus traps exist. Note Esc/Enter/arrow expectations.
4. **Targets and spacing.** Flag touch targets under 44x44px and adjacent targets without gap.
5. **Screen reader semantics.** Verify names, roles, states: alt text, labels tied to inputs, heading hierarchy, landmark regions, aria-live for dynamic content, and error text linked to its field.
6. **Prioritize.** Sort by blocker (locks a user out) > serious > minor.

## Output format
```
# A11y Audit: <surface> (WCAG 2.1 AA)
**Blockers:** <criterion X.X.X> — issue — fix
**Serious:** ...
**Minor:** ...
**Passed:** <what already conforms>
```
Cite the specific success criterion (e.g. 1.4.3 Contrast) and give a concrete, one-line fix per finding.
