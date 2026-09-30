# Text Resources

Use this reference when extracting, translating in structured formats, or reinserting text. Linguistic choices belong in [Chinese adaptation](chinese-adaptation.md); resource-level transformations belong in [asset processing](asset-processing.md).

## Locate the expression, not just the string

Find each display source: scenario text, choice operands, UI tables, plugins, image lettering, system scripts, executable resources, and dynamic templates. Trace a visible phrase to its consumer when its storage is unclear. An image or generated sentence will not necessarily appear in a plain-text dump.

Preserve a record's source locator and context independently of its wording. Useful context includes speaker, adjacent lines, scene/function, route conditions, voice or image references, and display constraints. Keep identical strings separate where referents or grammar differ; join fragments conceptually when they form one displayed expression.

Prefer native translation identifiers where their lookup is understood. If generating records, use the format's identity or a structural locator plus the source revision. Line numbers and raw text alone are fragile after updates.

## Match the editing boundary

| Representation | Edit | Preserve |
| --- | --- | --- |
| Native translation catalog | Translation values and supported contextual variants | Lookup originals, IDs, plural/context rules, locale selection |
| JSON/XML/CSV or engine database | Known human-facing fields | Types, IDs, references, quoting, delimiters, multiline semantics |
| Source script | Text-bearing operands or localization blocks | Commands, labels, variable names, branches, code expressions |
| Compiled script | Supported text records through a matching importer/compiler | Instruction layout, jump targets, string pools, format version |
| Executable/runtime strings | A proven resource or display boundary | Memory ownership, calling convention, encoding and matching context |

Classify ambiguous fields from their consumers before editing. A string can be a filename, event key, comparison value, or language expression; its readable spelling does not establish its role. Translating an actor's displayed name may also affect script comparisons or saved data.

## Keep control syntax functional

Identify the format grammar before applying substitutions. Distinguish a literal backslash or percent sign from an escape or format operator. Preserve paired markup, nesting, speaker controls, line/page breaks, waits, voice commands, and branch mapping.

Reorder placeholders only where the formatter supports it. Named arguments may allow Chinese word order; positional values may require format changes. Review the assembled expression for names, numbers, optional clauses, and alternate genders or roles where the source actually provides those branches.

For example, a template meaning “give [item] to [person]” needs both identities preserved even if Chinese changes their order. A choice's translated label must stay attached to the original choice target. Moving a voiced line across a wait or page command can change timing despite preserving all words.

## Follow the bytes through the reader

Determine encoding from the reader, declared format, and known content. Preserve undecodable bytes while investigating. Use strict conversion that identifies unrepresentable characters; replacement characters hide information loss.

Windows code page 932 and code page 936 encode different repertoires. Writing Chinese bytes with a new encoder does not change the runtime's decoder. If required characters cannot pass through the existing path, use a supported Unicode route or adapt the decoder and renderer together. [Microsoft code-page documentation](https://github.com/MicrosoftDocs/globalization/blob/main/globalization/encoding/code-pages.md)

| Constraint | Check at the relevant boundary |
| --- | --- |
| Encoded storage | Byte length, terminators, byte order, length prefixes and compression |
| Parser | Escaping, syntax, supported character repertoire and nesting |
| Compiled layout | String offsets, record sizes, relocation/jump references and checksums where present |
| Runtime buffer | Capacity and lifetime in the units the program actually uses |
| Display | Glyph availability, measured width, line/page behavior and ruby |

A character count cannot substitute for encoded byte length or drawn width. Changing a code page, font, line breaker, or fixed buffer solves a different part of the chain; see [program adaptation](program-adaptation.md) and [visual resources](visual-resources.md).

Apply normalization only to intended language fields. Compatibility normalization can fold width and other distinctions; original lookup keys and identifiers may require exact preservation. [Unicode normalization](https://unicode.org/reports/tr15/)

## Reinsert and update without losing work

Preserve current translations during re-extraction. Compare source wording and context as well as identifiers, and flag additions, removals, changed meanings, and collisions. A reused ID does not imply an unchanged sentence.

After generation, parse or inspect the result with the intended format rules and compare untouched structure. A lossy dump cannot support a faithful rebuild simply because its text looks complete. Check that the game selects the intended resource through the [engine guide](engine-selection.md), including stale compiled files and patch priority.

When only an extractor exists, use its output for investigation or translation preparation with that limitation stated. Establish a compatible writer, override, or runtime path before presenting the work as an installable patch.
