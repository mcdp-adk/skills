# 面向人类与 Coding Agent 的项目知识与文档体系

> 版本：2026-08-10  
> 状态：研究与设计阶段，尚未定稿为 Skill  
> 目标：建立一套足够简单、可长期维护、可跨 Coding Agent 使用的项目知识体系，使新 Agent 即使没有历史对话，也能快速理解项目并继续工作。

## 为什么会有这套讨论

问题最初来自 Coding Agent 的长任务记忆：

- 上下文越来越长以后，注意力会被稀释；
- `/compact`、自动压缩或新 session 可能丢失细节；
- 换模型、换 Agent、换 harness 后不能假设聊天历史仍然存在；
- `AGENTS.md` 又不适合无限增大。

因此最初的问题是：

> 工作目录里究竟应该维护哪些文档，才能让 Coding Agent 获得可靠的“项目记忆”？

讨论随后经历了三次扩展：

1. **软件工程**：把 PRD、Software Design Description（SDD）、ADR、Delivery Plan 与 Agent memory 统一起来。
2. **游戏与创意开发**：发现并非所有结果都能靠测试判定，“体验”“品味”“原型学习”和人类判断也必须进入开发闭环。
3. **Skill 化**：考虑把方法做成 Agent Skill，但同时要求不重复 OpenCode、OMO Slim 与现有 Skill 的职责。

中间一度把体系抽象成复杂的 Project Knowledge Protocol、Knowledge Roles、Authority、Domain Profile 等概念。随后主动收敛：这些概念有启发，但若成为日常使用模型，会违背“降低认知负担”的初衷。

## 当前收敛结论

目前最简单且足够完整的核心，是三层：

```text
项目长期知识
    ↑
文档体系 Skill（未来）
    ↓
Agent / Harness 的临时工作状态
```

长期知识先只分四个主要问题：

| 类别 | 回答的问题 |
|---|---|
| **目标** | 我们要做什么、为什么做、希望达到什么结果或体验？ |
| **设计** | 它应该怎样工作、怎样组织？ |
| **决策** | 哪些重要选择已经做过，为什么？ |
| **计划** | 当前准备怎样推进、怎样判断完成？ |

这不是四个强制文件名，而是四种稳定职责。

软件项目可以自然映射为：

```text
PRD           → 目标
SDD           → 设计
ADR           → 决策
Delivery Plan → 计划
```

游戏、Demo 或创意型交互项目则可以使用自己的形式，例如 Vision、Gameplay Design、Prototype Plan、Playtest notes；不要求生硬套用软件术语。

## 最重要的原则

### 1. Context 是工作内存，不是数据库

聊天历史、compact summary、session memory 都可以帮助当前执行，但不能成为项目长期知识的唯一来源。

### 2. 仓库中的长期知识必须能独立恢复项目认知

理想状态：

> 一个完全没有历史对话的新 Agent，能通过项目入口、相关长期文档、当前代码/资产、Git 和验证证据理解任务并继续工作。

### 3. `AGENTS.md` 是入口，不是百科全书

它适合保存：

- 少量稳定且重要的项目规则；
- 必要命令；
- 非显然的注意事项；
- 去哪里找目标、设计、决策和计划。

不要把整个项目知识复制进 `AGENTS.md`。

### 4. 临时状态留给 Harness

例如 OMO Slim 的 Deep Work、Codex/Kimi/ZCode 的 session / goal / plan state。

长期重要的信息应进入项目文档；当前执行进度不必都永久提交到 Git。

### 5. 不预付复杂度

没有真实需求时，不提前创建：

- 一整套空目录；
- 每种知识一个新文档类型；
- 大量模板；
- 复杂 ontology。

先用最小充分结构，项目复杂以后再自然生长。

## 本知识库内容

- [00-design-evolution.md](00-design-evolution.md)：从最初五层记忆模型到当前简化方案的完整演化。
- [01-research-foundations.md](01-research-foundations.md)：长上下文、compaction、AGENTS.md、Agent Plans 的最新研究。
- [02-current-model.md](02-current-model.md)：当前收敛后的核心模型。
- [03-software-engineering-profile.md](03-software-engineering-profile.md)：PRD / SDD / ADR / Delivery Plan 的对应关系。
- [04-creative-and-game-development.md](04-creative-and-game-development.md)：游戏、Demo、创意开发以及人与 AI 的边界。
- [05-skill-direction.md](05-skill-direction.md)：为什么适合做 Skill，以及 Skill 不应该做什么。
- [06-existing-skills-and-omo-slim.md](06-existing-skills-and-omo-slim.md)：与现有 Skill 库和 OMO Slim 的职责边界。
- [07-cross-agent-compatibility.md](07-cross-agent-compatibility.md)：OpenCode、Codex、Kimi Code、ZCode 的适配。
- [08-open-questions.md](08-open-questions.md)：目前仍未定稿的问题与下一步。
- [REFERENCES.md](REFERENCES.md)：论文、官方文档与源代码 URL。

## 这套体系现在不是什么

它不是最终目录规范，也不是完成的 `SKILL.md`。

当前阶段更重要的是先稳定：

> **Agent 到底需要哪些长期知识，以及这些知识和临时执行状态、现有工具之间如何分工。**

只有这个边界稳定后，才值得写最终 Skill。
