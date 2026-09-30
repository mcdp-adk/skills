# Resources and Patching

Use this reference to locate translatable content, choose a maintainable adaptation method, or construct a patch. Match engine-specific details to [Ren'Py](engines/renpy.md) or [RPG Maker MV/MZ](engines/rpg-maker.md) when applicable.

## Establish the resource model

Identify the exact release and available material: editable project, loose scripts, database files, archives, compiled code, or a mixture. Find the executable or runtime version and the files it actually reads. Existing patches, plugins, language settings, and caches can change that relationship.

Survey by source family and visible function. Keep unresolved or unreadable families in the coverage record even when extraction succeeds elsewhere.

| Content family | Where to investigate | Translation constraint |
| --- | --- | --- |
| Story and choices | Scenario scripts, event pages, common events, route conditions | Preserve speaker, sequence, branch conditions, and choice consequences |
| Interface and system messages | Language tables, screen definitions, database terms, plugin parameters | Distinguish display labels from resource names and program keys |
| Generated expressions | Templates, variable assignments, concatenation, formatting functions | Trace complete outputs and all meaningful branches |
| Recollection and extra modes | Replay entry points, gallery labels, unlock conditions | Text and state can differ from the ordinary route |
| Image lettering and special glyphs | Textures, atlases, pre-rendered labels, custom drawing | Separate in-scope text rendering from optional image localization |
| Persistent or player-supplied text | Name input, saved values, cached descriptions | Determine whether a loaded save uses new resources or stored text |

A useful coverage record names the source family, location, displayed purpose, extraction status, and remaining uncertainty. Add detail where it enables editing or identifies a gap. Counts of extracted or translated strings describe only the sources counted; they cannot establish whole-game coverage.

## Choose a method from available inputs

| Available mechanism | Preferred approach | Check before relying on it |
| --- | --- | --- |
| Working native localization support | Maintain its translation files and locale settings | The release contains the necessary identifiers and invokes the translation mechanism |
| Structured text resources | Parse and update known display fields | The writer preserves IDs, types, ordering where significant, and untouched fields |
| Text mixed with executable script | Edit translation blocks or identified language expressions | The parser distinguishes text from code, labels, paths, and comments |
| Compiled or packed material | Use a format-compatible reader and a known loading or rebuilding route | Successful extraction alone does not prove that modified content can be consumed |
| Runtime translation or replacement | Resolve strings at the correct display boundary using available context | Identity collisions, substituted values, caches, timing, and performance remain controlled |

Keep the smallest method that handles the title. A generic extractor is useful only if its output retains the information needed to put translations back. Check a tool's supported engine generation, format revision, input type, and output route before recommending it.

## Keep source and translation identities separate

The editable material must let a reader recover:

- Source release and location, including an engine ID or structural position when available.
- Original text and enough context to interpret it: speaker, adjacent lines, scene or function, conditions, and related uses.
- Current translation and its treatment: translated, intentionally retained, unresolved, or excluded from the agreed scope.
- Relevant format constraints and what linguistic review has actually been completed.

Use a native translation format when it already carries these relationships. Supplement only its missing information. Separate records can share the same translation when their meaning and usage agree; equality of source text alone is insufficient.

For example, a menu action and a line of dialogue can both contain `戻る` while requiring different phrasing. Conversely, several resource entries can form a single sentence. Keep the mapping needed to edit those cases without inventing one universal string key.

On a new source release, compare original content and context as well as identifiers before reusing a translation. A reused ID can contain changed text; a shifted line number can still refer to unchanged text. Preserve edited translations during re-extraction and surface collisions instead of silently overwriting them.

## Preserve syntax and bytes

Read and write through the actual format. For structured files, round-trip through the matching parser; for script, preserve executable structure. Identify placeholders by their function, including format type and nesting. Chinese word order can move supported named arguments, but positional substitutions and control commands may constrain reordering.

| Boundary | Concrete check |
| --- | --- |
| Serialization | Quotes, backslashes, literal newlines, and markup survive the format's escaping rules |
| Program identity | Labels, filenames, database IDs, resource keys, and comparisons still refer to their intended objects |
| Encoding | Reader and writer agree on encoding, byte order, and any required marker |
| Length | Measure the actual limit: encoded bytes, code units, drawn width, or available lines |
| Binary layout | Changed lengths are reflected in offsets, size fields, checksums, or compression where the format requires them |

Windows code page 932 is a Japanese Shift-JIS variant; 936 uses a different Chinese mapping. Changing the encoding of a file does not change the game's decoder. Preserve source bytes until the reader is known, use strict conversion that reports unrepresentable characters, and distinguish a legacy decoder problem from a missing font. [Microsoft code-page documentation](https://github.com/MicrosoftDocs/globalization/blob/main/globalization/encoding/code-pages.md)

Unicode compatibility normalization can fold distinctions such as width variants. Apply text cleanup only to the intended human-language fields; keep identifiers and lookup originals exact unless their matching rules explicitly allow normalization. [Unicode normalization specification](https://unicode.org/reports/tr15/)

If the reader cannot represent the required Chinese characters, choose an actual adaptation of the decoder/rendering path or another supported text mechanism. A global system-locale change is not a substitute for establishing a distributable solution.

## Establish a reusable edit-to-game path

When implementing a new method, take a few entries through the real chain: source location, editable translation, generated resource, package placement, selected language, and game display. Include independently handled cases such as a dialogue block, choice, dynamic sentence, and alternate font where present. Use [quality and evidence](quality-and-evidence.md) to judge what the observations establish.

Then change the maintained translation and repeat generation. This distinguishes a reusable method from a hardcoded demonstration. Keep source, operations, and outputs identifiable; automation is useful where repeated manual steps are error-prone, but a reproducible native editor operation can also be sufficient.

If the requested task excludes runtime verification, complete the authorized static work and state which parts of this chain remain unobserved. Do not present a documented method as already working in that title.

## Build from maintained material

Generate a candidate from the selected translations, adaptation code, and resource configurations. Record which source release and maintained inputs it uses. Intermediate outputs may be incomplete; identify their purpose and coverage so they cannot be mistaken for an accepted release.

Keep linguistic corrections in the editable translation source. If a supposedly generated file contains the only copy of a correction, preserve it and recover that correction into the maintained inputs before regeneration.

Choose the package form from the verified loading method:

- An added language directory needs the matching selection and resource paths.
- Replacement files need exact target paths and a restoration method for the overwritten originals.
- A binary delta needs a matching base file and an applicability check before patching.
- A runtime component needs compatible startup/loading behavior and its actual required resources.

Include only the agreed patch files and required distributable dependencies. Separate test data, original game content unrelated to the patch, and working material from the deliverable. Installation instructions must state compatibility with the source release and any interacting patches; file presence alone does not establish loading priority.

After changing shared code, fonts, terminology, or resource mappings, identify the affected outputs and evidence. Rebuild those outputs and revisit the relevant checks. Keep unresolved work visible even if a defective candidate is discarded.
