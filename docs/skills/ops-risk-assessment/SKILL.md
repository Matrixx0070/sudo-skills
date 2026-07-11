---
name: ops-risk-assessment
version: 1.0.0
description: Identify, assess, and mitigate operational risks in a structured risk register.
author: matrixx0070
tags: [operations, risk, mitigation, register, resilience]
capabilities: []
---

# Risk Assessment

## When to use
Use this to surface what could go wrong in an operation, initiative, or system, and to decide which risks warrant action, ownership, and monitoring before they become incidents.

## METHOD
1. **Define the scope.** State the system, project, or process under assessment and the time horizon.
2. **Identify risks.** Brainstorm across categories: operational, technical, security, financial, people, vendor, compliance, and external. Write each as a cause → event → consequence.
3. **Assess each risk.** Rate likelihood (1-5) and impact (1-5); compute the score (L × I) and place it in a heat map band (low/medium/high/critical).
4. **Choose a response.** For each risk select avoid, mitigate, transfer, or accept, with a rationale.
5. **Define mitigations.** For mitigated risks, specify concrete actions, an owner, a due date, and the residual score after action.
6. **Add detection.** Name the leading indicator or trigger that signals the risk is materializing.
7. **Prioritize.** Sort by inherent score; escalate anything critical.

## OUTPUT FORMAT
- **Scope & horizon.**
- **Risk register table:** ID, risk (cause/event/consequence), category, likelihood, impact, score, response, mitigation, owner, due, residual score, trigger.
- **Heat map:** counts per band.
- **Top risks:** the critical/high items, called out.
- **Monitoring plan:** indicators and review cadence.
