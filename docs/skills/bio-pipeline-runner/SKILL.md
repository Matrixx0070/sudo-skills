---
name: bio-pipeline-runner
version: 1.0.0
description: Plan and execute an nf-core bioinformatics pipeline (rnaseq, sarek, atacseq) with a validated samplesheet and profile.
author: matrixx0070
tags: [nf-core, nextflow, rnaseq, sarek, pipeline]
capabilities: []
---

When to use: the user wants to run a standardized nf-core pipeline on sequencing data and needs the samplesheet, config, and command assembled correctly the first time. Use for rnaseq (expression), sarek (variant calling), or atacseq (chromatin accessibility).

METHOD
1. Confirm the pipeline choice against the biological question and the assay: rnaseq for DGE/quantification, sarek for germline/somatic variants, atacseq for open chromatin.
2. Pin the version (`-r <release>`) for reproducibility and pick the reference genome (iGenomes key or explicit FASTA/GTF).
3. Build the samplesheet in the pipeline's exact schema: rnaseq uses sample,fastq_1,fastq_2,strandedness; sarek uses patient,sample,lane,fastq_1,fastq_2; atacseq uses sample,fastq_1,fastq_2,replicate. Validate paths and paired-end pairing.
4. Choose an execution profile: docker/singularity/conda for containers plus an executor (local/slurm) and resource limits (`-c` custom config) matched to the machine.
5. Dry-run with `-stub` or `-profile test` to catch schema errors before burning compute.
6. Launch, then inspect the MultiQC report and pipeline_info execution report for failures and resource waste.

OUTPUT FORMAT
- Chosen pipeline, version, and genome with rationale.
- The validated samplesheet.csv.
- The full `nextflow run nf-core/<pipeline>` command with profile, params, and outdir.
- Post-run checklist: MultiQC sections to inspect, common failure modes, and where results land. Note that the run itself must be executed by the user's compute; report commands, do not fabricate results.
