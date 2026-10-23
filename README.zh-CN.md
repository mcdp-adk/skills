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

活跃技能放在 `skills/`；归档技能保留在 `deprecated/`，并标记 `metadata.internal: true`。

## 技能一览

| 技能 | 用途 |
| --- | --- |
| [`chinese-typography`](skills/chinese-typography/SKILL.md) | 在撰写或编辑中文及中英混排文本时，统一空格和标点。 |
| [`design-md`](skills/design-md/SKILL.md) | 在界面开发中遵循项目的 DESIGN.md，并按 Google 的开放 DESIGN.md 格式创建、更新和校验它。 |
| [`everything-cli`](skills/everything-cli/SKILL.md) | 在 Windows 上查找位置不明的文件、目录和项目。 |
| [`migrate-practices`](skills/migrate-practices/SKILL.md) | 参考已有仓库的工作实践，在目标仓库中重新实现。 |
| [`repo-style-guide`](skills/repo-style-guide/SKILL.md) | 为分支名、commit message 以及 PR 和 issue 标题提供兜底格式。 |

额外依赖：

- **design-md**：校验时通过 npx 运行 `@google/design.md`。
- **everything-cli**：需要安装 Everything 和 ES（`es.exe`），并保持 Everything 运行。

## 许可证

[MIT](LICENSE)
