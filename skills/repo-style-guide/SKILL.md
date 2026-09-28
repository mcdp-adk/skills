---
name: repo-style-guide
description: Standardize names, wording, and links in Git and GitHub collaboration. Use when naming branches, creating or rewriting commits, pushing or merging changes, or creating, editing, or publishing issues, pull requests, and comments.
---

# Repository Style Guide

Follow the user's explicit instructions for the task, then explicit project conventions and templates, then these defaults. Use English by default and reuse project terminology.

## Applying the conventions

Before recording or publishing names or text, check their final form against the applicable conventions. Treat reused and tool-generated wording as drafts to check and adapt.

Local commits can proceed under the current task's instructions, with each message checked. Before publishing names or text whose later correction would require rewriting shared history or disrupt others' work, show the complete proposed text and wait for confirmation. Group related items into one preview, including the full messages for a series of commits.

Previously approved text needs no further confirmation while it and the applicable conventions remain unchanged. Check new or changed text produced by later operations. If the user explicitly requests direct execution, check the text and proceed within that request.

## Commits

Keep one coherent intention per commit, including its supporting tests and docs. Write the message for the change that commit represents, whether newly created, combined, or rewritten. Reuse existing text where it remains accurate and useful.

For ordinary change commits, use `type(scope): description`, with `!` before the colon for breaking changes. Use lowercase types following Conventional Commits and established project usage. Choose the type for the change represented by that commit. Reuse established scopes; otherwise use the affected module or directory in lowercase kebab-case. Omit scope when no single area fits.

Describe the commit's overall change in imperative mood, without a trailing period.

Default to a title only. Add a body when readers need more context or explanation to understand the commit, such as its rationale, behavior, or important consequences. Separate it from the title with a blank line. Use short paragraphs for connected explanations or `-` bullets for parallel points, with plain wording rather than repeated commit-title prefixes. Keep the length proportional to the explanation needed, without fixed section headings.

Put references and standard metadata in a footer, separated from the preceding text by a blank line, with each entry on its own line. Use `Refs: <reference>` for ordinary associations and the appropriate syntax for other relationships or metadata.

Preserve operation-specific structure in merge and revert messages, and tool-interpreted markers such as `fixup!`. Describe the integration or reversal where relevant.

## Branch names

Use `type/short-topic`: a lowercase change type followed by a short kebab-case topic. Choose the type using the same meanings as commit types, based on the branch's overall purpose. Where the project or tool requires a prefix, use that prefix with the topic.

## Issues and pull requests

### Titles

Use natural language to name the problem, requested outcome, or proposed change. Use existing labels for classification rather than type or status prefixes in titles.

### Bodies and comments

Use the applicable project or task template for the body. Distinguish proposals from established decisions, and give readers enough context or accessible references to understand the text without the private task conversation.

Publish comments that add information needed to decide or continue the work, such as a question, decision, blocker, or new evidence. Omit routine progress narration and repeated summaries; link existing information instead.

## References

Link related commits, issues, and PRs when the connection helps explain the current work. Make the relationship clear and include enough context for readers to understand the item on its own, with links to supporting detail.
