# Patch Delivery

Use this reference to assemble a localization result and describe what its evidence supports. Apply checks to the requested result and changed mechanisms, including non-text assets.

## Account for content and assets

Compare the requested scope with the resource inventory and maintained edits. Distinguish completed work, intentionally retained material, context-only assets, excluded changes, unresolved readings, and inaccessible sources. A string count or low Japanese-residue count cannot establish whole-game coverage: kanji-only labels, images, generated messages, and unreadable sources may be missed.

For translated content, record the actual bilingual and target-language review ranges described in [translation method](translation-method.md). For other assets, identify the edited source, generated resource, dependencies, and checks appropriate to its role. An extracted asset is not necessarily an edited or integrated asset.

## Match the claim to the evidence

| Evidence | Supported conclusion | Still separate |
| --- | --- | --- |
| Resource inventory | Located sources and known gaps | Unexamined or unreadable sources |
| Bilingual comparison | Fidelity in the reviewed range | Unreviewed entries and runtime contexts |
| Target-language reading | Coherence, voice, terminology, readability | Fidelity without comparison |
| Parsing, compilation, or re-decoding | Structural acceptance by that reader | Correct game loading and behavior |
| Static font or asset inspection | Examined mappings, metadata, dimensions or streams | Actual selection and presentation |
| Runtime observation | Candidate behavior on the observed path and state | Other routes, versions and saved states |
| Clean installation | Package applicability under stated conditions | Broader compatibility |

In-game language checking reveals context and presentation problems that file review can miss. It complements the other checks rather than replacing them. [IGDA on localization QA](https://igda.org/news-archive/how-to-get-the-most-from-lqa-what-it-is-and-best-practices/)

## Check the changed mechanism

| Change | Relevant coverage |
| --- | --- |
| Dialogue, UI string, or shared term | Meaning, context, syntax, applicable occurrences and display |
| Choice or dynamic template | Branch identity, cancellation if present, meaningful substitutions and complete outputs |
| Parser, compiler, or archive writer | Retained structure, identifiers, references, format generation and actual consumption |
| Font or layout | Affected renderers, target glyph forms, input repertoire, ruby, clipping and hit regions |
| Image, atlas, animation or scene data | Transparency, geometry, frame/cell references, timing and dependent variants |
| Audio, video or subtitle | Runtime decoding, channels, loop/cue behavior, synchronization, skipping and transitions |
| Program hook or binary adaptation | Exact target, matching context, buffer/lifetime behavior, loading and failure behavior |
| Saved or initialized value | New-game initialization, patch save/load, and any claimed earlier-save compatibility |

Select cases from independently handled mechanisms and meaningful boundaries. A changed atlas needs its dependent uses checked; a local wording repair need not trigger a full game replay. Reuse earlier evidence only while its candidate inputs and relevant behavior remain applicable.

## Protect the player's state during runtime checks

Identify the test installation and actual save, configuration, unlock, and synchronization locations before launching. Copying the game folder may leave external play data shared. Use a supported alternate state location or another adequate isolation method; preserve progress before a run that could change it.

Use known entry points or isolated test saves where useful. A forced scene jump can establish rendering while bypassing progression. A save can retain names, object values, script positions, or cached text and can bypass new initialization; trace the affected value's source before claiming compatibility or introducing migration.

If adequate protection for shared play state is unresolved, stop that run and continue independent work. If runtime verification is outside the requested scope, report the prepared material and unobserved behavior without claiming runtime acceptance.

## Construct the actual deliverable

Generate from maintained translations, editable assets, adaptation code, and configurations. Retain corrections in those inputs before rebuilding. Identify the base release and final candidate; exclude intermediate experiments and unrelated original content from the package.

| Package method | Required relationship |
| --- | --- |
| Added locale or resource directory | Selection settings and paths correspond to the supplied content |
| Replacement files or archives | Exact destination, base compatibility and restoration of overwritten originals |
| Binary delta | Matching original bytes and an applicability check before modification |
| Runtime component | Correct architecture/runtime, startup path, translation/assets and required configuration |

Preserve required resource notices with redistributed fonts, media, or components. Include only the dependencies needed by the chosen patch method, not every utility used to produce it.

When installation verification is in scope, apply the packaged candidate to a clean copy of the specified release using its own instructions. A working development directory with extra assets or fallback settings does not establish package sufficiency. Confirm resource precedence and removal/restoration behavior, including pre-existing patches.

## State the result precisely

Record the candidate, input state, method, observations, supported conclusion, and concrete gaps in existing project records. Hashes or file lists identify a candidate; they do not prove meaning or presentation. A process that failed before launch establishes no runtime outcome.

Use the [patch readme](../assets/patch-readme.md) for player-facing instructions. State included content and assets, base release, application and restoration steps, save conditions, and limitations. If a required aspect is incomplete, name it and describe the options; accepting reduced coverage is a user decision.
