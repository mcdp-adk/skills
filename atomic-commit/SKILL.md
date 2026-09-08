---
name: atomic-commit
description: "Group related Git changes into one coherent commit and name it `type(scope): description`. Use when committing work, splitting or grouping changes into commits, or writing a commit message."
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

## Name it

For `scope`, reuse an established name for this area when one exists: a scope in recent commits, or a directory or package name when commits have none. Write it as the repository already writes it. When nothing established exists, invent a lowercase kebab-case scope. When paths span several historical scopes and the change is still one intention, use the narrowest established scope that covers it.

- Write `type` in lowercase. Always include `scope`. Use Conventional Commits types.
- Write `description` in the repository's language, in imperative mood, with no trailing period.
- Use `!` only for compatibility-breaking changes.
- Use one line. If the repository requires trailers or another format, follow the repository.

```text
feat(auth): add passkey login
feat(user-profile): add avatar upload
feat(api)!: remove legacy pagination
```

## Create it

Stage the chosen paths or hunks. Read the staged diff and confirm it matches the intention and the message.

Pass the entire one-line message as one argument. If the shell would interpolate `$` or backticks, write the message to a temp file outside the repository and use `git commit -F`.
