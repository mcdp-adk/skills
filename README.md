# Agent Skills

**English** | [简体中文](README.zh-CN.md)

A small collection of [Agent Skills](https://agentskills.io) for coding agents. Choose the skills that fit your work and install them individually or together.

## Install

Requires Node.js 22.20 or newer. Install with the [Vercel Labs `skills` CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add mcdp-adk/skills
```

Follow the prompts to choose your skills, or specify one with `--skill`:

```bash
npx skills add mcdp-adk/skills --skill repo-style-guide
```

Active skills live in `skills/`; archived skills are retained in `deprecated/` with `metadata.internal: true`.

## Available skills

| Skill | What it does |
| --- | --- |
| [`chinese-typography`](skills/chinese-typography/SKILL.md) | Standardizes spacing and punctuation when writing or editing Chinese and mixed Chinese-English text. |
| [`eroge-localization`](skills/eroge-localization/SKILL.md) | Provides methods for localizing Japanese eroge into target languages, with detailed Chinese guidance, asset processing, and engine adaptation references. |
| [`everything-cli`](skills/everything-cli/SKILL.md) | Finds files, directories, and projects on Windows when their location is unknown. |
| [`repo-style-guide`](skills/repo-style-guide/SKILL.md) | Standardizes names and wording when preparing Git branches and commits or writing GitHub issues, pull requests, and comments. |

Additional requirements:

- **everything-cli**: Install Everything and ES (`es.exe`), and keep Everything running.

## License

[MIT](LICENSE)
