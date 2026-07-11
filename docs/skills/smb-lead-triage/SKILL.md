---
name: smb-lead-triage
version: 1.0.0
description: Score raw inbound leads into a "call these 5 today" list on fit/intent/value/freshness, with tailored openings and follow-up timing — outreach owner-approved.
author: matrixx0070
tags: [small-business, sales, leads, triage, pipeline]
---

# Lead Triage

## When to use
Use this when inbound leads are piling up and the owner or a small sales team needs to know exactly who to contact first today — instead of working the list in random order or letting hot leads go cold.

**Not for:** building a call list from existing CRM deals with history (use smb-call-list) or CRM data hygiene (use smb-crm-cleanup). This triages fresh, un-worked inbound.

## Method
1. **Gather the leads.** List new and open inbound leads with source, date received, stated need, budget signal, and any prior contact.
2. **Score each lead.** Rate on fit (matches ideal customer), intent (urgency and buying signals), value (estimated deal size), and freshness (newer and un-contacted ranks higher). Decision point: combine into one score, but let strong intent override a mediocre fit — an urgent buyer beats a perfect-profile tire-kicker.
3. **Rank and cut to five.** Surface the top 5 to call today; hold the rest in a warm queue.
4. **Draft the approach.** For each of the five, write a one-line context brief and a suggested opening (call or message) referencing their stated need.
5. **Set follow-ups.** Recommend next-touch timing for leads not reached and for the warm queue.
6. **Flag mismatches.** Note leads that are poor fit or spam to deprioritize.

Present outreach drafts for the owner to approve before sending; customer contact is owner-approved.

## Example
18 new leads. Top pick: "Marisol, form fill 2 hrs ago, needs a catered event for 60 next month, budget noted" — score 9/10 (high intent + fresh + fits). Opening: "Hi Marisol, saw you need catering for 60 next month — happy to lock a date; what's the day?" Warm queue: a good-fit lead with no urgency → next touch in 3 days. Deprioritized: a "free samples?" message with no event → spam-ish, hold.

## Pitfalls
- **Scoring fit over intent.** A ready-to-buy lead who's slightly off-profile still outranks a perfect fit with no urgency.
- **Working the list oldest-first.** Freshness matters — a 2-hour-old inbound converts far better than a week-old one.
- **Generic openings.** Reference the lead's stated need, not "just following up."
- **Sending unapproved.** Draft the outreach; the owner approves before any message goes out.

## Output format
```
Leads reviewed: <n> | new: <n>
Call these 5 today:
  1. <name> — source <..> — score <n>/10 — need <..>
     Opening: "<suggested>"
Warm queue (ranked): <lead> — next touch <when>
Follow-up schedule: <not-reached leads — timing>
Deprioritized / spam: <lead — why>
```
