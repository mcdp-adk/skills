# Knowledge in Project Work

Read this reference when a project-knowledge task has an unclear, large, contradictory, or tempting-to-overdesign knowledge arrangement. It explains the core model in `SKILL.md` and leaves the arrangement to the project's actual work and readers.

For the underlying research on context files, acting context, instruction adherence, and Agent plans, see the selectively loaded [research index](research/README.md).

## Project work creates the need

Project knowledge is useful only when it changes project work: what someone builds, creates, decides, evaluates, or learns. Start with that work and its actual consumer, then ask what the consumer must understand or do. A knowledge arrangement is a means of making that understanding available, not a deliverable in its own right.

The need may be to establish a missing source, apply existing knowledge to a decision, or evolve a source after evidence changes what the project knows. Treat these as distinct jobs and choose only the one the current work requires.

## Knowledge is produced and consumed

Work produces knowledge as well as consuming it. An implementation reveals current behavior; an experiment reduces uncertainty; a playtest exposes an experience; a failure changes what is plausible; a decision sets direction. Connect each durable result to the work that needs it next.

For each meaningful claim, identify the carrier that can express it most faithfully. Prose may preserve intent, relationships, rationale, constraints, or lessons. Code, tests, schemas, assets, scenes, prototypes, builds, screenshots, video, telemetry, issue history, and Git may express behavior or evidence more precisely. A useful arrangement connects these sources rather than making one summarize or replace the others.

## Carriers are peers

No carrier is inherently the project database. Choose the carrier by the consumer's need, fidelity, update cycle, accessibility, and authority.

Keep the distinction between the carrier and the connection. The carrier holds the knowledge; an entry point, link, index, issue relationship, reproduction path, or other connection makes it findable in the work. Add the connection needed for the actual reader.

## Keep execution and durable knowledge distinct

Immediate progress and other execution-only detail belongs in the current working context. Durable project knowledge preserves what future work needs: intent, relationships, rationale, direction, plans, evidence, and learning. Ground-truth artifacts show what currently exists or what actually happened; history can preserve how it changed.

Persist a result when a future person or Agent will need it, when it changes a durable decision or direction, or when the project needs a recoverable path across sessions. Keep it in the lightest suitable carrier that keeps future work connected to the result.

## Connect before creating

Inventory existing entry points and candidate sources before adding anything. Correct or connect an authoritative source before creating a competing one. Merge or retire duplicate material only when scope and authority are clear. Create a new carrier only when an independently useful durable gap remains.

The same project may use many forms. Name and place each one according to the responsibility, reader, and change cycle it actually serves.

Connect sources at the point where a reader needs to move between them. Say what the target contains and when it matters. When behavior and intent differ, connect both and label the difference rather than smoothing it away.

## Make source and certainty visible

Project knowledge often has several voices. A person may confirm a goal; a design document may describe an intended system; code may reveal current behavior; Git may show what changed; an experiment may provide evidence without settling the product decision.

Before writing or acting on an important claim, classify its basis:

- confirmed by an appropriate project authority;
- stated by an existing source that the project treats as authoritative;
- directly verifiable in a current artifact;
- inferred from available evidence;
- unknown, disputed, stale, or superseded.

Do not resolve a conflict by silently choosing the most convenient source. Identify the conflict, preserve the distinction between intended and actual behavior, and seek a decision from the appropriate authority when the result would change scope or direction. If no decision is available, record the uncertainty and its consequence rather than manufacturing a requirement.

Keep one authoritative expression for each meaning. A pointer may explain when to read that source, but a duplicate summary will eventually drift. When a source is superseded, say so and point to its replacement if retaining the historical record helps readers. Do not let a current implementation silently become an intended requirement, or let a plausible interpretation become a confirmed decision.

## Failure modes

The causal model fails when a knowledge arrangement impedes the work it should support. Look for these signals while diagnosing a real task:

- a source exists but the actual consumer cannot find it;
- parallel sources compete without visible authority;
- intended design is presented as current behavior, or current behavior as confirmed intent;
- a summary stands in for an artifact whose details control action;
- temporary execution state has become stale durable truth;
- a polished document hides conflict, uncertainty, or the limits of evidence;
- structure was created before a real reader or change cycle needed it.

Repair the smallest cause that restores a reliable path. Keep the entry point and connections proportional to the work they support.

## A practical recoverability check

When the task is specifically about recoverability, start at the actual project entry point and ask whether a new collaborator can, for this work:

1. find the relevant knowledge;
2. understand the purpose and relationships that matter;
3. identify important reasons, constraints, decisions, and current direction;
4. locate the implementation and evidence;
5. know what to read or inspect next.

If an answer requires guessing or trusting an unmarked inference, improve the connection, authority label, or source that the current work actually needs. Do not claim recoverability merely because files exist.
