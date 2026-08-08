---
name: atomic-commit
description: Plan, review, and complete atomic Git commits. Use when the current task requires deciding what one commit should contain or how it should be expressed, including splitting scope, checking readiness, staging candidate changes, generating or reviewing the message, creating the commit, and verifying it. Do not use for ordinary status checks, history queries, or Git operations that require no commit-content or message decision.
---

# Atomic Commit

Make each commit express one intention that can be understood, verified, and reverted independently. Use one-line messages: `type(scope): description` for ordinary changes and `type(scope)!: description` for breaking changes.

Atomic history supports fault isolation, independent rollback, and change comprehension. File count is not the criterion; the commit must form one coherent state.

When write operations are not authorized, only analyze scope or propose a message. Modify the index only when staging is authorized, and create a commit only when committing is explicitly authorized.

## Understand the repository and changes

Confirm the repository root, then inspect:

- `git status`, distinguishing staged, unstaged, and untracked files;
- the complete working-tree and staged diffs, examining every candidate hunk;
- the actual content of candidate untracked files, which ordinary `git diff` does not show;
- the latest 10 commit subjects, or the full history when fewer than 10 exist;
- recent history for the candidate paths, such as `git log -10 -- <paths>`.

Use repository-wide history to determine language, description length, and wording conventions. Use candidate-path history to determine whether scopes follow directories, packages, modules, features, or files. This Skill fixes the message shape; the repository determines its established expression.

If the index already contains changes of uncertain ownership, establish their origin before proceeding so another intention does not enter the commit.

## Determine the atomic scope

State the commit intention in one sentence and list the repository-relative paths and hunks that implement it. An atomic scope satisfies all four tests:

- **Single intention:** The message does not need “and” or “also” to connect unrelated purposes.
- **Independent rollback:** Reverting the commit removes only that intention, without removing unrelated work or leaving an incomplete state.
- **Complete state:** The repository remains coherent and verifiable after the commit. Inseparable tests, documentation, configuration, and generated artifacts belong with the change.
- **Indivisible scope:** If two parts can still be understood, verified, and reverted independently after separation, split them.

When one file contains multiple intentions, stage only selected hunks when the boundaries are reliable. Otherwise stop and explain that the current working tree cannot form the intended atomic scope; do not edit the working tree merely to manufacture staging boundaries.

Determine atomic scope before choosing the message scope. When candidate paths map to several historical scopes, reconsider whether the change should split. If it is genuinely indivisible, use the narrowest established scope that covers the whole intention. Without precedent, use the real shared domain; do not concatenate scopes or use vague names such as `misc`.

For amend, revert, and other operations that create or replace a commit, judge the complete resulting commit against its parent, not only the newly introduced delta.

Stop when the candidate includes credentials, secrets, personal data, or temporary files that should not enter the repository.

## Write the one-line message

```text
type(scope): description
type(scope)!: description  # breaking change
```

- Write `type` and `scope` in lowercase.
- Always include `scope`, using the stable name selected after determining atomic scope.
- Write `description` in the repository's customary language and imperative mood. Keep it brief and omit the final period.
- Use `!` only for compatibility-breaking changes so release and changelog tooling can identify them.
- Do not add a body or footer. Report a conflict before committing when repository policy requires trailers or another format.

| type | Use for |
|------|---------|
| `feat` | User-visible capability |
| `fix` | Defect correction |
| `docs` | Documentation-only change |
| `style` | Formatting with no semantic change |
| `refactor` | Structural change that adds no feature and fixes no defect |
| `perf` | Performance improvement |
| `test` | New or corrected tests |
| `build` | Build system or dependency change |
| `ci` | CI configuration or scripts |
| `chore` | Other maintenance work |
| `revert` | Reversal of an earlier commit |

```text
feat(auth): add passkey login
fix(parser): handle empty arrays
feat(api)!: remove legacy pagination
docs(readme): clarify local setup
```

Include only information needed to understand this change and suitable for permanent repository history.

## Stage, commit, and verify

Stage only confirmed paths or hunks. Reread the staged diff and confirm that every change serves the same intention, necessary tests and documentation are present, and the message accurately summarizes the content. Before creating or replacing a commit, confirm the expected complete commit diff.

Pass the entire one-line message as one argument. When only a shell is available and the message contains `$`, backticks, or other interpolation-sensitive characters, write it to a temporary file outside the repository and use `git commit -F`.

After committing, read `git log -1 --format=%H%n%B` and the complete patch. Confirm that the recorded message exactly matches the approved line and that the commit diff equals the complete result reviewed before committing.

If the message, scope, or command result differs from the approved result, preserve the state and report it. Do not automatically amend, revert, push, or bypass hooks; each action requires separate explicit authorization.
