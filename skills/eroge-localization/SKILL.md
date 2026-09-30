---
name: eroge-localization
description: Localize Japanese eroge into Simplified Chinese with guidance for translation, resource adaptation, and patch acceptance. Use when investigating a game's localization requirements, translating or reviewing its text, adapting resources, or preparing and checking a Chinese patch.
---

# Eroge Localization

Apply the references in this package to the requested Japanese-to-Simplified-Chinese localization task. They provide reusable language knowledge, technical methods, and acceptance criteria. Work from the title's actual version, resources, and agreed scope; use the matching material without repeating research already covered here.

## Scope

For a whole-game request, account for dialogue, narration, choices, interface text, and generated messages. Treat image lettering, redraws, and voice replacement as separate scope decisions. For a local correction or investigation, work on the requested content and its affected uses.

Patch preparation produces the package and its instructions. Include publication or changes to a player's existing installation only when requested.

Use existing project records, editable files, and terminology decisions. Establish missing facts from the supplied materials; bring choices about coverage, characterization, visual style, or accepted limitations to the user with a recommendation and its consequences. Ordinary file organization and implementation choices belong to the current task.

## Choose the relevant reference

Read only the rows that apply. An engine guide supplements the shared technical guidance when its conditions match the game.

| Current need | Reference and what it supplies |
| --- | --- |
| Interpret, translate, or revise text | [Text and context](references/text-and-context.md): Japanese meaning, character voice, dynamic expressions, and linguistic review |
| Resolve a recurring term or register | [Terminology](references/terminology.md): reusable distinctions and context-dependent Chinese candidates |
| Find content, preserve editable translations, or build a patch | [Resources and patching](references/resources-and-patching.md): coverage, source relationships, encoding, loading, and package construction |
| Choose or adapt fonts and layout | [Fonts and layout](references/fonts-and-layout.md): Chinese glyphs, display paths, character coverage, and line fitting |
| Judge coverage, a repair, or a deliverable | [Quality and evidence](references/quality-and-evidence.md): language, runtime, compatibility, and patch acceptance |
| Work with Ren'Py resources | [Ren'Py](references/engines/renpy.md): native translation, script availability, language selection, and engine-specific constraints |
| Work with RPG Maker MV or MZ resources | [RPG Maker MV/MZ](references/engines/rpg-maker.md): database and event text, escapes, plugins, fonts, and saved state |

For an unlisted engine, start from the shared resource guidance and identify the actual reader, format, and display mechanism. Research the unresolved mechanism; record title-specific findings with the title's materials. An engine name or familiar extension alone does not establish compatibility with a tool or method.

## Keep the work grounded

- Keep the original release unchanged. Edit maintainable translation or adaptation sources and generate the patch from them; apply and run it in a suitable test copy when runtime work is in scope.
- Preserve the relationship between source location, context, current translation, generated output, and checked candidate. Identical Japanese strings can need different translations in different contexts.
- Resolve meaning at the level of a complete expression. Maintain variable identity and program behavior while adapting Chinese wording and order.
- Use the title's glossary for confirmed choices and their conditions. The bundled terminology reference provides meanings and candidates, not automatic substitutions. Use the [title glossary template](assets/templates/title-glossary.md) only when an existing format does not already serve this purpose.
- Match completion claims to actual evidence. Translation review, structural checks, runtime observation, and installation checks answer different questions; [quality and evidence](references/quality-and-evidence.md) defines their boundaries.

## Use the prepared knowledge

The references include the working knowledge needed for their stated scope. Source links document the basis of technical or linguistic claims. Revisit a source when a version mismatch, conflicting evidence, or an uncovered mechanism makes further research useful.

Keep tool choices conditional on the available materials and their supported formats. A method documented for an editable developer project may not apply to a shipped game. Establish that distinction before producing a large translation set or recommending additional tools.

Return the requested result in its maintenance location, with the applicable source version, remaining uncertainties, and evidence for any completion claim. When delivering a patch, adapt the [release notes template](assets/templates/release-notes.md) to the actual package and supported installation method.
