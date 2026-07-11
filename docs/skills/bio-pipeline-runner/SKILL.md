---
name: bio-pipeline-runner
version: 1.0.0
description: Plan and assemble an nf-core bioinformatics run (rnaseq, sarek, atacseq) with a schema-validated samplesheet, pinned version, and correct profile.
author: matrixx0070
tags: [nf-core, nextflow, rnaseq, sarek, atacseq, pipeline]
capabilities: []
---

## When to use

Use this when the user wants to run a standardized nf-core pipeline on sequencing data and needs the samplesheet, config, and command assembled correctly the first time — rnaseq (expression), sarek (variants), or atacseq (open chromatin).

**Not for:** custom one-off analyses with no nf-core equivalent, QC of an already-produced count matrix (use bio-single-cell-qc), or interpreting biology from finished results.

## Method

1. Match pipeline to the assay. **Decision:** rnaseq for DGE/quantification, sarek for germline/somatic variants, atacseq for open chromatin. If the assay doesn't map cleanly, stop and clarify rather than force-fit.
2. Pin the version with `-r <release>` and pick the reference (iGenomes key or explicit FASTA/GTF).
3. Build the samplesheet in the pipeline's exact schema:
   - rnaseq: `sample,fastq_1,fastq_2,strandedness`
   - sarek: `patient,sample,lane,fastq_1,fastq_2`
   - atacseq: `sample,fastq_1,fastq_2,replicate`
   Validate paths exist and paired-end mates match.
4. Choose the execution profile: docker/singularity/conda for containers plus an executor (local/slurm) and resource limits via `-c`. **Decision:** singularity on shared HPC (no root), docker on a personal box.
5. Dry-run with `-profile test` or `-stub` to catch schema errors before burning compute.
6. Launch, then inspect MultiQC and `pipeline_info` execution reports for failures and resource waste.

## Example

Bulk RNA-seq, 6 samples, reverse-stranded, on a SLURM cluster. Choose `nf-core/rnaseq -r 3.14.0`, genome `GRCh38`. Samplesheet rows read `ctrl_1,/data/c1_R1.fq.gz,/data/c1_R2.fq.gz,reverse`. Profile: `-profile singularity` with a `slurm.config` capping 16 CPU / 72 GB per process. `-profile test` passes, then the full run. MultiQC STAR alignment rate ~92% confirms the stranded setting was right.

## Pitfalls

- Leaving strandedness as `auto` when the kit is known — silently wrong DGE if guessed incorrectly.
- Not pinning `-r`, so a later default-branch change makes the run irreproducible.
- Skipping the `-profile test` dry-run and discovering a samplesheet typo after hours of alignment.
- Requesting more memory per process than the node has, so every job pends forever.

## Output format

```
# nf-core Run Plan — <pipeline>
Pipeline: nf-core/<name>  Version: -r <release>  Genome: <key/FASTA+GTF>  Rationale: <one line>

## samplesheet.csv
<header + rows in exact schema>

## Command
nextflow run nf-core/<pipeline> -r <ver> \
  --input samplesheet.csv --outdir results \
  --genome <key> -profile <container>,<executor> -c <custom.config>

## Post-run checklist
MultiQC sections to check | common failure modes | where results land
```
The run executes on the user's compute — report commands, never fabricate results.
