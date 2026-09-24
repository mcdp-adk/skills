---
name: setup-project-conventions
description: Configure this project's writing, collaboration, and contribution conventions.
disable-model-invocation: true
---

# Setup Project Conventions

Explore, resolve project choices, show the resulting files, confirm, then write. The sibling files are seed templates; project rules take precedence over their defaults.

## 1. Explore

Read existing AGENTS.md / CLAUDE.md, contributor guidance, linked project conventions, and issue/PR templates. Check Git remotes and relevant examples where available.

Identify explicit language and contribution rules, work-record locations, maintenance responsibilities, engineering guidance, and sharing boundaries. Reuse existing tracker, labels, domain docs, and artifact contracts, including those configured by Matt's setup; keep their definitions in their existing sources.

Explicit rules settle a choice. Examples inform a recommendation.

## 2. Present findings and ask

Summarize the existing choices and gaps. Take the sections in order. Ask one unresolved choice, wait for its answer, then continue. Lead with the recommended answer. Skip settled or inapplicable choices.

### A. Writing languages

Establish the project's current readers and collaborators from project guidance and the user's context. Identify their language needs, distinguishing product users from contributors where relevant. Clarify missing information that affects the recommendation.

Recommend a shared language for contributor communication and material they maintain, including requirements, design explanations, development records, and code comments. Offer English, the current conversation language (name it; omit a duplicate English option), or another language. Ask one unresolved choice at a time, carrying each answer forward to the content it covers. Ask separately where different readers, existing conventions, or tooling create an actual difference. Choose the language of user documentation for its intended readers.

For multilingual material, record the language of each version and reference its existing translation guidance. When a new multilingual arrangement is requested, establish its languages and file locations, then clarify how corresponding versions should be kept aligned if that is still unresolved.

Use English for the main convention files produced by this setup unless the user chooses otherwise. The separate chinese-wording.md uses Chinese. Record both choices in language.md. If Chinese is used, generate chinese-wording.md and its pointer from the wording seed, preserving the recommended forms unless the user or existing project conventions specify an override.

Apply the chosen collaboration language to both issues and PRs, including titles, bodies, and comments. Resolve commit-message language separately when unsettled. For example, English commits and Chinese collaboration means English commit messages and Chinese issue/PR titles and discussions.

### B. Commit format

Skip when not applicable or already specified. Ask: Use type(scope): description for commit titles, including ! for breaking changes? Recommend yes. Otherwise collect the preferred format and update the commit rule in changes.md. Write the description in the chosen commit-message language.

### C. Record maintenance

Skip when an explicit project rule already settles this or there are no shared work records. Ask: When a task or handoff has not assigned body maintenance, should the creator maintain the body and others propose changes in comments? Recommend yes. On no, record the preferred fallback in collaboration.md. Adapt the question and template to the project's actual records and discussion locations. Task and workflow assignments take precedence over this fallback.

### D. Independent reader check

Skip when already configured. Ask: Before publishing new or substantially changed instructions, decisions, or handoffs that others will act on, should a subagent unfamiliar with this conversation read the draft and explain what they understand and would do next? Recommend yes; ordinary short replies use self-review. On yes, include reader-check.md and its entry-point pointer. On no, omit both.

Use the remaining template rules directly in the draft. Raise an additional question for a concrete conflict or missing fact needed to finish it.

## 3. Confirm and edit

Show the complete proposed files and the Agent skills block, including the selected languages and any project-specific adaptations. Let the user edit the draft before confirming the write.

Default shared files to docs/conventions/ and the reader procedure to docs/agents/; use equivalent existing locations where present. Omit inapplicable commit, issue, or PR rules and tailor the entry summaries and triggers to the remaining content. Link existing tracker and engineering guidance instead of copying it. Preserve fixed fields, labels, identifiers, and paths required by tools or workflows when adapting prose.

Prepare the files from these sibling seed templates:

- [language.md](language.md): the chosen languages, written to docs/conventions/language.md.
- [chinese-wording.md](chinese-wording.md): the Chinese wording introduction and table, written to docs/conventions/chinese-wording.md when Chinese is used. Keep its content focused on wording choices.
- [collaboration.md](collaboration.md): shared-record and communication conventions, written to docs/conventions/collaboration.md.
- [changes.md](changes.md): applicable change and delivery conventions, written to docs/conventions/changes.md.
- [reader-check.md](reader-check.md): the subagent reading procedure, written to docs/agents/reader-check.md when adopted.

## 4. Write

If CLAUDE.md exists, edit it; otherwise edit AGENTS.md. If neither exists, ask which to create. Update relevant entries within an existing Agent skills block, preserving unrelated entries and surrounding content.

Write the confirmed files, resolving placeholders and relative links. Keep the adopted rules and their references accessible from the project. Check the generated files, links, conditional inclusions, and entry points against the confirmed draft.

## 5. Done

Report the files and what each governs. The user can edit these project conventions directly later.

## Agent skills entry template

```markdown
## Agent skills

### Writing languages

<One-line summary of the chosen artifact languages>. Before writing project content, see `docs/conventions/language.md`.

### Chinese wording

Use the project's preferred Chinese wording when writing Chinese. See `docs/conventions/chinese-wording.md`.

### Collaboration

Record maintenance, handoff, and sharing follow the project conventions. Before editing shared records, handing off work, or publishing project material, see `docs/conventions/collaboration.md`.

### Changes and delivery

<One-line summary of the adopted commit convention>. Before preparing commits or PR changes, or reporting delivery and acceptance, see `docs/conventions/changes.md`.

### Independent reader check

Before publishing new or substantially changed instructions, decisions, or handoffs that others will act on, see `docs/agents/reader-check.md` for the reading procedure and when self-review suffices.
```
