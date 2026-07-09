---
name: eli5
version: 1.0.0
description: Explain any concept like the listener is five years old - simple words, one concrete analogy, no jargon, without being condescending.
triggers:
  - eli5
  - explain like i am five
  - explain this simply
  - simple explanation
  - break this down for me
capabilities: []
inputs:
  - name: concept
    required: true
    description: The concept, text, or question to explain simply.
  - name: audience
    required: false
    description: Optional real audience (e.g. "my mom", "a new intern") to calibrate tone.
---

# ELI5

## Purpose
Turn any explanation into one a smart child (or a busy adult outside the field) instantly gets: short sentences, everyday words, one strong analogy.

## Hard rules
1. **One core analogy.** Pick a single everyday comparison and carry it through. Do not stack three different metaphors.
2. **No jargon without translation.** Every technical term must be replaced or immediately explained in parentheses using everyday words.
3. **Short.** Three to six short paragraphs maximum. If the input is a question, answer it in the first sentence.
4. **True.** Simplification must not become wrong. If precision is lost, add one line at the end starting with "The fine print:" noting what was simplified.
5. **Never condescending.** No "it's really easy!", no baby talk. Respect the reader; simplify the idea, not the person.

## Workflow
1. Identify the ONE thing the person actually needs to understand.
2. Choose the analogy closest to daily life (kitchen, traffic, school, money, weather).
3. Explain in this order: what it is, why it matters, how it works, what would happen without it.
4. End with the one-sentence takeaway, bolded.

## Example
**Input:** What is DNS?

**Output:**
DNS is the internet's phone book. You know your friend's name, not their phone number - your phone looks the number up for you. Same thing: you type a website's name, and DNS quietly looks up the numeric address computers actually use.

Why it matters: without it, you would have to memorize strings like 142.250.72.14 instead of just google.com.

**Takeaway: DNS turns names people remember into numbers computers need.**

The fine print: real DNS is a chain of several lookups with caching along the way, not one big book.
