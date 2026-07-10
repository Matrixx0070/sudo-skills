---
name: meeting-notes
version: 1.0.0
description: Structure a raw meeting transcript or scribble into decisions, action items with owners and dates, and open questions - so nothing agreed in the room evaporates afterwards.
triggers:
  - meeting notes
  - clean up these notes
  - structure this transcript
  - action items from this meeting
  - what did we decide
capabilities: []
inputs:
  - name: transcript
    required: true
    description: Raw transcript, chat log, or rough notes from the meeting.
  - name: attendees
    required: false
    description: Names/roles present, to help attribute owners correctly.
---

# Meeting Notes

## Purpose
Convert meeting chaos into the three things that matter afterwards: what was decided, who does what by when, and what remains unresolved.

## Hard rules
1. **Decisions are verbatim-faithful.** A decision is recorded only if someone in the transcript actually agreed to it. Proposals that got no agreement go under Open Questions, not Decisions.
2. **Every action item has an owner.** If the transcript assigns no one, write "owner: UNASSIGNED" loudly rather than guessing a name. Same for dates: "by: not set".
3. **Attribute carefully.** Never put words in a named person's mouth; when the speaker is unclear, use "someone raised".
4. **Discussion is not minutes.** Summarize threads of debate in one line each at most; the deliverable is decisions and actions, not a play-by-play.
5. **Keep disagreement visible.** If someone objected and was overruled, one line notes it - that context matters in a month.

## Workflow
1. Read the whole transcript once before writing anything.
2. Extract decisions (with who agreed), then actions (owner, task, date), then open questions.
3. Write a two-line summary at the top for people who were not there.
4. If `attendees` is provided, sanity-check every owner against that list.

## Output format
```
**Summary:** <two lines>

**Decisions**
1. ...

**Action items**
- [ ] <task> — owner: <name>, by: <date | not set>

**Open questions**
- ...
```

## Example
**Input (raw):** "ok so pricing... Sam thinks $29 is too low, Ana wants to test both. fine we'll A/B it. Sam will set up the test this week. also the churn dashboard is still broken, nobody knows why, Jo will look maybe"

**Output:**
**Summary:** Agreed to A/B test $29 vs current pricing rather than settle the debate now. Churn dashboard breakage remains undiagnosed.

**Decisions**
1. Run an A/B price test instead of picking a price now (Ana proposed, Sam agreed; Sam had argued $29 is too low).

**Action items**
- [ ] Set up the pricing A/B test — owner: Sam, by: this week
- [ ] Investigate broken churn dashboard — owner: Jo (tentative), by: not set

**Open questions**
- What is actually breaking the churn dashboard?
