---
name: smb-sales-brief
version: 1.0.0
description: Surface top and bottom sellers plus seasonality, then produce a two-week content brief mapped to channels.
author: matrixx0070
tags: [sales, analysis, content, seasonality, marketing, calendar]
capabilities: []
---

# Sales Brief

## When to use
Run this when the owner wants to know what's selling and what to post about next. It connects the numbers to a concrete two-week content plan without committing to any spend.

**Not for:** executing or sending anything (use smb-run-campaign); pricing decisions (use smb-price-check); this skill plans content and publishes nothing.

## Method
1. **Pull the data.** Recent sales from connected systems, or ask the owner for a period to analyze.
2. **Rank products.** Top sellers by revenue and by units; bottom sellers that are dragging or stale.
3. **Detect seasonality and trend.** Compare against prior periods; flag items rising or fading and any recurring seasonal pattern. Decision point: separate a genuine trend from a one-off spike (a single big order isn't a pattern).
4. **Turn findings into angles.** Which winners to amplify, which slow movers to promote or clear, which stories the data suggests.
5. **Build a two-week content brief.** A dated calendar of post ideas mapped to channels, each with a hook and the product or angle it supports.
6. **Present for editing.** The owner edits; hand off to smb-run-campaign when ready to execute.

## Example
Last 30 days: top by revenue = leather wallets ($4,200), top by units = keychains (210); bottom = phone cases (stale 3 months). Trend: wallets up 18% MoM, cases fading — not a one-off. Angles: amplify wallets (gift angle), clear cases with a bundle. Two-week calendar: Mon IG "wallet gifting" hook, Wed email "case + wallet bundle," Fri IG keychain UGC. Handoff: smb-run-campaign to launch the bundle.

## Pitfalls
- Reading a single large order as a "trend" and building a campaign on noise.
- Ranking only by revenue and missing a high-unit item worth featuring for reach.
- A content calendar with hooks but no product/angle tied to each post — pretty but empty.
- Drifting into sending or spending; this brief stops at a plan the owner edits.

## Output format
- **Top/bottom seller tables:** product | revenue | units | trend arrow.
- **Seasonality note** (2-4 sentences).
- **Two-week calendar:** date | channel | hook | supporting product.
- **Handoff line** pointing to smb-run-campaign when the owner is ready to execute.
