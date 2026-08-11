# 与现有 Skill 库和 OMO Slim 的职责边界

## 1. 用户现有 Skill 库

仓库：

https://github.com/mcdp-adk/skills

当前 README 列出的主要 Skills：

- `atomic-commit`
- `everything-cli`
- `grok-search`
- `readable-artifacts`
- `reader-centered-writing`
- `review-to-closure`

新 Skill 应尽量复用而不是覆盖这些能力。

## 2. 与 `readable-artifacts` 的边界

源：

https://github.com/mcdp-adk/skills/blob/main/readable-artifacts/SKILL.md

它已经负责：

- 文件职责是否混杂；
- semantic boundaries；
- split / merge / naming；
- one authoritative expression；
- reference instead of duplication；
- 约 200 行作为 soft review point。

因此新 Skill 不再定义：

> “一个文档应该多少行、具体怎么拆。”

新 Skill只需要决定：

> “这条项目知识属于哪类长期知识、是否值得持久化。”

## 3. 与 `reader-centered-writing` 的边界

源：

https://github.com/mcdp-adk/skills/blob/main/reader-centered-writing/SKILL.md

它已经负责：

- reader / outcome；
- reading path；
- 清晰自然表达；
- 人类可读文档结构。

因此新 Skill 不重新教授技术写作。

如果要创建/大改长期文档，可以使用该 Skill 改善最终表达。

## 4. 与 `review-to-closure` 的边界

源：

https://github.com/mcdp-adk/skills/blob/main/review-to-closure/SKILL.md

它负责：

```text
review
→ finding disposition
→ authorized fix
→ verification
→ full re-review
→ closure
```

而且已经定义了 context boundary 时怎样保存 review handoff。

所以新 Skill 不建立第二套 review lifecycle。

## 5. 与 `atomic-commit` 的边界

源：

https://github.com/mcdp-adk/skills/blob/main/atomic-commit/SKILL.md

Git commit 的：

- atomic scope；
- staging；
- message；
- verification；

继续由它负责。

项目知识 Skill 只关心：

> 是否存在需要随当前变更同步更新的长期知识。

## 6. OMO Slim 的现有能力

仓库：

https://github.com/alvinunreal/oh-my-opencode-slim

Skills overview：

https://github.com/alvinunreal/oh-my-opencode-slim/blob/master/docs/skills.md

当前特别相关的是：

- Deep Work；
- Codemap；
- Verification Planning；
- Reflect。

## 7. Deep Work：临时执行状态

源：

https://github.com/alvinunreal/oh-my-opencode-slim/blob/master/src/skills/deepwork/SKILL.md

它维护：

```text
.slim/deepwork/<short-task-slug>.md
```

内容可包括：

- current goal；
- confirmed research；
- phase status；
- Oracle gates / review notes；
- validation；
- blockers / follow-ups。

官方要求真正的 code/doc deliverables 放项目路径，`.slim/deepwork/` 只保留 progress state。

因此：

> **Deep Work = runtime working memory，不是长期项目文档的替代品。**

## 8. Codemap：As-Is 代码地图

源：

https://github.com/alvinunreal/oh-my-opencode-slim/blob/master/src/skills/codemap/SKILL.md

它维护：

- `.slim/codemap.json`：change detection state；
- root / nested `codemap.md`：repository atlas。

边界：

```text
SDD / design docs → 应该怎样
Codemap           → 当前代码实际上怎样
```

新 Skill 只引用 Codemap，不重新生成 repository map。

## 9. Verification Planning：证据方法

源：

https://github.com/alvinunreal/oh-my-opencode-slim/blob/master/src/skills/verification-planning/SKILL.md

它负责：

- frame claim；
- uncertainty / failure modes；
- evidence path；
- verification affordance；
- 最终解释证据和局限。

因此复杂 Plan 需要验证设计时：

> 调用或遵循 Verification Planning，而不是在新 Skill 中复制一套测试方法论。

## 10. Reflect：Agent 工作流自身的改进

源：

https://github.com/alvinunreal/oh-my-opencode-slim/blob/master/src/skills/reflect/SKILL.md

Reflect 已负责：

- 分析反复出现的 workflow friction；
- inventory existing assets；
- 判断应做 skill / agent / command / config / playbook 还是不做；
- 避免重叠资产。

可以这样理解：

```text
project-docs Skill
→ 管“项目以后需要知道什么”

OMO Reflect
→ 管“Agent 系统以后应该怎么工作”
```

## 11. 最终边界

新 Skill 的 single responsibility 应保持：

> **让 Agent 用最少但足够的长期项目知识理解当前任务，并在工作后维护这些知识。**

其他专门能力继续由现有 owner 负责。
