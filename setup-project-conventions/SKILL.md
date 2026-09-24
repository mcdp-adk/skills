---
name: setup-project-conventions
description: "Configure this repo's writing languages, collaboration rules, change delivery workflow, and reader checks. Run when setting up project conventions."
disable-model-invocation: true
---

# Setup Project Conventions

Set up the per-repo conventions that contributors and agents follow:

- **Writing languages**: which languages to use, with a separate wording guide when Chinese is used
- **Collaboration**: how to write and maintain shared records, hand off work, and share information
- **Changes and delivery**: how changes enter the project, commit conventions, and delivery evidence
- **Reader checks**: when a fresh-context subagent should read a draft before publication

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Process

### 1. Explore

Look at the current repo to understand its starting state. Read whatever exists; don't assume:

- `AGENTS.md` and `CLAUDE.md` at the repo root: does either exist? Is there already an `## Agent skills` section in either?
- Contributor guidance, linked project conventions, and issue/PR templates
- `docs/conventions/` and `docs/agents/`: does this skill's prior output already exist?
- Git remotes, default branch, documented branch and integration rules, and available merge methods
- Relevant examples of project writing and contributions

Identify explicit language and contribution rules, work-record locations, maintenance responsibilities, engineering guidance, and sharing boundaries. Reuse existing tracker, labels, domain docs, and workflow definitions; keep their definitions in their existing sources.

Explicit rules settle a choice. Examples inform a recommendation.

### 2. Present findings and ask

Summarise what's present and what's missing. Take the sections in order. Ask one unresolved choice, wait for its answer, then continue. Lead with the recommended answer so the user can accept it in a word. Skip settled or inapplicable choices.

**Section A: Writing languages.**

Establish the project's current readers and collaborators from project guidance and the user's context. If this is unclear, ask:

> Who will read and maintain this project's content?

Use the answer to recommend a language for contributor communication and material they maintain, including requirements, design explanations, development records, and code comments. Name the content covered by the recommendation, then ask which language to use. Offer:

- **English**
- **Current conversation language**: name it; omit this option when it duplicates English
- **Other**: ask for the language

Carry each answer forward to the content it covers. If the user describes different languages for different content, record that arrangement. Ask separately only where readers or project requirements differ. User documentation follows its intended readers; it may need a different language from contributor material.

For existing multilingual material, record the versions and link its translation guidance. If the user requests a new multilingual arrangement, ask them to describe the versions they need. Collect missing languages, file locations, and maintenance expectations one at a time, rather than proposing a fixed set of language combinations.

Use English for the main convention files produced by this setup unless the user chooses otherwise. The separate `chinese-wording.md` uses Chinese. Record both choices in `language.md`. If Chinese is used, generate `chinese-wording.md` and its pointer from the wording seed, preserving the recommended forms unless the user or existing project conventions specify an override.

Apply the chosen collaboration language to both issues and PRs, including titles, bodies, and comments. When Git is used and commit-message language is unsettled, ask which language commit messages should use. Record that answer separately from the collaboration language.

**Section B: Changes and delivery.** Skip Git-specific choices when the project doesn't use Git.

> Explainer: This is how a change enters the project: where work starts, where it is submitted, and how it is integrated. Existing project workflows take precedence.

**Submission workflow.** If exploration settled it, use that workflow. Otherwise, ask:

> How should changes enter this project?

Recommend **pull requests** when available. Describe the applicable choices briefly so the user can accept the recommendation or choose another workflow:

- **Pull requests**: develop on a task branch and submit a PR to the receiving branch. Use the platform's equivalent, such as a merge request, where applicable.
- **Branch merges**: develop on a task branch and merge it into the receiving branch without a PR.
- **Direct commits**: commit changes on the receiving branch, without a PR.
- **Other**: ask the user to describe their workflow in a short paragraph; record it as prose and clarify only missing steps needed to use it.

For projects without Git, collect their delivery workflow as freeform prose and skip the branch, merge-method, and commit-format questions.

**Branches.** Use existing branch rules. Otherwise, use the default branch as the starting point for new work and the receiving branch, and include that choice in the preview without a separate confirmation. When a branch cannot be established, ask for its name directly. Continue a task's assigned branch where applicable. Leave branch naming and workspace tools to existing project conventions.

**Integration.** For workflows that merge branches, ask only if the merge method is unsettled:

> How should task branches be integrated?

Recommend **merge commit**. Offer the methods supported by the project:

- **Merge commit**: retain the individual commits and add a merge commit.
- **Squash**: combine the submitted changes into one commit.
- **Rebase**: replay the individual commits onto the receiving branch without a merge commit.

Record the selected method in `changes.md`. Skip this question for direct commits or when the user's custom workflow already explains integration.

**Commit format.** If not already specified, ask:

> Use `type(scope): description` for commit titles, with `!` for breaking changes? (recommended: **yes**)

On **yes**, keep the seed's commit format. Otherwise, collect the preferred format and update the commit rule in `changes.md`. Write descriptions in the chosen commit-message language.

Use [changes.md](./changes.md) as the PR-based seed. Replace its integration section with the selected workflow and resolved branches. For branch merges without a PR, keep the task-branch and merge steps. For direct commits, describe committing on the receiving branch. In both cases, replace PR-specific reporting with the project's delivery record or task handoff. For other workflows, write the integration section from the user's description. Keep only applicable rules; the generated file describes this project's workflow, not a menu of alternatives.

Adapt work references and completion rules to the project's record system, even when it differs from the code host. Use automatic closing links only where that system supports them and its workflow permits closure on merge.

**Section C: Record maintenance.** Skip when an explicit project rule already settles this or there are no shared work records.

The default is that the creator maintains the body and others propose changes in comments, unless a task or workflow assigns responsibility differently. Describe this using the project's records and discussion locations, then ask:

> Do you want to keep this default division of responsibility? (recommended: **yes**)

On **yes**, keep the seed's fallback. Only if the user says no, ask who maintains the records and how others propose changes; record that arrangement in `collaboration.md`.

**Section D: Independent reader check.** Skip when already configured.

> Explainer: A subagent unfamiliar with this conversation reads a draft and explains what they understand and would do next. This checks whether readers can act on it without private conversation context. It applies to new or substantially changed instructions, decisions, and handoffs; ordinary short replies use self-review.

> Do you want to use this reader check before publishing? (recommended: **yes**)

On **yes**, include `reader-check.md` and its entry point. On **no**, omit both.

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

[one-line summary of the submission workflow, integration method, and commit conventions]. See `docs/conventions/changes.md`.

### Independent reader check

[one-line summary of when drafts need a fresh-context reader]. See `docs/agents/reader-check.md`.
```

Include the `### Chinese wording` sub-block and its file only when Chinese is used. Include the `### Independent reader check` sub-block and its file only when the check is adopted.

Then write the docs files using the seed templates in this skill folder as a starting point:

- [language.md](./language.md): chosen languages and language-version rules
- [chinese-wording.md](./chinese-wording.md): Chinese wording choices (only when Chinese is used)
- [collaboration.md](./collaboration.md): shared records, handoffs, and sharing boundaries
- [changes.md](./changes.md): submission, integration, commit conventions, and delivery evidence
- [reader-check.md](./reader-check.md): fresh-context reading procedure (only when adopted)

Resolve placeholders and relative links. Check that the written files and entry points match the confirmed draft.

### 5. Done

Tell the user setup is complete and which files hold the conventions. Mention they can edit these files directly later.
