---
name: eng-deploy-checklist
version: 1.0.0
description: Run a pre-deploy verification covering migrations, feature flags, CI and approvals, monitoring, and rollback triggers before shipping.
author: matrixx0070
tags: [deploy, release, rollback, migrations, ci]
capabilities: []
---

When to use: immediately before promoting a change to a shared or production environment. The goal is to catch the failure that would page someone at 3am, and to know how to undo the release fast.

METHOD
1. Code readiness: target commit is on the intended branch, CI is green, required approvals are in, and the diff contains only what this release intends to ship.
2. Migrations: schema changes are backward-compatible with the currently-running code (expand-then-contract), reversible or forward-fixable, and tested against a production-shaped dataset. Long-running migrations run out-of-band.
3. Feature flags: new behavior ships dark or ramped; default state is safe; kill-switch exists and is tested.
4. Config & secrets: new env vars/keys exist in the target environment. Never assume `--update-env` removed deleted keys — verify.
5. Observability: dashboards, logs, and alerts cover the new path. You know which metric proves success and which signals failure.
6. Rollback plan: write down the exact rollback command, the error-rate/latency thresholds that trigger it, and who decides.
7. Sequencing: order dependent steps (migrate → deploy → flip flag) and name the deploy window and on-call owner.

OUTPUT FORMAT
- Release: name / commit / environment
- Checklist (each item: PASS / FAIL / N/A with a one-line note)
- Blocking Issues (must fix before deploy)
- Rollback Plan (trigger thresholds + exact command + owner)
- Go / No-Go recommendation
