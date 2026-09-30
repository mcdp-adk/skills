# Text and context

Use this reference for Japanese-to-Simplified-Chinese dialogue, narration, choices, UI text, and language review. Read [terminology](terminology.md) for recurring lexical distinctions; put the title's adopted names, contextual variants, and unresolved decisions in its existing glossary or the [title glossary template](../assets/templates/title-glossary.md).

## Reconstruct the expression

A resource row is a storage boundary, not necessarily a sentence or a scene. Establish the speaker, addressee, narrative viewpoint, preceding response, following payoff, and route conditions before choosing Chinese subjects or emotional wording. File order can interleave branches. An existing translation supplies continuity but does not override Japanese evidence.

Use the smallest context that resolves the actual ambiguity: adjacent turns for an omitted object; the scene header for speaker identity; a route condition for an alternate relationship; an image or voice reference for a gesture or vocal delivery. Match those references to the same release and scene. These context categories follow a practitioner's account of localization kits and string annotations, rather than requiring one particular kit format. [IGDA: localization context](https://igda.org/news-archive/high-quality-localization-help-loc-help-you/)

| Source feature | Resolve before drafting | Chinese consequence |
| --- | --- | --- |
| Omitted subject/object | Who performs the action, who receives it, what is being referred to? | Add only what Chinese needs; retain a deliberate unknown actor or object. |
| Topic change or internal monologue | Is the narrator reporting a fact, recalling a thought, or describing someone else's belief? | Keep knowledge and certainty with the correct person. |
| Negation/condition/aspect | What is denied; what depends on a condition; has it begun, continued, or finished? | Preserve scope and sequence, including 未、还、已经、才、如果. |
| ～そう／らしい／かもしれない | Appearance, reported information, inference, or possibility? | Preserve the evidence level rather than converting every form into a fact. |
| ～てくれる／てもらう／てあげる | Actor, beneficiary, speaker's social alignment, gratitude or self-importance? | Express direction and attitude naturally; a bare 给 can lose the viewpoint. |
| Causative/passive | Who causes or permits whose action; who is affected? | Distinguish 让、使、准许、被迫 according to the full construction and context. |

Benefactive expressions preserve a direction even when the benefit is an action rather than an object; the speaker's in-group can include another person. ～てくれる and ～てもらう may convey appreciation or respect as well as concrete benefit. [Japan Foundation: direction](https://www.kyozai.jpf.go.jp/kyozai/material/BTS00004/ja/render.do), [attitude](https://www.jpf.go.jp/j/project/japanese/teach/tsushin/grammar/201412.html)

For example, 教えてもらった centers the receiver: identify whom they learned from before adding 帮我. 歌わせてください can request permission to sing; 歌わされた can report being made to sing. The causative form alone does not settle permission versus compulsion. [Japan Foundation: permission](https://www.kyozai.jpf.go.jp/kyozai/material/BMA00097/ja/render.do), [causative passive](https://www.irodori.jpf.go.jp/assets/data/pre-intermediate/pdf/ZZ_L16.pdf)

## Voice, agency, and disclosure

Preserve a character's vocabulary range, sentence rhythm, politeness, evasiveness, and changes under stress. 私、僕、俺 and endings such as わ、ぞ、です can contribute to characterization without needing a fixed Chinese substitute on every occurrence. Choose the whole utterance's voice; importing a Chinese dialect or a stock internet persona requires evidence or an established title decision.

Read adult dialogue through the same grammatical distinctions as ordinary dialogue: action, participant, body state, desire, intention, agreement, coercion, and outcome are separate facts. Retain the source's refusal, uncertainty, pressure, or consent without either softening it or adding a moral judgment. A character's claim about another person's feelings remains that character's claim. Bodily arousal or orgasm does not establish consent; treat that as a boundary on inference, not a reason to rewrite the fiction. [RAINN: bodily response and consent](https://rainn.org/share-the-facts/consent-101-respect-boundaries-and-building-trust/)

Keep anatomical specificity and lexical register separate. Clinical terminology can explain a term in a glossary without becoming the character's spoken wording. An affectionate diminutive, euphemism, crude term, or boast needs an equivalent level of directness; neither an adult scene nor a dictionary's register label determines the speaker's age or intention.

| Naming problem | Keep in the title glossary |
| --- | --- |
| Formal name, alias, nickname | Separate written forms, pronunciation, referent, adopted Chinese form, and who uses each. |
| ～さん／様／ちゃん／君 | Address relationship and scene conditions; politeness or intimacy may move into sentence wording. |
| 先生／先輩／お兄ちゃん | Actual role or relationship, and whether the label is literal, affectionate, role-played, or mocking. |
| Anonymous role or hidden identity | The label available at that narrative point, plus when a later name becomes usable. |
| Shared spelling for different people | Distinct referents and occurrence conditions; link aliases only with evidence. |

A familiar nickname becoming a surname, or a title becoming a personal name, can be plot information. Preserve the change even if both forms identify the same person. Knowledge in a character profile does not license revealing it in an earlier line. Translate a quoted misidentification as a misidentification.

## Idioms, jokes, and sounds

Identify what an idiom or joke does in the conversation: insult, reassurance, evasion, innuendo, cultural reference, or later callback. Match that function while retaining facts needed by the payoff. 舐める can mean licking or underestimating; なめるな may therefore be 别小看我. The adult genre does not choose the sense. [Shogakukan: 舐める](https://kotobank.jp/word/嘗める-589904)

For a pun, read setup and response together. Preserve a name's pronunciation if the joke depends on it; preserve its meaning if that is the mechanism. When one Chinese form cannot carry both, use a restrained local adaptation or record the unresolved tradeoff with source, candidates, and the lost effect. Avoid adding explanations that spoil a reveal or interrupt voiced timing.

Japanese onomatopoeia can represent audible events, a voice, motion, texture, sensation, or emotion; one form can belong to several categories. For example, どんどん can mark repeated beating or rapid progress. Translate the current function rather than assigning one Chinese sound per Japanese spelling. [NINJAL: sound and state categories](https://www2.ninjal.ac.jp/Onomatope/column/nihongo_1.html)

| Expression type | Preserve |
| --- | --- |
| Audible action | Source, repetition, intensity, and whether the sound is foregrounded. |
| Breathing/vocalization | Breath versus voiced sound, interruption, duration, emotional context. |
| Mimetic state | Sensation, movement, or feeling; Chinese may use a descriptive phrase. |
| Stammer/unfinished phrase | Hesitation or interruption and the point at which meaning becomes available. |
| Recurrent verbal tic | Recognizable characterization without making every line mechanically identical. |

Treat a sequence of vocalizations as a passage with rhythm. Shortened sounds, ellipses, and repeated syllables may carry timing; preserve their communicative effect within the title's typography. 喘ぐ、呻く、嬌声 and 吐息 are not interchangeable labels for pleasure; consult their distinctions in [terminology](terminology.md).

## Choices, UI, and generated text

Choices express what the player can select at that point. Preserve action, object, commitment, uncertainty, and differences between neighboring choices. An implied route consequence is not automatically part of the option wording. Buttons, state labels, settings, and help messages need their functional context: 回想 can be replay, while a history panel is a different feature.

For generated sentences, inspect the assembled expressions, not just their pieces. A display name may have an honorific appended; a counted item may need a Chinese classifier; a standalone status label may also appear inside narration. Retain variable identity and all valid branch meanings. Give fragments contextual variants only where the format supports them.

Illustrative example: `{name}さんを待つ` may become `等{name}` or another title-approved form of address; keeping a fixed suffix solely because it appears beside a variable can make the full Chinese expression unnatural. Conversely, removing a suffix that distinguishes two identities can erase information.

Preserve placeholder syntax, control tags, escape sequences, and their functional relationships. Reordering, splitting, and literal punctuation depend on the resource grammar. See [resources and patching](resources-and-patching.md) for format constraints. Resolve length pressure through accurate concise wording or supported presentation changes; silently deleting a condition or object changes the content.

## Review the complete scope

Every translated unit needs bilingual comparison and Chinese reading. These answer different questions; representative passages, summaries, or a fluent rewrite do not cover the remaining text.

| Reading | Check across all included content |
| --- | --- |
| Japanese–Chinese comparison | Omissions/additions; referents and action direction; negation, condition, sequence and certainty; register; terminology conditions; placeholders and control information. |
| Chinese reading in narrative or functional order | Continuity, antecedents, character voice, idiomatic wording, pacing, naming disclosures, and distinct choices or labels. |

After smoothing Chinese, compare the changed meaning with Japanese again. Change wording to solve a stated problem rather than to cycle through equally suitable synonyms. Review adjacent and dependent text when a referent, shared term, or relationship changes; only the affected scope needs reopening if other work remains valid.

Resolve uncertainty from the title's source context first. A dictionary establishes possible senses; a manual establishes the documented function; neither proves which sense an isolated row uses. A material unresolved issue should retain its source location, competing readings, and the effect on the translation. See [quality and evidence](quality-and-evidence.md) for coverage and remaining-limit records.
