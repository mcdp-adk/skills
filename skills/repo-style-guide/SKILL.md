---
name: repo-style-guide
description: Sets fallback formats for branch names, commit messages, and PR and issue titles. Use when naming a branch, writing a commit message, or titling a PR or issue.
---

# Repository Style Guide

## Precedence

The user's instructions come first, then the project's conventions, then these fallbacks. Follow the conventions on every point they set and the fallbacks on every other point. The project's conventions are:

- Written rules: commit message tooling config (commitlint, commitizen, commit-msg hooks), `CONTRIBUTING`, `AGENTS.md`, `CLAUDE.md`, and PR and issue templates.
- The commit history, when the last 20 non-merge commit subjects on the default branch share one pattern: a type prefix, a scope, and an emoji are each present in all 20 or in none, and the text after them starts with the same letter case in all 20. Any other history, including one shorter than 20 commits, sets no convention.

## Fallbacks

**Type**: the first of these that fits the change. Behavior includes the content the project ships, such as prompts, skills, and templates.

1. `revert`: reverts an earlier commit.
2. `fix`: corrects behavior that deviates from its intended design.
3. `perf`: makes existing behavior faster or lighter.
4. `feat`: adds or changes behavior.
5. `refactor`: restructures without changing behavior.
6. `style`: changes formatting only.
7. `test`: changes tests only.
8. `docs`: changes documentation only.
9. `build`: changes the build system or dependencies.
10. `ci`: changes CI configuration.
11. `chore`: anything else.

**Issue title**: one sentence in sentence case with no trailing period. For a defect, state the faulty behavior; for anything else, state the requested outcome.

**Branch**: `type/topic`, where `type` is the type of the branch's whole change and `topic` is two to four lowercase ASCII words joined by hyphens.

**Commit message**: one line, `type: subject`, or `type!: subject` when users or dependent code must change to keep working. The type alone precedes the colon. The subject starts with a lowercase imperative verb and ends without a period, and the whole line is at most 72 characters. The why belongs in the PR, so the line carries only the what; a change that will not fit in one line is more than one commit, so split it. Tool-generated messages (merge, revert, `fixup!`, `squash!`) stay as the tool writes them.

**PR title**: the commit message line for the PR's whole change. For a single-commit PR, that commit's line verbatim.
