---
name: data-create-viz
version: 1.0.0
description: Produce a publication-quality static visualization in Python with a deliberately chosen chart type.
author: matrixx0070
tags: [visualization, python, matplotlib, charts, reporting]
capabilities: []
---

# data-create-viz

When to use: you need a polished static chart — for a report, slide, or export — where clarity and correct chart-type choice matter more than interactivity. Prefer this over a dashboard when the audience needs one clear picture.

## METHOD

1. **Name the message.** Every chart makes one point. Write it in a sentence first; the chart's title should state that point, not just label the axes.
2. **Choose the chart type by data relationship**:
   - Trend over time → line.
   - Comparison across categories → horizontal bar (sorted).
   - Part-to-whole → stacked bar or (rarely, ≤4 slices) donut — never a pie for many slices.
   - Distribution → histogram or box/violin.
   - Correlation → scatter, with trend line if a relationship is claimed.
   - Composition over time → stacked area.
3. **Build in Python** (matplotlib/seaborn). Sort bars by value, start value axes at zero for bars, label directly instead of relying on legends where possible.
4. **Design for legibility**: high contrast, minimal gridlines, no chartjunk, colorblind-safe palette, readable font sizes at final display scale.
5. **Annotate** the key data point (peak, inflection, outlier) so the message is unmissable.
6. **Export** at high resolution (PNG 2x and, when scalable output helps, SVG).

## OUTPUT FORMAT

- The runnable Python script.
- The exported image file(s) with descriptive filename.
- A one-line caption stating the chart's single takeaway.
- A note on the data source, filters, and time window.

Verify axes, units, and totals before exporting. If the chosen chart type would mislead (e.g., truncated axis inflating a bar), fix it and say why.
