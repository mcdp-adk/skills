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
npx skills add mcdp-adk/skills --skill writing-to-be-understood
```

## Skills 一览

| Skill | 什么时候用 | 说明 |
|---|---|---|
| [`atomic-commit`](atomic-commit/SKILL.md) | 提交时需要确定范围，并写成 `type(scope): description`。 | 相关改动放一起；只有无关意图才拆。 |
| [`everything-cli`](everything-cli/SKILL.md) | 文件、目录或项目位置不明，需要在 Windows 上快速定位。 | 需要安装 Everything 和 ES（`es.exe`），并保持 Everything 运行。 |
| [`grok-search`](grok-search/SKILL.md) | 需要从 Web 或 X 获取最新信息，或借助外部来源核实内容。 | 需要 Python 3.10+ 和 xAI API key。详见[配置与用法](grok-search/README.md)。 |
| [`writing-to-be-understood`](writing-to-be-understood/SKILL.md) | 正在为给人看的文字选择措辞，让对方能从文本里读懂对话内容。 | |

## 许可证

[MIT](LICENSE)
