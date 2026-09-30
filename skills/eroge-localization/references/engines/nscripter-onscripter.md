# NScripter / ONScripter

## Runtime families determine the route

Typical inputs include `0.txt`, numbered text scripts, `nscript.dat`, `arc.sar`,
`arc*.nsa`, or `.ns2` archives. Identify the actual executable and script dialect;
an NScripter-derived archive is not evidence of Unicode or command compatibility.
Distinguish stock NScripter, Studio OGA's ONScripter, ONScripter-EN, PONScripter,
and title-specific builds. Keep the executable version with the translation format.

[ONScripter's maintainer documentation](https://ogapee.github.io/www/onscripter_en.html)
explicitly describes incomplete command compatibility. A replacement interpreter
can change DLL calls, movie playback, text behavior, and saves. Its Unicode font
requirement concerns font rendering, not a promise that scripts accept UTF-8.
Establish a decoder and glyph path capable of the target text. A font substitution
cannot repair text decoded as the wrong code page.

## Script recovery and editing

With source, retain script files and their concatenation order. With a shipped game,
identify the script container before using a decoder: standard `nscript.dat` and
modified/encrypted variants need different handling. The historical
[insani utility catalog](https://nscripter.insani.org/sdk.html) identifies NSDec for
script recovery, NSAOut/SARDec for resources, `nscmake` for script output, and
`nsaarc` for NSA packing. These are distinct capabilities and old releases, not a
general decoder for newer title-specific formats.

1. Recover readable text without changing bytes in place; preserve the original
   script and determine its encoding from the parser and a round trip.
2. Map text by script, label, occurrence, and nearby commands. Distinguish prose
   from quoted arguments used as filenames, control strings, or comparisons.
3. Translate dialogue, name strings, choice captions, save/menu messages, and other
   display arguments. Preserve labels, `%`/`$` variables, array references, command
   separators, and quoting. Map voice commands to the corresponding translated line.
4. Preserve click waits and page boundaries, including dialect-specific `@` and `\`
   markers. A text parser must handle command arguments as well as dialogue lines.
5. Emit source or a recognized encoded container accepted by the selected runtime.
   Use `nscmake` only for its supported standard script format; packaging a script
   does not add decoding for the target language or change command semantics.

If the intended runtime cannot represent the target language, choose an explicit compatible
interpreter adaptation or a documented title-specific encoding modification.
Treat that choice as a changed runtime dependency. Use
[text resources](../text-resources.md) for encoding and stable passage identities.

## Resource archives and loose overrides

List every archive, including numbered volumes, and preserve referenced relative
paths. Maintain raw resources as rebuild inputs and converted files as editing
inputs. Some images are compressed inside NSA with SPB/NBZ or other methods;
an exported BMP/PNG is not automatically the original archive payload.

For the current upstream ONScripter NSA reader,
[the implementation](https://github.com/ogapee/onscripter/blob/master/NsaReader.cpp)
checks direct files before NSA/NS2 archive entries. A same-path loose replacement
is therefore a possible route for that reader. Verify the corresponding SAR reader,
fork, or stock executable separately; filenames and patch-volume order vary.

For rebuilding, use a writer that supports the archive version and compression
required by the title, with exact resource paths. `nsaconv` is documented primarily
as an archive/image resizing converter; its presence does not establish a general
edited-directory-to-archive route. Extraction and packing must be selected separately.

## Text layout and nontext resources

Inspect `setwindow` and title macros for character grid, font size, spacing, and
line count. Check choice hit regions and name/backlog rendering separately.
ONScripter supports `default.ttf` beside the scripts or an explicit font argument;
use a licensed font covering the target text with predictable metrics. The following
documented command uses a Chinese font path; it selects inputs and font rather than
rewriting scripts:

```text
onscripter --root staging --font staging/fonts/Chinese.ttf
```

Image buttons and sprites may encode multiple cells or combine color and mask data.
Edit lettering without changing the cell count, dimensions, alpha convention, or
button geometry. Translate text assets and raster UI separately; use
[visual resources](../visual-resources.md) for mask and atlas handling.

Preserve audio channel bindings, loop behavior, and the timing of wait commands.
CD-track emulation and MP3/Ogg/WAV support are interpreter/build-specific. Movie
commands may rely on optional libraries or unavailable original DLL behavior.
Replacing voice or video therefore requires its own supported encode/playback path;
an interpreter that displays translated dialogue may still fail media playback.

Runtime acceptance means the selected interpreter actually consumes the translated
text and assets, renders the target language, and preserves route and replay behavior.
Save compatibility, native DLL integration, and unsupported commands remain distinct
gaps; record them rather than describing an interpreter port as a drop-in patch.
