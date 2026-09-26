---
name: repo-style-guide
description: Apply default conventions for names, wording, and links. Use when naming Git branches, preparing commits, or writing GitHub issues, pull requests, and comments.
---

# Repository Style Guide

Follow the user's explicit instructions for the task, then explicit project conventions and templates, then these defaults. Use English by default and reuse project terminology.

## Branch names

Use `type/short-topic`: a lowercase Conventional Commits type followed by a short kebab-case topic. Name the branch for its overall purpose. Where the project or tool requires a prefix, use that prefix with the topic.

## Commits

Keep one coherent intention per commit, including its supporting tests and docs.

For ordinary change commits, use `type(scope): description`, with lowercase Conventional Commits types and `!` before the colon for breaking changes. Reuse established scopes; otherwise use the affected module or directory in lowercase kebab-case. Omit scope when no single area fits.

Describe the commit's change in imperative mood, without a trailing period. Default to a one-line message; add a body when the reason, constraints, or references are needed to understand the change.

For messages recording Git operations, such as merges, follow the project or tool's established format. Check generated messages for an accurate description and useful references; supplement them when important information is missing.

## Issues and pull requests

### Titles

Use natural language to name the problem, requested outcome, or proposed change. Use existing labels for classification rather than type or status prefixes in titles.

### Bodies and comments

Use the applicable project or task template for the body. Distinguish proposals from established decisions, and give readers enough context or accessible references to understand the text without the private task conversation.

Publish comments that add information needed to decide or continue the work, such as a question, decision, blocker, or new evidence. Omit routine progress narration and repeated summaries; link existing information instead.

## References

Link related commits, issues, and PRs when the connection helps explain the current work. Make the relationship clear and include enough context for readers to understand the item on its own, with links to supporting detail.
