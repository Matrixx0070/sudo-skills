---
name: cs-sentiment-scan
version: 1.0.0
description: Scan a batch of tickets or feedback into themes with sentiment, then produce a prioritized "fix these 3" list.
author: matrixx0070
tags: [customer-support, sentiment, feedback, analytics, prioritization]
capabilities: []
---

When to use: you have a pile of tickets, reviews, survey responses, or chat logs and need to know what customers are actually feeling and what to fix first. Use this to turn noise into a short, ranked action list.

METHOD
1. Read the full batch before categorizing. Note volume and time window so trends are meaningful ("40 tickets, last 7 days").
2. Cluster feedback into themes by underlying problem, not surface wording — "can't find export," "export button hidden," and "where is download" are one theme.
3. Tag each item's sentiment (Positive / Neutral / Negative / Angry) and intensity. Capture representative verbatim quotes per theme — real words carry more weight than paraphrase.
4. Size each theme: frequency (how many), severity (blocked vs. annoyed), and trend (rising/steady/falling). Flag any account-value or churn signals.
5. Rank themes by frequency × severity × trend. Separate quick wins (cheap, high relief) from deeper investments.
6. Produce a "fix these 3" list — the three highest-leverage actions — each with the theme, evidence, expected impact, and suggested owner. Note anything positive worth reinforcing.

OUTPUT FORMAT
- Scope: volume + time window
- Themes table: theme | count | sentiment | trend | sample quote
- Fix these 3: action → evidence → expected impact → owner
- Quick wins vs. bigger bets
- What's working (positive signals to keep)
