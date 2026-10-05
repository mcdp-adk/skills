---
name: repo-style-guide
description: Fallback form for branch names, commit messages, and PR and issue titles. Use when naming a branch, writing a commit message, or titling a PR or issue.
---

# Repository Style Guide

These are fallbacks. The user's instructions come first, then the project's conventions: written ones (commitlint config, CONTRIBUTING, AGENTS.md, templates) and the style stable across recent `git log`. Apply a fallback only where both are silent, or the history is empty or mixed.

- **Issue title**: a plain sentence naming the problem or the requested outcome.
- **Branch**: `type/short-topic`, kebab-case, where `type` is the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) type of the branch's overall change.
- **Commit message**: one Conventional Commits header, `type(scope)!: subject`; the header is the whole message. Mark breaking changes with `!`. The why belongs in the PR. A change that will not fit in one header is more than one commit: split it. Keep tool-generated messages (merge, revert, `fixup!`, `squash!`) as the tool writes them.
- **Scope**: include one when it locates the change, reusing the scopes already in `git log`.
- **PR title**: the same header form as a commit, describing the whole change.
