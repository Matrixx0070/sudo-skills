---
name: hr-people-report
version: 1.0.0
description: Build headcount, attrition, diversity, and org-health reports — every metric defined, small-n protected, insight before data dump.
author: matrixx0070
tags: [people-analytics, attrition, diversity, headcount, reporting, org-health]
capabilities: []
---

## When to use

Reach for this when preparing a monthly/quarterly people review, answering a leadership question about the workforce, or tracking a metric like regretted attrition. Report numbers accurately, define every metric, and lead with insight.

**Not for:** forward-looking hiring plans (use hr-org-planning), pricing a role (use hr-comp-analysis), or live pipeline status (use hr-recruiting-pipeline).

## Method

1. **Scope the report** — audience, period, and org cut (company/function/team). State the as-of date and data source.
2. **Headcount** — starting/ending headcount, hires, exits, net change, open reqs; break down by function and level.
3. **Attrition** — annualized attrition = exits ÷ average headcount. Split voluntary vs. involuntary and regretted vs. non-regretted; show trend vs. prior periods.
4. **Diversity** — representation by relevant dimensions at overall, leadership, and hiring-funnel stages, with period delta. Decision point: for any small-n group, suppress or aggregate to protect privacy rather than publishing an identifiable count.
5. **Org health** — spans/layers, tenure distribution, internal mobility, and engagement/eNPS if available.
6. **Interpret** — call out the 3-5 signals that matter, likely drivers, and recommended actions. Decision point: distinguish correlation from cause and flag any data-quality caveat before it misleads a decision.

## Example

Q2, Engineering, as-of 2026-06-30, source Workday. Headcount 210 → 218 (+12 hires, -4 exits). Annualized attrition 7.5% (3 voluntary / 1 involuntary; 2 of the 3 voluntary flagged regretted) vs. 6.1% in Q1 — trending up. Regretted exits both cite comp; two open competing offers matched market 60th. Women in eng 26% overall but 14% at manager+ — a leadership-pipeline gap. Insight + action: launch a mid-level promotion review to widen the manager funnel; revisit senior-eng bands after the comp signal.

## Pitfalls

- Publishing a raw number for a group of 2-3 people, making individuals identifiable.
- Quoting an attrition rate without stating the formula or the denominator (average vs. ending headcount).
- Reporting diversity at company level only, hiding the leadership-tier gap.
- Dumping every chart with no ranked insight, so leadership can't tell what matters.

## Output format

```
Executive summary: top 3-5 insights + recommended actions
Headcount: table + net-change waterfall (start, hires, exits, end)
Attrition: rate (formula), voluntary/involuntary, regretted split, trend
Diversity: representation by level + funnel, period delta (small-n suppressed)
Org health: spans, layers, tenure, mobility, eNPS
Metric definitions + data caveats
```
