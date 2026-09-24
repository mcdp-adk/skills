# Changes and Delivery

## Submission and integration

Submit changes through pull requests to `<receiving-branch>`.

- Start new work on a task branch from `<starting-branch>`. Continue an assigned task branch when one is already in use for this work.
- Open the PR against the receiving branch. Follow [collaboration.md](./collaboration.md) for language, titles, discussion, and record maintenance.
- Merge using a merge commit, retaining the individual commits. Keep independently meaningful changes separate; fold process-only corrections into the relevant commits when preparing the branch for integration, subject to existing history-rewriting rules.

<Link existing branch or integration guidance where present; otherwise omit this line.>

## Commits

Use type(scope): description for commit titles, with lowercase Conventional Commits types and ! before the colon for breaking changes. Reuse established scopes; omit scope when no single area fits. Write the description in the chosen commit-message language, in imperative mood, without a trailing period, describing this commit's change.

Keep each commit focused on one coherent intention, including supporting tests and docs.

Default commit messages to one line. Add a short body only for essential reasoning that needs to travel with that commit and cannot fit the title. Reference overall context already captured in a PR or design record instead of repeating it.

## Delivery record

Describe the resulting change and verification in the PR; keep it current as the diff changes. Link related work. Use closing links only when the merge fully resolves the work under the tracker's rules; otherwise use a contextual link. Summarize material changes since review.

Follow existing work-record requirements. When no separate record is required or available, explain the purpose and scope in the PR. Determine completion from the applicable workflow and acceptance criteria; submitting a change alone does not establish completion.

## Delivery evidence

<Link existing engineering standards and verification guidance where present; otherwise omit this line.>

Follow the project's implementation and review workflow. Report actual checks, relevant conditions, failures, and unverified work. Reference existing evidence when it still applies to the delivered change.

A passing check supports only what it exercised. Distinguish implementation, self-checks, acceptance, and integration. Where work records use acceptance markers, update them for verified criteria within the task's authority. Make unfinished delivery explicit.
