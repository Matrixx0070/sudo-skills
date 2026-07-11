---
name: bio-single-cell-qc
version: 1.0.0
description: Quality-control single-cell RNA-seq with MAD-based filtering, ambient-RNA correction, doublet removal, and pre/post diagnostics.
author: matrixx0070
tags: [single-cell, scrnaseq, qc, doublets, ambient-rna, bioinformatics]
capabilities: []
---

## When to use

Use this when the user has a raw single-cell (or single-nucleus) RNA-seq count matrix and needs principled QC before clustering or annotation. It catches empty droplets, dying cells, ambient RNA, and doublets before they distort downstream biology.

**Not for:** already-QC'd matrices, clustering/annotation itself, bulk RNA-seq, or running the upstream alignment pipeline (use bio-pipeline-runner for that).

## Method

1. Load the count matrix (10x/H5AD) and compute per-cell metrics: total counts, genes detected, percent mitochondrial (and ribosomal/hemoglobin where relevant).
2. Filter by median absolute deviation, not hard cutoffs. Flag cells beyond ~3–5 MADs on log counts and log genes, and above a MAD threshold on percent-mito. **Decision:** loosen to 5 MADs for heterogeneous tissue where rare populations sit in the tail; tighten to 3 for a clean single cell line.
3. **Decision:** correct ambient RNA (SoupX/CellBender) only if the empty-droplet profile shows contamination; report the fraction. Skip for nuclei with low ambient signal.
4. Detect doublets (Scrublet/scDblFinder). Inspect the score distribution, set the threshold on the bimodal gap, drop predicted doublets.
5. Filter genes: keep those detected in a minimum number of cells (e.g. ≥3).
6. Re-check metrics post-filter. **Decision:** if a whole cluster vanished, you over-filtered — relax and re-run rather than proceed.

## Example

A 10x PBMC run loads at 8,200 cells. Percent-mito is bimodal; the 3-MAD cutoff lands at 12% and removes 640 dying cells. Scrublet shows a clean gap at 0.25, dropping 410 doublets. SoupX estimates 6% ambient and is applied. Genes kept: detected in ≥3 cells. Final: 7,050 cells. Post-filter violin confirms the platelet and DC populations survived.

## Pitfalls

- Applying one hard percent-mito cutoff (e.g. 5%) across tissues — cardiomyocytes and hepatocytes are legitimately high-mito.
- Skipping doublet detection, then "discovering" a fake intermediate cell type that is really two cells.
- Filtering so aggressively that a real rare population is erased — always compare pre/post.
- Not reporting the ambient contamination fraction, so downstream users can't judge residual signal.

## Output format

```
# scRNA-seq QC — <sample>
Tool versions: scanpy=_ / scDblFinder=_ / SoupX=_

## QC summary
cells in → out; removed by: mito=_, counts=_, genes=_, doublets=_

## Thresholds (with MAD justification)
counts: ±_ MAD | genes: ±_ MAD | mito: _ MAD | min cells/gene: _

## Diagnostics
violin counts/genes/mito (pre vs post); counts-vs-genes scatter (mito-colored); doublet-score histogram

## Reproducible code
<scanpy or Seurat block>
```
Note tissue-specific mito/count expectations. State tool versions.
