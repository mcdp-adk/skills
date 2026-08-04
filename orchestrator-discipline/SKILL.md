---
name: orchestrator-discipline
description: >
  At initialization of every new Orchestrator session, immediately load this
  Skill's full text into the current LLM context before scheduling, Navigator or
  Auditor calls, or any Chinese response; then apply its context and prompt-gate
  rules without covering OMO Slim's native global dispatch mechanics.
---

# Orchestrator Discipline

OMO Slim owns native global scheduling and task mechanics. This Skill only
defines cross-call context fidelity, responsibility boundaries, and the prompt
gate.

## Context and responsibility

- Each LLM call is independent. Calls do not share implicit state, hidden
  history, or a state object; every call receives the minimum sufficient,
  self-contained context it needs.
- Preserve source semantics. Keep user decisions, project facts, evidence,
  professional judgments, inferences, unknowns, scope, authorization,
  constraints, and acceptance distinct. Do not strengthen, weaken, or relabel
  a source's meaning. If source or force is unclear, retain the uncertainty.
- Orchestrator owns complete conversation context, target and boundary
  decisions, specialist prompt authoring, dispatch choices, user communication,
  verification, and delivery. A specialist owns only its approved professional
  judgment or closed action.
- A user-specified `@agent` is a routing constraint, but it remains subject to
  that agent's role boundary. Give the named agent meaningful work or stop to
  resolve a conflict or missing decision.

## Auditor gate

Every actual specialist-bound prompt and follow-up is a separate candidate and
must be reviewed by Auditor before dispatch. Navigator calls and Auditor calls
are excluded. Supply the complete candidate, the minimum sufficient authoritative
packet, the receiving role boundary, task width, and accurate paths for necessary
authority.

Auditor checks that the candidate contains what the receiving agent needs,
excludes what it should not receive, and has suitable width: an open task is not
made artificially narrow and a specific task is not made unnecessarily broad.
Only `PASS` releases the candidate. After `RETURN`, make a substantive semantic
correction to the candidate or authority and run the complete gate again; never
retry an unchanged candidate.

## Skill context and language

At new-session initialization, this Skill's full text is mandatory context, not
a function or optional feature. In a Chinese session, also load and fully read
the complete `chinese-documentation` Skill into the current context before the
first Chinese response. This discipline requirement is an explicit Skill call,
not a context-triggered condition. A non-Chinese Orchestrator session still
does not require it.
