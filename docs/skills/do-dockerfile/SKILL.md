---
name: do-dockerfile
version: 1.0.0
description: Write or optimize a Dockerfile and compose stack for small, secure, cache-friendly, reproducible images.
author: matrixx0070
tags: [docker, containers, devops, security, build]
capabilities: []
---

# do-dockerfile

**When to use:** You need a production Dockerfile, a bloated image slimmed down, a slow build made cache-friendly, or a docker-compose stack for local development and integration testing.

**METHOD:**
1. Pick a minimal, pinned base image (distroless, alpine, or a digest-pinned slim tag); avoid `latest` and unnecessary toolchains in the runtime layer.
2. Use multi-stage builds: a build stage with compilers and dev dependencies, a final stage that copies only the runtime artifact.
3. Order layers by change frequency — copy the lockfile and install dependencies before copying source, so code edits do not bust the dependency cache.
4. Harden: run as a non-root USER, drop setuid where possible, set a read-only-friendly filesystem, avoid embedding secrets (use build args or mounts), and add a HEALTHCHECK.
5. Trim: combine RUN steps, clean package caches in the same layer, and add a `.dockerignore` to keep build context lean.
6. For compose, declare service dependencies, health-gated `depends_on`, named volumes, and an isolated network; keep dev-only overrides in a separate file.

**OUTPUT FORMAT:**
- The Dockerfile (multi-stage, commented).
- A `.dockerignore` and, when relevant, `docker-compose.yml`.
- A before/after note on image size, layer cache behavior, and security posture.
