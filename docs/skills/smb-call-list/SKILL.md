---
name: smb-call-list
version: 1.0.0
description: Rank the top-5 leads worth calling today with tailored, history-grounded talking points and proposed calendar blocks — no auto-send.
author: matrixx0070
tags: [sales, crm, leads, outreach, productivity]
capabilities: []
---

# Call List

## When to use
Use this when you start the day and want a focused call list instead of a cluttered pipeline. It surfaces the five leads most likely to move, arms you with what to say, and reserves time to dial.

**Not for:** first-touch scoring of raw inbound (use smb-lead-triage), or bulk CRM hygiene (use smb-crm-cleanup). This assumes leads already exist in the CRM with some history.

## Method
1. Pull open leads and deals from the CRM: last-contact date, deal value, stage, and recent activity (email replies, site visits, form fills).
2. Score each on freshness, intent signals, deal size, and stall risk. Decision point: prefer warm-but-cooling leads (had contact, going quiet) over cold ones with no signal.
3. Select the top five. For each, draft three talking points grounded in real history. Decision point: if a fact is missing, say "no record of X" — never invent a detail.
4. Propose 2-3 calendar blocks that fit around existing meetings, clustering calls to protect focus time.
5. Confirm the blocks with the owner before writing anything to the calendar. Do not send emails or log outreach automatically.

## Example
Lead: Dana Reyes, Northside Dental. Why-now 8/10 — opened your quote email twice this week, deal $14k, stalled 9 days in Proposal. Talking points: (1) reference her question about the 12-month plan, (2) the Q3 install slot she asked about is still open, (3) no record of pricing objection — ask directly. Suggested block: today 10:00-10:30.

## Pitfalls
- **Inventing rapport.** Fabricated "we last spoke about..." details get caught on the call and burn trust — cite only logged facts.
- **Ranking by deal size alone.** A huge cold lead beats a warm mid-size one on paper but not in reality; weight intent.
- **Writing to the calendar unasked.** Always propose blocks and wait for a yes.
- **Over-long lists.** Six-plus "priority" calls means none are; hold the rest in a warm queue.

## Output format
```
Call these 5 today:
1. <name>, <company> — why-now <n>/10 — last contact <date> — deal $__
   - <talking point 1>
   - <talking point 2>
   - <talking point 3>
[...2-5]

Suggested call blocks:
  - <day> <start>-<end>
"Approve these blocks and I'll add them to your calendar."
```
