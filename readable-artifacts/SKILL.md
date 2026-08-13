---
name: readable-artifacts
description: Plan and revise file-level structure for code, documentation, configuration, and prompts so people and agents can understand them quickly. Use when responsibilities are mixed, reading paths are unclear, a hand-authored file approaches or exceeds roughly 200 lines, or a task requires decisions about splitting, merging, naming, or references.
metadata:
  internal: true
---

# Readable Artifacts

Readable structure lowers comprehension cost: readers can identify a file's purpose, find what the current task needs, and understand how related material fits together. Length is only one factor in that result.

## Understand the current structure

Before changing structure, identify the file's purpose, readers, responsibilities, important constraints, and entry points. Inspect callers, neighboring files, and actual usage until you can explain why the content belongs where it is.

Do not reorganize content based only on length or appearance while its existing relationships remain unexplained. That usually moves complexity instead of reducing it.

## Set semantic boundaries

A file should answer one coherent question or hold responsibilities that change together. Use that principle to decide:

- Keep definitions, rules, exceptions, and verification guidance near where they first matter.
- Keep material together when it must be read together to make sense. Split material that can be named independently, change independently, or serve a different reader.
- Keep one authoritative expression of each meaning. Elsewhere, use a pointer that states what the target contains and when to read it instead of copying the content.
- Name files and directories for their actual purpose. Broad names such as `utils`, `common`, and `helpers` tend to accumulate unrelated responsibilities.

Judge a split by the resulting reading path. If understanding one invariant, following a short procedure, or changing one local behavior requires repeated jumps across files, the boundaries may be too fine.

## Treat roughly 200 lines as a soft review point

The roughly 200-line figure originated as practical guidance for `CLAUDE.md` files loaded fully into Claude Code context: long persistent instructions consume attention and reduce adherence. Anthropic's context-engineering guidance further treats context as a finite attention budget that should contain the smallest high-signal set sufficient for the task.

This Skill extends roughly 200 lines into a soft review point for hand-authored text artifacts, including source code, rather than a universal limit. People and agents must scan, locate, and combine meaning in both code and documentation; near this scale, check whether multiple semantic units have accumulated. The number does not prove quality. Semantic cohesion remains the stronger criterion.

When a file approaches or exceeds this scale, consider these steps in order:

1. Remove stale or duplicated material, and remove other material only when it supports neither understanding nor behavior.
2. Extract genuinely independent responsibilities, reader branches, or long reference material, and leave a clear pointer.
3. Recheck navigation cost from the reader's entry point. Undo the split if it hides prerequisites or increases cross-file coupling.

Do not apply this review point to generated files, source material preserved verbatim, or files constrained by an external format. Content that must be understood together may also exceed roughly 200 lines when preserving the complete semantic unit is easier to read than splitting it.

For the underlying treatment of attention budgets, progressive disclosure, and just-in-time retrieval, read [Anthropic's context-engineering article](references/effective-context-engineering.md).

## Check the result

Review the result from the actual consumer's entry point. Confirm that each file's purpose is clear, related material remains close enough, and names and pointers guide later reading. Keep code behavior, links, loading order, and format constraints valid; an artifact is not more readable if it no longer works correctly.
