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
| [`eroge-hanhua-workflow`](skills/eroge-hanhua-workflow/SKILL.md) | 指导日文 R18 游戏的简体中文汉化，涵盖资源调查、补丁验证与交付。 |
| [`everything-cli`](skills/everything-cli/SKILL.md) | 在 Windows 上查找位置不明的文件、目录和项目。 |
| [`explain-as-you-go`](skills/explain-as-you-go/SKILL.md) | 在执行编程任务时，解释实现选择和代码库模式。 |
| [`repo-style-guide`](skills/repo-style-guide/SKILL.md) | 在命名分支、准备提交或撰写 GitHub issue、PR 和评论时，统一命名与表达风格。 |

额外依赖：

- **everything-cli**：需要安装 Everything 和 ES（`es.exe`），并保持 Everything 运行。

## 许可证

[MIT](LICENSE)
