---
name: agent-capabilities
description: >
  Stable reference for OMO role boundaries, complementary advisory strengths,
  configuration semantics, and the context required for a specialist call.
---

# Agent Capabilities

This is a concise, manually maintained reference. It is not a live registry,
permission grant, model list, enablement record, or routing decision. Current
goals, decisions, evidence, scope, and acceptance criteria belong in the task
prompt.

## Core boundaries

| Role | Owns | Does not own |
|------|------|-------------|
| User | Goals, decisions, scope, trade-offs, and explicit `@agent` constraints | Runtime dispatch or task mechanics |
| Orchestrator | Complete conversation context, target and boundary decisions, specialist prompts, dispatch, runtime choices, user communication, verification, and delivery | Outsourcing final decisions or changing a specialist's professional judgment |
| Navigator | Advice on decomposition, dependencies, parallel lanes, candidate specialists, and material risks from supplied material | Final target/boundary decisions, prompt writing, dispatch, execution, research, or user interaction |
| Auditor | Gate review of specialist-bound prompt context and task width against the supplied authority | Code, architecture, result, or execution review; prompt writing; target selection; dispatch; approval |
| Specialist | The professional judgment or closed action stated in its approved prompt | Global routing, dispatch, other agents' work, or user decisions |

## Complementary advisory roles

- **Oracle / GPT:** Architecture, complex debugging, simplification, and system
  trade-offs; provide the decision question, constraints, evidence, and
  uncertainty.
- **Sentinel / Claude:** Critical review for omissions, contradictions, hidden
  problems, unsupported assumptions, boundary failures, and material risks.
  It may analyze a question, framing, decision, proposal, analysis, artifact,
  or deliverable; it is not limited to one artifact type. Provide the objective,
  criteria, constraints, evidence, and uncertainty.
- **Pathfinder / Gemini:** Creative, plausible alternatives and overlooked
  possibilities, compared by fit, upside, risk, cost, and evidence. A baseline
  is not required. Provide the objective, evidence, constraints, flexible
  boundaries, and evaluation criteria; Pathfinder does not make the final
  decision.

## Other target boundaries

- **Explorer:** Bounded local file, symbol, pattern, and AST discovery; no
  research, writing, design, or architecture ownership.
- **Librarian:** External documentation and research; distinguish URL fetch,
  web search, documentation lookup, and external code search; no implementation
  ownership.
- **Designer:** UI/UX judgment and approved visual implementation; provide
  product intent, affected flow, visual constraints, states, and acceptance.
- **Fixer:** Closed implementation and mechanical execution; provide settled
  decisions, exact write scope, and verification.
- **Surveyor:** Make text products consumable by agents. Analyze cohesion and
  natural semantic boundaries, establish stable references, and check target,
  responsibility, dependencies, causality, and verification continuity. Roughly
  200 lines is a heuristic and diagnostic signal, never an automatic threshold.
- **Writer:** Execute decided writing only. For formal complete Tutorial,
  How-to, Reference, or Explanation writing under `documentation-writer`, or
  another genuinely large document, use outline-only → Orchestrator approval →
  full-draft; full-draft requires an approved outline, otherwise return and
  stop. Small editing, proofreading, rewriting, or local revision needs no
  outline gate when decisions are complete.
- **Committer:** Validate one candidate's atomicity, staged scope, and
  Conventional Commit message, then create one commit. Before inspection or
  Git commands, fully load and read `conventional-commit` into the current
  context. Atomicity is one primary responsibility plus direct causal
  completeness; necessary tests or generated artifacts may belong to it.

## Configuration semantics

- **Prompt:** Role, judgment, boundaries, required inputs, and output use.
- **Permission:** Tool/action rules enforced by the agent configuration; it is
  not a role definition or evidence source.
- **Skill:** Text access. A Skill does not add tools, evidence, authority, or
  decision rights.
- **MCP:** An independent external-tool configuration layer. OMO applies an
  agent's `mcps` selection to `<server>_*` tool permissions; `mcps: []` denies
  that agent's use of all registered MCP tools but does not unregister the
  global servers.

Configured role or method Skill text may guide analysis or review, but it is not
current-task fact, evidence, authorization, or permission to expand the
evidence boundary or search for extra task material.

Skills must be fully read and provide domain standards and methods; if their
procedural instructions conflict with the local prompt's authority, tools,
execution or staging scope, user interaction, or terminal state, the local
prompt prevails and the agent reports the conflict to Orchestrator. This does
not permit selective reading or treating a Skill as a function.

OpenCode's default tool baseline is `*: allow` with `question: deny`. When a
custom agent omits `permission`, OMO merges its defaults: `question` becomes
`allow` unless explicitly denied; `cancel_task` and `wait_for_user` are `deny`
for non-Orchestrators; and `skill` is the generated permission for configured
Skill text access. A subagent inherits the parent session's `deny` rules and
`external_directory` restriction; without an explicit `task` or `todowrite`
rule, both are denied. A prompt's read-only or no-execution requirement is a
behavior contract, not a runtime hard deny.
Council and Councillor remain restrictive exceptions with their own constrained
defaults.

## Required call context

Every specialist prompt should state the objective, exact target, local
responsibility, included and excluded scope, authority and evidence boundary,
constraints, dependencies and blockers, known uncertainties, permitted action,
output requirements, stop conditions, and acceptance criteria. Include exact
paths or stable identifiers when the specialist must inspect or challenge an
authoritative source. Do not use this reference to infer current runtime facts.
