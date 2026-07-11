---
name: do-release-checklist
version: 1.0.0
description: Build a production release checklist covering pre-flight, canary rollout, rollback triggers, and comms.
author: matrixx0070
tags: [release, deployment, canary, rollback, devops]
capabilities: []
---

# do-release-checklist

**When to use:** You are shipping to production and want a repeatable checklist that reduces risk, or you are formalizing an ad-hoc deploy process into canary + rollback + communication steps.

**METHOD:**
1. Pre-flight: confirm CI is green on the exact commit, migrations are backward-compatible, feature flags default safe, config/secrets are in place, and the on-call is aware.
2. Choose a progressive strategy — canary or blue/green — and define the exposure ramp (e.g., 1% → 10% → 50% → 100%) with a bake time and health check at each step.
3. Define explicit rollback triggers before you start: the metrics (error rate, latency, SLO burn) and thresholds that abort the rollout, and who has authority to call it.
4. Make rollback one action: keep the previous artifact hot, script the revert, and rehearse that migrations and flags roll back cleanly.
5. Communicate: announce start/steps/completion in the agreed channel, note the change window, and record what shipped and the deploy ID.
6. Post-release: watch dashboards through the bake, verify key user journeys, and close out with a short release note.

**OUTPUT FORMAT:**
- A checklist grouped into Pre-flight / Rollout / Rollback / Comms / Post-release.
- The canary ramp schedule with bake times and per-step health gates.
- Rollback trigger thresholds and the one-line revert command.
