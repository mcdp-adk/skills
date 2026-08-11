# 设计演化：从 Coding Agent 记忆到通用项目知识 Skill

本文记录这套想法为什么会变成现在的样子。它不是要求读者采用所有中间方案，而是说明哪些问题被保留、哪些抽象被主动放弃。

## 阶段 1：最初问题是 Coding Agent 会“失忆”

最初目标很具体：

> 如何避免 Coding Agent 在长上下文、compaction 或新 session 后丢失项目关键信息？

当时形成过一个五层心智模型：

```text
L0 Current Context
   当前对话、刚读的代码、当前工具输出

L1 Runtime Working Memory
   todo、progress、session checkpoint

L2 Durable Project Memory
   requirements、design、decisions、plans、runbooks

L3 Discovery / Navigation
   AGENTS.md、codemap、索引

L4 Ground Truth
   code、tests、schemas、Git
```

这套模型至今仍然成立，但更适合作为**理解边界的内部模型**，而不是要求项目建立五套目录。

核心结论只有一句：

> Context 可以丢；长期项目知识必须可重新读取。

## 阶段 2：把它与已有软件工程文档统一

随后发现，没有必要重新发明 `spec / architecture / plan` 一套平行术语。

已有流程本来就能承担长期记忆：

```text
PRD           → 项目为什么做、要实现什么
SDD           → 软件应该怎样设计
ADR           → 为什么做了重要选择
Delivery Plan → 当前复杂变化怎样交付
```

这使体系从“Agent memory 文件”变成了：

> **让已有工程文档同时成为人类和 Agent 的长期项目记忆。**

## 阶段 3：与 OMO Slim 明确分工

阅读 OMO Slim 官方实现后，几个边界变得清楚。

### Deep Work

```text
.slim/deepwork/<task>.md
```

是 git-local 的 persistent session/progress state。

因此：

```text
Delivery Plan = 长期任务级交付知识
Deep Work     = 本轮执行现场
```

不应合并。

### Codemap

Codemap 描述当前代码结构。

因此：

```text
SDD     = Intended / To-Be
Codemap = Actual / As-Is
```

### Verification Planning

它已经负责“什么证据足以证明变化成立”，所以新的文档体系不应该再复制测试方法论。

## 阶段 4：扩展到游戏、Demo 与创意项目

如果只看软件工程，很容易把一切理解成：

```text
requirements → implementation → tests
```

游戏暴露了这个模型的边界：

> “好玩”“有重量感”“节奏舒服”“视觉方向正确”没有统一、客观的自动 test oracle。

于是讨论加入了：

```text
目标 / 体验意图
    ↓
设计假设
    ↓
Prototype
    ↓
Human experience / evidence
    ↓
Learning
    ↓
更新设计
```

并得到两个重要结论：

1. 项目知识不只存在于 Markdown，也可以是 prototype、video、screenshot、asset、telemetry。
2. AI 可以参与 ideation、design、implementation、evaluation，但在主观价值与创作意图上，人类/真实用户仍保留最终判断。

## 阶段 5：尝试进一步抽象成 Project Knowledge Protocol

为了跨软件、游戏和其他项目，一度提出很多一级概念：

```text
Intent
Constraints
Experience
Model
Decision
Work
Evidence
Learning
Operations
Authority
Domain Profile
```

理论上它们更完整，也能解释更多情况。

但问题也明显：

> 一个本来用于降低 Agent 和人的认知负担的体系，开始需要大量新术语才能理解自己。

这被判断为过度设计。

## 阶段 6：当前收敛

现在主动退回到最小充分模型。

### 三层

```text
项目长期知识
    ↑
未来的文档体系 Skill
    ↓
Agent / Harness 临时执行状态
```

### 四类长期知识

```text
目标
设计
决策
计划
```

此前的 Experience、Evidence、Learning、Constraints 等并没有被否定，而是：

> **先作为四类文档内部的内容；只有真实项目复杂到值得独立维护时，再拆出来。**

## 当前设计准则

这套体系现在优先追求：

- 正确、完整、清晰；
- 简单直接；
- 最小充分；
- 适配已有项目，而不是强迫迁移；
- 不重复现有 Skill / Harness；
- 不因“最佳设计”扩大范围；
- 允许真实复杂度出现以后再生长。

因此下一步不应继续增加理论，而应写一个很小的 Skill 草案，用真实项目检验它是否真的降低认知负担。
