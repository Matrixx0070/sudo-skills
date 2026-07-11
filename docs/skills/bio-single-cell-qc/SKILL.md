---
name: bio-single-cell-qc
version: 1.0.0
description: Quality-control single-cell RNA-seq with MAD-based filtering, doublet removal, and diagnostic visualizations.
author: matrixx0070
tags: [single-cell, scrnaseq, qc, doublets, bioinformatics]
capabilities: []
---

When to use: the user has a raw single-cell (or single-nucleus) RNA-seq count matrix and needs principled QC before clustering or annotation. Use to catch empty droplets, dying cells, ambient RNA, and doublets before they distort downstream biology.

METHOD
1. Load the count matrix (10x/H5AD) and compute per-cell metrics: total counts, genes detected, and percent mitochondrial (and ribosomal/hemoglobin where relevant).
2. Filter by median absolute deviation, not hard cutoffs: flag cells beyond ~3-5 MADs on log counts and genes, and above a MAD threshold on percent-mito. Justify the multiplier and report cells removed per criterion.
3. Remove ambient RNA if needed (SoupX/CellBender) and note the contamination fraction.
4. Detect doublets (Scrublet/scDblFinder), inspect the score distribution, set the threshold on the bimodal gap, and drop predicted doublets.
5. Filter genes: keep those detected in a minimum number of cells.
6. Re-check metrics post-filter; confirm no biological population was wholly removed.

OUTPUT FORMAT
- QC summary: cells in → out, with a breakdown by filter reason.
- Diagnostic plots: violin/histogram of counts, genes, percent-mito (pre vs post); scatter of counts vs genes colored by mito; doublet-score histogram.
- The exact thresholds used and their MAD justification.
- Reproducible code block (scanpy or Seurat) and a caveat on tissue-specific mito/count expectations. State the tool versions.
