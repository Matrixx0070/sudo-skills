---
name: ops-process-doc
version: 1.0.0
description: Document a process with a flowchart, a RACI matrix, and a standard operating procedure.
author: matrixx0070
tags: [operations, process, sop, raci, documentation]
capabilities: []
---

# Process Documentation

## When to use
Use this to capture how a repeatable process actually runs so it can be trained, audited, or handed off, and whenever tribal knowledge needs to become a durable, followable SOP.

## METHOD
1. **Frame the process.** State its name, purpose, trigger (what starts it), and definition of done.
2. **Identify actors.** List every role that touches the process; you will map them in the RACI.
3. **Map the steps.** Walk the process end to end. For each step capture the action, the actor, inputs, outputs, and decision points.
4. **Draw the flowchart.** Render the sequence as a Mermaid `flowchart` with decision diamonds for branches.
5. **Build the RACI.** For each step assign Responsible, Accountable, Consulted, Informed — exactly one Accountable per step.
6. **Write the SOP.** Turn steps into numbered, imperative instructions with tools, timing, and quality checks.
7. **Add controls.** Note exceptions, escalation paths, and where errors are caught.

## OUTPUT FORMAT
- **Overview:** name, purpose, trigger, done-when, frequency.
- **Flowchart:** Mermaid `flowchart TD`.
- **RACI matrix:** rows = steps, columns = roles.
- **SOP:** numbered steps with owner, tools, expected duration, quality check.
- **Exceptions & escalation.**
- **Revision info:** owner, version, review cadence.
