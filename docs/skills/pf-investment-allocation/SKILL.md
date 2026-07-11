---
name: pf-investment-allocation
version: 1.0.0
description: Explain a diversified asset-allocation framework tailored to risk tolerance and time horizon (educational).
author: matrixx0070
tags: [investing, asset-allocation, diversification, risk, personal-finance]
capabilities: []
---

## When to use

Use this when the owner wants to understand how a diversified portfolio is *structured* — the logic of splitting across stocks, bonds, and cash by risk and time horizon. Good for framing a conversation before they meet an advisor, or for understanding a target-date fund's design.

**Not for:** recommending specific securities, tickers, or fund products; timing the market; or telling the owner to buy or sell. You explain frameworks, never issue picks.

This skill provides education and structure, not individualized investment advice. Allocation involves real risk of loss; recommend a licensed fiduciary advisor before the owner commits money.

## Method

1. Establish the goal and its time horizon: short (<3 yr), medium (3-10 yr), or long (10+ yr).
2. Assess risk capacity (can they afford a loss?) and risk tolerance (can they emotionally hold through a 30% drop?). Use the lower of the two.
3. Decision point — set a stock/bond split by horizon and risk. Common educational anchors: long+aggressive ~90/10, long+moderate ~70/30, medium ~50/50, short ~20/80 or all cash.
4. Diversify *within* stocks (domestic + international, broad sectors) and bonds (varied duration/quality) — concentration is the main avoidable risk.
5. Hold an emergency fund (3-6 months expenses) in cash *outside* the invested portfolio so the owner never force-sells in a downturn.
6. Decision point — is any single position >10% of the portfolio (e.g., employer stock)? Flag concentration risk.
7. Set a rebalancing rule: revisit yearly or when a bucket drifts >5 points from target.

## Example

Owner, retirement 25 years out, moderate tolerance. Framework: 70% stocks / 25% bonds / 5% cash. Within stocks: ~45% domestic broad-market, ~25% international. Emergency fund of $18,000 (6 months) held separately. Employer stock is 22% of holdings → flagged as concentration; framework suggests diversifying over time. Rebalance each January.

## Pitfalls

- Confusing risk tolerance with risk capacity — an aggressive personality with an unstable income still needs a buffer.
- Chasing last year's winner; diversification means always owning something underperforming.
- Skipping the emergency fund and being forced to sell investments at the worst time.
- Recommending specific products. Stay at the framework level and defer picks to a licensed professional.

## Output format

```
ALLOCATION FRAMEWORK (educational) — [owner]
Goal: [goal]   Horizon: [x] yrs   Risk: [conservative|moderate|aggressive]

TARGET SPLIT
Stocks  [x]%   (domestic [x]% / international [x]%)
Bonds   [x]%
Cash    [x]%

EMERGENCY FUND: $[x] held separately ([n] months)
CONCENTRATION FLAGS: [position — % — note]
REBALANCE: [yearly / >5pt drift]

This is a framework, not a recommendation. Confirm with a licensed fiduciary before investing.
```
