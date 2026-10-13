---
name: design-md
description: Applies, creates, updates, and validates a project's DESIGN.md in Google's open DESIGN.md format. Use when changing the UI of a project that has a DESIGN.md, or when writing, editing, or checking a DESIGN.md or recording a project's visual design system.
compatibility: Validation requires Node.js to run `@google/design.md` through npx.
---

# DESIGN.md

`DESIGN.md` sits at the repository root. Its YAML front matter holds the design tokens, the exact values; its Markdown body gives the intent behind them and how to apply them.

## Apply it to UI work

Read `DESIGN.md` before changing the UI; if the project has none, carry on without it.

- Take values from the tokens. A component entry styles that component, and entries with related keys (`button-primary-hover`) style its states; a reference such as `{colors.primary}` stands for the token it names.
- Follow the prose for how to apply them, the Do's and Don'ts as guardrails, and the Overview wherever no token or rule decides.
- When the task needs something `DESIGN.md` does not define or contradicts, such as a new color or component style, tell the user. Once they decide, record the decision in `DESIGN.md` as below.

## Create or update the file

Read [the format reference](references/spec.md), a snapshot of Google's DESIGN.md specification, before writing.

Record the decisions the project has already made, taking every value from a source:

- The existing UI: theme configuration, CSS variables, and component styles. Values that recur become tokens.
- Brand material the user provides.
- Decisions the user states.

When a section has no source, ask the user for the decision. If the project deliberately leaves it undefined, leave the section out; for a token group, also list it under `omitted` with the reason.

When sources disagree with each other or with the existing `DESIGN.md`, show the user the differing values and let them decide. Bringing implementation code in line with `DESIGN.md` is separate work.

- Section headings, schema keys, and component properties are English, exactly as the spec names them; token names are the project's choice. Write the prose in the project's established language, or English when none is established.
- Change a token and the prose describing it together.
- Spend the prose on what the values cannot say: the intent behind them and how to apply the design where no token decides.

## Validate

After writing, run from the repository root:

```bash
npx -y -p @google/design.md@0.4.0 designmd lint DESIGN.md
```

Run it as written: this form works on every platform, and its version matches the format reference.

Resolve every error; fix each warning or tell the user why it stands. The linter reads only the tokens, so check that every value the prose shares with a token matches it. If the linter cannot run, tell the user that the file has not been machine-validated.
