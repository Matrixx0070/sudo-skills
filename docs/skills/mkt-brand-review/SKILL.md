---
name: mkt-brand-review
version: 1.0.0
description: Review marketing content against a brand voice and style guide, flagging deviations by severity with concrete fixes.
author: matrixx0070
tags: [marketing, brand, review, copyediting, quality]
capabilities: []
---

When to use this skill when you have a piece of content (blog, email, ad, landing page, social post) and a brand voice or style guide, and you need an objective audit of how well the content conforms before it ships.

METHOD

1. Load the reference. Extract the brand's voice attributes (tone, personality), style rules (grammar, casing, punctuation, terminology, banned words), and formatting conventions. If no guide is supplied, ask for one or infer a baseline from sample on-brand content and state that assumption.
2. Read the target content in full once for overall impression before line-level analysis.
3. Check voice: does tone match (e.g., confident not arrogant, warm not casual)? Note mismatches with quotes.
4. Check style mechanics: terminology, product names, capitalization, Oxford comma, numerals, banned/discouraged words.
5. Check structure and formatting: headline conventions, CTA phrasing, length norms, accessibility (alt text, reading level).
6. Assign each finding a severity: CRITICAL (off-brand, factual, or legal risk), MAJOR (noticeable voice/style break), MINOR (polish).
7. Give a fix for every flag, not just a complaint.

OUTPUT FORMAT

- Summary: overall on-brand score (0-100) and one-line verdict.
- Findings table: Severity | Location/quote | Issue | Suggested fix.
- Grouped by CRITICAL, MAJOR, MINOR.
- Quick wins: top 3 highest-impact edits.
- Sign-off recommendation: ship / revise / block.
