---
name: do-terraform
version: 1.0.0
description: Write or review Terraform with clean modules, safe state, drift detection, and disciplined plan review.
author: matrixx0070
tags: [terraform, iac, devops, cloud, review]
capabilities: []
---

# do-terraform

**When to use:** You need to author infrastructure-as-code, refactor sprawling configs into modules, set up remote state, investigate drift, or review a `terraform plan` before apply.

**METHOD:**
1. Structure code: reusable modules with explicit `variables.tf`/`outputs.tf`, thin root configs per environment, and pinned provider and module versions.
2. Configure remote state with locking (S3+DynamoDB, GCS, or Terraform Cloud); never commit state or secrets, and isolate state per environment to limit blast radius.
3. Keep resources declarative and idempotent; prefer `for_each` over `count` for stable addressing, and use `data` sources instead of hardcoding IDs.
4. Detect drift with `terraform plan -detailed-exitcode` on a schedule; reconcile by importing real resources or correcting config, never by manual console edits.
5. Review every plan: read `+`/`~`/`-` symbols carefully, flag any destroy-then-create on stateful resources, check for unintended replacements, and confirm secret values are not printed.
6. Gate apply behind CI with a saved plan artifact so the reviewed plan is the applied plan.

**OUTPUT FORMAT:**
- Module/root file layout with the key `.tf` snippets.
- Backend/state configuration.
- A plan-review summary: adds, changes, destroys, and any high-risk replacements called out explicitly.
