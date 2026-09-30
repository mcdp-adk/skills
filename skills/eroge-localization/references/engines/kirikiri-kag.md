# Kirikiri / KAG

## Identify the runtime and script layer

An XP3 archive suggests Kirikiri; it does not identify the game's scenario language.
Look inside a recognized archive for `startup.tjs`, `.tjs`, `.ks`, and the startup
imports. KAG commonly has `system/Config.tjs` and `scenario/first.ks`; custom TJS
systems may use different text stores and renderers. Record the executable version,
KAG version if present, and native plugins before selecting a route.

Kirikiri 2, Kirikiri Z, and modified commercial runtimes are separate compatibility
targets. The [KAG project documentation](https://krkrz.github.io/krkr2doc/kag3doc/contents/Prepare.html)
describes the traditional layout, not every Kirikiri game. Its Unicode guidance is
UTF-16LE with a BOM; [Kirikiri Z's script loader](https://github.com/krkrz/krkrz/blob/master/base/ScriptMgnIntf.cpp)
also has configurable read encoding. Determine the actual loader rather than treating
all `.ks` or `.tjs` files as UTF-8.

## Obtain editable inputs

- **Project available:** use its scenarios, TJS system, source images, font setup,
  media, and release profile. Keep the title's existing native plugins and loader.
- **Shipped game only:** inventory all XP3 archives, appended executable data, and
  loose files. Preserve both archive membership and internal paths when extracting.
  [GARbro](https://github.com/morkt/GARbro) can browse recognized variants and extract
  resources; game-specific encryption support depends on its format implementation.
  Keep raw extraction separately from converted previews.

An unreadable archive, unknown filter, or compiled/encrypted TJS is a missing input
capability. An extracted scenario is useful only after its route back into the
target loader is established. Use [asset processing](../asset-processing.md) for
the source-to-output mapping, particularly when several archives contain one name.

## Edit scenarios and system text

1. Follow the startup imports to the scenario parser and locate the display call.
   Collect literal dialogue, speaker labels, choices, backlog headings, and menu
   strings; custom macros can carry text in attributes rather than plain lines.
2. Associate each passage with file, label, occurrence, and nearby voice/image tags.
   Keep TJS expressions, variable names, storage names, and jump targets intact.
3. Translate display text with a parser that distinguishes plain text, `[tag]`,
   `@command`, labels, comments, and `[iscript]` blocks. A `&` attribute value is an
   evaluated TJS expression. These distinctions come from the
   [KAG tag reference](https://krkrz.github.io/krkr2doc/kag3doc/contents/Tags.html).
4. Preserve the meaning of `[r]`, `[l]`, and `[p]`; decide Chinese line wrapping from
   the message layer instead of converting editor line endings into new pauses.
   KAG 3's treatment of source newlines differs from older KAG.
5. Serialize using the verified decoder's accepted format. Inspect an encoded
   Chinese sample for loss before packaging; re-encoding does not change a decoder.

For custom TJS systems, extract text from the title's data structures or text API.
Treat code literals used in comparisons as program data until their callers are known.
Use [text resources](../text-resources.md) for identities and encoding decisions.

## Images, UI, fonts, and media

Image-backed buttons, title screens, and CG lettering need raster edits. Keep canvas,
alpha, offsets, masks, and animation frame relationships; a transition rule image is
control data, not a translation surface. For TLG assets, establish both decode and
encode support, or change the storage reference to a supported PNG when the title's
loader permits it. Renaming PNG bytes to `.tlg` is not a format conversion.

Adjust message geometry, font face, size, and ruby behavior in the title's configuration
and macros. If `mappfont` maps a face to a prerendered `.tft`, rebuild that font with
`krkrfont.exe` for the Chinese character set or revise the mapping to a valid live
font. A new OS font alone may leave the prerendered mapping active.

Voice replacements retain their scenario bindings. Track loop metadata and event
timing when replacing audio; video must remain compatible with the exact runtime
and plugins. Traditional KAG documents archive videos as uncompressed entries.
Keep animation descriptions and other asset metadata alongside their images.
See [visual resources](../visual-resources.md) and [media resources](../media-resources.md).

## Rebuild or override

With a project, [Releaser](https://krkrz.github.io/docs/kirikiriz/j/contents/Releaser.html)
creates standard XP3 or an executable with embedded data. Preserve a compatible
release profile and package a staging directory; for a standard supported project:

```text
krkrrel project -out ..\release\data.xp3 -nowriterpf -go
```

For a shipped title, inspect its startup storage registration before selecting a
patch archive or loose override. `patch.xp3` is a convention used by some systems,
not a universal precedence rule. Match the original internal storage name and verify
which archive wins. An encrypted original does not imply that an unencrypted patch
will be accepted. The [storage documentation](https://krkrz.github.io/docs/kirikiriz/j/contents/StorageSystem.html)
defines names such as `game.xp3>image/base.jpg`; it does not define every game's policy.

A patch's runtime acceptance requires the target loader to consume its replacements
and retain choice, backlog, and media behavior. Native menu strings, compiled code,
custom protection, and plugin-specific formats may need [program adaptation](../program-adaptation.md).
