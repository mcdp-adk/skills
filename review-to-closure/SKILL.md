---
name: review-to-closure
description: Goal-anchored review and fix–verify–re-review workflow for code, documents, configurations, plans, and other artifacts. Use after non-trivial changes when review is requested or required, after addressing review findings, before declaring reviewed work complete, or whenever review must cover the cumulative result rather than only a checklist, latest diff, or previous findings.
---

# Review to Closure

Review the complete cumulative result against the original final purpose. Continue through accepted fixes, proportionate verification, and full re-review until no unresolved material findings remain or an explicit authority decision ends the loop.

## Core model

- **Goal-anchored:** Keep the original final purpose, settled boundaries, and authorization as the basis for every round. Findings help achieve that purpose; they do not replace it.
- **Bounded-open:** Keep authority and task boundaries closed while leaving the issue space open. Known concerns are starting points, not an exhaustive checklist.
- **Cumulative:** Review the current complete result and the context needed to judge it, not only the latest diff, excerpt, or previous findings.
- **Evidence-based:** Read reachable authority sources directly. Distinguish verified facts, reasoned findings, suggestions, and unresolved uncertainty.
- **Review plus verification:** Review can expose defects and missing evidence, but it does not replace tests or other behavior-level verification.

## Establish the review contract

Before the first review, make these items explicit:

- the original final purpose and the decision the review must support;
- the complete cumulative result under review;
- settled boundaries, authorization, and explicit exclusions;
- authority sources, required reads, and relevant verification evidence;
- known concerns, clearly marked as non-exhaustive;
- the materiality threshold for findings.

A **material finding** is one that could change the decision or materially affect purpose fit, correctness, security, data integrity, maintainability, operability, or another quality required by the task. Taste and optional improvement do not block closure unless the review contract makes them material.

The review contract is logical state, not necessarily a file. Keep it stable across rounds unless the user or another authority changes the purpose, boundaries, or acceptance conditions.

## Perform the review

Inspect enough of the target and its relevant relationships to support the decision. Do not expand into unrelated work, but do not let a supplied checklist become the ceiling of the review.

Evaluate purpose fit first: determine whether the cumulative result actually achieves the original final purpose within the settled boundaries. Then examine material risks, hidden assumptions, regressions, unintended consequences, missing evidence, and viable simplifications or alternatives that could change the decision.

For every material finding, provide:

- the affected part of the cumulative result;
- supporting evidence;
- the causal impact on the original purpose or required quality;
- any important uncertainty.

End each review with one clear outcome:

- **PASS:** no unresolved material findings remain within the review contract;
- **CHANGES_REQUIRED:** one or more material findings require disposition;
- **BLOCKED:** missing authority or evidence prevents a reliable judgment.

Non-blocking suggestions may accompany PASS, but must remain distinguishable from material findings.

## Disposition findings

Do not implement every finding automatically. A participant with appropriate task authority must give each material finding an explicit disposition. A finding does not grant modification authority: accept and fix it only within existing user or task authorization; otherwise request authority or escalate.

- accept it and fix it within existing authorization;
- reject it with evidence;
- mark it outside the settled scope;
- explicitly accept the risk through appropriate authority;
- escalate it because authority or evidence is missing.

Unresolved or silently ignored material findings prevent closure.

## Fix and verify

Apply only accepted fixes within the task's authorization. After fixing, run verification proportionate to the changed behavior and risk. Preserve enough evidence to show what changed, what was checked, and what remains uncertain.

A fix is not closure. It changes the cumulative result and can expose or introduce other problems.

## Re-review the complete result

After every material finding has an explicit disposition, decide the next step. If accepted findings require fixes, apply them and complete proportionate verification. If no fix is authorized or required, proceed with the disposition evidence. Then review again using the original review contract and the current complete cumulative result. Provide previous findings, their dispositions, and relevant verification evidence as history, not as the new scope.

The re-review must:

- confirm that accepted findings were resolved without violating the original purpose;
- reconsider the whole cumulative result under the same materiality standard;
- independently look for additional material findings;
- avoid limiting itself to the latest changes or prior findings.

The standard must remain stable; the reviewer identity does not have to. Reusing a reviewer preserves context, while a fresh independent reviewer can reduce anchoring when risk justifies the additional cost.

Repeat disposition → authorized fix and verification when needed → full re-review while material findings remain and the task still authorizes correction.

## Close or escalate

Close the loop only when:

- the latest review returns PASS;
- no accepted material finding remains unresolved;
- findings outside the fix path have explicit, authorized dispositions;
- verification evidence is sufficient for the task's risk and scope;
- the cumulative result still serves the original final purpose.

PASS is scoped assurance, not a claim of absolute defect absence. Without a new PASS, only an explicit authority decision—accepted risk, an authorized scope or purpose change, or escalation of a BLOCKED or non-converging review—can end or redirect the loop.

Escalate instead of looping indefinitely when findings repeat without progress, fixes oscillate, reviewers apply conflicting standards, new criteria appear without authority, or evidence cannot resolve the disagreement.

## Preserve only necessary state

Use the lightest carrier that preserves the review contract, findings, dispositions, verification evidence, and current outcome accurately:

1. Keep them in the active context for small, single-session reviews.
2. Update an existing authoritative task, issue, plan, or state artifact when one already exists.
3. Create a dedicated checkpoint only when work crosses a context boundary, handoff or compaction is likely, findings become too complex to carry accurately, or an audit record is required.

Do not create a project file solely to satisfy this workflow. Before a context boundary, persist enough state for another session to resume without reconstructing decisions from memory.

## Review handoff brief

When handing the review to another participant, changing reviewers, or crossing a context boundary, pass the review contract in the following shape. Use it as message content by default; persist it only under the rules above. On later rounds include previous findings and dispositions; omit that section on the first review.

```markdown
## Original final purpose and decision

## Complete cumulative result

## Settled boundaries, authorization, and exclusions

## Authority sources, required reads, and verification evidence

## Known concerns
Starting points, not an exhaustive checklist.

## Materiality threshold

## Previous findings and dispositions

## Review mandate
Review the complete cumulative result against the original purpose. Identify any
additional material issue within the settled boundaries that could change the
decision. Do not limit the review to known concerns, the latest diff, or previous
findings.

## Required outcome
Return PASS, CHANGES_REQUIRED with material findings, or BLOCKED with the missing
authority or evidence.
```
