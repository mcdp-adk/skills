# RealLive and AVG2000: Scenario Bytecode

Use this reference for a confirmed RealLive/AVG2000 distribution. A scenario archive often named `Seen.txt` and numbered entries are investigation clues; identify the runtime and modified formats separately.

## Select compatible tools

[RLdev](https://github.com/eglaysher/rldev) supplies scenario/archive utility `kprl`, compiler `rlc`, and image converter `vaconv`. Retain its accompanying function definitions with the tool build. [Toolkit README](https://raw.githubusercontent.com/eglaysher/rldev/master/README)

Resolve which executable consumes the scenario data before choosing a compilation target. Keep extracted source, resource identifiers, and scenario numbers associated. A reconstructing disassembler does not recover the original project or establish a faithful compiler round trip.

## Recover and reinsert a scenario

The manual distinguishes `kprl -d` disassembly from `-x` bytecode decompression. For a confirmed RealLive target, these templates illustrate source extraction, compilation, and updating a copied archive:

```text
kprl -d -e utf-8 -o WORK/disassembled ORIGINAL/Seen.txt
rlc -e utf-8 -t reallive -f ORIGINAL/RealLive.exe -i ORIGINAL/Gameexe.ini -o WORK/seen0001.txt WORK/disassembled/seen0001.ke
kprl -a OUT/Seen.txt WORK/seen0001.txt
```

Substitute the actual source and scenario number. Retain included resources beside the source and prepare `OUT/Seen.txt` as a copy first. `-a` modifies that archive. `-f` reads the executable version, but a source `#version` can override it. Use the correct `avg2k`, `reallive`, or `kinetic` target; autodetection can misclassify Kinetic. RLdev documents incomplete code-generation coverage. [RLdev manual](https://github.com/eglaysher/rldev/blob/master/Manual.html)

Inspect reconstructed instructions before translating. Retain unsupported instructions through a proven structural writer or obtain suitable source; deleting them to achieve compilation changes the game. Rebuild a representative unchanged scenario before investing in a large edited corpus when implementation verification is in scope.

The archive writer updates a fixed index of scenario entries. Use its insertion operation rather than concatenating translated bytecode or hex-replacing longer strings. [Archive implementation](https://raw.githubusercontent.com/eglaysher/rldev/master/src/kprl/archiver.ml)

## Text decoding and coverage

UTF-8 editable source does not make the runtime Unicode. RLdev's Chinese output transform uses a nonstandard GB2312-based mapping requiring matching interpreter changes or a compatible rlBabel extension. Font substitution cannot supply that decoder. [Encoding and extension model](https://github.com/eglaysher/rldev/blob/master/Manual.html)

Trace translated content through the actual decoder and renderer. Keep language expression, control syntax, speaker transition, voice cue, and scenario destination distinct. Classify configuration strings by their consumers: a title is display text, while a resource path or function key can be program identity.

Follow generated phrases and comparison operands separately from dialogue literals. Check whether choices, backlog, name input, and system UI use the same text path. Use [program adaptation](../program-adaptation.md) where the existing decoder or display boundary cannot represent the target language.

## Images and media

`vaconv` supports PDT/G00/PNG conversion. Preserve emitted masks and G00 XML/cut metadata; converting pixels alone loses reconstruction information. [Image conversion options](https://github.com/eglaysher/rldev/blob/master/Manual.html)

Keep button states, cut placement, alpha, and image paths with the edited art. Trace audio and video through their scene commands, including voice numbering, loops, waits, and transitions. An image converter says nothing about archive packing or media encoding; use [visual resources](../visual-resources.md) and [media resources](../media-resources.md) for those constraints.

## Deliver through the actual loader

Select a supported archive replacement or demonstrated loose-scenario route; extraction does not establish lookup precedence. Record the chosen runtime and any required extension with the patch. Custom opcodes, encryption, unsupported decoding, and incomplete source reconstruction are distinct gaps. Apply [patch delivery](../patch-delivery.md) to the observed loading and compatibility scope.
