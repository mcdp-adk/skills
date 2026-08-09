# Agent Skills

[English](README.md) | **简体中文**

本仓库收录了一组供 AI 编程助手使用的 [Agent Skills](https://agentskills.io)，可按需安装。

## 安装

通过 [Vercel Labs `skills` CLI](https://github.com/vercel-labs/skills) 安装（需要 Node.js 22.20 或更高版本）：

```bash
npx skills add mcdp-adk/skills
```

可按提示选择需要的 skill，也可以用 `--skill` 直接指定：

```bash
npx skills add mcdp-adk/skills --skill reader-centered-writing
```

## Skills 一览

| Skill | 什么时候用 | 说明 |
|---|---|---|
| [`atomic-commit`](atomic-commit/SKILL.md) | 需要规划一次 Git 提交，包括划分范围、编写提交信息、暂存改动和最终检查。 | 不适合只查看 Git 状态或提交历史。 |
| [`everything-cli`](everything-cli/SKILL.md) | 文件、目录或项目位置不明，需要在 Windows 上快速定位。 | 需要安装 Everything 和 ES（`es.exe`），并保持 Everything 运行。 |
| [`grok-search`](grok-search/SKILL.md) | 需要从 Web 或 X 获取最新信息，或借助外部来源核实内容。 | 需要 Python 3.10+ 和 xAI API key。详见[配置与用法](grok-search/README.md)。 |
| [`readable-artifacts`](readable-artifacts/SKILL.md) | 文件职责混杂、阅读顺序不清，或需要决定如何拆分和引用。 | 约 200 行只是提醒检查结构，并非硬性限制。 |
| [`reader-centered-writing`](reader-centered-writing/SKILL.md) | 需要撰写或重写 README、技术说明等面向读者的文档。 | 包含中文技术写作指南。 |
| [`review-to-closure`](review-to-closure/SKILL.md) | 完成较复杂的改动或修复审查意见后，需要确认所有问题都已处理完毕。 | 按照“审查—修复—验证—复审”的流程推进，并始终对照原始目标。 |

## 许可证

[MIT](LICENSE)
