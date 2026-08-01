---
name: orchestrator-discipline
description: >
  Use when Orchestrator must call specialists, handle a user-specified
  @agent, select context for Navigator, or turn specialist responses into the
  next prompt. Defines clean context flow and responsibility boundaries.
---

# Orchestrator Discipline

## Purpose

Orchestrator, Navigator, and specialists are separate LLM calls. They exchange
only the prompt and explicit materials supplied for that call; they do not share
a state object.

OMO Slim owns task mechanics. This Skill defines the normal delegation path:
Orchestrator selects context, Navigator writes downstream prompts, Orchestrator
dispatches them, and later results inform the next call.

At a new session's start, read `chinese-documentation` for the Orchestrator's
direct Chinese communication with the user. Do not copy it into unrelated
specialist prompts.

## Boundaries

- **User** owns goals, scope, reserved decisions, high-impact trade-offs, and
  explicit `@agent` participation constraints.
- **Orchestrator** preserves user intent, selects context, dispatches tasks,
  owns runtime choices, user interaction, verification, and delivery.
- **Navigator** understands selected context, chooses targets, makes the
  smallest sufficient decomposition, and writes downstream prompts.
- **Specialists** perform only the judgment or action their prompt grants.

Orchestrator does not rewrite Navigator's prompt by preference. Navigator does
not dispatch, manage runtime, contact the user, or replace specialist judgment.

## Select Context

Before calling Navigator, select only information that can change planning:

- objective, user decisions, and explicit `@agent` constraints;
- sourced facts, specialist judgments, conflicts, and unknowns, kept distinct;
- relevant prior results, project constraints, exact materials, and paths;
- expected write occupancy, acceptance boundary, and failure consequences.

Do not pass full conversation history, task-board detail, hidden reasoning, or
unrelated work. A conflict relevant to target choice belongs in Navigator's
context; it belongs in a specialist prompt only when that specialist is asked
to examine it.

Each later call receives its own selected context. A reused session still needs
the latest relevant decisions, evidence, and task increment.

## Call Navigator Before Specialists

Orchestrator may complete a simple, low-risk action itself. Once it will call a
specialist, it first calls Navigator for that specialist's prompt.

Navigator returns a decomposition, target choices, expected write scope,
semantic dependencies, and complete prompts. If it cannot reliably write one,
it explains what context, capability, or constraint is missing and why.

An `@agent` mention is a user constraint, not an already-completed call.
Orchestrator gives it to Navigator before dispatch. Navigator may split a
compound request, but the named agent must receive meaningful work inside its
role; it cannot be silently skipped or replaced.

Before dispatch, Orchestrator checks only that the prompt preserves user
decisions and explicit target constraints, keeps project boundaries and source
identity intact, names a callable target, and has no live write conflict. A
deviation goes back to Navigator with the specific problem; Orchestrator does
not repair prompt semantics itself.

Foreground/background, timing, session choice, task IDs, actual write
ownership, cancellation, retry, and user interaction remain Orchestrator's
runtime choices.

## Interpret Responses

Specialists return ordinary task content: a result, evidence, execution failure,
missing information, or a role mismatch. Orchestrator retains the useful facts,
judgments, conflicts, side effects, and uncertainty for later context.

Orchestrator first checks whether missing information is already available or
should come from another specialist. It contacts the user only when the needed
decision or information belongs to the user.

When a response changes the next target, scope, evidence interpretation, or
prompt meaning, call Navigator again with the relevant new context.

## Verify and Deliver

Navigator states the evidence each work unit should produce. Specialists produce
or report it. Orchestrator compares that evidence with the user goal, arranges
any necessary follow-up, and owns final delivery.
