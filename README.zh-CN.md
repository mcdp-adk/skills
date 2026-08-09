# Agent Skills

[English](README.md) | **简体中文**

一组面向 coding agent 的 [Agent Skills](https://agentskills.io)。按需安装即可。

## 安装

使用 [Vercel Labs `skills` CLI](https://github.com/vercel-labs/skills) 安装。该工具需要 Node.js 22.20 或更高版本：

```bash
npx skills add mcdp-adk/skills
```

CLI 会引导你选择要安装的 skill。也可以直接安装指定 skill：

```bash
npx skills add mcdp-adk/skills --skill reader-centered-writing
```

## 可用 Skills

| Skill | 适用场景 | 备注 |
|---|---|---|
| [`atomic-commit`](atomic-commit/SKILL.md) | Git 变更需要确定连贯的提交范围、提交信息、暂存方案或最终验证。 | 不用于常规的状态或历史查询。 |
| [`everything-cli`](everything-cli/SKILL.md) | 在 Windows 上查找位置未知的文件、目录或项目。 | 需要 Everything 桌面应用和 ES (`es.exe`)。 |
| [`grok-search`](grok-search/SKILL.md) | 任务需要从 Web 或 X 获取最新信息或进行外部核实。 | 需要 Python 3.10+ 和 xAI API key。配置与用法见[详细说明](grok-search/README.md)。 |
| [`readable-artifacts`](readable-artifacts/SKILL.md) | 文件的职责、阅读路径、边界或引用关系需要调整。 | 将约 200 行视为检查点，而非硬性上限。 |
| [`reader-centered-writing`](reader-centered-writing/SKILL.md) | 面向人的文档需要帮助读者理解信息、作出决定或采取行动。 | 包含中文技术写作指南。 |
| [`review-to-closure`](review-to-closure/SKILL.md) | 非简单变更或 review 修复需要完整的审查、验证和复审闭环。 | 始终以原始目标和累积结果为审查依据。 |

## 许可证

[MIT](LICENSE)
