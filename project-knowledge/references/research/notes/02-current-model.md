# 当前核心模型：四类长期知识 + 两个外围层

## 1. 为什么从复杂模型收敛回来

讨论过程中曾提出：

- Intent；
- Constraints；
- Experience；
- Model；
- Decision；
- Work；
- Evidence；
- Learning；
- Operations；
- Authority；
- Domain Profile。

这些概念在分析问题时有用，但如果全部成为一级文档类型，会造成新的认知负担。

当前原则是：

> **保留这些思想，但只在真实项目需要时显式拆出来。**

日常核心先保持四类。

## 2. 四类长期项目知识

### 目标

回答：

> 我们要做什么？为什么？最终希望什么结果成立？

可能包括：

- 产品目标；
- 用户/受众；
- success criteria；
- non-goals；
- 游戏的创作意图与体验目标；
- 研究项目的问题与预期。

### 设计

回答：

> 为了达到目标，这个东西应该如何工作或组织？

可能包括：

- 软件架构；
- 业务/系统模型；
- gameplay / interaction design；
- technical design；
- 数据流、依赖方向、接口；
- 重要的体验实现思路。

### 决策

回答：

> 哪些长期重要且非显然的选择已经做过？为什么？

典型形式是 ADR，但游戏、创意项目不必强制使用 ADR 名称。

价值在于防止未来 Agent：

- 重新争论已经解决的问题；
- 把经过权衡的设计误当成“可以随手优化”的偶然实现。

### 计划

回答：

> 从当前状态到目标，接下来如何推进，怎样知道已经完成？

对于复杂任务，它至少可以包括：

- scope；
- milestones；
- acceptance criteria；
- verification / evidence；
- 关键依赖；
- 必要的 discoveries / decision notes。

## 3. 两个外围层

### 项目入口：`AGENTS.md`

它不是第五类项目知识。

它只负责：

```text
重要规则
必要命令
项目知识在哪里
当前任务应该按需读什么
```

例如：

```markdown
## Project knowledge

- Goals / requirements: `docs/...`
- Design: `docs/...`
- Important decisions: `docs/...`
- Active plans: `docs/...`

Read only the documents relevant to the current task.
```

实际路径应适配项目，而不是强制统一。

### Runtime state：Harness 负责

例如：

- OMO Slim Deep Work；
- Codex session / plan mode；
- Kimi session / goal；
- ZCode task / Goal Mode / Project Memory。

它们回答：

> 这一轮现在做到哪？

而不是：

> 六个月后项目维护者应该知道什么？

## 4. Ground Truth 不只是 Markdown

长期项目认知还来自：

```text
Code
Tests
Schemas
Assets
Scenes
Prototypes
Builds
Screenshots / videos
Telemetry
Git history
```

因此“文档体系”只是方便称呼。

更准确地说，这是：

> **项目长期知识如何被组织、找到和维护。**

但没有必要为此再引入复杂的新术语体系。

## 5. 知识沉淀的简单判断

Agent 工作过程中发现一条重要信息，只问：

### 只对本轮执行有用？
→ 留在 runtime state / conversation。

### 以后的人或 Agent 还需要知道？
→ 更新长期项目知识。

然后判断它主要属于：

```text
为什么/要什么 → 目标
应该怎样      → 设计
为什么这样选  → 决策
接下来怎样做  → 计划
```

如果都不合适，而且同类信息已经反复出现，再考虑创建新的专门文档，例如：

- Runbook；
- experiments；
- playtests；
- research notes。

## 6. Fresh Agent Test

这套体系最终可以用一个简单问题检查：

> 给一个完全没有旧聊天历史的新 Agent，它能否通过项目入口、相关长期文档、当前 artifacts、Git 和验证手段继续工作？

至少应能回答：

1. 最终目标是什么？
2. 当前设计是什么？
3. 哪些重要选择不能随意推翻？
4. 当前复杂任务准备怎样推进？
5. 去哪里查看真实实现和验证结果？

能回答，就已经达到了项目记忆的主要目的。
