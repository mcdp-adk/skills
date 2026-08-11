# 是否应该做成 Skill：当前判断

## 1. 结论

**适合做成 Skill，但 Skill 不等于项目知识本身。**

更准确的三层关系：

```text
项目长期文档 / artifacts
        ↑
  project-docs Skill
        ↓
Harness 的临时状态与执行能力
```

### 项目长期知识

属于具体项目，应留在 repo 或项目自己的持久存储中。

### Skill

保存跨项目复用的方法：

> Agent 怎样发现、读取、维护和更新这套长期知识。

### Harness

负责当前 session 的：

- progress；
- orchestration；
- subagents；
- runtime memory；
- tool execution。

## 2. 为什么 Skill 是合适的载体

Agent Skills 是开放的、可按需加载的 reusable workflow 格式：

https://agentskills.io/

规范：

https://agentskills.io/specification

Skill 的 progressive disclosure 是：

1. 启动时主要暴露 `name + description`；
2. 触发后读取 `SKILL.md`；
3. references / scripts / assets 按需读取。

这与本体系的目标一致：

> 不把整套知识管理方法永久塞进所有 context，只在相关任务触发。

OpenCode、Codex、Kimi Code 当前都支持 `SKILL.md` 形式的 Skills。

## 3. Skill 的核心职责应该很小

未来 Skill 只需要帮助 Agent 完成类似流程：

```text
发现已有长期文档
    ↓
识别当前任务需要哪些
    ↓
按需读取
    ↓
正常工作
    ↓
发现长期有价值的新信息
    ↓
更新合适的长期文档
```

主要回答三个问题：

### 开始工作
我现在需要读哪些项目知识？

### 工作过程中
这个新发现只是当前 session 状态，还是未来也需要知道？

### 工作结束
目标、设计、决策或计划是否需要同步更新？

## 4. Skill 不应该负责什么

不要重复：

- 怎么写漂亮的文档；
- 文档怎么拆到约 200 行；
- 通用 code review；
- Git commit；
- 如何做 verification planning；
- 如何调度 subagents；
- 如何维护 Deep Work session；
- 如何生成 Codemap。

这些已有更合适的能力负责。

## 5. 不强制目录与文件名

新 Skill 不应该看到任何项目都强制创建：

```text
docs/
  goal/
  design/
  decisions/
  plans/
```

更合理：

```text
已有 PRD
→ 把它认作目标来源。

已有 GDD
→ 识别它承担哪些职责。

已有 docs/architecture
→ 继续使用。

已有 GitHub Issue / Plan
→ 判断它是否已经足够承担当前计划。
```

原则：

> **适配现有约定，不为了 Skill 重建第二套知识库。**

只有全新项目没有任何结构时，才给出最小默认方案。

## 6. 不要把所有分析概念变成用户概念

讨论中曾提出较完整的：

```text
Intent
Constraints
Model
Decision
Work
Evidence
Learning
Operations
Authority
Domain Profile
```

它们可以继续作为 Skill 内部推理参考。

但第一版用户模型应维持：

```text
目标 / 设计 / 决策 / 计划
```

除非真实项目证明需要更复杂的一级结构。

## 7. Anthropic Skill Creator 怎么参考

官方源：

https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md

值得吸收的原则包括：

- 先明确 Skill 的 intent 和 trigger；
- `description` 是重要触发入口；
- `SKILL.md` 保持聚焦；
- 详细内容放 references；
- 使用 progressive disclosure；
- subjective tasks 不要强行制造客观 assertions。

其 `evals/`、viewer、benchmark workspace 等工作流属于 Anthropic 自己的 Skill Creator 工具链，而不是 Agent Skills 格式规范要求。

因此第一版可以：

> 以 `SKILL.md` 的结构与内容质量为标准，不把 Anthropic eval harness 作为跨 Agent 的必要依赖。

## 8. 预计的第一版形态

可能甚至只需要：

```text
project-docs/
├─ SKILL.md
└─ references/
   ├─ software.md      # 需要时
   └─ creative.md      # 需要时
```

是否真的需要 references，应等 `SKILL.md` 草案出现后再判断。

不要预先搭一个复杂 Skill package。
