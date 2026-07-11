---
name: smb-margin-analyzer
version: 1.0.0
description: Break down unit economics per product or service, rank by contribution, and model pricing scenarios before the owner commits.
author: matrixx0070
tags: [small-business, margin, pricing, unit-economics, profitability, break-even]
capabilities: []
---

# Margin Analyzer

## When to use
Use this when the owner suspects some offerings carry the business while others quietly bleed, or when a price/cost change is on the table and they want the effect modeled first. Good for "which products actually make money?" and "if I raise this 10%, what happens?"

**Not for:** publishing or changing prices (that's the owner's call, downstream); full campaign planning (use smb-run-campaign); tax or bookkeeping cleanup (use smb-month-end-prep).

## Method
1. **List offerings in scope.** Capture unit price and units sold for the period. If data isn't connected, ask the owner for the short list that matters most.
2. **Assign direct costs.** Per unit: materials, direct labor, processor fees, shipping. If a cost is unknown, mark it estimated rather than skipping it.
3. **Compute unit economics.** Gross profit per unit, gross margin %, and total contribution (margin/unit × units) per offering.
4. **Rank two ways.** By total contribution and by margin %. Decision point: an item can be low-margin but high-contribution (keep, optimize) or high-margin but trivial volume (fine, don't over-invest). Flag negative-margin items explicitly.
5. **Run scenarios on selected items.** Model +/- price and cost changes. Show new margin and the break-even volume shift — how much volume you can lose before the change stops paying.
6. **Recommend.** Price, bundle, or discontinue moves with projected margin impact. Do not change prices; that decision affects customers and revenue and is the owner's to approve.

## Example
Owner sells a $40 gift box (cost $31, 200/mo) and $18 candles (cost $6, 90/mo). Boxes: $9/unit margin (22.5%), $1,800 contribution. Candles: $12/unit (66.7%), $1,080. Scenario — raise box to $45: margin jumps to $14 (31%). Break-even: sales can fall from 200 to 129/mo before contribution drops below today's $1,800. Recommendation (for approval): raise boxes, promote candles harder.

## Pitfalls
- Counting only COGS and forgetting processor fees and shipping — the true margin is thinner than it looks.
- Killing a "low-margin" item that's actually a top contributor by dollars, or a loss leader that drives attached sales.
- Modeling a price rise with zero demand sensitivity; always state the volume you can afford to lose.
- Treating estimated costs as facts — label assumptions so the owner can correct them.

## Output format
- **Period / offerings covered.**
- **Unit economics table:** offering | price | unit cost | gross profit/unit | margin % | total contribution.
- **Ranking:** top contributors; thin/negative-margin flags.
- **Pricing scenarios:** offering | change modeled | new margin | break-even volume shift.
- **Recommendations (for owner approval)** with the assumption each rests on.
