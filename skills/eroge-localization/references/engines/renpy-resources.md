# Ren'Py Resources

## Identify scripts, archives, and runtime

Confirm Ren'Py from bundled engine files or existing logs as well as `game/` contents. Record the game's engine version separately from its release. Match authoring tools to that runtime; Ren'Py generations and custom builds can differ in Python, bytecode, and supported APIs. [Compatibility notes](https://www.renpy.org/doc/html/incompatible.html)

Distinguish readable `.rpy` source, compiled `.rpyc`, `.rpa` archives, and supplied `game/tl/<language>/` translations. Archives can contain scripts and other assets; extraction does not decompile scripts. For compiled-only distributions, use supplied templates or compatible source recovery before assuming source-based tools apply. [Script discovery and compilation](https://www.renpy.org/doc/html/language_basics.html#files), [archives](https://www.renpy.org/doc/html/build.html#archives)

## Native translation with available source

Choose one language identifier, such as `schinese`; the original language is `None`, regardless of its language. Use the matching launcher's Generate Translations operation, or the SDK's translation command. These authoring commands can load project code, so use a working copy with suitable state handling. The executable path varies by SDK; this is the documented Windows Python 3 layout:

```powershell
.\lib\py3-windows-x86_64\python.exe renpy.py C:\work\game-project translate schinese
.\lib\py3-windows-x86_64\python.exe renpy.py C:\work\game-project dialogue --strings
```

`translate` generates translation scripts; `dialogue --strings` exports review material and is not a translation importer. Preserve existing edited entries and generated IDs. [Translation CLI](https://www.renpy.org/doc/html/cli.html#translation-and-localization)

Dialogue blocks use generated identifiers, while menu and interface translations use exact `old`/`new` keys. Include applicable common-interface translations. Replace the illustrative identifier below with the target's generated one:

```renpy
translate schinese start_01234567:
    "欢迎回来，[player_name]。"

translate schinese strings:
    old "続きから"
    new "继续游戏"
```

Keep dialogue speakers, attributes, and non-text statements. Source label/text changes can change translation identifiers, so avoid restructuring source while maintaining translations. Preserve original lookup keys including contextual tags. [Translation model](https://www.renpy.org/doc/html/translation.html), [identifier implementation](https://github.com/renpy/renpy/blob/master/renpy/translation/__init__.py)

## Screens and assembled expressions

Inspect screen `text`, `textbutton`, and labels, Python-generated messages, and data tables in addition to dialogue. Translate labels without altering actions such as `Jump`, `Return`, or preference changes. `_()` marks literal strings for extraction; wrapping a variable does not enumerate every value it may contain. [Screen language](https://www.renpy.org/doc/html/screens.html)

Keep complete templates, for example `_("所持金：[money] 円")`, and translate them as complete expressions. Translation precedes interpolation. Preserve substitutions and their flags, including `!t` for translating a substituted value, and context keys such as `{#context}`. Retain paired markup and timing tags such as `{w}`, `{p}`, `{nw}`, and `{fast}`. Literal `[` and `{` use `[[` and `{{`. [Text processing](https://www.renpy.org/doc/html/text.html)

Immediate calls to `renpy.translate_string` do not make dynamic strings statically discoverable. Inventory their possible keys separately. Keep speaker identity distinct from displayed name strings; see [text resources](../text-resources.md).

## Fonts, artwork, and media

For standard GUI projects, language-specific GUI variables can select the bundled Chinese font. Trace the actual styles because custom screens and older templates may bypass these variables:

```renpy
translate schinese python:
    gui.text_font = "fonts/Chinese.ttf"
    gui.name_text_font = "fonts/Chinese.ttf"
    gui.interface_text_font = "fonts/Chinese.ttf"
    gui.button_text_font = "fonts/Chinese.ttf"
    gui.system_font = "fonts/Chinese.ttf"
    gui.language = "unicode"
```

The font file must exist with the required glyphs. `gui.language` selects line-breaking behavior, not the translation language. Check dialogue, input, history, ruby, and button geometry independently. [GUI translation](https://www.renpy.org/doc/html/gui.html#translation-and-gui-variables)

Language-specific files retain relative resource paths: `game/gui/title.png` can have a counterpart at `game/tl/schinese/gui/title.png`. Preserve the original reference so the language-aware loader can select the alternate. Check image layers, animation, and image-backed UI through [visual resources](../visual-resources.md). For voice or movies, establish that the playback path uses translated-file lookup and retain cue/channel associations; handle codec and duration constraints separately through [media resources](../media-resources.md). [File translation](https://www.renpy.org/doc/html/translation.html#image-and-file-translations)

## Selection and patch loading

An existing preferences screen can expose `Language("schinese")` and `Language(None)`. Distinguish a forced startup `config.language` from a first-run `config.default_language`; remembered preferences and `RENPY_LANGUAGE` also affect selection. A populated translation directory does not prove it is selected. [Language selection](https://www.renpy.org/doc/html/translation.html#default-language)

Standard distributions discover added scripts, so additive translation files are a possible route. Inspect custom packaging and `config.archives` before relying on that route; archive list order controls which matching entry wins. If renaming or removing source, account for an orphaned `.rpyc`, which can still execute. Preserve original compiled files; source builds can use `old-game/` to retain earlier script IDs. [Archive order](https://www.renpy.org/doc/html/config.html#config.archives), [old-game](https://www.renpy.org/doc/html/build.html#the-old-game-directory)

Runtime string collection, where supported by `RENPY_UPDATE_STRINGS`, only finds encountered strings; it is not whole-game static extraction. Saves also retain script positions and Python state. Treat script changes, saved text, replay, rollback, and language switching as separate compatibility questions in [patch delivery](../patch-delivery.md). [Saved state](https://www.renpy.org/doc/html/save_load_rollback.html#what-is-saved)
