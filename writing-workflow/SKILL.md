---
name: writing-workflow
description: Reader-centered writing and substantive rewriting for human-facing documents such as READMEs, technical explanations, guides, reports, and Chinese technical content. Use when facts or conclusions must become a document readers can understand, navigate, and act on; do not use for ordinary code edits.
---

# Reader-Centered Writing

A document is complete when its intended readers can understand what matters and make the intended decision or take the intended action. Structure, language, and length all serve that result.

## Define the reader and outcome

Before drafting, establish:

- who will read the document and what they already know;
- what they must understand, decide, or do afterward;
- which statements are established facts and which remain inference or unknown;
- what the document covers and explicitly does not cover.

Use the reader and outcome to select information. A user-facing document should prioritize successful use; a maintainer-facing document usually needs design relationships and tradeoffs.

Ask for clarification only when missing information would change the document's direction or factual meaning. Make reversible choices such as wording, headings, and paragraph order directly from the reader's needs.

## Build the reading path

Organize material in the order readers solve their problem, not the order in which the information was collected:

- When readers need to act, lead with the result, entry point, and necessary steps; add reasons and detail afterward.
- When readers need to understand, establish the minimum background and overall relationships before mechanisms, tradeoffs, and exceptions.
- Make headings correspond to reader tasks so scanning reveals where to go.
- Use lists for parallel items and sequences. Use tables only when fixed dimensions need comparison.
- Give each paragraph one central idea, with causal, conditional, and sequential relationships made explicit.

Disclose detail in layers when useful, but keep information required for the reader's task on the main path. State missing sources, conflicting facts, and logical gaps directly or supply the needed evidence; do not hide them behind more terminology or structure.

## Write clearly and naturally

Use words the intended reader can understand precisely. Technical terms earn their place by increasing accuracy. Give necessary terms enough context at first use, and replace abstractions that name no concrete object, action, or decision criterion with direct statements.

Write in the requested output language and preserve established terminology. Keep one term for each concept throughout the document.

When the output is Chinese, or Chinese terminology, typography, and sentence structure materially affect quality, read the [Chinese writing reference](references/chinese-writing-reference.md). Keep detailed language-specific rules and examples there rather than duplicating them here.

## Revise from the reader's entry point

Read the finished document from the intended reader's entry point. Confirm that readers can recognize its purpose, locate what they need, and understand important relationships without relying on the author's unstated background. Remove sentences that do not improve understanding or action while preserving necessary causality.

When rewriting existing material, preserve meaning and certainty. Do not turn inference into fact or advice into a decision. Keep real paths, fields, commands, and references accurate.
