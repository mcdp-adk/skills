# AliceSoft systems

## Identify the generation before choosing tools

AliceSoft is a publisher, not one file format. `ADISK.DAT` suggests an older family;
ALD scenario archives suggest System 3.x; a System 4 AIN executable with ALD/AFA assets
suggests System 4. `System39.ain` also exists in System 3.9, so `.ain` alone is ambiguous.
Confirm with file headers, executable/version information, and known title compatibility.

With an original project, use its compiler, resource tools, and asset sources. With
shipped files, preserve archive volumes and use a tool that explicitly supports the
observed version. The [xsys35c project](https://github.com/kichikuou/xsys35c) separates
its System 3.x toolchain from older `sys3c` and newer System 4 tooling; it lists titles
with exact decompile/recompile results rather than claiming every title is supported.

## System 3.x: scenario reconstruction and Unicode

In a working copy of a supported title, the documented source route is:

```text
xsys35dc . --outdir=src
xsys35c --project=src/xsys35c.cfg --outdir=rebuilt
```

First inspect the generated configuration and outputs, and establish an unchanged
rebuild. Then edit message literals while preserving commands, labels, page identity,
and function interfaces. The generated sources are reconstructed inputs, not proof
that the original authoring project or all symbolic names were recovered.

[Unicode mode](https://github.com/kichikuou/xsys35c/blob/master/docs/unicode.adoc)
uses `unicode = true` in `xsys35c.cfg` to emit UTF-8 scenarios. **Those outputs require
xsystem35 and are incompatible with the stock System 3.x runtime.** This is a
compiler-and-interpreter route, not a file-encoding-only fix. Supply a Chinese font
through xsystem35's `.xsys35rc` settings `ttfont_gothic` and `ttfont_mincho`.
Retain Japanese coverage if untranslated names or resources remain.

## System 4: edit AIN text without discarding identity

[alice-tools AIN editing](https://github.com/nunuhara/alice-tools/blob/master/README-ain.md)
separates string entries `s[id]` from message entries `m[id]`:

```text
alice ain dump -t -o text.txt Game.ain
alice ain edit -t text.txt -o translated.ain Game.ain
```

The dump starts commented out; uncomment only intended edits. Keep IDs unchanged,
and resolve repeated entries to one authoritative replacement. Strings can be
program data as well as displayed text, so inspect callers before translating them.
Translate narrative, choices, names, help text, and UI in their respective stores.
An AIN text patch does not translate external data tables or raster UI.

Determine the target AIN/runtime's encoding and font path separately. Editing tools'
UTF-8 text interfaces do not imply stock-runtime UTF-8 decoding. For a runtime port,
[xsystem4](https://github.com/nunuhara/xsystem4) has a title compatibility table;
use it as a separate dependency with title-specific behavior limits.
Use [program adaptation](../program-adaptation.md) if Chinese requires code changes.

## Images, tables, and other resources

Extract raw ALD/AFA members separately from converted previews. The archive tool's
default extraction can convert CGs and expand nested FLAT containers; `--raw`
preserves native members for a reconstruction path:

```text
alice ar list assets.afa
alice ar extract --raw -o raw assets.afa
```

For System 3.x VSP/PMS/QNT assets, [the image utilities](https://github.com/kichikuou/xsys35c/blob/master/docs/vsp.adoc)
decode to PNG and encode PNG with `-e`. Preserve stored offsets and palette metadata;
ordinary image editors may discard PNG `oFFs` chunks. For System 4 CGs and FLAT UI,
select format-aware converters/rebuilders and retain nested records, masks, and indices.

Text also occurs in `.ex` structured data and `.acx` tables. The respective
[EX](https://github.com/nunuhara/alice-tools/blob/master/README-ex.md) and
[ACX](https://github.com/nunuhara/alice-tools/blob/master/README-acx.md) routes dump,
edit, and build; preserve numeric types, table structure, and references. EX output
for games older than Evenicle needs its documented `--old` route. Prevent spreadsheet
auto-conversion from altering CSV values. Handle voices, loop metadata, movies, and
their indices as separate assets; use [media resources](../media-resources.md).

## Rebuild boundaries

Build a supported archive from an explicit manifest; preserve member identities and
the required archive version. [The archive manual](https://github.com/nunuhara/alice-tools/blob/master/README-alice-ar.md)
has an old AFAv2-only packing note, while the
[project history](https://github.com/nunuhara/alice-tools) records AFAv1 packing in 0.13.0.
Pin the actual tool's capabilities; ALD extraction does not establish ALD packing.

Deliver native replacements, an established override, or a runtime-port package with
its dependency stated. Runtime acceptance requires the intended interpreter to consume
the rebuilt scenarios/data and assets; encoding, archive packing, HLL/native calls,
font metrics, and media compatibility are independent boundaries.
