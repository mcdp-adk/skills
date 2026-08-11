# 跨 Agent / Harness 兼容

> 核心目标不是让所有工具行为完全一样，而是让长期项目知识不依赖任何一个工具的私有 memory。

## 1. 最低公共能力

本体系只需要 Agent 能：

1. 读取项目文件；
2. 搜索当前 artifacts；
3. 运行必要工具；
4. 更新普通项目文件；
5. 使用 Git / verification mechanism。

因此即使没有复杂的 memory、subagent 或 Skill，长期项目知识仍然可用。

## 2. OpenCode

Rules：

https://opencode.ai/docs/rules/

Skills：

https://opencode.ai/docs/skills

当前官方文档支持：

- project `AGENTS.md`；
- `/init`；
- custom `instructions`；
- `SKILL.md` skills；
- `.agents/skills/` 兼容路径；
- need-to-know external-file loading 示例。

特别重要的是：

> 不建议因为存在很多文档，就通过 `instructions` 把所有项目文档永久注入 context。

长期知识仍应按任务读取。

## 3. Codex

AGENTS.md：

https://developers.openai.com/codex/agent-configuration/agents-md

ExecPlan：

https://developers.openai.com/cookbook/articles/codex_exec_plans

Long-horizon example：

https://developers.openai.com/blog/run-long-horizon-tasks-with-codex

Skills：

https://developers.openai.com/codex/build-skills

Codex 的能力与本体系高度兼容：

- `AGENTS.md` 作为 project instructions；
- root → cwd instruction chain；
- Skills progressive disclosure；
- ExecPlan 作为 self-contained living plan；
- long-horizon 工作强调 durable project memory 与 milestone verification。

因此软件项目中的 Delivery Plan 可以直接吸收 ExecPlan 的优秀原则，而不需要复制 Codex 的专有目录结构。

## 4. Kimi Code

Skills：

https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html

Sessions：

https://www.kimi.com/code/docs/en/kimi-code-cli/guides/sessions.html

Agents：

https://www.kimi.com/code/docs/en/kimi-code-cli/customization/agents

Kimi 当前支持：

- `AGENTS.md`；
- Agent Skills；
- persistent sessions；
- `/compact`；
- isolated subagent contexts。

这些 session features 属于执行便利层。

长期目标/设计/决策仍应该能从项目自身恢复。

## 5. ZCode

Agent：

https://zcode.z.ai/en/docs/agents

Subagents：

https://zcode.z.ai/en/docs/subagents

当前 ZCode 文档明确区分：

```text
AGENTS.md
→ 人维护、repo versioned、团队共享

Project Memory
→ Agent 自动积累、本机保存、不进 Git
```

而且当前只读取：

- user global `~/.zcode/AGENTS.md`；
- current Workspace root `AGENTS.md`；

不会做多层 nested `AGENTS.md` merge。

这进一步说明核心体系不应依赖某种 harness-specific instruction inheritance。

## 6. Skills 是比较好的跨产品执行层

Agent Skills 官方开放规范：

https://agentskills.io/specification

OpenCode、Codex、Kimi 均已经支持相同核心格式。

因此未来 `project-docs` Skill 可以尽量采用标准 `SKILL.md`，避免针对某个 harness 写死。

## 7. Harness-private memory 的正确定位

可以使用：

```text
OpenCode / OMO → Deep Work
Codex          → current session / plan mode
Kimi           → session / compact / goal-like state
ZCode          → task / Goal Mode / Project Memory
```

但规则始终是：

> **如果这条信息明天换 Agent 后仍然必须存在，就不能只留在 harness-private state。**
