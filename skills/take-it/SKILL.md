---
name: take-it
description: Prepares, verifies, and reviews a change in isolation before presenting the finished candidate for final sign-off. Use when direction is agreed and the user hands off execution until the result is ready to approve.
disable-model-invocation: true
---

# Take It

Carry an agreed direction from discussion to a single, sign-off-ready candidate without pulling the user into intermediate iterations.

## Process

### 1. Stage in isolation

Prepare the change where the live target and external systems remain untouched until the user approves, so inspecting or discarding the candidate has no live side effects.

Reshape the touched structure so the change fits as if it were always meant to be there, rather than layering a patch over existing structure.

### 2. Verify

Run the checks and validations that apply to the touched work and resolve every failure. Passing checks prove only what those checks test; they do not by themselves prove that the change fulfills the user's intent.

### 3. Review as a gate

Have an independent reviewer with a fresh context check the staged candidate against the user's intent, giving it everything needed to judge the candidate without relying on this conversation.

Treat the review as a sanity gate that catches blind spots, not as an authority to loop until zero findings:

- Fix findings that establish a genuine defect against the agreed intent, and re-run the review only when a fix materially changes the candidate.
- When a finding does not establish a genuine defect against the agreed intent, clarify the missing context once or set the finding aside, rather than spinning in review loops or distorting the design to appease the reviewer.

### 4. Present for sign-off

Once verification passes and the review gate is clear, open the full candidate outside chat for inspection rather than pasting full diffs into the conversation. In chat, give the user a concise, concrete summary of what changed and why, what is verified, and what remains unverified or traded off, then wait for approval before applying the change.
