# Project Knowledge Research Index

This directory preserves design evidence and background knowledge for the `project-knowledge` Skill. It is not a set of runtime instructions or a specification, and it does not override `SKILL.md`. The Markdown snapshots under `notes/` are retained as research material, including candidate designs that may have evolved or remained undecided.

Do not read the entire collection by default. Select the original or snapshot that bears on the current design question, trade-off, or edge case. The Skill's normal execution path should remain usable without loading the research corpus.

See [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md) for the redistribution notices for bundled PDFs. Link-only originals are listed below but are not redistributed here.

## Research snapshots

These 11 files were copied from the project research directory without rewriting or formatting. They are background snapshots, not instructions.

| Snapshot | Read it when |
|---|---|
| [README.md](notes/README.md) | You need the research project's scope, status, evolution, or map of its source notes. |
| [00-design-evolution.md](notes/00-design-evolution.md) | You need to understand why the model was simplified and which intermediate abstractions were deliberately dropped. |
| [01-research-foundations.md](notes/01-research-foundations.md) | You need the evidence and reasoning behind durable repo-native knowledge, context boundaries, thin `AGENTS.md`, and artifact-first action. |
| [02-current-model.md](notes/02-current-model.md) | You need the research project's then-current model of long-term knowledge, entry points, runtime state, and Fresh Agent recovery. |
| [03-software-engineering-profile.md](notes/03-software-engineering-profile.md) | You need the proposed relationship among PRDs, design descriptions, ADRs, delivery plans, and verification. |
| [04-creative-and-game-development.md](notes/04-creative-and-game-development.md) | You need the earlier analysis of games, prototypes, experiential evidence, multimodal artifacts, and human–AI creative boundaries. |
| [05-skill-direction.md](notes/05-skill-direction.md) | You need the rationale for making this method a progressive-disclosure Skill and for keeping its core small. |
| [06-existing-skills-and-omo-slim.md](notes/06-existing-skills-and-omo-slim.md) | You need the proposed responsibility boundaries with documentation, review, commit, Codemap, verification, and harness capabilities. |
| [07-cross-agent-compatibility.md](notes/07-cross-agent-compatibility.md) | You need background on preserving project knowledge across OpenCode, Codex, Kimi Code, ZCode, and other harnesses. |
| [08-open-questions.md](notes/08-open-questions.md) | You need to inspect unresolved trigger, entry-point, plan-retention, authority, and persistence questions from the design stage. |
| [REFERENCES.md](notes/REFERENCES.md) | You need the research project's source bibliography and external links. |

## Bundled paper originals

All seven PDFs below are preserved as downloaded, unmodified PDF content. Only their local filenames identify the papers in this package. Each is available under the stated CC BY 4.0 license.

### Evaluating AGENTS.md

- **Title:** *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?*
- **Authors:** Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev
- **Version/date:** v2, 2026-06-23
- **Abstract:** https://arxiv.org/abs/2602.11988
- **Canonical PDF:** https://arxiv.org/pdf/2602.11988
- **Local file:** [2602.11988-evaluating-agents-md-context-files-v2.pdf](originals/2602.11988-evaluating-agents-md-context-files-v2.pdf)
- **License:** https://creativecommons.org/licenses/by/4.0/
- **SHA-256:** `EFA31841F8ADA102CC488E080209762957D78FF1A22BD6D4CD73B6BB565B6BEC`
- **Size:** 2,736,310 bytes
- **Read it when:** You need evidence about the benefits, costs, or risks of repository-level context files.

### What Context Does a Coding Agent Actually Need to Act?

- **Title:** *What Context Does a Coding Agent Actually Need to Act?*
- **Authors:** Brian Sam-Bodden
- **Version/date:** v1, 2026-06-19
- **Abstract:** https://arxiv.org/abs/2607.09691
- **Canonical PDF:** https://arxiv.org/pdf/2607.09691
- **Local file:** [2607.09691-what-context-does-a-coding-agent-need-v1.pdf](originals/2607.09691-what-context-does-a-coding-agent-need-v1.pdf)
- **License:** https://creativecommons.org/licenses/by/4.0/
- **SHA-256:** `CF5E72BA371A96915D2ED540BB3C6663EBD64925E1C7F64BEFFF14C39905A766`
- **Size:** 406,887 bytes
- **Read it when:** You need to reason about the difference between finding a work location and having enough context to act on the actual artifact.

### Instruction Adherence in Coding Agent Configuration Files

- **Title:** *Instruction Adherence in Coding Agent Configuration Files: A Factorial Study of Four File-Structure Variables*
- **Authors:** Damon McMillan
- **Version/date:** v1, 2026-05-11
- **Abstract:** https://arxiv.org/abs/2605.10039
- **Canonical PDF:** https://arxiv.org/pdf/2605.10039
- **Local file:** [2605.10039-instruction-adherence-config-files-factorial-v1.pdf](originals/2605.10039-instruction-adherence-config-files-factorial-v1.pdf)
- **License:** https://creativecommons.org/licenses/by/4.0/
- **SHA-256:** `922118FE2003E8D257A8E4836DCCE8FAC2A11500E61E776E4A7BA70F0B6DBD70`
- **Size:** 1,392,622 bytes
- **Read it when:** You need to weigh claims about configuration-file structure, size, placement, or instruction adherence.

### An Exploratory Study of Agent Plans

- **Title:** *An Exploratory Study of Agent Plans for Agentic AI Coding Tools in Open-Source Software*
- **Authors:** Muhammad Auwal Abubakar, Seyedmoein Mohsenimofidi, Jai Lal Lulla, Jie M. Zhang, Christoph Treude, Sebastian Baltes, Matthias Galster
- **Version/date:** v2, 2026-08-06
- **Abstract:** https://arxiv.org/abs/2608.04661
- **Canonical PDF:** https://arxiv.org/pdf/2608.04661
- **Local file:** [2608.04661-exploratory-study-agent-plans-oss-v2.pdf](originals/2608.04661-exploratory-study-agent-plans-oss-v2.pdf)
- **License:** https://creativecommons.org/licenses/by/4.0/
- **SHA-256:** `E202E94DEDA20A0393DC6D026FD3A247B2742748783DFF21FC92ACE6085573E3`
- **Size:** 745,567 bytes
- **Read it when:** You need background for separating repository instructions from durable task-level plans.

### Do Context Files Help Coding Agents?

- **Title:** *Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories*
- **Authors:** Prakhar Khatri
- **Version/date:** v1, 2026-07-28
- **Abstract:** https://arxiv.org/abs/2607.27250
- **Canonical PDF:** https://arxiv.org/pdf/2607.27250
- **Local file:** [2607.27250-do-context-files-help-coding-agents-ablation-v1.pdf](originals/2607.27250-do-context-files-help-coding-agents-ablation-v1.pdf)
- **License:** https://creativecommons.org/licenses/by/4.0/
- **SHA-256:** `FCF153DBD49B7FAEA48E9C0A83697942B1E5ECDE89524421CF3B7A963FA57967`
- **Size:** 193,268 bytes
- **Read it when:** You need a caution against assuming that context-file strategies automatically improve correctness.

### GameDevBench

- **Title:** *GameDevBench: Evaluating Agentic Capabilities Through Game Development*
- **Authors:** Wayne Chi, Yixiong Fang, Arnav Yayavaram, Siddharth Yayavaram, Seth Karten, Qiuhong Anna Wei, Runkun Chen, Alexander Wang, Valerie Chen, Ameet Talwalkar, Chris Donahue
- **Version/date:** v2, 2026-06-30
- **Abstract:** https://arxiv.org/abs/2602.11103
- **Canonical PDF:** https://arxiv.org/pdf/2602.11103
- **Local file:** [2602.11103-gamedevbench-agentic-game-development-v2.pdf](originals/2602.11103-gamedevbench-agentic-game-development-v2.pdf)
- **License:** https://creativecommons.org/licenses/by/4.0/
- **SHA-256:** `65BDE4527F8F401648A618E9FB3A1E5354F538799AF20E9E5A56F181C2500CA9`
- **Size:** 19,517,539 bytes
- **Read it when:** You need evidence about multimodal and agentic difficulties in game-development tasks.

### The Human Creativity Benchmark

- **Title:** *The Human Creativity Benchmark*
- **Authors:** Aspen Hopkins, Allison Nulty, Alexandria Minetti, Anoop Pakki, Angad Singh
- **Version/date:** v1, 2026-06-29
- **Abstract:** https://arxiv.org/abs/2606.30561
- **Canonical PDF:** https://arxiv.org/pdf/2606.30561
- **Local file:** [2606.30561-human-creativity-benchmark-v1.pdf](originals/2606.30561-human-creativity-benchmark-v1.pdf)
- **License:** https://creativecommons.org/licenses/by/4.0/
- **SHA-256:** `D2ED58D1A5A0E8CBFDB1D5D31F1DFB704191DCBA4A919749E2A54C7D26F4C4B0`
- **Size:** 13,716,036 bytes
- **Read it when:** You need to distinguish technical agreement from human judgment about aesthetic direction or creative quality.

## Link-only originals

The following authoritative sources are referenced but not bundled because their redistribution licenses are not established here:

- Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Anthropic, [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- Anthropic, [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- OpenAI, [Using PLANS.md for multi-hour problem solving](https://developers.openai.com/cookbook/articles/codex_exec_plans)
- OpenAI, [Run long horizon tasks with Codex](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)
- [MDA: A Formal Approach to Game Design and Game Research](https://aaai.org/papers/ws04-04-001-mda-a-formal-approach-to-game-design-and-game-research/)
- [Game design documentation: four perspectives from independent game studios](https://doi.org/10.1145/3321388.3321389)

These entries remain links only; this package makes no claim to redistribute those works.
