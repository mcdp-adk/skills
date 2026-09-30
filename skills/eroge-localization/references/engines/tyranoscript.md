# TyranoScript

## Locate the web project and its version

Look for `index.html`, the `tyrano/` runtime, `data/scenario/*.ks`, and configuration
such as `data/system/Config.tjs`. Inspect the runtime's version and custom plugins.
TyranoScript shares KAG-like tags but executes in a JavaScript/HTML environment;
Kirikiri archive and TJS procedures do not transfer automatically.

With a project, edit its scenarios, runtime configuration, and original assets.
With a shipped desktop package, first locate the packaged web application: a wrapper
may expose files directly or contain them in its own archive. Recovering those files
does not recreate the author's TyranoBuilder editing project. Identify packaging
and its write path separately from scenario localization.

## Native translation tables where available

The [official localization feature](https://tyranoscript.com/usage/advance/translate)
requires **TyranoScript V600 or later**. The same page offers a plugin for versions
before V530; it does not establish support for every intervening or custom version.
For supported projects, create a language in TyranoStudio's Development > Translation,
select scenarios, edit entries, and save or use its CSV import/export.

Register text-bearing tag parameters, including custom macro parameters; otherwise
the extractor can omit captions even when it collects dialogue. Preserve extracted
identities and review regenerated tables when scenarios change.

Choose a project language code, for example `zhcn`, and use that same value in tables,
language selection, and conditional assets:

```text
[lang_set name="zhcn"]
```

This code is an application identifier, not automatic locale negotiation. Map browser
language values and saved user preferences explicitly. The official example's `ch`
is also an example identifier, not a requirement for Simplified Chinese.
Keep character-name translations distinct from scenario passages.

## Direct scenario and UI editing

For an older runtime or a single-language build, edit display literals in scenarios
and title-specific macros. Preserve labels, branch expressions, storage references,
variables, and `[iscript]` JavaScript. Track choices and menu text separately from
plain dialogue. Use [text resources](../text-resources.md) for occurrence identities.

Tyrano renders text through layers and HTML/CSS. Translate the display values of
tags such as `glink` and `ptext`, then inspect system screens, HTML templates, CSS,
and JavaScript-generated text. A translated scenario does not cover a menu assembled
by a custom plugin. Keep markup and escapes valid in the actual consuming context.

Adjust message area, font metrics, margins, and ruby treatment alongside translation.
The [V6 tag reference](https://tyranoscript.com/tag/) documents font face selection and
web-font use. Define the font in the title's CSS, ensure the shipped font covers the
Chinese corpus, and reference the defined family. An installed development-machine
font alone is insufficient for a portable build.

## Images and language-dependent assets

Keep image-backed choices, title graphics, and CG lettering in the asset inventory.
Preserve dimensions, alpha, and click geometry. Tyrano's
[background tutorial](https://tyranoscript.com/usage/tutorial/back) uses `data/bgimage`
and the `storage` attribute. For a native-language project, an explicit branch can
select a translated image without changing the Japanese asset:

```text
[if exp="TYRANO.kag.lang==='zhcn'"]
[bg storage="room_zhcn.jpg" time=3000]
[else]
[bg storage="room.jpg" time=3000]
[endif]
```

Use the actual tag's resource directory; backgrounds, foreground images, UI graphics,
and custom plugin assets may resolve differently. Keep localized files and the branch
that selects them together. See [visual resources](../visual-resources.md) for image
editing and [asset processing](../asset-processing.md) for mapping source to deployment.

## Media, packaging, and limits

Retain voice/audio storage references and cue timing. Video tags resolve their own
media directory and depend on the shipped browser or desktop wrapper's codecs.
For translated opening movies, preserve dimensions and duration or revise dependent
wait/cue logic. External subtitle files need an implemented subtitle consumer;
placing an SRT beside a movie does not connect it to a Tyrano movie tag.

Build or export from the available project using its established route, or replace
recognized package members with a compatible writer. Preserve relative URLs and
filename case; test cache behavior, local-file restrictions, and font loading in
the intended wrapper/browser. Native translation tables do not translate raster
assets, custom JavaScript, or video lettering automatically. These remain explicit
resource or program changes, even when language switching is already working.
