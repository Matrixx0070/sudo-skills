---
name: do-ci-pipeline
version: 1.0.0
description: Design or repair a CI/CD pipeline with well-ordered stages, caching, quality gates, and artifact promotion.
author: matrixx0070
tags: [ci, cd, devops, automation, pipeline]
capabilities: []
---

# do-ci-pipeline

**When to use:** You need to build a CI/CD pipeline from scratch, diagnose a slow or flaky one, or add gates before a risky change ships. Works for GitHub Actions, GitLab CI, CircleCI, Jenkins, or Buildkite.

**METHOD:**
1. Map the delivery graph: what triggers a run (push, PR, tag, schedule), what must pass before merge, and what promotes to each environment.
2. Split work into ordered stages — lint/typecheck, unit test, build, integration test, package, deploy — and run independent stages in parallel to shrink wall-clock time.
3. Add caching keyed on lockfile hashes (dependencies, build layers, test fixtures) with a documented cache-bust path; never cache secrets or environment-specific output.
4. Define gates: required status checks, coverage/threshold enforcement, security scan (SAST/deps), and manual approval for prod.
5. Produce immutable, versioned artifacts once and promote the same artifact across environments — never rebuild per stage.
6. Instrument the pipeline itself: surface duration, flake rate, and failure cause; fail fast and report clearly.

**OUTPUT FORMAT:**
- A pipeline config file (correct syntax for the named platform).
- A stage table: name, depends-on, cache key, gate, artifact.
- A short list of the top 3 risks (flake sources, cache staleness, secret exposure) with mitigations.
