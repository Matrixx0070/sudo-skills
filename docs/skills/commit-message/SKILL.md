---
name: commit-message
version: 1.0.0
description: Write a conventional-commit message from a description or diff summary - honest subject, wrapped body explaining why, no invented scope or claims.
triggers:
  - commit message
  - write a commit message
  - conventional commit
  - describe this change for git
capabilities: []
inputs:
  - name: change
    required: true
    description: What changed - a diff, a diff summary, or a plain description.
  - name: convention
    required: false
    description: House style if not conventional-commits (e.g. plain imperative, ticket-prefixed).
---

# Commit Message

## Purpose
Produce the commit message a maintainer thanks you for two years later: what changed, why, and what to watch out for.

## Hard rules
1. **Subject ≤ 72 chars, imperative, no period.** `fix(parser): handle empty input` not `Fixed some parser issues.`
2. **Type and scope must be honest.** `fix` only for behavior corrections; `feat` only for new capability; `refactor` must not change behavior. If the change mixes types, pick the dominant one and mention the rest in the body.
3. **Body explains WHY, not a line-by-line WHAT.** The diff already shows what; the message records the reasoning, the bug's cause, or the constraint that forced this design.
4. **State breaking changes and side effects explicitly** (`BREAKING CHANGE:` footer when the convention supports it).
5. **Never invent.** No ticket numbers, benchmarks, or reviewer names that were not provided. If the change description is too thin to know WHY, say so and write the best honest subject possible.

## Workflow
1. Identify the single dominant intent of the change.
2. Draft subject: `type(scope): imperative summary`.
3. Body (wrapped ~72 cols): 1-3 short paragraphs - the problem, the cause or reasoning, anything reviewers/operators must know.
4. Footers: breaking changes, ticket refs (only if given).

## Output format
```
type(scope): subject

<why-focused body>

<footers if any>
```

## Example
**Input:** "we stopped caching user avatars because stale images showed after profile updates, now they get a cache-busting hash in the url"

**Output:**
```
fix(avatars): cache-bust avatar URLs with a content hash

Profile updates left stale avatars on screen because the CDN kept
serving the cached image at the unchanged URL. Appending a content
hash makes every new upload a new URL, so caches stay hot for
unchanged avatars while updates appear immediately.

Old cached URLs remain valid until CDN TTL expiry; no purge needed.
```
