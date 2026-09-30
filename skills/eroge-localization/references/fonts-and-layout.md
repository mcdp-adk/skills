# Fonts and Layout

Use this reference for Chinese glyph support, font selection, missing characters, and layout changes. Engine configuration belongs in the matching [Ren'Py](engines/renpy.md) or [RPG Maker MV/MZ](engines/rpg-maker.md) reference.

## Locate each display path

Trace a visible string to its renderer and font selection. Dialogue, speaker names, menus, history, input fields, ruby, and plugin windows can have different settings. A bitmap atlas or pre-rendered label needs its own resource method; adding a font file will not change it.

Record the actual family or file, style overrides, fallback, size, outline, and width constraints for the path being changed. Investigate shared settings when the same defect appears in several places. Different visual styles can come from different fonts or from settings on one font; choose replacements after identifying that distinction.

## Separate three questions

| Question | Useful evidence | Insufficient evidence |
| --- | --- | --- |
| Does the font map the character? | Character-to-glyph mapping in the font used | Filename, family name, or a byte search |
| Does the game use that font? | Loading/configuration evidence and observation on the affected display path | The file exists beside the executable |
| Does the text render suitably? | Actual Chinese forms, punctuation, line metrics, and layout | All requested code points appear in a coverage report |

OpenType's `cmap` maps character codes to glyph indices; unsupported characters normally map to glyph zero. Variation sequences can require additional mapping. Coverage checks must examine applicable mappings rather than names or raw byte occurrences. [Microsoft OpenType specification](https://learn.microsoft.com/en-us/typography/opentype/spec/cmap)

Prefer a Simplified Chinese design where the intended appearance is Simplified Chinese. Pan-CJK families can contain regional glyph variants; a shared Unicode character does not guarantee the chosen Japanese form matches the desired Chinese form. Source Han Sans provides regional configurations, including Simplified Chinese, and is one candidate when its visual style suits the title. [Adobe's font configurations](https://github.com/adobe-fonts/source-han-sans/blob/release/README.md)

Choose a font format supported by the shipped runtime. Keep the existing visual role in view: a body sans-serif replacement may be unsuitable for a decorative title. A static font can be a simpler compatibility candidate than a variable font where runtime support is unknown; verify against the actual loader.

## Determine the required character set

Build coverage from the final visible strings, including Chinese punctuation, names, Latin text, digits, symbols, ruby, retained Japanese, and generated messages. Parse control syntax so markup is distinguished from visible text; include characters contributed by runtime substitutions.

Treat player input separately. If players may enter names outside the fixed script, either support the agreed input range with an appropriate font or keep a suitable fallback that is actually available in the delivered environment. A font subset derived only from dialogue cannot establish support for arbitrary names.

With a font inspection tool, compare required code points against the selected font's Unicode mappings and inspect missing entries. For example, fontTools exposes a Unicode mapping through `TTFont.getBestCmap()`; its result is a coverage aid, not evidence about the game's font selection or appearance. Use equivalent facilities already available in the task environment. [fontTools font inspection API](https://fonttools.readthedocs.io/en/stable/ttLib/ttFont.html)

Subset only when the size benefit is useful and the needed characters are bounded. If using fontTools' subsetter, `--no-ignore-missing-unicodes` makes missing requested Unicode characters an error; its documented default permits those omissions. Keep required layout features and inspect the output mappings after subsetting. [fontTools subsetting options](https://fonttools.readthedocs.io/en/stable/subset/)

Retain the chosen font's provenance and applicable license with the maintained resource. For a redistributed or modified font, check the supplied license's terms, including any reserved names and notice requirements. Source Han Sans distributes its license alongside the font sources. [Source Han Sans license](https://github.com/adobe-fonts/source-han-sans/blob/release/LICENSE.txt)

## Fit Chinese text without changing its meaning

Use the title's punctuation style consistently. Horizontal Simplified Chinese ordinarily uses fullwidth Chinese punctuation and opening/closing pairs. Avoid a closing mark stranded at the start of a line or an opening mark at the end; keep paired ellipses and dashes together where required by the chosen convention. These are layout constraints, not reasons to add or remove story information. [W3C Chinese layout requirements](https://www.w3.org/TR/clreq/)

Distinguish a mandatory line/page break in script from automatic wrapping. Preserve pauses, voice alignment, and page progression when moving a break. A line-breaking algorithm supplies permissible break positions; the renderer still chooses breaks based on available width and metrics. [Unicode line-breaking specification](https://unicode.org/reports/tr14/)

For overflow, determine the constraint before changing the translation:

1. Check whether concise, accurate Chinese expresses the same meaning.
2. Check width, padding, font metrics, line height, and wrapping behavior at the affected control.
3. Adjust the appropriate layout or supported line/page boundaries.
4. Revisit neighboring text, ruby, hit areas, and alternate window sizes affected by shared settings.

Changing every font size to fix one window can make unrelated text unreadable. Shortening a choice can also change its apparent promise or contrast with other choices; review the whole choice set after a layout-driven revision.

## Diagnose by symptom

| Symptom | First distinction to resolve |
| --- | --- |
| Corrupted characters rather than empty boxes | Decoding or escaping before font selection |
| Empty boxes for particular characters | Missing mappings versus the wrong selected font |
| Correct text on one machine only | Bundled font and explicit selection versus system fallback |
| Correct dialogue but broken menus | Independent style, plugin, atlas, or language path |
| Text fits until a name or number changes | Substitution width and runtime input coverage |
| Glyphs are present but look Japanese | Regional glyph choice and supported language features |
| Clipped accents, punctuation, or ruby | Line height, bounds, baseline, and outline metrics |

Use the affected game path to confirm a repair when runtime work is authorized. Keep unobserved behavior separate from successful static font inspection; acceptance records are described in [quality and evidence](quality-and-evidence.md).
