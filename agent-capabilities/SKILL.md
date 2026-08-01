---
name: agent-capabilities
description: >
  Shared static reference for OMO agent roles, route-relevant capabilities,
  special target conditions, and the context each target needs. Use for
  specialist selection, multi-agent reasoning, or prompts that must reference
  another agent's responsibilities.
---

# Agent Capabilities

## Purpose

This Skill is the manually maintained shared source of stable agent knowledge.
Refresh it when the user changes OMO configuration or agent definitions. It is
not a live registry, a task record, a permission grant, or a fixed routing map.

Navigator reads it when planning. Orchestrator may use it to understand static
boundaries. Specialist use is defined in Shared Reference by Path.

## System Roles

| Role | Responsibility | Not responsible for |
|------|----------------|---------------------|
| User | Goals, decisions, scope, trade-offs, and explicit `@agent` participation constraints. | Runtime dispatch or task mechanics. |
| Orchestrator | Conversation context, actual dispatch, runtime choices, user interaction, verification, and delivery. | Rewriting Navigator's planning semantics or specialist judgment. |
| Navigator | Task understanding, target selection, smallest sufficient decomposition, and downstream prompts. | Dispatch, runtime choices, user interaction, or specialist judgment. |
| Specialist | Its prompt's professional judgment or action. | Global routing, dispatch, other agents' work, or user decisions. |


## Target Reference

Each entry records only facts that change target selection or prompt
completeness. “Unavailable” and “not established” are facts; do not guess.

| Target | Role and limits | Route-relevant facts | Required context |
|--------|-----------------|----------------------|------------------|
| Explorer | Bounded local discovery; no research, writing, design, or architecture ownership. | Local file, symbol, pattern, and AST discovery. | Workspace, discovery question, bounded scope, expected evidence. |
| Librarian | External documentation and research; no implementation ownership. | `webfetch`, `websearch`, `context7`, `grok-search`, `gh_grep`; URL fetch, search, docs lookup, and external code search differ. | Research question, time/version boundary, source expectation, required method. |
| Oracle | Architecture, complex debugging, simplification, and system trade-offs; no implementation or research ownership. | Read-only analysis; `simplify` when relevant. | Decision question, constraints, evidence, uncertainty, decision value. |
| Designer | UI/UX judgment and approved visual implementation. | Browser/Electron work requires `agent-browser` and task-specific starting conditions. | Product intent, flow, affected paths, visual constraints, states, acceptance. |
| Fixer | Closed implementation and mechanical execution; no research, architecture, or visual-design ownership. | Local read/write, commands, tests. | Closed specification, exact write scope, settled decisions, verification. |
| Sentinel | Evidence-grounded review of a supplied artifact. | Read-only; no implementation, research, or final approval. | Artifact, objective, criteria, evidence boundary, materiality bar. |
| Pathfinder | Alternatives against an established baseline. | Read-only; no baseline invention or implementation. | Decision goal, baseline, criteria, fixed constraints, flexible boundaries, cost/risk tolerance. |
| Surveyor | Semantic boundary analysis of supplied artifacts. | Read-only local analysis; no broad discovery or rewriting. | Workspace, artifacts, consumer, purpose, boundaries, dependencies, evidence boundary. |
| Writer | Approved text-file writing and editing. | `documentation-writer`, `chinese-documentation`; no Bash or task delegation; external research and professional-format workflows route elsewhere. | Audience, purpose, scope, language, document type, approved structure, location, text format. |
| Committer | One verified atomic Git commit. | Limited Git inspection/add/commit and `conventional-commit`; no edit, test, push, cleanup, or redesign. | Repository context, completed validation, one intent, non-empty explicit repository-relative files; no directories or globs. |
| Observer | Visual interpretation. | Currently unavailable; requires enabled visual target and precise files. | Files, observation goal, required text precision. |
| Council | Response synthesis. | Currently unavailable; no tools or evidence gathering. | Original question and all labelled councillor responses. |
| Councillor | Internal independent perspective. | Not an ordinary target; unavailable while Council is unavailable. | Assigned perspective, self-contained question, and evidence. |
| ACP | External agent wrapper. | No current target configured. | External capability, input boundary, invocation conditions. |

Important distinctions: URL fetch is not Web search; Web search is not browser
interaction; local read is not write; Bash is not unrestricted Git; visual input
is not visual responsibility; text writing is not DOCX/PDF/PPTX/XLSX work.

## Shared Reference by Path

When a call's local judgment requires multi-agent roles, capabilities, or
boundaries, its prompt may reference this Skill's canonical exact path. Use the
active `SKILL.md` path returned when this Skill was loaded, not a repository
development path. The reference must state why to read it, which headings
matter, and which local question it supports. Current goals, decisions,
materials, evidence, scope, and acceptance still belong directly in the task
prompt.

Reading this source does not let a specialist select targets, dispatch work,
change roles, or infer current runtime conditions. If the source cannot be
confirmed, report that limitation rather than inventing a substitute.

## Skill and Method Facts

Distinguish a configured Skill from one loaded into the current call, and a
loaded Skill from a file read by exact path. Neither expands a role or
permission.

Navigator is configured with `skills: ["*"]`; its prompt owns when to load them.

This reference supports target selection and prompt writing; Navigator's prompt
defines the planning method and the public downstream prompt contract.
