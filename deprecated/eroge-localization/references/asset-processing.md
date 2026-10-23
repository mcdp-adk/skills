# Asset Processing

Use this method for the assets the project needs to inspect or change. A dialogue-only correction may need a voice clip for context; a localized title screen may need textures, layout data, animation, and input regions. Asset type alone does not decide scope.

## Select assets by purpose and dependency

Inventory source families before treating extraction results as coverage. For each relevant family, identify where it is stored, where it is used, what the task needs from it, and whether it is readable. Inaccessible families remain visible gaps.

| Purpose | Likely assets and dependencies | Typical processing decision |
| --- | --- | --- |
| Dialogue, choices, narration | Scripts, speaker tables, voice IDs, timing, branch data | Translate display content; preserve behavior and contextual references |
| Interface and controls | Labels, textures, atlases, layouts, focus/hit regions, help text | Determine whether wording is drawn, baked into images, or mixed |
| Scenes and galleries | Backgrounds, layered characters, expressions, CG variants, animation, unlock data | Extract context; edit only selected visual content and its dependents |
| Text rendering | Fonts, bitmap glyphs, metrics, styles, ruby data | Adapt the actual renderer and required character repertoire |
| Audio | Voice, sound effects, music, cue/loop metadata | Use as context or replace/retime when requested |
| Movies and subtitles | Video/audio streams, subtitle tracks or images, cue data, transitions | Choose subtitle, overlay, or media re-encoding to fit the runtime |
| Dynamic and persistent content | Databases, templates, state variables, saved values | Follow generated outputs and initialization separately from static resources |

Use existing resource records where adequate. Keep enough information to recover the relationship: source release and locator, asset identity, consumers, editable source, conversion settings, generated output, destination, and remaining uncertainty. This is a content requirement, not a prescribed spreadsheet or directory tree.

## Build the required processing path

1. **Extract without losing the source representation.** Retain original names, IDs, relative paths, and container membership. Separate decompression from decoding and conversion. Keep original bytes or a recoverable source when a tool produces only a flattened image, transcoded audio, or plain-text dump.
2. **Choose a working representation.** Use an editable form that preserves what the return path needs: structural text records, image layers, animation frames and timing, audio cues, or scene/object references. Record lossy conversions before relying on their output.
3. **Establish the return path.** Identify the supported encoder, importer, compiler, archive writer, loose-file override, or runtime substitution. Required metadata must survive through that path. A viewable export does not supply a writer.
4. **Modify the maintained input.** Keep manual translation and asset edits in the editable source. Regeneration should consume those edits rather than overwrite them with a fresh extraction.
5. **Generate and integrate.** Rebuild only the affected dependency set, preserving the target's IDs, formats, and load locations. Include changed metadata or catalogs when the consumer uses them.
6. **Check the relevant boundaries.** Inspect structural output first, then actual loading and presentation when runtime work is in scope. [Patch delivery](patch-delivery.md) separates the conclusions each check supports.

Before scaling an unfamiliar implementation, carry a small representative asset through the complete required path. Include a distinct mechanism when it could fail independently, such as a dialogue script and an image atlas. If runtime observation is outside scope, describe the unobserved boundary instead of treating the method as demonstrated in the game.

## Preserve identities across transformations

| Relationship | Failure to prevent |
| --- | --- |
| Asset name or object ID → consumer | Renaming an image without updating scripts, indexes, or serialized references |
| Source record → editable entry | Merging equal strings from different scenes or losing branch context |
| Texture → atlas metadata | Replacing pixels while leaving stale rectangles, pivots, or animation references |
| Media → event/cue | Changing duration while leaving voice stops, subtitles, or transitions unchanged |
| Font → renderer/style | Shipping a font without changing the display path that selects it |
| Archive member → index/load order | Building valid bytes that lose to an older archive or cached file |
| Translation → source revision | Reusing an identifier whose source meaning changed |

Some assets are intentionally unchanged. Record why they are context-only, shared, or outside scope when that affects coverage. A whole archive may need reading to locate assets, but that does not mean every member needs conversion or inclusion in the patch.

## Choose tools by operation

Separate the capabilities needed: identify, list, extract, decode, edit, encode, rebuild, and load. Check each selected tool against the actual format generation and operation. Successful decoding in one tool does not establish that another writer creates compatible output.

Prefer a native importer when the project and matching environment are available. For shipped games, use the [engine guides](engine-selection.md) to establish format-specific alternatives. Tool examples in those guides are conditional methods; use an already suitable equivalent when it preserves the same constraints.

Apply shared procedures in batches only after inputs can be distinguished reliably. Stop the affected batch on an unknown record type, identity collision, missing writer requirement, or unexpected loss of metadata; retain the failure context and continue independent known work where useful. Do not silently convert partial output into a completed set.

## Keep rebuilds maintainable

Record tool versions and consequential options with the maintained work, especially codec settings, source encodings, archive modes, and compiler targets. Reproducibility can come from a documented editor operation as well as a command; create project automation only where repetition justifies it.

On a source update, compare original assets and their consumers before reusing edits. Surface changed content and broken mappings instead of applying translations solely by row number or filename. Package the outputs of those maintained inputs using [patch delivery](patch-delivery.md).
