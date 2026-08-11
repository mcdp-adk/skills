# 研究基础：为什么需要 Repo-Native 项目记忆

> 研究检查日期：2026-08-10。  
> 下面同时使用论文/预印本与厂商工程实践；预印本结果应视作证据而非最终定论。

## 1. 长上下文不等于长期记忆

Anthropic 的 Context Engineering 实践强调：context 是有限的注意力预算，应保持高信号，并通过按需检索、compaction、structured memory 和 subagents 管理长期任务。

长任务的核心问题不是“能不能塞进去”，而是：

> 当前步骤真正需要什么信息，以及丢失历史后怎样重新获得它。

官方工程文章：

- Effective context engineering for AI agents  
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Effective harnesses for long-running agents  
  https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Harness design for long-running application development  
  https://www.anthropic.com/engineering/harness-design-long-running-apps

后两篇的共同经验是：

- 新 session 不能假设拥有旧 session 的记忆；
- compaction 并不足以保证清晰 handoff；
- incremental work、Git、progress/state artifact 和 structured handoff 可以帮助恢复；
- 长任务应有明确的验证闭环。

## 2. Compaction 很重要，但不能当唯一事实源

2026 的 *Parallel Context Compaction for Long-Horizon LLM Agent Serving* 明确指出 LLM summarization 是有损的，而且 retention 会出现运行间波动：

https://arxiv.org/abs/2605.23296

2026 的 *CompactionRL* 又证明，专门训练 Agent 学会 context compaction 可以提升 agentic coding benchmark：

https://arxiv.org/abs/2607.05378

因此合理结论不是“不要 compact”，而是：

> **Compaction 用于延长当前执行；项目长期事实仍需要可重新读取的外部载体。**

## 3. 按目标检索通常比提前把所有知识压成摘要更合理

SUMER 在长上下文记忆任务上研究 goal-directed search：

https://arxiv.org/abs/2511.21726

其结果支持一个适合工程实践的原则：

> 保存可检索的信息源，在知道当前目标以后再读取相关内容；不要默认把所有信息预先压成一个万能 Memory 摘要。

这项研究并非 coding benchmark，因此不应直接外推数值，但它支持“按需读取”的架构方向。

## 4. `AGENTS.md` 的研究结果是矛盾的

这部分尤其重要，因为不能简单说“有 AGENTS.md 一定更好”。

### 4.1 有研究观察到效率改善

*On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents*：

https://arxiv.org/abs/2601.20404

10 个仓库、124 个 PR 的实验报告：

- median runtime 更低；
- output token 更少；
- task completion behavior 大致可比。

### 4.2 有研究观察到成功率下降、成本上升

*Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?*：

https://arxiv.org/abs/2602.11988

研究发现不必要的 repository instructions 可能：

- 降低 task success；
- 增加超过 20% 的 inference cost；
- 诱导更广泛但未必必要的探索。

作者建议 human-written context files 只保留 minimal requirements。

### 4.3 最新消融实验未发现正确率显著提升

*Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories*，2026-07-28：

https://arxiv.org/abs/2607.27250

其 Claude Code + Codex controlled ablation 未观察到 context strategy 对 correctness 的可测提升。

### 4.4 Context file 本身也会产生 smell

*Configuration Smells in AGENTS.md Files*，最新 v5：2026-07-30：

https://arxiv.org/abs/2606.15828

分析的常见 smell 包括：

- Lint Leakage；
- Context Bloat；
- Skill Leakage；
- Conflicting Instructions。

### 4.5 当前最稳健的综合结论

`AGENTS.md` 不是项目知识数据库，也不是自动提高 Agent 能力的魔法文件。

它更适合成为：

> **少量稳定规则 + 必要命令 + 项目知识入口。**

## 5. “200 行”不是 LLM 的神奇阈值

*Instruction Adherence in Coding Agent Configuration Files*：

https://arxiv.org/abs/2605.10039

该实验在其测试条件内没有检测到 file size、instruction position、file architecture 等变量对目标 instruction compliance 的显著 effect；更明显的是 session 内持续生成以后 compliance 会下降。

因此：

> “约 200 行”适合作为人工审查点和语义拆分提示，而不是认知极限。

真正重要的是：

- 一个文件是否承担一个清楚职责；
- 是否会独立更新；
- Agent 是否能只读当前任务需要的部分；
- 是否存在重复和过期信息。

## 6. 最新研究开始把 Agent Plan 当成独立工件

*An Exploratory Study of Agent Plans for Agentic AI Coding Tools in Open-Source Software*：

https://arxiv.org/abs/2608.04661

当前版本 v2：2026-08-06。

研究在 36,710 个 engineered GitHub repositories 中筛出少量 repository-preserved Agent Plans。虽然采用率仍低且样本集中，但这些 Plan 常包含：

- implementation steps；
- concrete files / locations；
- testing / validation information。

这支持一个重要边界：

> **任务级 Plan 与全局 `AGENTS.md` 是不同职责。**

## 7. 源代码仍然比自然语言摘要更接近行动事实

2026 的：

*What Context Does a Coding Agent Actually Need to Act?*

https://arxiv.org/abs/2607.09691

研究把“找到工作位置”和“真正执行修改”分开，发现自然语言摘要无法替代待修改代码本身所携带的行为信息。

因此：

> 文档用于目标、设计、决策、导航和计划；真正修改实现时，Agent 仍应读取相关源码/资产，而不是只依赖摘要。

## 8. 本体系由此采用的原则

1. Context 是工作集。
2. Compaction 是续航机制，不是唯一长期记忆。
3. 长期知识落到 repo-native artifacts。
4. `AGENTS.md` 尽量薄。
5. 任务 Plan 与项目级 instructions 分开。
6. 按任务检索，不全量预加载。
7. 文档不替代 source、tests、assets 和真实运行证据。
8. 文件按语义拆分，不迷信固定行数。
