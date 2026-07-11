---
name: do-kubernetes
version: 1.0.0
description: Author or debug Kubernetes manifests with correct probes, resource limits, autoscaling, and safe rollouts.
author: matrixx0070
tags: [kubernetes, k8s, devops, orchestration, scaling]
capabilities: []
---

# do-kubernetes

**When to use:** You need to write a Deployment/Service/Ingress set, debug a CrashLoopBackOff or pending pod, add autoscaling, or make a rollout safe and reversible.

**METHOD:**
1. Start from the workload shape: stateless Deployment vs stateful set vs job; set replicas and a rollout strategy (RollingUpdate with maxUnavailable/maxSurge tuned for capacity).
2. Configure the three probes distinctly — startup (slow boot), readiness (gate traffic), liveness (restart when wedged) — with realistic thresholds so a slow start does not trigger restarts.
3. Set resource requests and limits on every container; requests drive scheduling and HPA, limits prevent noisy-neighbor. Avoid CPU limits that throttle latency-sensitive services.
4. Add an HPA (or KEDA) keyed on CPU/memory or a custom metric, with sane min/max and stabilization windows.
5. Externalize config via ConfigMap/Secret, mount rather than bake, and set securityContext (non-root, drop capabilities, readOnlyRootFilesystem).
6. To debug: `kubectl describe` for events, `logs --previous` for crashes, check probe failures, image pull errors, and resource pressure before editing.

**OUTPUT FORMAT:**
- Valid YAML manifests (Deployment, Service, HPA, and Ingress as needed).
- A probe/resource table per container.
- Rollout and rollback commands, plus the likely root cause when debugging.
