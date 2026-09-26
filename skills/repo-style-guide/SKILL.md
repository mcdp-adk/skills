---
name: repo-style-guide
description: Keep naming, content, and links consistent when preparing Git commits or creating and updating GitHub issues and pull requests.
---

# Repository Style Guide

Apply these conventions to the requested operation; they do not prescribe a delivery workflow.

Follow the user's explicit instructions for this operation, then explicit project conventions and templates, then these defaults. Use project examples to establish language and terminology; incidental variation does not override defaults.

## Commit and PR titles

Use `type(scope): description`, with lowercase Conventional Commits types and `!` before the colon for breaking changes. Reuse established scopes; otherwise name the affected module or directory in lowercase kebab-case. Omit scope when no single area fits.

Write in the project's language, in imperative mood, without a trailing period. Describe the commit's own diff or the PR's complete diff. Squash commit titles follow the same convention.

## Content

- **Commits:** Keep one coherent intention per commit, including its supporting tests and docs. Default to a one-line message.
- **Issues:** Title the problem or requested outcome in natural language. Follow the selected planning workflow for the body. Reuse project labels for classification and status rather than adding title prefixes or inventing a taxonomy.
- **PRs:** Describe the resulting change and verification. Keep the description current as the diff changes; scale detail to complexity.

## Issue references

Put issue relationships in the PR body by default. Use `Closes #123` only when the PR fully resolves that issue and targets the default branch; use `Related to #123` for partial work or context. Individual commits need not repeat these references.
