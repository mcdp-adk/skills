# Siglus: scene strings and proprietary assets

Use this reference when the distribution contains Siglus scene packages, commonly `Scene.pck`, and related `Gameexe.dat`, `.g00`, or proprietary sound files. Confirm the executable and package family together; similar extensions do not prove compatible encryption or compiler settings.

## Choose the editing boundary

| Material | Practical route | Boundary |
| --- | --- | --- |
| Original `.ss` and `.inc` sources | Edit display literals, compile scenes, build the package | Preserve declarations, labels, calls, and include order |
| Compiled scene `.dat` | Extract a string map, replace identified strings, retain bytecode | A string writer does not reconstruct arbitrary script logic |
| `Scene.pck` only | Extract scenes first; select a compatible parser/profile | Extraction alone does not supply original source |
| `Gameexe.dat` | Decode configuration separately | Display title, font settings, resource paths, and logic values require different treatment |

[SiglusSceneScriptUtility](https://github.com/Jirehlov/SiglusSceneScriptUtility) is an optional maintainer tool with extraction, compilation, and asset operations. Its profile numbers describe compatibility presets, not chronological engine versions. Match the release's format and settings; a newer preset is not automatically appropriate. [Profile and compilation documentation](https://github.com/Jirehlov/SiglusSceneScriptUtility/blob/main/manual.md)

## Extract, edit, and rebuild

These commands use an already available tool on working copies. The extractor reports its actual output directory; compilation takes that directory rather than assuming the parent destination is the generated project.

```text
siglus-ssu -x ORIGINAL/Scene.pck WORK/extracted
siglus-ssu -m WORK/chapter.dat
siglus-ssu -m --apply WORK/chapter.dat
siglus-ssu -c --dat-repack WORK/repack-input OUT/Scene.pck
```

The string-map operation produces `.dat.csv`; fill its `replacement` column while retaining string indices and original values. `--apply` modifies the specified DAT in place, so it must point to a copy. Dialogue, speaker names, and other strings are separate kinds; the last category can contain identifiers or asset references. CSV escape sequences must remain reversible. [String-map implementation](https://raw.githubusercontent.com/Jirehlov/SiglusSceneScriptUtility/main/src/siglus_ssu/textmap.py)

For the package step, prepare the extracted metadata and patched DAT files together. `--dat-repack` packages existing compiled scenes; it is different from compiling edited `.ss` source. Source compilation also needs its include/configuration material. A disassembly or reconstructed source is not proof that every original construct recompiles faithfully. [CLI entry points](https://raw.githubusercontent.com/Jirehlov/SiglusSceneScriptUtility/main/README.md), [repack modes](https://github.com/Jirehlov/SiglusSceneScriptUtility/blob/main/manual.md)

Keep outer encryption/compression and scene-string XOR settings distinct. Use the same string XOR multiplier when reading and writing; an incorrect value can yield apparently valid files with unreadable text. Extraction settings are not all persisted for a later compile. [String encoding options](https://github.com/Jirehlov/SiglusSceneScriptUtility/blob/main/manual.md)

## Text and program dependencies

- Translate the display value, retaining its string ID, speaker relationship, and associated voice cue.
- Inspect control syntax in actual strings and the consuming commands before changing braces, delimiters, or line breaks; do not import another engine's escape rules.
- Search configuration and system scenes for menus, backlog, name entry, and error text beyond dialogue strings.
- Trace generated text and comparison operands before translating the `other` string category. A Japanese filename or lookup key remains a program dependency.
- Separate a font selection setting from the decoder and renderer. Font coverage cannot repair a writer/runtime encoding mismatch; see [program adaptation](../program-adaptation.md).

## Images, sound, and video

G00 has multiple representations, including compressed pixels, palettes, cut-based images, and JPEG data. Keep the source type and metadata with the editable image; a flat PNG does not describe every original cut, position, or canvas. [G00 reader/writer](https://raw.githubusercontent.com/Jirehlov/SiglusSceneScriptUtility/main/src/siglus_ssu/g00.py)

For type-2 G00, retain the emitted JSON sidecar and cut images. Trimmed extraction omits reconstruction information. When building against a reference image, specify a separate output path: an omitted output can overwrite the reference. Keep button states, crop rectangles, and animation relationships while redrawing visible lettering. [Image modes](https://github.com/Jirehlov/SiglusSceneScriptUtility/blob/main/manual.md)

NWA decoding, OWP-to-Ogg conversion, and OVK voice extraction are separate sound operations. Preserve voice numbering and script associations. Decoding to WAV or Ogg does not establish a compatible encoder or archive writer for the target release. [Sound format implementation](https://raw.githubusercontent.com/Jirehlov/SiglusSceneScriptUtility/main/src/siglus_ssu/sound.py)

Treat OMV/video replacement as a separate format-specific writer problem, retaining timing and audio relationships. Use [media resources](../media-resources.md) for subtitles and timing, and [patch delivery](../patch-delivery.md) for the final package boundary.

## Compatibility limits

Modified executables, unsupported encryption, mobile forks, unknown scene instructions, and incomplete reconstruction require a release-specific reader/writer or original authoring material. Do not replace a runtime or claim package compatibility from a successful extraction alone.
