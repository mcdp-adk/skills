# Software Development

Read this reference only when a software project uses common engineering artifacts, or when the relationship between durable project knowledge, current execution, and the code or other artifacts that show what exists needs clarification. Use it for conditional mapping, not as a document stack or a replacement for the project's own conventions.

## Map responsibilities conditionally

The same responsibility may appear under different names, and one artifact may carry several responsibilities:

| Project responsibility | A common carrier |
|---|---|
| Goal | PRD or product source |
| Design | SDD or design description |
| Decisions | ADR or decision record |
| Plans | Delivery Plan or equivalent substantial-work plan |

Treat the mapping by responsibility rather than filename. An issue, specification, README, Git record, project convention, or another existing source may already be the right carrier. Keep one useful source connected to the project's entry point instead of installing a second set of documents.

## Keep intended design separate from actual structure

An SDD or other design description generally expresses intended design: how the system should work, its boundaries, relationships, interfaces, and important constraints. Code, configuration, generated structure, and other current artifacts show what exists now. Read both when the task depends on the difference. A mismatch is project knowledge about the work to resolve, not a reason to rewrite either source as the other.

## Keep durable plans separate from current execution

A Delivery Plan or equivalent can preserve the goal, scope, milestones, dependencies, completion criteria, and durable evidence needed for substantial work. Current progress, attempts, and tool details belong to the current execution state. Use the plan to recover what future work needs, not to preserve every step of one session.

## Treat implementation and verification as evidence

Implementation methods and verification practices provide ways to produce or test evidence for a plan. TDD, tests, integration work, user flows, migrations, performance measurements, and other evidence paths can serve the plan without becoming additional durable responsibilities. Read the relevant implementation and evidence sources before acting; update the lasting goal, design, decision, or plan only when the result changes it.

## Apply the mapping to the actual project

Before substantial software work, follow the project's entry point to the relevant goal, design, decisions, and plan sources, then inspect the code and other artifacts that control the action. After the work, compare the result with those sources and update only lasting changes. If the existing project already connects these responsibilities adequately, keep using it.

## Sources

- [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://arxiv.org/abs/2602.11988) — empirical context for treating repository instructions as selective aids rather than a universal replacement for ground truth.
- [An Exploratory Study of Agent Plans for Agentic AI Coding Tools in Open-Source Software](https://arxiv.org/abs/2608.04661) — empirical context for plans as optional task-level artifacts rather than a required project-wide document.
