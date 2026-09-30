---
name: eroge-localization
description: Localize Japanese eroge into target languages using shared translation, asset processing, and engine adaptation methods, with detailed Chinese guidance. Use when investigating game resources, translating or reviewing content, adapting assets or program behavior, or preparing a localization patch.
---

# Eroge Localization

Use the prepared methods in this package for the requested localization work. Choose them from the game's actual resources and loading behavior; an engine name narrows the investigation but does not determine every format or modification route.

## Establish the task

Determine the Japanese source release, target language and regional conventions, available materials, desired result, and affected content. A playable distribution, editable project, translation draft, and existing patch provide different modification opportunities. Reuse established project records rather than imposing a new project structure.

Apply the shared methods to the requested target language. The prepared language-specific guidance is most detailed for Simplified Chinese; use it only where it fits the target. Resolve additional language requirements from the actual content and runtime rather than assuming that an engine or font supports every language.

For a whole-game request, inventory the sources of dialogue, narration, choices, interface text, and generated messages, together with the assets they depend on. Select image, animation, audio, video, subtitle, font, and data changes from the project's needs. An asset can be useful as translation context without needing modification. For a scoped correction, follow its affected references rather than processing the whole game.

Bring consequential choices about linguistic style, asset replacement, coverage, and accepted limitations to the user with a recommendation. Technical investigation and routine implementation choices belong to the task. Patch preparation includes its files and instructions; publication and changes to the player's existing installation require that scope to have been requested.

## Read for the work at hand

| Need | Prepared guidance |
| --- | --- |
| Identify an engine, generation, or modification route | [Engine selection](references/engine-selection.md): matching engine guides and investigation of unlisted formats |
| Locate, extract, convert, modify, and re-integrate assets | [Asset processing](references/asset-processing.md): shared method, dependencies, and reversible working formats |
| Extract or rewrite strings, scripts, or data fields | [Text resources](references/text-resources.md): identity, control syntax, encodings, and compiled data |
| Interpret Japanese and translate or review the requested content | [Translation method](references/translation-method.md): context, voice, complete expressions, and review |
| Adapt wording for a Chinese target | [Chinese adaptation](references/chinese-adaptation.md): expression, address, register, and regional usage |
| Resolve recurring Japanese terms for a Chinese target | [Chinese terminology](references/chinese-terminology.md): semantic distinctions and contextual candidates |
| Adapt images, UI, animation, fonts, or layout | [Visual resources](references/visual-resources.md) |
| Adapt audio, video, or subtitles | [Media resources](references/media-resources.md) |
| Change decoding, resource loading, or runtime behavior | [Program adaptation](references/program-adaptation.md) |
| Package results or assess a completion claim | [Patch delivery](references/patch-delivery.md): coverage, compatibility, installation, and evidence |

Read only the relevant shared references and engine details. A known engine still needs the matching generation and asset-specific method; an unfamiliar engine can use the shared investigation and processing methods immediately.

## Preserve the useful relationships

- Keep original material, editable work, and generated output distinguishable. Corrections belong in the maintained inputs so rebuilding preserves them.
- Retain each asset's identity, source location, consumers, transformation, and destination. Text equality or a filename alone may lose scene, object, or version context.
- Resolve complete expressions and preserve program semantics. Localized names and labels must remain separate from resource identifiers and control data.
- Keep reusable meanings here and title-specific choices with the title. Adapt the [language decisions template](assets/language-decisions.md) only when no suitable record already exists.
- Match completion claims to the actual candidate and inspected scope. File extraction, successful conversion, game loading, and acceptable presentation establish different things.

## Apply documented methods selectively

The references contain working guidance; source links support its technical basis. Consult upstream material when a version difference, conflicting result, or uncovered mechanism requires it. Named utilities are optional candidates, selected for the specific input and output route, rather than prerequisites for using this skill.

When a method's support ends, record the exact unresolved boundary and investigate that boundary. Avoid rediscovering the already covered parts or treating a listed tool's extraction capability as proof of a complete patching route.

Return the requested material in its maintenance location. For a patch, adapt the [patch readme template](assets/patch-readme.md) to its actual base release, assets, application method, and supported behavior.
