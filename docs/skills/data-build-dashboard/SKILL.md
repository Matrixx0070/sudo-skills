---
name: data-build-dashboard
version: 1.0.0
description: Build a self-contained interactive HTML dashboard with KPI cards, charts, and filters that runs from a single file.
author: matrixx0070
tags: [dashboard, html, visualization, interactive, reporting]
capabilities: []
---

# data-build-dashboard

When to use: the user wants an explorable dashboard rather than a static chart or a one-off number — a KPI overview, a metrics tracker, or a report others will click through. Deliver one HTML file that opens in any browser with no server, build step, or network dependency.

## METHOD

1. **Define the decisions** the dashboard supports. List the 3-6 KPIs that answer them and the dimensions users will slice by (date, region, segment).
2. **Shape the data.** Embed it inline as a JSON array in a `<script>` block. Pre-aggregate heavy rollups; keep raw rows only if filtering needs them. Note the row count so you do not embed millions of rows.
3. **Lay out top-down**: KPI cards (with delta vs prior period) across the top, primary trend chart next, breakdown charts below, detail table last.
4. **Add interactivity**: a date-range control and dimension filters that recompute every KPI and chart from the embedded data. Wire filters through one shared `applyFilters()` function so state stays consistent.
5. **Style** with a clean CSS system: responsive grid, readable type scale, and a palette that works in light and dark. Use one charting library via CDN with an offline fallback, or hand-rolled SVG.
6. **Self-test** the numbers: totals must reconcile with the source before delivery.

## OUTPUT FORMAT

- A single `.html` file, fully self-contained (data + CSS + JS inline).
- Top: title, last-updated timestamp, KPI card row with period-over-period deltas.
- Middle: interactive filters + primary time-series chart.
- Bottom: breakdown charts and a sortable detail table.
- A short note listing the data source, refresh method, and any assumptions.

Deliver a file that works when double-clicked offline. State how to refresh the data.
