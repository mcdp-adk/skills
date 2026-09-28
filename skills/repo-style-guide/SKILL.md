---
name: repo-style-guide
description: Standardize names, wording, and links in Git and GitHub collaboration. Use when naming branches, creating or rewriting commits, pushing or merging changes, or creating, editing, or publishing issues, pull requests, and comments.
---

# Repository Style Guide

Follow the user's explicit instructions for the task, then explicit project conventions and templates, then these defaults. Use English by default and reuse project terminology.

## Context and references

Write messages and descriptions so their intended readers can understand what they represent and the key facts without access to the private task conversation. Use accessible references for supporting evidence, detailed discussion, and history. Include sources and related work when needed to explain the record's origin, rationale, or relationship to other work, and make each relationship clear. Keep the text proportional to its purpose.

## Commits

Keep one coherent intention per commit, including its supporting tests and docs. Write the message for the change that commit represents, whether newly created, combined, or rewritten.

For ordinary change commits, use `type(scope): description`, with `!` before the colon for breaking changes. Use lowercase types following Conventional Commits and established project usage. Choose the type for the change represented by that commit.

Include a scope when the change has a meaningful project area. Reuse the scope names and granularity established for similar changes. Otherwise, choose a feature or module that captures the main change, using project terminology in lowercase kebab-case. Supporting tests, configuration, and wiring across directories do not by themselves make the scope broader. Omit scope when no meaningful area captures the change.

Describe the commit's overall change in imperative mood, without a trailing period.

Add an explanatory body when readers need more than the title to understand the commit, such as its rationale, behavior, or important consequences. Separate it from the title with a blank line. Use short paragraphs for connected explanations or `-` bullets for parallel points, with plain wording rather than repeated commit-title prefixes and without fixed section headings.

Put references and standard metadata in a footer, whether or not an explanatory body is needed. Separate it from the preceding text with a blank line, with each entry on its own line. Use `Refs: <reference>` for ordinary associations and the appropriate syntax for other relationships or metadata.

Preserve operation-specific structure in merge and revert messages, and tool-interpreted markers such as `fixup!`. Describe the integration or reversal where relevant.

## Branch names

Use `type/short-topic`: a lowercase change type followed by a short kebab-case topic. Choose the type using the same meanings as commit types, based on the branch's overall purpose. Where the project or tool requires a prefix, use that prefix with the topic.

## Issues and pull requests

### Titles

Use natural language to name the problem, requested outcome, or proposed change. Use existing labels for classification rather than type or status prefixes in titles.

### Bodies and comments

Use the applicable project or task template for the body. Distinguish proposals from established decisions.

Publish comments that add information needed to decide or continue the work, such as a question, decision, blocker, or new evidence. Omit routine progress narration and repeated summaries; link existing information instead.

## Applying the conventions

Before recording or publishing names or text, check their final form against the applicable conventions. Reuse existing or tool-generated wording where it remains accurate and useful, adapting it to the final record.

Local commits can proceed under the current task's instructions, with each message checked. Before publishing names or text whose later correction would require rewriting shared history or disrupt others' work, show the complete proposed text as it will be recorded and wait for confirmation. Include any body and footer in the preview. Group related items into one preview, including the full messages for a series of commits.

Previously approved text needs no further confirmation while it and the applicable conventions remain unchanged. Check new or changed text produced by later operations. If the user explicitly requests direct execution, check the text and proceed within that request.
