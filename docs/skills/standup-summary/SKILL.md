---
name: standup-summary
version: 1.0.0
description: Turn raw notes about yesterday's work into a crisp standup update - done / doing / blocked - honest about what actually shipped versus what is in progress.
triggers:
  - standup
  - standup update
  - what did I do yesterday
  - daily update
  - write my standup
capabilities: []
inputs:
  - name: notes
    required: true
    description: Raw notes, commit messages, or a brain-dump of recent work.
  - name: audience
    required: false
    description: Who reads it (team channel, manager 1:1, client) to calibrate detail.
---

# Standup Summary

## Purpose
Produce the update a good teammate gives: short, concrete, honest about status, with blockers stated plainly enough that someone can actually help.

## Hard rules
1. **Done means done.** Something goes under "Done" only if the notes show it finished (merged, shipped, sent, verified). In-progress work with "almost" or "just needs" belongs under "Doing".
2. **Concrete over vague.** "Fixed the login timeout (PR #214, merged)" beats "worked on auth issues". Keep ticket/PR numbers when present.
3. **Blockers name the blocker.** "Blocked on staging access (asked infra Tue, no reply)" - what, who, since when. A blocker without an owner is a complaint, not a blocker.
4. **Three lines per section max.** If there are more items, keep the three most important and roll the rest into one "plus small stuff: ..." line.
5. **No filler.** No "continued to make progress on", no "various tasks".

## Workflow
1. Sort every note into done / doing / blocked. When unsure, downgrade (doing rather than done).
2. Order by what the audience cares about most.
3. Trim each item to one line; keep identifiers (PR, ticket, doc link).
4. If nothing is blocked, omit the section entirely rather than writing "no blockers" ceremony.

## Output format
```
**Done:** ...
**Doing:** ...
**Blocked:** ... (omit if none)
```

## Example
**Input (raw):** merged the retry fix finally, started poking at the flaky e2e suite its something with timeouts, waiting on Dana for the API key to test payments, also reviewed two PRs

**Output:**
**Done:** Merged the retry fix; reviewed 2 PRs.
**Doing:** Investigating flaky e2e suite - looks timeout-related, narrowing it down.
**Blocked:** Payments testing needs the API key from Dana (asked yesterday).
