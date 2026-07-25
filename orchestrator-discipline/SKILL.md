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

Before every substantive delegation, follow this mandatory process.

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

### Step 4 — Extract Applicable Requirements

From each loaded Skill, extract:

- Methods the agent must follow.
- Approval gates the agent must honour.
- Deliverable and evidence requirements.
- Verification criteria the Skill imposes.
- Any content that conflicts with the agent's OMO role boundary,
  actual permissions, user goals, or frozen decisions.

A Skill describes a method; it does not expand an agent's OMO
capabilities. The final task contract must be simultaneously compatible
with the agent's OMO role boundary, actual permissions, the user goal,
all relevant Skill methods, and every frozen decision. A requirement
from one source that is incompatible with any of the others is not an
automatic deletion — it is a conflict that must enter Conflict
Resolution. Do not silently drop any constraint from the contract
before resolving the incompatibility.

### Step 5 — Compose the Task Contract

Combine the extracted Skill requirements with:

- The task objective, scope, and user goal.
- Frozen decisions that the agent must accept.
- The agent's OMO role boundaries and actual permissions.
- Direct dependencies (terminal results from completed lanes).
- Accepted facts, evidence, paths, and artifacts.

Write a **derived Skill application contract** — concrete instructions
that incorporate what the Skill requires, translated into the current
task's context. A Skill name or loading instruction alone cannot serve
as the Skill application contract. When the local binding requires the
target to load a Skill, the delegation prompt may and must name that
Skill, but must simultaneously provide the role-compatible application
contract derived by the Orchestrator. Never paste the Skill's body
into the delegation prompt.

### Conflict Resolution

When a Skill requirement conflicts with OMO boundaries, actual
permissions, user goals, or frozen decisions:

1. If the conflict can be resolved by rewriting the deliverable or
   selecting a different agent without changing the task objective,
   scope, cost level, final deliverable, or any frozen decision,
   do so directly.
2. If a simple analysis, implementation, or verification split (one
   that does not change the objective, scope, cost level, final
   deliverable, or any frozen decision) would resolve the conflict,
   split the work.
3. Otherwise, stop and ask the user. Do not silently drop a Skill
   requirement or stretch an agent beyond its OMO contract.

### Target-Side Skill Loading

Whether the target agent must reload a Skill is determined by the
local binding table above:

- **Oracle** must be instructed to load `simplify` when the task
  substantively needs simplification review. Oracle's static prompt
  does not load it automatically. The loading instruction alone is not
  sufficient; the delegation prompt must also include the
  Orchestrator-derived role-compatible Skill application contract.
- Agents without configured Skills must never receive a Skill name as
  a substitute for instructions. Incorporate the relevant substance
  directly into the task prompt.
- **Committer** and **Writer** static prompts already mandate their
  Skills at task start. Do not instruct them to load Skills. The Skill
  application contract in the delegation prompt provides role-specific
  requirements derived from those Skills.

### Task Contract Content

Every delegation prompt is self-contained and receives only what the
target needs for its lane:

| Included | Excluded |
|----------|----------|
| Task objective | Full scheduling plan |
| Scope (read, search, write boundaries) | Other agent state |
| Confirmed facts and frozen decisions | Internal routing rationale |
| Direct dependencies (completed, reconciled) | Rejected alternatives |
| Role-specific Skill application contract | Task IDs |
| Deliverable and evidence requirements | Complete conversation history |
| Acceptance criteria | Other lanes' internal state |
| Blocker handling instructions | |

### Materialized Handoff

Downstream agents receive already coordinated and reconciled facts,
suggestions, paths, and constraints. Do not:

- Pass a Skill name as if it were completed research.
- Require an agent to load a Skill it does not have configured.
- Ask an agent to resolve Skill conflicts that belong in the
  Orchestrator's compilation step.

## Task Contract Checklist

Apply this checklist proportionately. Include each item when relevant
to the lane; skip items that do not apply.

- **Objective:** what the lane must accomplish, stated in terms of the
  user goal.
- **Rationale:** why the work matters, tied to the user goal.
- **Scope:** read, search, and write boundaries. Which paths,
  subsystems, or domains are in scope and which are excluded.
- **Ownership:** which files, subsystems, or decisions the agent owns,
  and which paths it must not touch.
- **Frozen decisions:** decisions already made that the agent must
  accept without reopening.
- **Delegated decisions:** decisions the agent may make locally within
  its role boundaries.
- **Terminal dependencies:** completed results from other lanes that
  the agent must use as accepted input.
- **Accepted facts, evidence, paths, and artifacts:** concrete material
  the agent should rely on, plus explicit uncertainty where facts are
  incomplete.
- **Skill application contract:** concrete instructions derived from
  relevant Skills, translated into the current task context. A Skill
  name or loading instruction alone cannot fulfil this item. When the
  local binding requires the target to load a Skill, name it
  explicitly, but always accompany it with the role-compatible
  application contract derived by the Orchestrator. Never paste a
  Skill body.
- **Constraints and prohibited actions:** what the agent must not do,
  including capabilities it must not use even if available.
- **Deliverable and evidence requirements:** what the agent must
  produce and what evidence must support it.
- **Acceptance and verification:** who verifies the result and against
  what criteria.
- **Blocker behavior:** what the agent should do if critical input is
  missing or the task does not fit its role. The agent should return a
  brief reason rather than attempting partial work outside its
  contract.

## Session References

A new session must never receive dangling references such as "continue
above," "use our previous result," or "follow that skill." Every new
task prompt is self-contained.

A reused session still receives the latest decisions, changed
boundaries, and current increment. Do not assume the agent remembers
prior task content just because the session is reused.
