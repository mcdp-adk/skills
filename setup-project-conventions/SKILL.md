---
name: setup-project-conventions
description: "Configure this repo's writing languages, collaboration rules, commit conventions, and reader checks. Run when setting up project conventions."
disable-model-invocation: true
---

# Setup Project Conventions

Set up the per-repo conventions that contributors and agents follow:

- **Writing languages**: which languages to use, with a separate wording guide when Chinese is used
- **Collaboration**: how to write and maintain shared records, hand off work, and share information
- **Changes and delivery**: commit conventions, PR descriptions, and delivery evidence
- **Reader checks**: when a fresh-context subagent should read a draft before publication

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Process

### 1. Explore

Look at the current repo to understand its starting state. Read whatever exists; don't assume:

- `AGENTS.md` and `CLAUDE.md` at the repo root: does either exist? Is there already an `## Agent skills` section in either?
- Contributor guidance, linked project conventions, and issue/PR templates
- `docs/conventions/` and `docs/agents/`: does this skill's prior output already exist?
- Git remotes and relevant examples of project writing and contributions

Identify explicit language and contribution rules, work-record locations, maintenance responsibilities, engineering guidance, and sharing boundaries. Reuse existing tracker, labels, domain docs, and artifact contracts, including those configured by Matt's setup; keep their definitions in their existing sources.

Explicit rules settle a choice. Examples inform a recommendation.

### 2. Present findings and ask

Summarize the existing choices and gaps. Take the sections in order. Ask one unresolved choice, wait for its answer, then continue. Lead with the recommended answer. Skip settled or inapplicable choices.

**Section A: Writing languages.**

Establish the project's current readers and collaborators from project guidance and the user's context. Identify their language needs, distinguishing product users from contributors where relevant. Clarify missing information that affects the recommendation.

Recommend a shared language for contributor communication and material they maintain, including requirements, design explanations, development records, and code comments. Offer:

- **English**
- **Current conversation language**: name it; omit this option when it duplicates English
- **Other**: ask which language

Carry each answer forward to the content it covers. Ask separately where different readers, existing conventions, or tooling create an actual difference. Choose the language of user documentation for its intended readers.

For multilingual material, record the language of each version and reference its existing translation guidance. When a new multilingual arrangement is requested, establish its languages and file locations, then clarify how corresponding versions should be kept aligned if that is still unresolved.

Use English for the main convention files produced by this setup unless the user chooses otherwise. The separate `chinese-wording.md` uses Chinese. Record both choices in `language.md`. If Chinese is used, generate `chinese-wording.md` and its pointer from the wording seed, preserving the recommended forms unless the user or existing project conventions specify an override.

Apply the chosen collaboration language to both issues and PRs, including titles, bodies, and comments. Resolve commit-message language separately when unsettled. For example, English commits and Chinese collaboration means English commit messages and Chinese issue/PR titles and discussions.

**Section B: Commit format.** Skip when commits don't apply or the project already specifies a format.

> Use `type(scope): description` for commit titles, with `!` for breaking changes? (recommended: **yes**)

On **yes**, keep the seed's commit format. Otherwise, collect the preferred format and update the commit rule in `changes.md`. Write descriptions in the chosen commit-message language.

**Section C: Record maintenance.** Skip when an explicit project rule already settles this or there are no shared work records.

> When a task or handoff hasn't assigned body maintenance, should the creator maintain the body and others propose changes in comments? (recommended: **yes**)

On **yes**, keep the seed's fallback. Otherwise, record the preferred fallback in `collaboration.md`. Adapt it to the project's actual records and discussion locations. Task and workflow assignments take precedence over this fallback.

**Section D: Independent reader check.** Skip when already configured.

> Before publishing new or substantially changed instructions, decisions, or handoffs that others will act on, should a subagent unfamiliar with this conversation read the draft and explain what they understand and would do next? (recommended: **yes**)

Ordinary short replies use self-review. On **yes**, include `reader-check.md` and its entry point. On **no**, omit both.

Use the remaining template rules directly in the draft. Raise an additional question for a concrete conflict or missing fact needed to finish it.

### 3. Confirm and edit

Show the user a draft of:

- The `## Agent skills` block to add to whichever of `CLAUDE.md` / `AGENTS.md` is being edited (see step 4 for selection rules)
- The complete contents of `docs/conventions/language.md`, `docs/conventions/collaboration.md`, and `docs/conventions/changes.md`
- `docs/conventions/chinese-wording.md` when Chinese is used
- `docs/agents/reader-check.md` when the reader check is adopted

Let the user edit before confirming the write.

Default shared files to `docs/conventions/` and the reader procedure to `docs/agents/`; use equivalent existing locations where present. Omit inapplicable commit, issue, or PR rules and tailor the entry summaries to the remaining content. Link existing tracker and engineering guidance instead of copying it. Preserve fixed fields, labels, identifiers, and paths required by tools or workflows when adapting prose.

### 4. Write

**Pick the file to edit:**

- If `CLAUDE.md` exists, edit it.
- Else if `AGENTS.md` exists, edit it.
- If neither exists, ask the user which one to create; don't pick for them.

If an `## Agent skills` block already exists in the chosen file, update the relevant entries in-place rather than appending a duplicate. Preserve unrelated entries and surrounding sections.

The block:

```markdown
## Agent skills

### Writing languages

[one-line summary of the chosen languages and where each applies]. See `docs/conventions/language.md`.

### Chinese wording

[one-line summary of the preferred wording for Chinese content]. See `docs/conventions/chinese-wording.md`.

### Collaboration

[one-line summary of record maintenance, handoffs, and sharing conventions]. See `docs/conventions/collaboration.md`.

### Changes and delivery

[one-line summary of commit, PR, and delivery conventions]. See `docs/conventions/changes.md`.

### Independent reader check

[one-line summary of when drafts need a fresh-context reader]. See `docs/agents/reader-check.md`.
```

Include the `### Chinese wording` sub-block and its file only when Chinese is used. Include the `### Independent reader check` sub-block and its file only when the check is adopted.

Then write the docs files using the seed templates in this skill folder as a starting point:

- [language.md](./language.md): chosen languages and language-version rules
- [chinese-wording.md](./chinese-wording.md): Chinese wording choices (only when Chinese is used)
- [collaboration.md](./collaboration.md): shared records, handoffs, and sharing boundaries
- [changes.md](./changes.md): commits, PR descriptions, and delivery evidence
- [reader-check.md](./reader-check.md): fresh-context reading procedure (only when adopted)

Resolve placeholders and relative links. Check that the written files and entry points match the confirmed draft.

### 5. Done

Tell the user setup is complete and which files hold the conventions. Mention they can edit these files directly later.
