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
npx skills add mcdp-adk/skills --skill atomic-commit
```

## Available skills

| Skill | What it does |
| --- | --- |
| [`atomic-commit`](atomic-commit/SKILL.md) | Groups related changes into a coherent commit, splits changes only when they serve unrelated purposes, and writes commit messages in the `type(scope): description` format. |
| [`chinese-typography`](chinese-typography/SKILL.md) | Keeps spacing and punctuation consistent when writing, editing, or checking Chinese and mixed Chinese-English text. Preserves Markdown, diagram, and code syntax. |
| [`everything-cli`](everything-cli/SKILL.md) | Quickly finds files, directories, and projects on Windows when you do not know where they are stored. |
| [`explanatory-mode`](explanatory-mode/SKILL.md) | Explains the work as it proceeds, including the reasons for important decisions. Explanations stay in the conversation and are not added to the codebase. |
| [`grok-search`](grok-search/SKILL.md) | Searches the Web or X for current information and checks claims against external sources. |

Additional requirements:

- **everything-cli**: Install Everything and ES (`es.exe`), and keep Everything running.
- **grok-search**: Requires Python 3.10+ and an xAI API key. See the [setup and usage guide](grok-search/README.md).

## License

[MIT](LICENSE)
