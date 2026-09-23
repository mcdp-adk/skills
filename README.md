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

## Available skills

| Skill | What it does |
| --- | --- |
| [`chinese-typography`](chinese-typography/SKILL.md) | Keeps spacing and punctuation consistent when writing, editing, or checking Chinese and mixed Chinese-English text. Preserves Markdown, diagram, and code syntax. |
| [`eroge-hanhua-workflow`](eroge-hanhua-workflow/SKILL.md) | Guides Simplified Chinese localization of Japanese R18 games, from resource investigation and organization through translation, review, adaptation, and patch verification and delivery. Keeps source resources, editable work, and generated outputs distinct so different agents can continue the work. |
| [`everything-cli`](everything-cli/SKILL.md) | Quickly finds files, directories, and projects on Windows when you do not know where they are stored. |
| [`explain-as-you-go`](explain-as-you-go/SKILL.md) | Explains implementation choices and codebase patterns through brief insights as coding work proceeds. |
| [`grok-search`](grok-search/SKILL.md) | Searches the Web or X for current information and checks claims against external sources. |
| [`repo-style-guide`](repo-style-guide/SKILL.md) | Keeps naming, content, and links consistent across Git commits and GitHub issues and pull requests. |

Additional requirements:

- **everything-cli**: Install Everything and ES (`es.exe`), and keep Everything running.
- **grok-search**: Requires Python 3.10+ and an xAI API key. See the [setup and usage guide](grok-search/README.md).

## License

[MIT](LICENSE)
