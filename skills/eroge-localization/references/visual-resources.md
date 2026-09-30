# Visual Resources

Use this reference for images, UI art, sprites, animation, and fonts. Shared asset mapping and rebuild procedures are in [Asset Processing](asset-processing.md); text-specific resource identity is in [Text Resources](text-resources.md). This file covers visual constraints that ordinary extraction and file replacement do not capture.

## Identify the image construction

Find how a displayed image is built: standalone raster, layered source, atlas entry, tiled background, vector, generated UI, or text rendered at runtime. A title logo or button label may be pixels; a dialogue window may combine texture, layout, and live text. Keep separate asset variants for route, expression, costume, hover/pressed/disabled state, screen size, and locale where the project uses them.

For lettering inside art, identify every occurrence and its complete composition before editing. Preserve the original hierarchy, contrast, placement, and surrounding illustration. If only a flattened image exists, work from a copy and keep unaffected pixels and transparency. OCR can locate candidate text but cannot confirm stylized lettering or give an editable replacement source.

## Preserve geometric and import behavior

Before exporting, retain the target canvas and any geometry referenced elsewhere: crop, nine-slice borders, margins, anchors, pivots, hit regions, sprite rectangles, trim offsets, frame order, and animation timing. Update dependent metadata through the project's importer or packer. For atlases, preserve entry IDs and settings such as rotation, padding, tight packing, and platform overrides. The packed atlas can use settings that differ from its source images; inspect its target-platform output. [Unity Sprite Atlas](https://docs.unity3d.com/Manual/class-SpriteAtlas.html)

Compare source and export for pixel dimensions, color mode, alpha convention, palette, bit depth, profile, and required compression. Check transparent edges on light and dark backgrounds for halos. Avoid repeated lossy saves; keep an editable or lossless intermediate where available. If the runtime scales multiple resolutions, regenerate them from a shared master and keep the project's selection rules.

Also preserve color-space and sampler expectations where the engine records them: gamma versus linear interpretation, filtering, mipmaps, wrap mode, and platform texture overrides can change perceived color, edge sharpness, or text legibility. Compare the imported or packed result, since source-file metadata may not carry through the build pipeline.

For animation or layered characters, retain the project’s state mapping rather than flattening interchangeable parts. Check all language-visible frames and transitions for blank frames, jumps, stale Japanese lettering, or mismatched canvas registration. A localized image should not silently replace every expression or state that shared the same original file.

## Check fonts and text layout

Trace a font to its actual renderer. Dialogue, names, menus, backlog, input, ruby, bitmap text, and plugin windows may use separate fonts or fallback rules. Determine whether an issue comes from decoding, font selection, missing glyphs, regional glyph design, shaping, or layout before changing font settings.

Build the required characters from final visible strings, punctuation, Japanese retained in the game, symbols, ruby, and runtime substitutions. Include arbitrary player input only if that behavior is in scope. A Unicode cmap check establishes character mapping, not which font the game loads or whether the glyph looks like Simplified Chinese. OpenType defines cmap lookup; fontTools exposes the selected Unicode map through TTFont.getBestCmap(). [OpenType cmap](https://learn.microsoft.com/en-us/typography/opentype/spec/cmap) · [fontTools TTFont API](https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html)

Example Python check for a known required string:

    from fontTools.ttLib import TTFont
    required = set(map(ord, "中文示例"))
    cmap = TTFont("font.otf").getBestCmap() or {}
    missing = required - set(cmap)
    print("missing:", sorted(f"U+{cp:04X}" for cp in missing))

For a bounded character set, fontTools can make missing Unicode characters a hard failure during subsetting:

    fonttools subset font.otf --unicodes-file=required-unicodes.txt --no-ignore-missing-unicodes --output-file=font-subset.otf

The subset still needs review for required layout tables and runtime compatibility; subset success does not prove font selection or visual quality. [fontTools subset options](https://fonttools.readthedocs.io/en/stable/subset/)

Codepoint coverage does not by itself validate variation selectors, combining marks, ligatures, or shaping substitutions. Include the actual sequences from the content and inspect them with the renderer and locale settings the game uses. If fallback fonts participate, check that adjacent glyphs do not change baseline, weight, or spacing unexpectedly.

Use a font design and regional glyph forms appropriate to Simplified Chinese. Check fallback, shaping, variable-font support, metrics, line height, baseline, outline, punctuation, and ruby in the target renderer. Preserve the font license and notices if distributing it. Chinese line breaking and punctuation placement should follow the project style and the renderer’s actual behavior. [W3C Chinese Layout Requirements](https://www.w3.org/TR/clreq/)

## Fit the actual control

When text overflows, identify the owning constraint: fixed canvas, text box width, padding, line height, line/page break, ruby, or substituted name. Adjust the correct asset or layout property, then recheck nearby buttons and hit regions. Avoid a global font-size change for a local control defect.

Inspect art at the target scale, display density, and background. Check button states, image-language switching, atlas selection, animation, and each affected renderer. A correct exported image can still fail through wrong import settings, stale atlas metadata, missing fallbacks, or selection of the original resource.

For an image-heavy interface, check text safe areas and localization expansion against the actual localized string. The original label width is not a reliable constraint for Chinese; ensure translated text stays inside its visual background and does not cover an icon, state marker, or input focus cue.
