---
name: sec-threat-model
version: 1.0.0
description: Build a STRIDE-based threat model and attack-surface map for a feature or system.
author: matrixx0070
tags: [security, threat-modeling, stride, architecture, risk]
capabilities: []
---

## When to use

Use this when you are designing a new feature, reviewing an existing system, or preparing a security sign-off and need a structured view of what could go wrong. It is defensive: you enumerate risks so they can be mitigated, never to build exploits.

## METHOD

1. **Define scope.** Name the system, its trust boundaries, actors (users, admins, services, third parties), and the assets worth protecting (data, credentials, availability).
2. **Draw the data flow.** List entry points, processes, data stores, and external dependencies. Mark every trust boundary a request crosses.
3. **Apply STRIDE per element.** For each component ask: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege. Record concrete, plausible threats only.
4. **Rate risk.** Score each threat by likelihood x impact (High/Medium/Low). Note existing controls.
5. **Propose mitigations.** Map each unaddressed High/Medium threat to a specific control (authn, input validation, encryption, rate limiting, least privilege, logging).
6. **Flag residual risk.** State what remains unmitigated and who must accept it.

## OUTPUT FORMAT

- **Scope & assets** — one paragraph.
- **Trust boundaries** — bullet list.
- **Threat table** — columns: Element | STRIDE category | Threat | Likelihood x Impact | Existing control | Recommended mitigation.
- **Prioritized actions** — Highs first, each with an owner hint.
- **Residual risk** — explicit acceptance items.
