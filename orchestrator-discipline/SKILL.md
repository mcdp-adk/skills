---
name: orchestrator-discipline
description: >
  OMO Slim personal difference layer for consequential input
  reconciliation and delegation-prompt compilation. Provides a
  user-maintained local Agent–Skill binding, mandatory Skill pre-reading,
  and processes for reconciling material new inputs against the prior task
  state and composing task contracts that coordinate Skill requirements
  with current boundaries and decisions. Trigger when new user or subagent
  input could materially change an orchestration judgment, scope,
  constraints, or a subsequent delegation; when the Orchestrator considers
  or modifies a substantive delegation, selects candidate agents,
  establishes lane scope, or composes a task contract or acceptance
  criteria; or when the user names this Skill.
---

# Orchestrator Discipline

## Purpose

This Skill is the personal difference layer between the Orchestrator
and the underlying OMO Slim harness. OMO Slim's static prompts and
runtime injection already define agent roles, routing thresholds,
background tasks, task appending, session reuse, design handoffs,
cancellation, verification, and communication rules. This Skill does
not duplicate those rules. It adds three personal disciplines: a
user-maintained local Agent–Skill binding, reconciliation of
consequential user and subagent inputs against the prior task state,
and mandatory reading of relevant Skills before delegation followed by
compilation of their requirements into effective task contracts.

## Mandatory Pre-Load: chinese-documentation

Every time this Skill is loaded, you must immediately call the `skill`
tool to load `chinese-documentation` in full before proceeding. This
is unconditional. Do not begin substantive analysis, write user-facing
responses, or dispatch subagents until `chinese-documentation` has
loaded successfully. If the load fails, stop and report the blockage
explicitly.

**Coverage.** The Chinese documentation rules govern everything you
write directly — your communications with the user and the task briefs
you write for subagents. In Chinese contexts, write naturally and
straightforwardly. Avoid jargon. Do not use English words simply to
sound professional.

**Single source.** `chinese-documentation` is the sole source for
detailed language and formatting rules. The high-level goals above
describe the intended outcome; they do not constitute a second set of
rules. Do not copy detailed conventions, terminology lists, examples,
or checklists from that Skill into this one.

**Target-side boundary.** Do not instruct subagents that lack a
configured `chinese-documentation` Skill to load it. Your own task
briefs and handoffs must follow the Chinese documentation rules
directly. For subagents that produce user-facing output and do have the
Skill configured, relay language requirements through task acceptance
criteria rather than duplicating the rules inline.

## Local Agent–Skill Binding

This section is a user-maintained projection of native Skill
configuration: which agents have which Skills configured, their
visibility, and `skill` tool loading responsibility. It is not a
registry of all readable method files, not a general file-read
permission table, and not an ad-hoc task path record. Every OMO
configuration change must be reflected here.

| Agent | Configured Skills | Loading Responsibility |
|-------|-------------------|----------------------|
| Oracle | `simplify` | Oracle's static prompt does **not** load it automatically. For any task that substantively needs simplification review, the delegation prompt must explicitly instruct Oracle to load `simplify` before review. |
| Librarian | `grok-search` | Librarian's static prompt does **not** load it automatically. For any task that substantively needs current information, real-time data, X/Twitter search, or live fact-checking, the delegation prompt must explicitly instruct Librarian to load `grok-search` before research. |
| Designer | `agent-browser` | Designer's static prompt does **not** load it automatically. For any task that substantively needs browser or Electron interaction, the delegation prompt must explicitly instruct Designer to load `agent-browser` before proceeding. |
| Committer | `conventional-commit` | Committer's static prompt loads it at task start. You do not instruct Committer to load it. |
| Writer | `documentation-writer`, `chinese-documentation` | Writer's static prompt loads both Skills at task start. You do not instruct Writer to load them. |
| All other currently configured OMO subagents | (none) | — |

The Orchestrator has access to all configured Skills and may use
trusted exact paths provided by the user or current task. This does
not change the routing rules injected by OMO Slim.

## Consequential Input Reconciliation

Before consequential new user or subagent input changes orchestration,
recover from the prior task state only the compact, revisable basis
relevant to that change. Preserve material unknowns and alternatives;
when no prior support exists, remain open rather than inventing a
baseline.

Examine the input separately for decision authority, factual support,
and applicable scope. An explicit user decision controls matters the
user owns, but decision authority does not resolve separate factual
questions. Other claims and recommendations change only what their
support and scope reach.

Only the reconciled result may enter orchestration or a handoff. Before
applying a material change, identify its basis and effect boundary.
Direct counter-evidence or an invalidated premise must reopen the affected
judgment; unaffected boundaries and supported conclusions remain.

## Delegation-Prompt Compilation Process

Before every substantive delegation, compile the minimum context the
lane needs — no more, no less. Every item must earn its place by
shaping understanding, permissions, action, or acceptance. Three
invariants guide every choice:

- **Compile the minimum connected context.** Each included item must
  produce, support, constrain, preserve open questions, orient, or
  verify the current work. Drop background that would not change
  understanding, judgment, permission, action, or acceptance.
- **Calibrate reasoning freedom separately from action authority.**
  Permission to examine premises, find counter-evidence, or propose
  alternative frames does not imply permission to alter user goals,
  reserved decisions, scope, or high-consequence actions.
- **Make the handoff independently closable.** A new session armed only
  with its static role, the contract, and explicit materials must be
  able to start, judge permissions, deliver, and know when to conclude
  or stop. Self-contained does not mean copying full history.

### Step 1 — Identify Candidate Agents

Identify which agent or agents could plausibly perform the work, based
on the task objective, current routing guidance, target role contract,
and actual permissions. This Skill does not redefine agent roles.

Candidate agents and initial routing are provisional until relevant
method sources have been read and reconciled. Do not freeze lane scope,
contract terms, or acceptance criteria before Step 7.

### Step 2 — Determine Relevant Skills

Judge relevance by the task, not by configuration. A Skill is relevant
when its methods, boundaries, deliverables, or verification
requirements could affect how the work is scoped or how the task
contract must be written. When unclear, err on the side of reading.

Consider only: Skills the Orchestrator has already discovered, and
trusted exact method paths explicitly provided by the user or current
task. Do not scan arbitrary unconfigured directories.

After determining relevance, consult the binding table for the target
agent's native access mode — this informs target-side access, not the
relevance judgment. A Skill not configured for the candidate is not
automatically irrelevant.

### Step 3 — Ensure Relevant Method Sources Are Available

Before finalising routing, lane scope, contract, or acceptance, ensure
that every relevant authoritative body is complete, reliable, and
identifiable in the current Orchestrator context. Use the `skill` tool
for natively loadable Skills and ordinary file read for trusted exact
paths. Record the base directory or resource path for path-based reads.

Reuse a body only when it is complete in the current context, its source
identity is known, no concrete signal indicates a change, and the lane
does not need resources not yet read. Reacquire it in a new session,
when the body is incomplete, when source identity cannot be confirmed,
when new resources are needed, or when a user action, tool action, path,
version, or other concrete signal indicates that the source changed.

When a local source changed and its exact path is available, read that
path to observe the current file. Do not infer freshness from repeating
the same retrieval; use a method that can confirm the current source. If
no confirmed current body can be obtained, report the blockage. Base
reuse on the body's current completeness and identity — not on tool
invocation history, memory, or speculative compaction state.

Body reuse provides the authoritative source text only. Do not
automatically carry derived requirements, relevance judgments, or
conflict reconciliations into another lane. Reassess their applicability
there while preserving user-confirmed decisions and materialized results
that remain valid.

If a load or read fails, stop and report. Do not search for
substitutes, fall back to description or memory, or guess the body.

### Step 4 — Establish the Lane's Intended Contribution

Start from the user goal and confirmed decisions. Determine what this
lane must produce — a result, judgment, recommendation, or reduction
of specific uncertainty. State what triggered the task, but include
only the causes that affect understanding or action. Distinguish
user-confirmed goals from your current interpretation.

Do not write speculative root causes, problem framings, or solution
prescriptions as premises the subagent must accept. Resolve ambiguity
only from clear existing evidence. If that would add or change the user
goal, scope, final deliverable, or a reserved decision, ask the user. Do
not delegate that choice to the subagent on the user's behalf.

### Step 5 — Compile the Minimum Connected Context
Select only the inputs, paths, evidence, completed direct dependencies,
constraints, current understanding, and open questions the lane needs.
State what key evidence supports and what it does not prove; show how
dependencies, decisions, and unknowns affect the current work. Where
interpretation could diverge, naturally separate evidence from
assumptions, unresolved questions from reserved decisions, and
delegable local judgments from those you retain. Materialize upstream
outcomes as accepted findings, evidence, paths, artifacts, and current
state. Preserve their source, uncertainty, and decision status while
discarding process narratives. When a prerequisite is unfinished,
either block or narrow
the lane to independent work. Delete orphaned background.

### Step 6 — Calibrate Reasoning Freedom and Action Authority

Weigh unknowns, framing risk, cost, impact, and reversibility. Specify:

- Which premises the agent may examine and whether it may seek
  counter-evidence; whether it may only propose, also test, or continue
  under an alternative frame without changing user goals, reserved
  decisions, or scope.
- Which local judgments it may make and which decisions the user or
  Orchestrator reserves.
- What it may read, search, recommend, modify, or execute, and which
  actions require approval.
- When it must only report a contradiction or recommend a change, and
  under what conditions open-ended investigation is bounded.

Adapt, but do not formalise: high unknowns warrant broader reasoning
freedom; high impact, cost, or irreversibility narrows action
authority; when both are high, separate investigation from action or
set evidence gates; mature execution lanes allow necessary local
judgment; review, research, and diagnosis lanes keep conclusions open
to counter-evidence but do not expand the user goal or action
authority.

### Step 7 — Extract Skill Requirements and Resolve Conflicts

Even when the authoritative body is reused, re-extract for each lane:
the relevant methods, approval gates, deliverable and evidence
requirements, and verification criteria. Place them at the positions
they actually govern — in the work approach, action gates, outputs,
and acceptance — never as an appended summary, pasted body, or Skill
name substitute. A Skill cannot expand an agent's capabilities, and an
Orchestrator-level conflict must not be passed downstream.

Also reconcile the relevant requirements with project instructions
applicable to the current lane. Keep those instructions at their source
and materialize only the boundaries the target needs rather than copying
the full instruction files.

When a Skill requirement conflicts with OMO boundaries, actual
permissions, applicable project instructions, user goals, or frozen
decisions:

1. Rewrite the deliverable or select a different agent if the
   conflict can be resolved without changing the task objective,
   scope, cost level, final deliverable, or any frozen decision.
2. Split into analysis, implementation, or verification if that
   resolves the conflict without changing the above.
3. Otherwise, stop and ask the user. Do not silently drop a Skill
   requirement or stretch an agent beyond its OMO contract.

Regardless of how the body was obtained — native tool or trusted path
— it enters the same extraction, reconciliation, and contract
compilation process. After resolving conflicts, decide whether the
target needs the full body (see Target-Side Skill Access).

### Step 8 — Compose the Materialized Handoff

Write the contract compactly, following the task's natural causal
order — no fixed headings, no fixed sequence. Place materials near the
judgments, actions, or outputs they inform and replace dangling
references with facts, paths, artifacts, and current state.

Make explicit: output, purpose, lane-specific acceptance evidence,
completion and stopping behaviour, approval gates, and blocker
handling. Match acceptance to the lane's actual contribution: system
effects by behaviour, validation, and regression; judgments by
evidence quality, alternative explanations, residual uncertainty,
conclusion boundaries, decision value, and a justified stopping point;
cause identification by reproducibility, hypothesis discrimination,
causal evidence, and a safe next step.

Add structure for multiple dependencies, consequential assumptions,
contestable framing, approval gates, high-impact actions, or multiple
artifacts. Simple lanes need only a short paragraph or a few bullet
points. Length follows the risk of misunderstanding and wrong
decisions, not file count or task type name.

### Step 9 — Confirm Sufficiency, Closure, and Minimality

Judge three things:

- Can a new session understand why the task exists, select a
  reasonable first step, judge its permissions, and know what to
  deliver and when to stop?
- Is any relationship missing that would produce a wrong target,
  premise, permission, or acceptance reading?
- If removing an item would leave understanding, judgment, action,
  and acceptance unchanged, remove it.

When you find a problem, rewrite the relationship or delete the
redundancy. Do not add fixed headings.

## Target-Side Skill Access

Use the binding table to decide how a handoff should address target-side
native loading. Treat it as a maintained responsibility projection, not
as permission or access enforcement, and respect the target's current
availability and permissions. Default to compiling only the necessary
methods into the contract. Give the target the full body only when Step
7 determines that its details would materially affect the target's
local judgments.

Under that condition, when the target has the Skill configured and no
concrete signal makes the available body stale or uncertain, follow the
binding table and current target-side loading guidance.

Under the same condition, require a trusted exact-path read when the
target lacks the Skill, or when a concrete source change makes the
available body's freshness uncertain. This is a controlled task-level
exception, not native Skill loading — it grants neither discovery,
`skill` tool access, nor expanded permissions.

If the target's current role guidance also mandates native loading, keep
that requirement and identify the exact path as the current
authoritative method source for this lane. Compile the relevant
requirements and conflict boundaries in Step 7. If the path is
unreachable and the available body's freshness cannot be confirmed,
report the blockage rather than treating it as refreshed.

The contract for a path-based read must state: why the source is
needed, the exact read scope, the base directory or resource path,
which methods constrain this lane and which relevant content is
excluded or handled by other boundaries, and conflict and failure
behaviour. The target must not search for substitutes, bypass explicit
prohibitions, or execute Skill scripts or side effects unless
separately authorised and permitted.

Neither loading nor path reading substitutes for the concrete methods,
approval gates, deliverable, and verification requirements compiled in
Step 7.

## Session and Handoff Invariants

- A new session receives no hidden chat history and no other agent's
  internal state. It must operate from its static role, the contract,
  and the materials provided.
- A reused session still receives the latest decisions, changed
  boundaries, and current increment. Do not assume the agent remembers
  prior task content.
- Pass only the materialized facts, materials, relationships,
  constraints, and direct dependencies the current lane requires.
- Do not pass: full history, the full scheduling plan, task IDs,
  other agents' internal state, rejected alternatives, or irrelevant
  materials. Do not write dangling references ("continue above," "use
  our previous result," "follow that Skill"), pass a Skill name as if
  it were completed research, or pass unresolved conflicts downstream.
- When the contract requires the target to read a file path, that
  path must be reachable in the target session. If unreachable, the
  target must report the blockage rather than search for alternatives.
