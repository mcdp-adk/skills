# Agent Skills

**English** | [简体中文](README.zh-CN.md)

A small collection of [Agent Skills](https://agentskills.io) for coding agents. Install only the skills you need.

## Install

Use the [Vercel Labs `skills` CLI](https://github.com/vercel-labs/skills) with Node.js 22.20 or newer:

```bash
npx skills add mcdp-adk/skills
```

The CLI will ask which skills to install. To install a specific skill:

```bash
npx skills add mcdp-adk/skills --skill reader-centered-writing
```

## Available skills

| Skill | Use it when | Notes |
|---|---|---|
| [`atomic-commit`](atomic-commit/SKILL.md) | A Git change needs a coherent commit scope, message, staging plan, or final verification. | Not intended for routine status or history queries. |
| [`everything-cli`](everything-cli/SKILL.md) | A file, directory, or project has an unknown location on Windows. | Requires the Everything desktop app and ES (`es.exe`). |
| [`grok-search`](grok-search/SKILL.md) | A task needs current or externally verified information from the Web or X. | Requires Python 3.10+ and an xAI API key. See the [setup and usage guide](grok-search/README.md). |
| [`durable-project-knowledge`](durable-project-knowledge/SKILL.md) | Establish or reorganize durable project knowledge when explicitly required; help substantial work across sessions, handoffs, or collaborators discover, read, and maintain durable goal, design, decision, and plan knowledge; repair entry-point or source problems that block the work; and update lasting changes. | Includes conditional software-development and creative/experimental guidance. |
| [`reader-centered-writing`](reader-centered-writing/SKILL.md) | A human-facing document needs to help its readers understand, decide, or act. | Includes guidance for Chinese technical writing. |

## License

[MIT](LICENSE)
