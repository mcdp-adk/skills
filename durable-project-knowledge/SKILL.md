---
name: durable-project-knowledge
description: Use when a task explicitly requires establishing or reorganizing durable project knowledge; when substantial project work spans sessions, handoffs, or collaborators and needs to discover, read, and maintain durable goal, design, decision, or plan knowledge; when a durable knowledge entry point or source is missing, conflicting, or undiscoverable and blocks the work; or when completed work may have changed that durable knowledge.
---

# Durable Project Knowledge

Help a project keep the durable knowledge it needs for development, creation, and completion, and let evidence and learning change that knowledge when warranted. The project owns its durable knowledge and artifacts; this Skill provides a reusable cross-project method for finding, using, and maintaining them.

The working layers are:

```text
durable project knowledge and artifacts
                ↑
       durable-project-knowledge method
                ↓
current execution state and capability
```

Code, tests, assets, scenes, prototypes, and observed results are ground truth for what exists and what happened; read them directly when those details control the work.

## Four durable responsibilities

Use these as questions, not as required files, directories, or a universal template:

- **Goal:** What are we making or changing, why, and what result or experience is expected?
- **Design:** How should it work or be organized?
- **Decisions:** Which consequential choices were made, and why?
- **Plans:** How will substantial work proceed, and how will completion be judged?

An existing artifact may answer one or several questions. Let the project's conventions and actual readers determine the carrier.

## Before substantial work

1. Start from the actual task. Identify which of the four responsibilities the work needs, and what the Agent must decide, do, or evaluate.
2. Find the project's entry point and the existing sources that carry those responsibilities. Adapt to their names, locations, and connections instead of creating a parallel arrangement.
3. Read only the sources relevant to this task, then read the code, tests, assets, prototype, configuration, build, or other current artifacts needed to act. A summary can orient the work but cannot replace the source whose details determine what to do.
4. Classify important claims as confirmed authority, source statement, verifiable fact, inference, or unknown/conflict. Confirm only a direction-changing point that cannot be recovered from the project and is needed to proceed.

**Complete when:** the Agent can begin the current substantial work without treating an inference as fact, a source statement as confirmed authority, or a summary as ground truth.

## During work

1. Execute the current task normally. This method supplies knowledge context; it does not add a second project-management or execution process.
2. Keep current progress, attempts, orchestration, and tool details in the current working state.
3. Notice possible lasting changes to goals, design, decisions, or plans, and distinguish them from discoveries useful only to the current execution. Do not preserve every discovery.
4. There is no fixed division between people and Agents: either may research, design, implement, evaluate, and learn. For the question at hand, make participation and confirmation visible according to the project's authority, available knowledge, capability, authorization, risk, and verifiability. Treat Agent inference, preference, or simulated feedback as unconfirmed until appropriate authority confirms it.

**Complete when:** current execution state and possible durable changes remain distinguishable, with no temporary progress silently presented as project knowledge.

## After work

1. Compare the result and evidence with the affected goal, design, decisions, and plans.
2. Update project knowledge only when a lasting change will matter to future work. Preserve the difference between intended design, actual behavior, evidence, interpretation, and confirmed change.
3. When the task's authorized work produces evidence of a lasting change, update the existing authoritative source within that authorization. If writing is not authorized, briefly report the durable update needed and the authority gap; do not present an unconfirmed change as fact. Keep the source that best expresses each meaning rather than creating a parallel copy.
4. When no lasting knowledge changed, leave project knowledge unchanged.

**Complete when:** every affected durable responsibility is updated, justifiably left unchanged, or reported with its needed update and authority gap; its source and certainty remain clear, and current execution state has not been promoted into durable fact.

## Establish explicitly, or repair only when blocked

When the task explicitly requires establishing or reorganizing project knowledge, do that structural work within its write authorization. Otherwise, establish or repair an arrangement only when the current work is blocked because a reliable entry point or connection is missing, a needed responsibility has no usable source, relevant sources conflict, or required knowledge is undiscoverable.

Follow either path by reusing and connecting what already exists. Add only a real independent gap, using the smallest arrangement that gives the current readers a reliable path. Let project needs determine file names, locations, and whether one carrier should hold several responsibilities; do not preselect a project-wide document stack.

**Complete when:** the explicit structure need or blocking condition is resolved, the relevant readers can find the sources and ground truth needed for their work, the relationships among them are clear, and no structure beyond that need was introduced.

## Read conditional references

Read [software-development.md](references/software-development.md) when a software project uses engineering artifacts such as PRDs, SDDs, ADRs, Delivery Plans, or equivalent sources, or when the relationship between those sources, current execution, and ground truth needs clarification.

Read [creative-and-experimental-projects.md](references/creative-and-experimental-projects.md) when experience, taste, prototypes, experiments, multimodal artifacts, or human feedback affect what the project is trying to learn or deliver.

When the task ends, briefly state which durable sources were read or relied on, which lasting knowledge was updated or deliberately left unchanged, and which authority or unknown still affects subsequent work. Limit structural operations—creating, splitting, moving, or reorganizing durable sources—to tasks that explicitly require establishing or reorganizing durable project knowledge, or to a repair blocker where the required write is authorized. This does not limit normal updates to an existing authoritative source.
