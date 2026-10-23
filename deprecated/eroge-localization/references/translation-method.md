# Translation Method

Use this reference to interpret Japanese source material, write for the requested target language, or review a translation, including text spoken, drawn, or timed in other assets. Use [Chinese adaptation](chinese-adaptation.md) for Chinese expression and [text resources](text-resources.md) for insertion constraints.

## Recover the intended meaning

Treat a resource row as a storage unit. Recover the complete expression and its scene or UI function before translating. Identify speaker, addressee, viewpoint, preceding response, following payoff, and relevant route conditions; file order may interleave branches.

Use the smallest context that resolves the uncertainty: adjacent turns for an omitted object, a voice clip for delivery, a scene image for a gesture, or the caller for a UI label. Match those resources to the source release. Existing translations can provide continuity, but the Japanese source and its context remain authoritative for meaning. Context annotations and access to relevant game materials are established localization practices. [IGDA on localization context](https://igda.org/news-archive/high-quality-localization-help-loc-help-you/)

| Japanese feature | Resolve before choosing target wording |
| --- | --- |
| Omitted subject or object | Actor, recipient, referent, and whether concealment is intentional |
| Negation, condition, aspect | Scope, dependency, sequence, and whether an action began or finished |
| ～そう／らしい／かもしれない | Appearance, hearsay, inference, possibility, and whose knowledge is expressed |
| ～てくれる／てもらう／てあげる | Action direction, beneficiary, viewpoint, and attitude |
| Causative or passive | Permission, causation, compulsion, and affected participant |

Benefactive expressions carry viewpoint as well as direction. A causative alone does not settle permission versus coercion: 歌わせてください can request permission, whereas 歌わされた can report being made to sing. [Japan Foundation: benefactive viewpoint](https://www.jpf.go.jp/j/project/japanese/teach/tsushin/grammar/201412.html), [permission](https://www.kyozai.jpf.go.jp/kyozai/material/BMA00097/ja/render.do), [causative passive](https://www.irodori.jpf.go.jp/assets/data/pre-intermediate/pdf/ZZ_L16.pdf)

## Preserve voice and narrative knowledge

Express voice through vocabulary, rhythm, politeness, and emotional state. Japanese pronouns and sentence endings need not receive fixed word-for-word substitutes. Distinguish intentional ambiguity from missing context; target grammar should not invent a relationship, identity, or fact that the source has not established.

Distinguish action, intention, desire, bodily response, consent, and outcome in adult dialogue as elsewhere. Preserve who claims what about whom. A bodily response is not evidence of consent; this limits inference rather than licensing a rewrite of the scene. [RAINN on bodily response and consent](https://rainn.org/share-the-facts/consent-101-respect-boundaries-and-building-trust/)

Match anatomical specificity and directness separately. A clinical glossary explanation need not become spoken terminology; a euphemism need not become more explicit. Preserve refusal, uncertainty, coercion, affection, and boasting where the source expresses them.

Record title-specific name forms, aliases, honorific treatment, address relationships, and voice decisions in the existing glossary or [language decisions template](../assets/language-decisions.md). Give variants their conditions and target language. The same referent can have a formal name, nickname, and anonymous label that are not interchangeable before a reveal. When several targets are requested, keep their wording decisions distinct while sharing source context.

## Adapt function, sound, and timing

For idioms and jokes, establish the conversational function and read setup with payoff. Preserve facts required by callbacks. A pun may depend on pronunciation, written meaning, or both; record a consequential loss when no target wording carries the same mechanism.

Japanese mimetic expressions can describe sounds, motion, texture, sensation, or emotion. Translate the current function: どんどん can represent repeated beating or rapid progress. [NINJAL on mimetic categories](https://www2.ninjal.ac.jp/Onomatope/column/nihongo_1.html)

| Material | Preserve during adaptation |
| --- | --- |
| Vocalization and breathing | Voiced sound versus breath, duration, interruption, emotional context |
| Stammer or unfinished phrase | Hesitation and the point at which information becomes available |
| Repeated verbal tic | Recognizable voice with natural variation |
| Voiced dialogue or subtitle | Meaning and speaker association within actual cue and page timing |
| Lettering inside an image | Wording, reading order, visual hierarchy, and relevant scene context |
| Choice set | Distinct action, object, commitment, and uncertainty for each original branch |
| Button or status label | The operation or state shown, rather than an isolated dictionary gloss |

Use [media resources](media-resources.md) when timing changes and [visual resources](visual-resources.md) when lettering or layout changes. A shorter line should remain faithful; deleting a condition to fit a box changes the player's information.

## Read generated expressions as outputs

Inspect templates with their valid substitutions. Names, quantities, and optional clauses can change the wording a target language needs. Preserve variable identity and actual branching semantics while adapting word order and grammatical agreement. Follow [text resources](text-resources.md) for the formatter's constraints.

A standalone label may also occur inside a sentence. If one fragment cannot serve its actual contexts naturally, use supported contextual variants or adapt the complete expression. Establish the required distinction from real outputs before adding variants or changing program behavior.

## Review the requested range

Compare every included translated unit with Japanese for omissions, additions, referents, action direction, negation, conditions, sequence, certainty, register, terminology conditions, and control content. Then read the target text in narrative or functional order for continuity, voice, pacing, disclosure, and distinct choices.

These are different checks. Fluency does not prove fidelity, and a sample does not cover an unread chapter. Report the actual reviewed range when the task is limited. After smoothing target wording, compare changed meanings with the source again; reopen dependent passages when a shared decision changes.

Resolve uncertainty from source context before treating a dictionary candidate as a decision. Keep a material unresolved reading with its location, alternatives, and practical consequence. [Patch delivery](patch-delivery.md) explains how review scope contributes to completion claims.
