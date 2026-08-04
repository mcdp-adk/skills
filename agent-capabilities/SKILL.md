---
name: agent-capabilities
description: >
  Use whenever choosing an OMO specialist, writing or reviewing a specialist
  prompt, resolving role ownership, or interpreting prompt, permission, Skill,
  MCP, and routing semantics.
---

# Agent Capabilities

This Skill is a concise reference, not a live registry, permission grant,
enablement record, or routing decision. Current task facts and decisions belong
in the task prompt; keeping them separate prevents reference text from becoming
false runtime authority.

## Responsibility map

| Role | Owns | Does not own |
|------|------|-------------|
| User | Goals, scope, product choices and trade-offs requiring user authority, explicit routing constraints | Runtime mechanics and in-boundary technical execution |
| Orchestrator | Conversation context, routing, task boundaries, prompts, technical and execution decisions within user-set authority, verification, delivery, user communication | Inventing missing authority, making reserved user choices, or rewriting specialist judgment |
| Navigator | Decomposition, dependency, parallel-lane, specialist-fit, and planning-risk advice | Decisions, assignments, dispatch, execution, research, user interaction |
| Auditor | Pre-dispatch review of an exact specialist prompt against supplied authority | Prompt rewriting, target selection, implementation/result review, dispatch |
| Specialist | The bounded judgment or closed action in its approved prompt | Global routing, other agents' work, user decisions |

## Specialist map

Oracle, Sentinel, and Pathfinder share one role: read-only strategic technical
advisor and code reviewer for architecture, risk, complex debugging,
simplification, and engineering guidance. Their default strengths differ:

- **Oracle — first-principles reasoning:** clear logic, root-cause
  analysis, trade-offs, correctness, and maintainable simplification.
- **Sentinel — hidden risk and boundaries:** potential consequences,
  edge cases, security vulnerabilities, hidden assumptions, and solution flaws.
- **Pathfinder — divergence and creativity:** new framings, creative
  solution paths, cross-domain connections, and unrealized possibilities.

Choose by the strength the task needs, not by giving them different authority;
current model assignments belong to configuration.

- **Explorer:** Bounded local discovery of files, symbols, patterns, and ASTs.
- **Librarian:** External documentation, web, and public-code research.
- **Designer:** UI/UX judgment and approved visual implementation.
- **Fixer:** Bounded implementation and mechanical execution from settled
  decisions.
- **Council:** When configured, multi-model judgment and synthesis for critical
  trade-offs, not an implementation pool.
- **Observer:** When enabled, read-only analysis of images, screenshots, PDFs,
  and diagrams outside the main Orchestrator context.
- **Surveyor:** Text cohesion and semantic-boundary advice for all human-readable
  text files, including source code, keeping them within 200 lines whenever
  practical without treating the ceiling as hard. It identifies candidate
  source boundaries; architecture decisions remain with Orchestrator.
- **Writer:** Writing execution within a supplied direction, structure, output
  mode, and exact path when writing files; judgment is limited to
  structure-preserving wording, sentence order, and formatting.
- **Committer:** Validation and execution of one atomic commit with a message
  aligned to the repository's recent history.

Advisers advise; Orchestrator integrates their judgment within user-set
authority. Executors act only within supplied scope. Role prompts define each
specialist's capabilities, behavior, constraints, stops, and outputs.

## Configuration layers

- **`prompt`:** The agent's role, capabilities, behavior, constraints, stops,
  and any required output.
- **`orchestratorPrompt`:** A compact routing block: lane, role, capability
  summary, delegation conditions, and only necessary call or result guidance.
- **`permission`:** Enforced tool and action rules. It is capability evidence,
  not a role definition or task-domain authority.
- **Skill:** Fully read text that supplies standards or methods. It grants no
  facts, tools, permission, authorization, or decision rights.
- **MCP:** External-tool selection. `mcps: []` denies that agent's registered MCP
  tools without unregistering global servers.

Task authority and evidence govern task facts. The local role prompt governs
authorization, tool scope, user interaction, and terminal state. If a Skill
procedure conflicts with either, report the conflict rather than reading
selectively or overriding the task.

Effective permissions are runtime facts. Audit them against the current
configuration and authoritative OMO/OpenCode implementation, never this Skill.
