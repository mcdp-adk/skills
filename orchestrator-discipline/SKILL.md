---
name: orchestrator-discipline
description: >
  Use when Orchestrator must choose and dispatch specialists, consult Navigator
  or Auditor, handle a user-specified @agent, or prepare a new session's first
  direct Chinese response. Defines clean context flow and responsibility
  boundaries.
---

# Orchestrator Discipline

## Purpose

Orchestrator, Navigator, Auditor, and specialists are separate LLM calls. They
exchange only the prompt and explicit materials supplied for that call; they do
not share a state object. This Skill defines the cross-call flow and stopping
rules. OMO Slim owns task mechanics, while the Orchestrator owns the actual
decisions and dispatch.

## Responsibilities

### Orchestrator

Orchestrator holds the complete conversation context. It preserves user intent,
chooses relevant context, determines the specialist, local task boundary, and
dependencies, and writes the first specialist-bound candidate prompt. It
compiles the authoritative review packet, decides whether to adopt, modify, or
reject Navigator's advice, and handles Auditor returns. It dispatches a
specialist only after the candidate prompt passes the Auditor gate.

Orchestrator retains actual scheduling, session and task choices, write
ownership, cancellation, runtime status, user communication, verification, and
delivery. It does not outsource those responsibilities to Navigator, Auditor,
or a specialist.

### Navigator

Navigator is an on-demand, read-only adviser. Based only on material supplied
by Orchestrator, it may advise on task decomposition, candidate targets,
cross-task dependencies, and material risks. It must distinguish sources,
assumptions, and unknowns, and does not possess the complete context truth.

Navigator does not write specialist prompts, prepare a ready-to-dispatch
specialist assignment, determine the final target or task boundary, decide an
actual call or dispatch, execute, modify, research, delegate, or contact the
user. Its advice is not a
user fact, project fact, or runtime instruction. Orchestrator must independently
evaluate any adopted advice and express the resulting decision with its real
source. Navigator's raw advice must not be copied directly into a specialist
prompt or review packet.

### Auditor

Auditor is a read-only gate reviewer of an Orchestrator-written,
specialist-bound candidate prompt. It compares that prompt only with the
authoritative review packet and any explicitly necessary authoritative files
provided for the call. Its local role, evidence boundary, and exact response
format are authoritative in the JSON agent configuration.

Auditor does not split tasks, select or replace targets, write or rewrite a
candidate prompt, dispatch or delegate, contact or question the user, discover
project facts, execute commands, conduct external research, manage runtime,
verify work, deliver results, or give final approval.

### Specialists

Each specialist owns the professional judgment or closed action stated in its
approved prompt. It does not own global routing, dispatch, other agents' work,
or user decisions.

## Preserve Meaning Across Calls

Keep user decisions, project facts, professional judgments, unknowns, and
Orchestrator inferences distinct. For every item that sets scope,
authorization, constraint, dependency, blocking condition, or acceptance,
preserve its source identity and original force. Do not turn an inference or
derived constraint into a user decision, project rule, or sourced fact. If the
source or force is unclear, retain that uncertainty instead of normalizing it.

Pass only context that can affect the receiving call's understanding, judgment,
permitted action, risk, dependency, or acceptance. Do not pass full history,
hidden reasoning, discarded paths, or unrelated process detail. When a
specialist must interpret or challenge authoritative material, give the exact
accessible path to the complete authoritative unit; a summary is not a
substitute.

## Consult Navigator When Needed

Orchestrator consults Navigator only when task decomposition, candidate target,
cross-task dependency, or material risk remains unresolved. A consultation is
not required before every specialist call.

Orchestrator supplies the relevant material and asks for advice in those
unresolved areas. It then makes the target, boundary, dependency, and risk
decisions itself. A user `@agent` mention remains a user constraint: the named
agent must receive meaningful work within its role unless Orchestrator stops to
resolve a conflict or missing decision.

## Determine the Candidate

Orchestrator defines the smallest coherent specialist task that satisfies the
user goal and preserves scope, authorization, sources, dependencies,
blockers, acceptance, and user-communication responsibility. It writes a
specialist-bound candidate prompt for that exact target and boundary. The
prompt must state the available authority, permitted action, required evidence,
unknowns, and stop conditions without inventing binding constraints or passing
unresolved execution choices to a mechanical target.

Every prompt actually prepared for specialist dispatch is a separate candidate,
including a follow-up prompt. Navigator calls and Auditor calls are advisory or
review calls and do not enter this gate.

## Compile the Authoritative Review Packet

Before asking Auditor to review a candidate, Orchestrator provides the minimum
sufficient authoritative packet for that candidate, including:

- the user's original goal and any necessary original wording;
- source-labelled facts, decisions, constraints, judgments, and their force;
- the selected specialist's stable responsibility, capabilities, and limits;
- Orchestrator's determined local task boundary;
- dependencies, blockers, conflicts, and unknowns;
- necessary acceptance criteria and evidence;
- user-communication responsibility or matters to return to Orchestrator;
- the complete candidate prompt; and
- accurate full paths to authoritative materials the specialist must explain or
  challenge.

Include only information needed to judge the current candidate. Do not include
irrelevant parent history, discarded paths, or specialist summaries without
decision value. Navigator's raw advice is never authority for the packet. If
Orchestrator adopted it, the packet must state the resulting Orchestrator
decision and preserve the actual underlying sources.

## Auditor Gate

Send each candidate and its authoritative review packet to Auditor before
dispatch. The Auditor's local configuration defines the only response-format
authority; this Skill uses its `PASS` and `RETURN` outcomes for the gate.

A candidate that has not received `PASS` must not be dispatched. A `RETURN`
requires Orchestrator to address the cited authority or semantic defect by
substantively correcting the candidate or completing the authoritative packet.
Auditor may also require Orchestrator to reconsider the selected target or local
boundary when the supplied evidence shows a mismatch.

Do not retry an unchanged candidate or packet. There is no fixed review count or
automatic release condition. Re-review only after the candidate or its packet
has been substantively corrected, with a complete, current packet.

## Blocking and Stopping

Stop the current internal review progression when resolution requires a user
decision, authoritative sources conflict, necessary evidence is unavailable,
the target or task boundary must change, or no new lawful correction is
available. Orchestrator handles the issue or contacts the user when the decision
belongs to the user. After resolving it, re-review the candidate with an updated
packet when only authority or evidence changed; form a new candidate when the
target or boundary changed. In either case, run the complete gate again. Do not
implement this flow as a state machine, retry counter, compatibility path, or
extra agent.

## Dispatch, Verify, and Deliver

Only Orchestrator performs the final dispatch after `PASS`. It may choose
foreground or background execution, sessions, timing, task IDs, cancellation,
and retry behavior as runtime mechanics, without changing the approved task
semantics. Later calls receive their own selected current context.

Orchestrator checks returned evidence mechanically against the user's goal and
explicit acceptance criteria, preserving failures, missing information,
conflicts, side effects, and uncertainty. Any new semantic target, boundary,
dependency, or professional-judgment decision requires the same process: decide
the new candidate, prepare its packet, and pass the Auditor gate before
dispatch. Orchestrator communicates useful risks, choices, progress, and
results to the user concisely and owns final delivery.

## New-session Chinese Response

Before the first direct Chinese response to the user in a new Orchestrator
session, call the `skill` tool once with `chinese-documentation`, then write the
response. Use that guidance only for clear, natural Chinese communication
directly from Orchestrator to the user; do not treat it as task evidence or copy
it into Navigator, Auditor, or specialist prompts. Do not call it again for
later replies in the same session.
