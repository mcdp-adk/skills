# 扩展到游戏、Demo 与创意型项目

## 1. 为什么游戏是很好的压力测试

传统软件很容易围绕：

```text
Specification → Implementation → Verification
```

组织工作，因为很多问题有较清楚的 oracle：

- 是否能登录；
- 数据是否正确；
- API 是否兼容；
- 测试是否通过。

游戏、交互 Demo、创意工具则经常追求：

- 手感；
- 节奏；
- 情绪；
- 视觉层级；
- 趣味；
- 惊喜；
- 审美方向。

这些结果不能全部转成客观 test。

## 2. MDA 给出的重要启示

经典 MDA：

https://aaai.org/papers/ws04-04-001-mda-a-formal-approach-to-game-design-and-game-research/

区分：

```text
Mechanics → Dynamics → Aesthetics
```

设计者直接制作的是机制和系统，但最终希望产生的是玩家体验。

因此创意型项目需要一个额外的学习闭环：

```text
目标/体验意图
    ↓
设计假设
    ↓
Prototype / Artifact
    ↓
实际体验
    ↓
反馈与学习
    ↓
更新目标/设计/决策
```

这并不意味着必须增加五六类新顶级文档。

它只意味着：

> **计划可以包含“学习型 milestone”，长期设计需要吸收真实实验结果。**

## 3. GDD 不必硬映射成 PRD 或 SDD

2019 年对四家独立游戏工作室的研究指出，传统 exhaustive GDD 已较少见，但其沟通与协调功能仍通过不同媒介存在：

https://doi.org/10.1145/3321388.3321389

所以更适合把 GDD 看成历史上常见的“综合容器”。

在本体系中，游戏项目可以按真实需要拆成：

```text
Vision / Experience goals → 目标
Gameplay / Systems / Technical design → 设计
Important design choices → 决策
Prototype / Production milestones → 计划
```

不要求统一模板。

## 4. Prototype 的成功标准可能是“学到答案”

例如：

```text
Question:
grappling + wall running 是否形成值得继续的核心循环？

Plan:
做一个 disposable greybox。

Evidence:
人类 playtest + 观察。

Exit:
KEEP / MODIFY / KILL。
```

成功不一定是：

> “功能已经生产级完成。”

也可能是：

> “已经知道这个方向不值得继续。”

因此可以区分：

- Delivery milestone：交付已知目标；
- Learning milestone：减少关键不确定性。

但它们都可以放在“计划”这一大类中。

## 5. Project Knowledge 不只存在于文字

游戏尤其明显：

```text
“移动应该快速但有重量”
```

可能很难靠长篇文字准确表达。

更好的知识载体可能是：

- playable prototype；
- reference video；
- animation capture；
- screenshot；
- tuning parameters；
- audio reference。

GameDevBench（2026）证明当前 Coding Agent 在游戏开发中面对明显的多模态难度；图片和视频反馈可显著改善表现：

https://arxiv.org/abs/2602.11103

GameEngineBench 也显示当前 Agent 在真实 Unreal Engine C++ 任务中仍有大量未解决问题：

https://arxiv.org/abs/2607.03525

因此文档体系需要允许：

> 文档链接到最合适的 artifact，而不是强迫所有知识转写成 Markdown。

## 6. 人与 AI 的边界：不要简单分成“人创意、AI 执行”

2026 的 Human-AI creative search 研究显示，在特定任务上 human-AI hybrid group 可以表现出互补优势：

https://arxiv.org/abs/2602.10001

所以 Agent 可以参与：

- research；
- ideation；
- design alternatives；
- implementation；
- simulation；
- critique；
- summarization。

真正重要的边界是：

> **谁拥有最终判断权，以及有没有可靠的验证 oracle。**

## 7. 主观评价仍然需要人类权威

*The Human Creativity Benchmark*（2026）发现：

- technical correctness、visual hierarchy 等维度更容易形成专业共识；
- aesthetic direction、conceptual risk 等维度存在合理的 taste divergence。

https://arxiv.org/abs/2606.30561

因此：

```text
机器可验证
→ Agent 可高度自治

体验、品味、创作意图
→ AI 可以分析和提出方案，但人类/真实用户保留最终判断
```

## 8. AI Playtest 与 Human Playtest 是互补关系

LLM 自动 playtesting 已能帮助：

- coverage；
- crash finding；
- reachable-state exploration。

例如：

https://arxiv.org/abs/2507.09490

但人类更适合回答：

- 我理解了吗？
- 好玩吗？
- 紧张吗？
- 无聊吗？
- 我愿意继续玩吗？

所以“验证”在创意项目里可以同时包含：

```text
Technical evidence
Behavioral evidence
Human experiential judgment
```

不需要为了这三种 evidence 再创建三个强制目录。

## 9. 泛化后的核心仍然不变

无论软件、游戏、Demo、研究原型：

```text
目标
设计
决策
计划
```

仍然足够作为第一层长期知识模型。

创意型项目的区别主要在于：

- “目标”可能包含体验意图；
- “计划”可能包含 prototype / learning；
- “证据”可能需要人类评价与多模态 artifact；
- AI 不应把自己的主观判断静默升级成人类授权的最终目标。
