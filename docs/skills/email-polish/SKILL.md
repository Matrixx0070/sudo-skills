---
name: email-polish
version: 1.0.0
description: Rewrite the owner's raw email drafts into a warm, friendly-but-professional tone without changing intent, facts, names, dates, or requests.
triggers:
  - polish this email
  - email-polish
  - make this email sound better
  - rewrite my email
  - friendly professional email
capabilities:
  - fs.read
inputs:
  - name: raw_email
    required: true
    description: The owner's draft email text to polish.
  - name: recipient
    required: false
    description: Who the email is going to (name/role) to calibrate formality.
  - name: context
    required: false
    description: Any extra situational context (relationship, prior thread, goal).
---

# Email Polish

## Purpose
Take a rough or blunt email draft and return a version that reads as **friendly but professional** — warm, clear, and respectful — while preserving the original meaning exactly.

## Hard rules (never break)
1. **Preserve intent.** Do not add promises, commitments, dates, prices, or requests that were not in the original.
2. **Preserve facts.** Keep every name, date, number, link, and specific detail unchanged.
3. **No invented content.** If a detail is missing (e.g. a meeting time), leave a clearly marked placeholder like `[time]` rather than guessing.
4. **Keep it the owner's message.** Improve tone and flow, not the substance or the decision.
5. **Match length sensibly.** A short note stays short. Don't pad a two-line email into five paragraphs.

## Tone target
- Warm opening, but not gushing. One friendly line max before the point.
- Direct and clear in the middle — say what's needed without hedging.
- Courteous close ("Thanks", "Appreciate it", "Best") calibrated to the recipient.
- Contractions are fine (it's, I'll). Avoid corporate filler ("per my last email", "circling back", "synergy").
- Never passive-aggressive. If the draft is frustrated, soften the edge while keeping the point firm.

## Formality calibration
- **Unknown / senior / external recipient** → slightly more formal: full greeting ("Hi Dr. Lee,"), no slang.
- **Known colleague / friendly** → relaxed: "Hey Sam," casual sign-off.
- If `recipient` is not provided, default to a safe, universally-appropriate friendly-professional register.

## Workflow
1. Read `raw_email`. Identify: the core ask, key facts, and the emotional register.
2. Rewrite paragraph by paragraph, keeping structure unless it's genuinely unclear.
3. Fix grammar, spelling, and awkward phrasing.
4. Ensure a clear subject line exists — if none, propose one prefixed with `Subject:`.
5. Return the polished email only. If any placeholder was inserted, list them in a short `Notes:` line below.

## Output format
```
Subject: <line>

<polished email body>

Notes: <only if placeholders or judgment calls were made; omit otherwise>
```

## Example
**Input (raw):**
> hey need the report by friday its late again. send it.

**Output:**
```
Subject: Report — Friday deadline

Hi [name],

Hope you're doing well. Just a quick note — could you get the report over to me by Friday? It's slipped a couple of times now, so I want to make sure we stay on track this week.

Thanks a lot,
[Your name]
```
