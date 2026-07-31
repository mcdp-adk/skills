---
name: agent-capabilities
description: >
  OMO specialist-agent catalog covering fit, non-ownership, required inputs,
  configured Skills, loading responsibility, and exact-path method access.
  Use before choosing a target, writing a contract that depends on agent
  capability or permissions, deciding whether to load a Skill, or giving a
  target a Skill file path; check it instead of guessing from memory.
---

# Agent Capabilities

## Purpose and Authority

This Skill is a maintained projection of OMO agent responsibilities, action
classes, configured Skills, loading responsibility, and method-access rules.
It supports the Orchestrator and Navigator. Another agent may read it only
when a bounded task contract names this Skill's trusted exact path, relevant
scope, and failure behavior.

It does not define global routing, prove that an agent is currently enabled,
grant a tool or Skill, expand a role, or replace task-specific context. The
Orchestrator retains final routing and dispatch responsibility. Navigator may
use this knowledge to produce candidate plans and contracts only.

## Sources and Freshness

Task authority and capability evidence are separate. User decisions and
applicable project instructions control the task but cannot grant unavailable
capabilities.

Resolve capability facts in this order:

1. current runtime-visible agents, tools, Skills, and effective permissions;
2. current effective OMO user and project configuration, including resolved
   prompt overrides;
3. current built-in or custom static role definitions;
4. this maintained projection.

When a config, prompt, Skill, version, project override, or runtime state may
have changed, read the exact authoritative source supplied by the current
task. Prefer `~/.config/...`, project-relative paths, or an explicit current
path over machine-specific examples. If a higher source conflicts with this
projection, use the higher source and report the drift. If current capability
cannot be confirmed, return the uncertainty instead of guessing.

This projection is derived from OMO's current built-in agent definitions and
the effective agent definitions in
`~/.config/opencode/oh-my-opencode-slim.json`. Refresh it in the same change
whenever those sources change an agent, its Skill configuration, or its
permissions.

The catalog describes role fit, not availability. Treat an agent as
dispatchable only when current Orchestrator agent descriptions or routing
guidance advertise it. Do not infer availability from a catalog entry or use
a speculative task call to probe it. Navigator integration therefore requires
an `orchestratorPrompt`; disabled or internal agents without current routing
guidance are unavailable for ordinary dispatch.

## Capability Catalog

| Agent | Use for | Does not own / action class | Required input and stop behavior |
|-------|---------|-----------------------------|----------------------------------|
| Navigator | Candidate task decomposition, dependency order, specialist suggestions, and draft task contracts. | Advisory planning only; no dispatch, user decisions, file changes, task-state management, or final approval. | Needs a reconciled current-state packet. Return blockers when decisions, evidence, or prerequisites are missing. |
| Explorer | Fast local codebase discovery and compressed maps of files, symbols, and patterns. | Read-only discovery; no external research, design, implementation, or architecture decisions. | Needs a bounded workspace and discovery question. Return evidence and uncertainty, not guessed architecture. |
| Librarian | Current external documentation, official sources, library behavior, and real-world examples. | Research only; no implementation or architecture ownership. | Needs the research question, relevant versions or dates, source expectations, and output boundary. Distinguish official evidence from inference. |
| Oracle | Architecture, consequential trade-offs, complex debugging, simplification judgment, and material code review. | Read-only advice; no implementation, user decisions, or routine verification. | Needs the decision question, objective, constraints, evidence, uncertainty, and requested decision value. |
| Designer | User-facing UI/UX design and implementation, including layout, interaction, responsive behavior, and visual polish. | Does not own unrelated backend or headless logic. Read/write within the approved UI scope. | Needs product intent, user flows, relevant paths, design constraints, states, and acceptance evidence. |
| Fixer | Bounded, well-defined implementation and mechanical execution. | Read/write execution; no external research, architecture ownership, or visual design judgment. | Needs a complete specification, explicit scope and paths, preserved decisions, and proportionate verification. Stop on missing task-level decisions. |
| Sentinel | Evidence-grounded challenge of a concrete artifact or established position. | Read-only review; no design ownership, implementation, external research, or final approval. | Needs the exact artifact, objective, criteria, constraints, evidence, review boundary, and materiality bar. Return insufficient support when no finding is grounded. |
| Pathfinder | Comparison of plausible alternatives to an established approach. | Read-only alternative analysis; no architecture ownership, implementation, external research, or final approval. | Needs the baseline, objective, settled constraints, flexible boundaries, evidence, and comparison criteria. |
| Surveyor | Semantic boundary analysis for supplied files and artifacts. | Read-only local analysis; no broad discovery, rewriting, implementation, or general architecture review. | Needs exact artifacts, their consumers and purpose, current boundaries, dependencies, constraints, and acceptable retrieval cost. |
| Committer | Mechanical validation and creation of one atomic Git commit. | Restricted repository actions; no edits, tests, push, cleanup, split design, or history rewriting. | Needs one validated intent and explicit repository-relative file paths. Accept unchanged or reject. |
| Writer | Approved technical and non-technical prose creation, revision, and text-file maintenance. | Read/write prose execution; no task-level direction, external research, architecture, or final approval. | Needs approved audience, purpose, user goal, scope, language, structure, output location, and acceptance criteria. |
| Councillor | Independent read-only perspective within a supplied council question. | No implementation, final approval, or substitution for ordinary specialist routing. External retrieval exists only when current MCP configuration provides it. | Needs a self-contained question and supplied evidence. Return a bounded judgment from the assigned perspective. |
| Council | Synthesis of supplied councillor responses into a structured consensus report. | Synthesis only; no tools, councillor dispatch, evidence gathering, or final approval. | Needs the original question and each labelled councillor result, including failures. Preserve disagreements and remaining uncertainty. |
| Observer | Focused visual interpretation of supplied images, screenshots, PDFs, and diagrams. | Read-only visual analysis; no file changes or fabricated details. | Needs current routing guidance, a vision-capable runtime, exact files, and the observation goal. Extract exact visible text when required and state blur, absence, or uncertainty. |

## Configured Skills and Loading Responsibility

| Agent | Configured Skills | Loading responsibility |
|-------|-------------------|------------------------|
| Orchestrator | `*` | All discovered Skills may be visible. Load only Skills relevant to the current task; `orchestrator-discipline` conditionally requires this catalog when capability or access facts affect a judgment. |
| Oracle | `simplify` | The static role does not auto-load it. A task that substantively needs simplification must require loading it before that work. |
| Librarian | `grok-search` | The static role does not auto-load it. Current Web or X retrieval that needs this method must require loading it before research. |
| Designer | `agent-browser` | The static role does not auto-load it. Browser or Electron interaction must require loading it before use. |
| Committer | `conventional-commit` | Its static prompt loads it at task start; callers do not repeat that instruction. |
| Writer | `documentation-writer`, `chinese-documentation` | Its static prompt loads both at task start; callers provide task outcomes and acceptance rather than repeating their bodies. |
| Explorer, Fixer, Sentinel, Pathfinder, Surveyor, Councillor, Council, Observer | (none) | No native Skill loading responsibility is currently projected. |

Navigator integration is designed to use `skills: ["*"]`; it becomes a
capability fact only when the current effective config defines it. Navigator's
static prompt owns any mandatory loading of `agent-capabilities`. Other Skills
remain task-relevant, on-demand inputs.

`skills: ["*"]` makes discovered, described Skills visible and loadable unless
current restrictions deny them. It does not load every Skill body. A Skill not
configured for an agent can still be relevant to planning or to a task
contract.

## Skill and File-Access Semantics

Keep these states distinct:

- **Exists:** a method file is present at some path.
- **Discovered:** the runtime registered its metadata.
- **Configured:** the agent's Skill permissions include it.
- **Visible:** it appears in that agent's current available Skills.
- **Loaded:** the agent successfully called the `skill` tool and received the
  full body.
- **Read by path:** the agent read a trusted exact file through ordinary file
  access.

Default to compiling the necessary method, approval, output, and verification
requirements into the task contract. Give a target the full method body only
when its details materially affect that target's local judgment.

When the target has the Skill configured, follow its loading responsibility
and current visibility. Otherwise, or when freshness is uncertain, a contract
may require reading a trusted exact path. That contract must state why the
source is needed, the exact scope and base path, the methods relevant to the
task, excluded content, and failure behavior.

Path reading grants neither Skill discovery nor the `skill` tool, and never
expands the target's role, tools, or permissions. Do not execute referenced
scripts or side effects unless separately authorized and permitted. If the
path is unreachable or source identity cannot be confirmed, stop rather than
searching for substitutes.

Neither loading nor path reading replaces materializing the concrete
requirements that govern the task.

## Conflict and Stop Behavior

- Capability knowledge cannot override the user goal, applicable project
  instructions, actual permissions, or the target's current static role.
- A Skill description cannot expand an agent's responsibilities.
- If no agent fits, or sources conflict or current capability is uncertain,
  do not force a route. Navigator or another target returns the mismatch,
  evidence, and consequence to the Orchestrator. The Orchestrator stops and
  asks the user when the gap could change correct routing; it may continue
  only with minor uncertainty already known not to affect the target,
  permissions, or route.
- Keep global work graphs, current task state, user decisions, complete agent
  prompts, model pricing, and task IDs out of this Skill.
