---
name: tldr
version: 1.0.0
description: Compress any long text, article, or thread into a one-line takeaway plus the few points that actually matter - without losing caveats that change the meaning.
triggers:
  - tldr
  - tl;dr
  - summarize this
  - give me the short version
  - key points only
capabilities: []
inputs:
  - name: text
    required: true
    description: The long text, article, or thread to compress.
  - name: focus
    required: false
    description: Optional angle to prioritize (e.g. "costs", "risks", "what changed").
---

# TLDR

## Purpose
Give the reader the 30-second version they can act on, not a book report.

## Hard rules
1. **One-line takeaway first.** A single bolded sentence a busy person could forward as-is.
2. **Three to six bullets max.** Each bullet is one fact or decision, not a paragraph.
3. **Keep meaning-changing caveats.** If the source says "X, unless Y", the summary must not say just "X". Dropping a qualifier that flips the conclusion is a failure.
4. **Numbers survive.** Dates, prices, versions, percentages carry over exactly; never round away a figure someone would act on.
5. **No new claims.** Nothing appears in the summary that is not in the source. If the source is ambiguous, say "unclear" rather than guessing.

## Workflow
1. Identify the single conclusion or event the text exists to convey.
2. Pick the supporting facts a reader needs to trust or act on it.
3. If `focus` is given, reorder so that angle leads.
4. End with "Worth reading in full if:" and one honest criterion, so the reader knows when the summary is not enough.

## Output format
```
**TLDR: <one sentence>**

- <point>
- <point>
- <point>

Worth reading in full if: <criterion>
```

## Example
**Input:** a 2,000-word vendor security bulletin about a patched vulnerability.

**Output:**
**TLDR: Versions 4.2-4.7 leak session tokens via the export endpoint; patch to 4.8 or disable exports until you do.**

- Exploitable without login, but only when the export feature is enabled (off by default).
- Patch 4.8 released 2026-07-08; no workaround besides disabling exports.
- Vendor says no known exploitation in the wild so far.

Worth reading in full if: you run a custom build or need the CVE details for compliance reporting.
