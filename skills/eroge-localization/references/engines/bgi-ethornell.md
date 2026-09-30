# BGI / Ethornell: two script layers

Use this reference for a confirmed BGI/Ethornell distribution. Separate scenario files, internal system scripts, image formats, and archive containers before choosing a reader or writer; they are not one interchangeable format.

## Identify the script layer

| Material | Mechanism | Practical editing boundary |
| --- | --- | --- |
| `._bp` internal scripts | System VM implemented in `BGI.exe` | UI/rendering logic requires its own instruction-aware writer |
| Extensionless scenario files | Scenario VM implemented by `scr*._bp` | Dialogue/name extraction and relocation-aware insertion |
| Archive entries | Container around scripts/assets | Extraction plus a compatible archive writer or supported override |
| CompressedBG images | Proprietary pixel compression | Decode, redraw, and re-encode the supported image variant |

[EthornellTools](https://github.com/arcusmaximus/EthornellTools) documents the two VMs. Its `BgiDisassembler` handles internal scripts; that disassembler is not a scenario compiler or a complete system-script rebuild tool. `BgiImageEncoder` is a separate image writer. [Maintainer documentation](https://raw.githubusercontent.com/arcusmaximus/EthornellTools/master/README.md)

The VNTextPatch scenario parser selects a header-based V1 implementation or its V0 implementation. Record the actual header, parser result, and release; an extensionless filename does not identify the instruction set. Unknown/custom formats require a matching parser rather than forcing the fallback. [Parser selection and operands](https://raw.githubusercontent.com/arcusmaximus/VNTranslationTools/main/VNTextPatch.Shared/Scripts/Ethornell/EthornellDisassembler.cs)

## Extract and insert scenario text

The optional VNTextPatch utility is available from the archived [VNTranslationTools repository](https://github.com/arcusmaximus/VNTranslationTools). Put only the target scenario files in the original-scenario input directory, keeping relative names. These documented commands use a separate output directory:

```text
VNTextPatch extractlocal WORK/original-scenarios WORK/scenario.xlsx --format=ethornell
VNTextPatch insertlocal WORK/original-scenarios WORK/scenario.xlsx OUT/scenarios --format=ethornell
```

Retain the extracted row identities and original text; fill translations in the tool's expected fields. Keep speaker/name mappings consistent across scenarios. The format switch selects the scenario parser; it does not make arbitrary `._bp` scripts eligible inputs. [CLI and supported formats](https://raw.githubusercontent.com/arcusmaximus/VNTranslationTools/master/README.md)

The writer rebuilds the scenario string region and patches code-relative string addresses while retaining internal strings. It checks translation count and performs word wrapping during insertion. Therefore, inspect its encoding and wrapping policy before relying on it for Chinese; an XLSX containing Unicode does not establish Unicode runtime support. [Scenario writer](https://raw.githubusercontent.com/arcusmaximus/VNTranslationTools/main/VNTextPatch.Shared/Scripts/Ethornell/EthornellScript.cs)

Do not hex-replace longer strings in place. Operand offsets and string-region lengths can change; use the matching writer. Preserve code addresses, scenario names, resource references, and ordering independently from visible translation values.

## Recover text beyond dialogue

- Inspect system scripts for title menus, settings, backlog, name entry, save/load labels, and messages not returned by the scenario extractor.
- Classify strings at the consuming instruction: a filename or dispatch key remains a program dependency even if written in Japanese.
- Keep voice identifiers and message boundaries associated with the translated line. Preserve waits, markup, and control tokens unless their consuming instruction is understood.
- Trace dynamic strings and numeric formatting rather than translating reusable fragments independently. See [text resources](../text-resources.md).

## Fonts and layout are separate consumers

EthornellTools describes separate rendering calls for dialogue/name, backlog, and choices. Some releases use per-message font-size instructions and proportional-spacing configuration. Trace those consumers in the target system/scenario scripts; the documented addresses and parameters are examples for particular binaries, not universal patch offsets. [Rendering notes](https://raw.githubusercontent.com/arcusmaximus/EthornellTools/master/README.md)

Select a Chinese-capable font and compatible text encoding at the actual decoder/renderer. Preserve name-window positioning, choice hit areas, history behavior, and wrapping. Do not copy a byte patch from another release solely because both games contain BGI.exe. See [program adaptation](../program-adaptation.md).

## Images, audio, and packaging

For CompressedBG assets, keep original dimensions, alpha/masks, and any state/crop relationships while redrawing lettering. The optional encoder supports its documented proprietary image representation; a PNG preview is not an archive-ready replacement. Maintain the original resource path or update every proven consumer together. [Image encoder scope](https://raw.githubusercontent.com/arcusmaximus/EthornellTools/master/README.md)

Identify audio/video by their actual format and consuming script, retaining voice-to-line relationships, loop/timing information, and subtitles. Extraction of an archive does not establish reconstruction support or loose-file priority. Choose a release-compatible archive writer or an evidenced loader override; see [asset processing](../asset-processing.md) and [patch delivery](../patch-delivery.md).

## Compatibility limits

These tools cover specific known formats. Unsupported opcodes, custom packing, different internal VM versions, and runtime encoding changes remain separate engineering problems. A successful scenario insertion does not certify system-script, media, or package compatibility.
