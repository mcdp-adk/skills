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
npx skills add mcdp-adk/skills --skill writing-to-be-understood
```

## Available skills

| Skill | Use it when | Notes |
|---|---|---|
| [`atomic-commit`](atomic-commit/SKILL.md) | Committing work that needs a coherent scope and a `type(scope): description` message. | Groups related changes; splits only unrelated intentions. |
| [`everything-cli`](everything-cli/SKILL.md) | A file, directory, or project has an unknown location on Windows. | Requires the Everything desktop app and ES (`es.exe`). |
| [`grok-search`](grok-search/SKILL.md) | A task needs current or externally verified information from the Web or X. | Requires Python 3.10+ and an xAI API key. See the [setup and usage guide](grok-search/README.md). |
| [`writing-to-be-understood`](writing-to-be-understood/SKILL.md) | Choosing wording so the person reading can understand the dialogue content. | |

## License

[MIT](LICENSE)
