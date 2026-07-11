---
name: dsn-design-system
version: 1.0.0
description: Audit, document, or extend a design system - inventory components and tokens, surface inconsistency and drift, and specify new additions that fit the existing architecture.
author: matrixx0070
tags: [design, design-system, tokens, components, documentation]
capabilities: []
---

# Design System Work

## When to use
Reach for this when a product has drifted into one-off styles, when onboarding needs the system documented, or when a new component must be added without fragmenting what exists. Handles three modes: audit, document, extend.

## Method
1. **Inventory.** Enumerate tokens (color, type, spacing, radius, elevation, motion), primitives, and composed components. Record each component's variants, props, and states.
2. **Find drift (audit mode).** Group visually near-identical elements that use different values - the 6 shades of "gray", the 9 button paddings. Each cluster is a consolidation candidate. Flag components used off-spec and tokens defined but unused.
3. **Assess coverage.** Identify UI needs the system does not yet serve, and where teams route around it with custom CSS.
4. **Document (document mode).** For each component write purpose, when to use vs. not, anatomy, variants, states, tokens consumed, accessibility notes, and do/don't examples.
5. **Extend (extend mode).** Before adding anything, prove no existing component covers the need. Specify the new component from existing tokens and primitives, define its API, and name what it deprecates.
6. **Prioritize** changes by blast radius and reuse.

## Output format
```
# Design System: <audit | doc | extension> — <scope>
**Inventory:** tokens: N | components: N
**Drift / consolidation:** cluster — values found — proposed single source
**Gaps:** need — current workaround — proposal
**Component spec:** name — purpose — variants — states — tokens — a11y — do/don't
**Migration:** what changes — who is affected
```
Prefer consolidating onto existing patterns over inventing new ones.
