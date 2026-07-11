---
name: sec-code-audit
version: 1.0.0
description: Perform a security-focused code audit covering injection, authorization, secrets, and unsafe deserialization.
author: matrixx0070
tags: [security, code-audit, appsec, injection, authorization]
capabilities: []
---

## When to use

Use this before merging security-sensitive changes, when reviewing untrusted or legacy code, or during a scheduled appsec pass. The goal is to find and recommend fixes for defensive weaknesses, never to weaponize them.

## METHOD

1. **Map inputs and sinks.** Trace where external data enters (requests, files, env, messages) and where it reaches dangerous sinks (SQL, shell, eval, file paths, HTML, deserializers, template engines).
2. **Injection.** Confirm parameterized queries, escaped output, allow-listed commands, and safe path joins. Flag any string-concatenated query, shell call, or dynamic template.
3. **AuthN/AuthZ.** Verify every privileged action checks identity AND permission server-side. Hunt for missing checks, IDOR (object references without ownership checks), and client-trusted roles.
4. **Secrets.** Look for hardcoded keys, tokens, and passwords, and any secret written to logs or returned to clients. Confirm secrets load from config or a vault.
5. **Deserialization & parsing.** Flag unsafe deserialization (pickle, native serialize, YAML unsafe load), XXE-prone XML parsers, and prototype pollution.
6. **Crypto & sessions.** Check for weak hashing, missing TLS, predictable tokens, and long-lived or unrotated sessions.

## OUTPUT FORMAT

- **Summary** — files reviewed and overall risk posture.
- **Findings table** — Severity (Critical/High/Medium/Low) | File:line | Category | Description | Recommended fix.
- **Quick wins** — low-effort, high-value fixes first.
- **Follow-ups** — items needing design changes or owner decisions.
