---
name: smb-price-check
version: 1.0.0
description: Build a margin-by-product table plus three pricing-scenario views (hold, raise, reprice losers) to support a pricing decision.
author: matrixx0070
tags: [pricing, margin, scenarios, finance, strategy, decision]
capabilities: []
---

# Price Check

## When to use
Run this before the owner raises prices, launches a product, or reacts to a cost increase. It turns "should I change my prices?" into a numbers-backed decision the owner makes.

**Not for:** deep unit-economics with break-even modeling (use smb-margin-analyzer); publishing or updating prices in any system — the owner signs off before anything changes.

## Method
1. **Gather inputs.** Each product's price, unit cost, and recent units sold. Pull from connected sales/inventory data, or ask the owner for the short list that matters.
2. **Compute and rank.** Per-product gross margin (dollars and percent); rank by margin and by volume.
3. **Flag outliers.** Items below a healthy margin floor, loss leaders, and high-volume low-margin items where a small change moves the most money. Decision point: prioritize the high-volume low-margin items — that's where a 5% tweak has the biggest dollar impact.
4. **Build three scenario views** over the same products: **Hold** (current prices/margin); **Raise** (across-the-board or targeted increase, with estimated margin gain and a demand-sensitivity caveat); **Reprice losers** (fix only the worst margins, leave winners untouched).
5. **Summarize trade-offs and recommend.** Name a recommended scenario and the assumption it rests on. The owner approves before any price changes anywhere.

## Example
Three products: Mug $12/cost $5/300u; Tee $22/cost $14/180u; Sticker $4/cost $1.20/90u. Margins: Mug 58%, Tee 36%, Sticker 70%. Tee is high-volume low-margin — the lever. Hold: total margin $4,164/mo. Raise Tee to $25: +$540/mo, caveat "demand may soften above $24." Reprice losers: lift Tee to $25 only, leave Mug/Sticker. Recommendation: reprice losers — biggest gain, least risk to bestsellers. Assumption: Tee volume holds within ~10%.

## Pitfalls
- Ranking only by margin % and missing that the low-% product is where the real dollars move.
- Modeling a raise with no demand-sensitivity caveat, so the projection reads as a guarantee.
- Touching bestsellers "for consistency" when repricing only the losers is safer.
- Publishing a price to a live storefront before the owner has signed off.

## Output format
- **Margin table:** product | price | cost | margin $ | margin % | units | margin contribution.
- **Three scenario cards:** Hold / Raise / Reprice losers — each with projected total margin and a one-line trade-off.
- **Recommendation** + the assumption it rests on.
- **Approval note:** no price is published or updated in any system without owner sign-off.
