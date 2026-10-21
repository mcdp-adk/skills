---
name: migrate-practices
description: Rebuilds the working practices of reference repositories in a target repository, implementing each one anew for the target. Use when bringing practices from existing repositories into another repository.
disable-model-invocation: true
---

# Migrate Practices

A **practice** is anything in a repository that decides how work there is done, as opposed to what the repository delivers. Each practice serves a **root need**: an outcome it secures for the owner. Carry the root needs into the target and implement each one anew; a reference implementation is one earlier answer, kept only where it is already the best fit for the target.

## Process

### 1. Explore

Establish every fact yourself, by reading, by delegated research, and by experiment; ask the owner only for decisions.

- **References**: classify every tracked file of each reference repository, and every hosting-platform setting you can read, as practice or content. For each practice, record what it does, its root need, and how the reference implements it. The step is done when nothing in the references is left unclassified.
- **Target**: record what the target already has, what its toolchain can run, and which artifacts already have a form defined by a tool or skill the target uses.
- **Scope**: a practice moves unless the target lacks what it governs.

### 2. Present findings and ask

Summarise the practices as a list of practice, root need, reference implementation, and whether it moves, with the reason when it does not. Ask the owner to confirm the list and to add practices that live outside the references.

Then take each practice whose design branches, one at a time. Lead with the recommended answer so the owner can accept it in a word. Skip any question a settled answer already decides.

### 3. Design

Design each practice from its root need. Pick the earliest point on the path of the agent's output where the target decides the practice completely:

- **Settled**: the target's own configuration makes the conforming outcome the default or the only one reachable.
- **Checked**: a check decides the practice when the agent produces the output, and its failure names the rule and the fix. A check fails only on a violation; a missing tool fails with the step that provides it. A check whose result arrives after the agent has moved on binds the agent only through a completion criterion that waits for it.
- **Written**: what no configuration or check decides completely is written for the agent as a principle that decides cases nobody foresaw. A check that decides only part of a principle is replaced by the principle, since passing it would certify the cases it misses.

Where a tool or skill defines an artifact's form, use that form and its wording, changing only what the artifact's medium requires. The step is done when every moving practice has a design, and every check has been tried against a violation and a conforming case.

### 4. Confirm

Show the owner a plain-language table of practice and implementation, then the full content of every file and every setting change. Let them edit before writing.

### 5. Write

Write each document by the `writing-for-agents` skill: every line changes an agent's behavior against its default, and states the rule rather than its history or its mechanism. Match the style of the target's agent documents, or the owner's global ones when the target has none. Apply the settings, rerun every check against a violation and a conforming case, and land the change through the target's own route.

### 6. Done

Report what moved and how, what did not move and why, and anything left unverified.
