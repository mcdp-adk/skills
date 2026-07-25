---
name: orchestrator-discipline
description: >
  OMO Slim personal difference layer and delegation-prompt compilation
  workflow. Provides a user-maintained local Agent–Skill binding,
  mandatory Skill pre-reading before delegation, and a process for
  composing task contracts that reconcile Skill requirements with OMO
  role boundaries, actual permissions, user goals, and frozen decisions.
  Trigger whenever the Orchestrator prepares to delegate work.
---

# Orchestrator Discipline

## Purpose

This Skill is the personal difference layer between the Orchestrator
and the underlying OMO Slim harness. OMO Slim's static prompts and
runtime injection already define agent roles, routing thresholds,
background tasks, task appending, session reuse, design handoffs,
cancellation, verification, and communication rules. This Skill does
not duplicate those rules. It adds two things OMO Slim does not
provide: a user-maintained local Agent–Skill binding, and a mandatory
process for reading relevant Skills before delegation and compiling
their requirements into effective task contracts.

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

This section is a user-maintained projection of which agents have which
Skills configured. It is not the OMO Slim roster. Every OMO
configuration change must be reflected here.

| Agent | Configured Skills | Loading Responsibility |
|-------|-------------------|----------------------|
| Oracle | `simplify` | Oracle's static prompt does **not** load it automatically. For any task that substantively needs simplification review, the delegation prompt must explicitly instruct Oracle to load `simplify` before review. |
| All other currently configured OMO subagents | (none) | — |
| Committer | `conventional-commit` | Committer's static prompt loads it at task start. You do not instruct Committer to load it. |
| Writer | `documentation-writer`, `chinese-documentation` | Writer's static prompt loads both Skills at task start. You do not instruct Writer to load them. |

The Orchestrator has access to all configured Skills. This does not
change the routing rules injected by OMO Slim.

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
on the task objective and the OMO role capability categories. The
static OMO prompts are the authoritative source for role boundaries.

### Step 2 — Determine Relevant Skills

For each candidate, consult the local binding table above. Filter to
Skills whose subject matter is substantively relevant to the current
task. A Skill is relevant when its methods, boundaries, deliverables,
or verification requirements could affect how the work is scoped or how
the task contract must be written. When relevance is unclear, err on
the side of reading.

### Step 3 — Read Relevant Skills in Full

Before final delegation, load into your own context every Skill
identified as relevant in Step 2. Use the `skill` tool for each. Do
not skip a Skill because you recognise its name or recall its
description. Read the full body. If a Skill load fails, stop and
report.

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

### Step 7 — Apply Skill Requirements and Resolve Conflicts

Embed each relevant Skill's methods, approval gates, deliverable and
evidence requirements, and verification criteria at the positions they
actually govern — never as an appended summary, pasted body, or Skill
name substitute. A Skill cannot expand an agent's capabilities, and an
Orchestrator-level conflict must not be passed downstream.

When a Skill requirement conflicts with OMO boundaries, actual
permissions, user goals, or frozen decisions:

1. Rewrite the deliverable or select a different agent if the
   conflict can be resolved without changing the task objective,
   scope, cost level, final deliverable, or any frozen decision.
2. Split into analysis, implementation, or verification if that
   resolves the conflict without changing the above.
3. Otherwise, stop and ask the user. Do not silently drop a Skill
   requirement or stretch an agent beyond its OMO contract.

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

## Target-Side Skill Loading

The local binding table is the sole source of loading responsibility.
Instruct the target to load a Skill only when the table explicitly
requires it. Do not require Skills the target has not configured or
that its static prompt already mandates.

Regardless of target-side loading, the Orchestrator must compile every
applicable method, gate, deliverable, evidence, and verification
requirement into the contract. A loading instruction cannot substitute
for the concrete application requirements.

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
