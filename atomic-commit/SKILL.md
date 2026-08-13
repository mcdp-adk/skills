---
name: atomic-commit
description: Group related Git changes into one coherent commit and name it `type(scope): description`. Use when committing work, splitting or grouping changes into commits, or writing a commit message.
---

# Atomic Commit

One commit expresses one coherent intention. Name it in one line:

```text
type(scope): description
type(scope)!: description  # breaking change
```

Atomic means one change a reader can understand as a unit — not the smallest technically separable diff. Implementation belongs with the tests, docs, and config that make it complete. Unrelated work stays out.

## Decide what belongs

State the intention in one sentence. List the paths and hunks that implement it, including untracked files that belong to it.

Keep together what serves that intention. Split only when the working tree holds a second, unrelated intention — the kind that would force "and" or "also" into the message.

If one file mixes two intentions, stage the matching hunks when the boundary is clear. If it is not, stop and say so rather than rewriting the working tree to manufacture a split.

Look at recent commit subjects for language and how this repository names scopes. This skill fixes the message shape; the repository supplies the established wording. When paths span several historical scopes and the change is still one intention, use the narrowest established scope that covers it.

## Name it

- Write `type` and `scope` in lowercase. Always include `scope`.
- Write `description` in the repository's language, in imperative mood, with no trailing period.
- Use `!` only for compatibility-breaking changes.
- Use one line. If the repository requires trailers or another format, follow the repository.

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

## Create it

Stage the chosen paths or hunks. Read the staged diff and confirm it matches the intention and the message.

Pass the entire one-line message as one argument. If the shell would interpolate `$` or backticks, write the message to a temp file outside the repository and use `git commit -F`.
