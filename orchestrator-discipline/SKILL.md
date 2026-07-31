---
name: orchestrator-discipline
description: >
  OMO Slim delegation discipline for reconciling changed task state,
  assembling minimal self-contained handoffs, consulting Navigator when
  advertised, and validating task contracts before dispatch. Use whenever
  substantive work is being delegated, user or subagent input invalidates a
  prior assumption or decision, or a contract must be rewritten, split, or
  re-scoped—even when the route initially looks obvious.
---

# Orchestrator Discipline

## Purpose and Ownership

OMO Slim's injected prompt remains authoritative for global routing,
scheduling, background work, session reuse, verification, and user
communication. This Skill adds a personal discipline for reconciling the
current task state and using Navigator as a focused planning adviser.

The Orchestrator retains final ownership of the work graph, agent choice,
task contract, dispatch, conflict resolution, and user outcome. Navigator
may propose a decomposition, dependency order, specialist choice, candidate
contract, or blocker. Its output is advice, not approval or instruction.

Use `agent-capabilities` for maintained knowledge about agent fit, Skill
loading, and target-side method access. Do not duplicate that catalog here.

Before agent fit, Skill visibility, loading responsibility, or target-side
method access affects a judgment, load `agent-capabilities` in full when it is
available. This is conditional, not an automatic pre-load. If loading fails or
the Skill is unavailable, use explicit current OMO facts. Stop and report any
uncertainty that could change correct routing; retain and continue past only
minor uncertainty already known not to affect the target, permissions, or
route.

## Current-State Reconciliation

Before consequential user or subagent input changes orchestration, recover
only the compact, revisable prior basis relevant to that change. Preserve
material unknowns and alternatives rather than inventing a baseline.

Examine decision authority, factual support, and applicable scope
separately. A user decision controls matters the user owns, but does not
settle separate factual questions. Other claims and recommendations change
only what their evidence and scope reach.

Only reconciled state may enter Navigator or a formal handoff. Direct
counter-evidence or an invalidated premise reopens the affected judgment;
unaffected boundaries and supported conclusions remain.

## Handoff Invariants

Every candidate and final handoff must satisfy three conditions:

- **Minimum connected context.** Every included item must shape
  understanding, judgment, permission, action, or acceptance. Remove
  background that changes none of them.
- **Separate reasoning freedom from action authority.** Permission to test a
  premise or propose an alternative does not grant permission to change user
  goals, reserved decisions, scope, or high-consequence actions.
- **Independent closure.** A fresh target session, using only its static
  role, contract, and explicit materials, must know how to start, what it may
  do, what to deliver, and when to stop.

## Prepare the Current-State Packet

For a substantive new or changed delegation, prepare the smallest packet
that preserves the current causal chain:

- the current objective and the work unit's intended contribution;
- user-confirmed and reserved decisions;
- supported facts, material unknowns, and open questions;
- completed direct dependencies and the evidence they produced;
- applicable constraints, project instructions, and existing write
  ownership;
- exact materials and reachable paths, with their source identity;
- the current acceptance boundary and failure consequences.

Materialize upstream results as facts, artifacts, evidence, and remaining
uncertainty. Do not pass full history, process narration, the raw background
task board, unrelated task IDs, other agents' internal state, or unresolved
conflicts.

## Navigator-Assisted Delegation

When a substantive delegation needs nontrivial decomposition, dependency
ordering, specialist choice, or contract synthesis, consult Navigator before
finalizing it if Navigator is advertised in the current Orchestrator routing
guidance. Do not infer availability from a static catalog or probe by issuing
a speculative task: a probe either hard-fails or creates a real child session
and task-board state. Follow OMO's direct-execution and coordination-cost
gates when the route and contract are already clear.

Give Navigator the current-state packet and ask for candidate decomposition,
dependency order, specialist choices, contracts for work that is ready now,
and blockers. Then:

1. reconcile the proposal with current user decisions, runtime task state,
   write ownership, actual permissions, and unresolved conflicts;
2. remove stale or unsupported recommendations and add material runtime facts
   Navigator could not observe;
3. retain final responsibility for the work graph and each formal contract;
4. dispatch only the work whose prerequisites are satisfied;
5. when new evidence materially changes a premise, dependency, scope, or
   specialist choice, consult Navigator again when the same conditions apply.

Use OMO's current lifecycle rules to decide whether a Navigator session may be
reused. On every reuse, provide the latest decisions, changed boundaries, and
current increment explicitly. Never rely on hidden memory. Do not pass
Navigator's internal reasoning to target agents because it is uncoordinated
advice that could be mistaken for final direction.

## Direct Compilation Fallback

If Navigator is not configured, unavailable, or fails, the Orchestrator must
still be able to complete the delegation. Use OMO's current routing guidance
and, when available, `agent-capabilities`; obtain every relevant current
method body before it affects routing, scope, or acceptance.

Define the work unit, select a capable target, calibrate reasoning freedom and
action authority, resolve applicable Skill and project constraints, and
compose a self-contained contract. Rewrite or split the work when that
resolves a conflict without changing the user objective or a reserved
decision. Otherwise stop and ask the user.

Do not infer capability from a stale projection.

## Final Handoff Acceptance

Before dispatch, confirm that the contract preserves the reconciled
current-state packet without unresolved conflicts or irrelevant history. It
must state the target's reasoning freedom and action authority, required
contribution, output, acceptance evidence, failure behavior, and stopping
condition. Materialize applicable Skill requirements rather than passing a
dangling Skill name, and coordinate any Navigator proposal with current
runtime state.

Use `agent-capabilities` when agent fit, Skill visibility, loading
responsibility, or target-side method access affects the contract. A Skill or
file read never expands the target's role, tools, or permissions. If a required
source cannot be identified or reached, stop instead of guessing.

## Session and Stop Rules

- A new session receives no hidden parent history. A reused session still
  receives the latest decisions, changed boundaries, and current increment.
- Do not pass full scheduling history, rejected alternatives, irrelevant
  materials, or another agent's internal state.
- Exact paths supplied for reading must be reachable in the target session.
- Missing user decisions, unresolved Orchestrator-level conflicts, unknown
  capability that could change routing, or unavailable required sources are
  blockers, not invitations to improvise.
