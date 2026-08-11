# 当前尚未定稿的部分与下一步

## 1. 目前已经比较稳定的结论

### A. 最终目标

让 Agent：

- 快速理解项目；
- 不依赖长聊天历史；
- compact / session reset 后可恢复；
- 工作过程中持续维护长期知识；
- 不制造重复文档与上下文膨胀。

### B. 核心长期知识保持简单

第一版只使用：

```text
目标
设计
决策
计划
```

这是职责分类，不是强制文件名。

### C. `AGENTS.md` 保持薄

只负责：

- stable rules；
- necessary commands；
- knowledge entry points。

### D. Runtime state 交给 Harness

不重复：

- OMO Deep Work；
- Codex/Kimi/ZCode session/goal；
- 其他专门 progress state。

### E. 现有 Skills 各司其职

不重复：

- readable-artifacts；
- reader-centered-writing；
- review-to-closure；
- atomic-commit；
- OMO verification-planning；
- codemap；
- reflect。

### F. 文档不是唯一知识载体

尤其在游戏/创意项目：

- prototype；
- screenshot；
- video；
- tests；
- assets；
- telemetry；

都可以成为真正 evidence / reference。

## 2. 还需要决定：Skill 的 trigger 范围

可能的触发场景：

- 新项目初始化知识结构；
- Agent 开始复杂任务前寻找 authority docs；
- 项目文档发生明显漂移；
- 完成复杂任务后同步长期知识；
- 用户明确要求整理项目文档体系。

需要避免 Skill 在每个小改动上自动制造工作。

## 3. 还需要决定：是否需要统一 Knowledge Map

一种可能：

```text
docs/README.md
```

只做索引：

```text
目标在哪
设计在哪
决策在哪
当前计划在哪
```

但它不是绝对必要。

如果项目本身已有清晰 README / docs index，就不应再创建第二个索引。

因此合理规则可能是：

> “保证存在一个可发现的知识入口”，而不是“必须创建 docs/README.md”。

## 4. 还需要决定：Plan 是长期保存还是任务结束后归档/删除

不同项目需求不同：

- 需要 audit/history → archive；
- Git/PR 已足够记录，重要知识已晋升 → 可以删除；
- 长期 roadmap → 可能继续保留。

不应在第一版统一强制。

## 5. 还需要决定：是否需要专门的游戏/创意 profile

当前更倾向：

- 核心 `SKILL.md` 不绑定软件/游戏；
- software/game examples 放 reference；
- 只有真实任务需要时才加载。

但如果最终核心足够清楚，甚至可以不建立 profile 文件，只在主文档放少量示例。

## 6. 还需要决定：Skill 是否应该主动修改文档

几个安全级别：

### 只读模式
识别项目知识和缺口，只提出建议。

### 任务内同步
当用户已授权实现某个任务时，允许同步明显受影响的长期文档。

### 结构变更
新增目录、重组文档、删除/合并 source of truth，应更谨慎。

第一版 Skill 应避免因为“维护知识体系”而自动扩大用户原本的实现范围。

## 7. 还需要决定：如何处理“推断”与“项目权威”

一个关键规则应保留：

> Agent 可以从代码、历史和实验中形成推断，但不能把推断静默改写成用户已经确认的目标或长期设计。

例如：

```text
实现当前似乎允许 X
```

不等于：

```text
产品要求 X
```

当长期 authority 不清楚时，记录不确定性或提出冲突，而不是擅自制造需求。

## 8. 下一步最合适的工作

不建议继续增加理论层。

更合适的是：

1. 用当前四类模型写一个很短的 `SKILL.md` 草案；
2. 用 3–5 个真实项目场景检查它是否会：
   - 乱建文档；
   - 重复现有 Skill；
   - 误把 runtime state 持久化；
   - 漏掉真正重要的长期知识；
3. 只根据这些失败再增加规则。

这比先设计一个完整 ontology 更符合“简单、直接、最小充分”的原则。

## 9. 一个可能的 Skill 核心句

尚非最终文案，但可以作为设计锚点：

> 维护最少但足够的长期项目知识，使没有历史上下文的新 Agent 能理解项目目标、设计、重要决策和当前复杂计划；优先适配已有文档和工具，按任务读取所需内容，并在工作后只把真正长期有价值的信息同步回项目知识。
