# Agent Skills

[English](README.md) | **简体中文**

一组供 AI 编程助手使用的 [Agent Skills](https://agentskills.io)。按任务需要选择，可单独安装，也可一起安装。

## 安装

需要 Node.js 22.20 或更高版本。使用 [Vercel Labs `skills` CLI](https://github.com/vercel-labs/skills) 安装：

```bash
npx skills add mcdp-adk/skills
```

按提示选择需要的技能，也可以用 `--skill` 指定：

```bash
npx skills add mcdp-adk/skills --skill atomic-commit
```

## 技能一览

| 技能 | 用途 |
| --- | --- |
| [`atomic-commit`](atomic-commit/SKILL.md) | 将相关改动归为一次完整的提交，仅在改动目的无关时拆分，并按 `type(scope): description` 格式编写提交说明。 |
| [`chinese-typography`](chinese-typography/SKILL.md) | 在撰写、编辑或检查中文及中英混排文本时，统一空格和标点，保留 Markdown、图表及代码语法。 |
| [`everything-cli`](everything-cli/SKILL.md) | 在 Windows 上快速查找位置不明的文件、目录或项目。 |
| [`explanatory-mode`](explanatory-mode/SKILL.md) | 随任务进展解释正在做什么，以及重要选择的理由。解释只写在对话里，不加入代码库。 |
| [`grok-search`](grok-search/SKILL.md) | 搜索 Web 或 X 上的最新信息，或通过外部来源核实内容。 |

额外依赖：

- **everything-cli**：需要安装 Everything 和 ES（`es.exe`），并保持 Everything 运行。
- **grok-search**：需要 Python 3.10+ 和 xAI API key。详见 [配置与用法](grok-search/README.md)。

## 许可证

[MIT](LICENSE)
