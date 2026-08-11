# 软件工程映射：PRD、SDD、ADR 与 Delivery Plan

## 1. 这套模型与传统软件工程并不冲突

对于普通软件项目，四类长期知识可以非常自然地落成：

| 通用职责 | 常见软件文档 |
|---|---|
| 目标 | PRD |
| 设计 | Software Design Description（SDD） |
| 决策 | ADR |
| 计划 | Delivery Plan |

因此不需要再同时维护一套 `specs / architecture / plans` 的平行概念。

## 2. PRD：目标

PRD 主要回答：

- 为什么做；
- 用户需要什么；
- 什么行为必须成立；
- 什么不做；
- 产品层如何判断成功。

它可以理解为 Product Spec，但 `spec` 一词过宽，因此不要求整个项目统一使用 `specs/` 作为目录名。

## 3. SDD：设计

SDD 主要回答：

- 系统边界；
- 模块职责；
- 依赖方向；
- 数据/控制流；
- 核心接口；
- 关键技术约束；
- 目标架构。

关键点：

> **SDD 描述 Intended / To-Be Design。**

因此它与从代码生成的 Codemap 不同。

## 4. ADR：决策记忆

ADR 最有价值的问题是：

> “为什么当时选 A，而不是 B？”

适合保存：

- 重要架构选择；
- 候选方案；
- rationale；
- consequences；
- 何时应该重新评估。

不是每个实现细节都需要 ADR。

## 5. Delivery Plan：任务级交付契约

复杂任务的 Delivery Plan 回答：

> 怎样从当前状态走到一个可验证的结果？

典型内容：

```text
Goal / Scope
Milestones
Dependencies
Acceptance criteria
Verification
Important discoveries / decisions
Progress（需要时）
```

OpenAI 的 ExecPlan 是很接近的现成实践：

https://developers.openai.com/cookbook/articles/codex_exec_plans

其核心要求包括：

- self-contained；
- living document；
- 新读者不依赖之前的聊天记忆；
- end-to-end working behavior，而非只“改了代码”。

OpenAI 的 long-horizon Codex 实践也强调 durable project memory、milestones 和 milestone verification：

https://developers.openai.com/blog/run-long-horizon-tasks-with-codex

## 6. Delivery Plan 与 TDD 不重复

TDD 是一种实现和反馈方式。

Delivery Plan 解决更高层的问题：

- 交付哪些结果；
- milestone 顺序；
- 如何验证整体行为。

某个 milestone 可以使用 TDD，但最终还可能需要：

- integration；
- browser/user-flow E2E；
- migration rehearsal；
- performance evidence；
- production-like smoke test。

因此：

> **TDD 可以服务 Delivery Plan，但不能替代 Delivery Plan。**

## 7. 验证应属于 Plan 的一部分

复杂任务不应写完代码后才决定“跑什么测试”。

更合理：

```text
Claim
↓
什么证据可以支持或否定它？
↓
实现
↓
执行证据路径
```

OMO Slim 的 `verification-planning` 已经专门解决这一问题，因此新文档 Skill 不需要重新实现这套方法。

## 8. SDD 与 Codemap 必须分开

```text
SDD     = 应该怎样
Codemap = 现在怎样
```

如果代码偏离目标架构：

- Codemap 应如实反映当前实现；
- SDD 保留目标设计；
- Plan 负责处理偏差。

把两者合并会让 Agent 无法区分“设计”与“现状”。

## 9. Delivery Plan 与 Deep Work 必须分开

```text
Delivery Plan
→ 长期、可审阅的任务级交付知识

OMO Deep Work file
→ 当前执行 session 的 checkpoint
```

后者不应成为唯一长期 source of truth。
