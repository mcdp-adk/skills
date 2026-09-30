# Ren'Py

Use this reference for Japanese-to-Simplified-Chinese localization of a Ren'Py source project or desktop distribution. It describes documented mechanisms, not a game-tested patch.
Sources were checked on 2026-09-30 against the official online documentation, which identifies itself as **8.5.4**; implementation links refer to upstream `master`, not the target game's bundled code. Older releases and modified engines may differ; engine upgrades can require script changes. Match the game's runtime before choosing syntax or tools. [Documentation scope and incompatible changes](https://www.renpy.org/doc/html/incompatible.html)

## Identify the runtime and available material

1. Inventory the distribution without launching it. A `game/` tree containing `.rpy`, `.rpyc`, or `.rpa` is useful evidence: Ren'Py scans it and its subdirectories for scripts and archives. Confirm with bundled Ren'Py engine files or an existing engine log, rather than an executable name alone. [Game directory](https://www.renpy.org/doc/html/language_basics.html#game-directory)
2. Record the exact engine version and game build separately. Inspect the bundled version definitions and any existing logs; current upstream resolves version data through `renpy.versions`, while older bundled code may define it directly. Trace the installed code rather than assuming a fixed filename. The documented runtime identifiers are `renpy.version_string`, `renpy.version_only`, and `renpy.version_tuple`; their existence is not a reason to launch the game during a static investigation. [Version implementation](https://raw.githubusercontent.com/renpy/renpy/master/renpy/__init__.py), [version identifiers](https://www.renpy.org/doc/html/other.html#ren-py-version)
3. Classify the material before extracting it:

| Available material | Practical starting point |
| --- | --- |
| Complete `.rpy` source and assets | Generate native translation templates using a matching SDK. |
| Creator-supplied `game/tl/<language>/` templates | Fill the supplied templates; retain their original identifiers and keys. |
| `.rpyc` with little or no `.rpy` | Compiled scripts, not an editable source project; request source/templates or investigate recovery. |
| `.rpa` archives | List their contents first; archives can contain scripts and images, so the archive extension does not establish text coverage. |

`.rpyc` is compiled script; `.rpa` is an archive. Treat extraction and decompilation as separate operations, and preserve the original resources. The build system can archive both `.rpy` and `.rpyc`. [Script compilation](https://www.renpy.org/doc/html/language_basics.html#files), [archive contents](https://www.renpy.org/doc/html/build.html#archives)

## Source project: produce native translations

Choose one language identifier, such as `schinese`, and use it consistently. The original Japanese is the `None` language; `None` does not mean English. Translation files belong under `game/tl/schinese/`. [Language naming and directories](https://www.renpy.org/doc/html/translation.html#primary-and-alternate-languages)

With source available, select the project in the matching Ren'Py Launcher and use **Generate Translations**. A matching SDK also offers the following commands; these authoring operations load project code, so use a working copy. The Windows example uses the current documented SDK layout, which is version-dependent. [Translation generation](https://www.renpy.org/doc/html/translation.html#generating-translation-files), [translation CLI](https://www.renpy.org/doc/html/cli.html#translate)

```powershell
# Run from the matching SDK directory; replace the project path.
.\lib\py3-windows-x86_64\python.exe renpy.py C:\work\game-project translate schinese
.\lib\py3-windows-x86_64\python.exe renpy.py C:\work\game-project dialogue --strings
```

`translate` creates/updates translation scripts, preserving existing translated entries. `dialogue --strings` exports a review table; it does not create translation scripts. Keep tags in the authoritative export rather than using `--notags`. [Translation and dialogue commands](https://www.renpy.org/doc/html/cli.html#translation-and-localization)

Fill generated dialogue blocks, retaining the emitted identifier, speaker, attributes, and non-text statements. Replace this schematic identifier with the one emitted for the target game's line. [Generated block format](https://raw.githubusercontent.com/renpy/renpy/master/renpy/translation/generation.py)

```renpy
translate schinese start_01234567:
    # "お帰り、[player_name]。"
    "欢迎回来，[player_name]。"
```

Ren'Py selects dialogue translations by identifier and language. IDs are derived from script structure/text unless explicitly supplied; changing source labels or dialogue can change them. Keep the original script stable during localization and retain each translation's source location. [Identifier generation and lookup](https://raw.githubusercontent.com/renpy/renpy/master/renpy/translation/__init__.py)

Menus and marked interface strings use `old`/`new` pairs instead. Include the generated `common.rpy` for engine interface strings. [Generated string format](https://raw.githubusercontent.com/renpy/renpy/master/renpy/translation/generation.py)

```renpy
translate schinese strings:
    old "続きから"
    new "继续游戏"
```

Keep `old` exact, including punctuation and contextual tags. String translations also cover dialogue without a dialogue translation. `_()` marks literals for extraction and returns them unchanged; translation happens when displayed. [String translation](https://www.renpy.org/doc/html/translation.html#menu-and-string-translations)

## Preserve text behavior and context

Retain interpolation expressions, flags, escapes, voice paths, label targets, and resource names. `[[` displays `[`, and `{{` displays `{`. Preserve `{w}`, `{p}`, `{nw}`, and `{fast}`: they affect pauses or advancement. Match paired formatting tags; retain `{#context}` keys distinguishing identical visible strings. [Escapes, interpolation, and tags](https://www.renpy.org/doc/html/text.html)

Translate complete expressions around variables. `[mood!t]` translates the substituted value; `!i` interpolates again, and `!q` quotes text tags. Keep required flags. Review Japanese ruby/furigana deliberately; its delimiters are syntax. [Text substitution and ruby](https://www.renpy.org/doc/html/text.html#interpolating-data)

Preserve character identity and scene context independently of displayed names. A translated name is not a rename of the Python variable or character object. See [text and context](../text-and-context.md) for terminology and source-to-translation records.

## Screens, Python strings, and dynamic text

Inventory `text`, `textbutton`, and `label` screen statements as well as dialogue. Screens can display variable values and generated text, so a dialogue export alone is not a complete UI inventory. Keep actions such as `Jump(...)`, `Return(...)`, and preference changes intact when changing button labels. [Screen language](https://www.renpy.org/doc/html/screens.html)

Where source edits are available, mark complete literal templates for extraction and leave values to Ren'Py interpolation:

```renpy
screen score_panel():
    text _("所持金：[money] 円")

translate schinese strings:
    old "所持金：[money] 円"
    new "持有金额：[money] 日元"
```

Text translation precedes interpolation. Prefer one stable template over concatenating fragments or formatting a number into Japanese before lookup; otherwise the lookup sees different completed strings. This is an implementation recommendation based on the documented display order. [Text processing](https://www.renpy.org/doc/html/text.html)

Search data tables and Python-built messages for unmarked literals. Marking a variable with `_()` does not turn every possible value into an extractable literal. For manual lookup, `renpy.translate_string(s)` translates immediately but does not add `s` to generated templates; enumerate its possible keys in translation material. Existing duplicate `old` entries in one language are rejected, so consolidate mappings instead of layering conflicting files. [String lookup implementation](https://raw.githubusercontent.com/renpy/renpy/master/renpy/translation/__init__.py)

## Fonts and language selection

Bundle a distributable font covering Chinese and retained Japanese/Latin/symbols; the default font lacks Chinese coverage. `gui.language` controls line breaking, not translation selection. Start with the documented `unicode` default and inspect game-specific overrides. [Non-English text](https://www.renpy.org/doc/html/text.html#non-english-languages)

For a project using the standard GUI, language-specific variables can be changed in a translation block. The font path below is an example requiring a real bundled font:

```renpy
translate schinese python:
    gui.text_font = "fonts/Chinese.ttf"
    gui.name_text_font = "fonts/Chinese.ttf"
    gui.interface_text_font = "fonts/Chinese.ttf"
    gui.button_text_font = "fonts/Chinese.ttf"
    gui.system_font = "fonts/Chinese.ttf"
    gui.language = "unicode"
```

GUI values copied during initialization, such as button fonts, may need explicit updates too. Older GUI templates use different variable names, and custom screens/styles may bypass GUI variables. Trace actual dialogue, history, input, and button styles; adjust their font/size/width at the owning style rather than assuming one assignment covers everything. [GUI translation and older names](https://www.renpy.org/doc/html/gui.html#translation-and-gui-variables)

Add these buttons inside an existing preferences screen when source/UI edits are available:

```renpy
textbutton "简体中文" action Language("schinese")
textbutton "日本語" action Language(None)
```

`Language` changes the active translation. At launch, `RENPY_LANGUAGE` precedes `config.language`, then the remembered choice, first-run autodetection/default, and finally `None`. `config.language = "schinese"` forces a launch choice; `config.default_language` is a default, so it will not supersede an existing preference. [Selection order and action](https://www.renpy.org/doc/html/translation.html#default-language)

If `config.defer_tl_scripts` is enabled, language directories load only when selected; keep definitions needing initialization outside them. `config.clear_history_on_language_change` defaults to clearing history, so a language switch need not preserve old backlog entries. [Translation configuration](https://www.renpy.org/doc/html/config.html#translation)

For localized artwork, preserve relative paths: `game/gui/title.png` becomes `game/tl/schinese/gui/title.png`. Ren'Py prefers the language-specific file when that language is active. [Translated files](https://www.renpy.org/doc/html/translation.html#image-and-file-translations)

## Shipped distributions and compatibility

Prefer creator templates or recovered readable scripts with traceable origins. A standard desktop game scans added `.rpy` scripts, making an additive translation directory a plausible patch route; custom packaging/runtime restrictions still require separate evidence. Inspect `config.archives` when multiple archives contain a resource: its list order determines the first matching archive. Do not assume a renamed archive wins. [Script discovery](https://www.renpy.org/doc/html/language_basics.html#game-directory), [archive order](https://www.renpy.org/doc/html/config.html#config.archives)

Optional archive readers/decompilers must identify their supported archive/bytecode versions and provenance. Extracting an archive does not reconstruct missing source automatically; recovered text is working material, not proof of complete coverage. Follow [resources and patching](../resources-and-patching.md) for preserving originals and defining the overlay.

When runtime work is in scope, `RENPY_LANGUAGE=schinese` plus non-empty `RENPY_UPDATE_STRINGS` can collect encountered text into `game/tl/schinese/strings.rpy`. This observed-string fallback misses unseen paths and is not a static extraction method. [Observed-string implementation](https://raw.githubusercontent.com/renpy/renpy/master/renpy/translation/__init__.py)

When renaming or removing a source script, account for its corresponding compiled file: an orphaned `.rpyc` remains executable even without `.rpy`. Preserve release `.rpyc` files before rebuilding; `old-game/` exists to carry prior compiled IDs forward during source builds and improve save compatibility. Avoid blanket deletion of compiled originals. [Orphaned scripts](https://www.renpy.org/doc/html/language_basics.html#files), [old-game directory](https://www.renpy.org/doc/html/build.html#the-old-game-directory)

Saves contain script position, displayables, screens, and changed Python state. A new translation cannot be assumed to rewrite all stored text, and structural script edits can affect resume behavior. Preserve the original engine and control flow where practical; report save compatibility as unverified until relevant runtime evidence exists. [Saved state](https://www.renpy.org/doc/html/save_load_rollback.html#what-is-saved)

During static work, finish with a source inventory, retained IDs/keys/tokens, translated resource paths, and the intended loading/selection mechanism. Separate those findings from claims about rendered Chinese, coverage during play, or old saves. Use [fonts and layout](../fonts-and-layout.md) and [quality and evidence](../quality-and-evidence.md) to define the verification scope.
