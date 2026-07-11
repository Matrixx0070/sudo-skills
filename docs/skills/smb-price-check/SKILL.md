---
name: smb-price-check
version: 1.0.0
description: Build a margin-by-product table plus three pricing-scenario views to support a pricing decision.
author: matrixx0070
tags: [pricing, margin, scenarios, finance, strategy]
capabilities: []
---

When to use: Run this before the owner raises prices, launches a product, or reacts to a cost increase. It turns "should I change my prices?" into a numbers-backed decision the owner makes.

METHOD
1. Gather each product's price, unit cost, and recent units sold. Pull from connected sales/inventory data or ask the owner for the short list that matters.
2. Compute per-product gross margin (dollars and percent) and rank products by margin and by volume.
3. Flag margin outliers: items priced below a healthy floor, loss leaders, and high-volume low-margin items where a small change moves the most money.
4. Build three scenario views over the same products:
   - Hold: current prices, current margin.
   - Raise: an across-the-board or targeted increase, with estimated margin gain and a demand-sensitivity caveat.
   - Reprice losers: fix only the worst margins, leaving winners untouched.
5. Summarize the trade-offs and name a recommended scenario. The owner approves before any price actually changes anywhere.

OUTPUT FORMAT
- Margin table: product, price, cost, margin $, margin %, units, margin contribution.
- Three scenario cards with projected total margin and one-line trade-off each.
- A clear recommendation plus the assumption it rests on.
- No price is published or updated in any system without owner sign-off.
