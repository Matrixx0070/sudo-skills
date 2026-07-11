---
name: do-observability
version: 1.0.0
description: Instrument logs, metrics, and traces, then define SLOs and actionable alerts that page on user pain.
author: matrixx0070
tags: [observability, monitoring, slo, telemetry, alerting]
capabilities: []
---

# do-observability

**When to use:** You need to add or improve instrumentation on a service, define what "healthy" means as SLOs, or replace noisy alerts with ones that page only on real user impact.

**METHOD:**
1. Cover the three pillars: structured logs (JSON, leveled, with correlation IDs), metrics (RED for services — Rate, Errors, Duration; USE for resources — Utilization, Saturation, Errors), and distributed traces across service boundaries.
2. Standardize on OpenTelemetry so instrumentation is vendor-portable; propagate trace context through every hop and attach a request/trace ID to logs.
3. Define SLIs from the user's perspective (successful requests, latency percentiles) and set SLOs with explicit targets and windows; derive an error budget from each SLO.
4. Alert on symptoms, not causes: page on SLO burn rate (fast and slow burn), keep the alert count low, and make every page actionable with a runbook link.
5. Build dashboards that answer "is it the service, its dependencies, or the infra?" and expose golden signals at a glance.
6. Control cost and cardinality: sample traces, bound label dimensions, and set retention deliberately.

**OUTPUT FORMAT:**
- Instrumentation snippets (log schema, metric definitions, trace setup).
- An SLI/SLO table with targets, windows, and error budgets.
- Alert rules with burn-rate thresholds and runbook references.
