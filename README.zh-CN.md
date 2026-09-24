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
npx skills add mcdp-adk/skills --skill repo-style-guide
```

## 技能一览

| 技能 | 用途 |
| --- | --- |
| [`chinese-typography`](chinese-typography/SKILL.md) | 在撰写、编辑或检查中文及中英混排文本时，统一空格和标点，保留 Markdown、图表及代码语法。 |
| [`eroge-hanhua-workflow`](eroge-hanhua-workflow/SKILL.md) | 指导日文 R18 游戏的简体中文汉化，涵盖资源调查与整理、翻译与校对、必要适配及补丁验证与交付。明确原始资源、编辑成果和生成结果的边界，便于不同 Agent 继续工作。 |
| [`everything-cli`](everything-cli/SKILL.md) | 在 Windows 上快速查找位置不明的文件、目录或项目。 |
| [`explain-as-you-go`](explain-as-you-go/SKILL.md) | 在完成编程任务的过程中，用简短讲解说明实现选择和代码库模式。 |
| [`grok-search`](grok-search/SKILL.md) | 搜索 Web 或 X 上的最新信息，或通过外部来源核实内容。 |
| [`repo-style-guide`](repo-style-guide/SKILL.md) | 统一 Git 提交与 GitHub issue、PR 的命名、内容和关联约定。 |
| [`setup-project-conventions`](setup-project-conventions/SKILL.md) | 通过交互设置项目的写作与协作约定，展示完整规则和 Agent 读取入口，确认后写入项目。需手动调用。 |

额外依赖：

- **everything-cli**：需要安装 Everything 和 ES（`es.exe`），并保持 Everything 运行。
- **grok-search**：需要 Python 3.10+ 和 xAI API key。详见 [配置与用法](grok-search/README.md)。

## 许可证

[MIT](LICENSE)
