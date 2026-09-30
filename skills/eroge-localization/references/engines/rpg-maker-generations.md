# RPG Maker Generations

## Distinguish the data model first

| Generation | Typical shipped evidence | Editing boundary |
| --- | --- | --- |
| XP | `Game.ini`, RGSS DLL, `.rxdata`, possibly `Game.rgssad` | Ruby-serialized database/maps and scripts |
| VX | RGSS2, `.rvdata`, possibly `Game.rgss2a` | Generation-specific Ruby data and scripts |
| VX Ace | RGSS3, `.rvdata2`, possibly `Game.rgss3a` | Generation-specific Ruby data and scripts |
| MV | `index.html`, `js/rpg_*.js`, `data/*.json` | JSON records and JavaScript/plugins |
| MZ | `index.html`, `js/rmmz_*.js`, `data/*.json` | JSON and JavaScript with MZ-specific fields and commands |

Confirm from multiple files and the actual loader; a wrapper can obscure these paths. MV deployments often put the content root in `www/`. For MZ, inspect `Utils.RPGMAKER_NAME` and `Utils.RPGMAKER_VERSION` in the supplied core. A wrapper version is not the RPG Maker version. [MZ runtime identifiers](https://developer.rpgmakerweb.com/rpg-maker-mz/Utils.html)

This guide covers the listed generations. Earlier 2000/2003 formats and title-specific replacement runtimes need their own format investigation; do not send their data through an RGSS or JSON writer.

## XP, VX, and VX Ace: preserve Ruby structures

Recover the data with an archive reader that supports the actual RGSS archive generation. Preserve raw originals and internal paths. Then select the matching data importer/writer: `.rxdata`, `.rvdata`, and `.rvdata2` are not interchangeable JSON files.

The [Ruby translator documentation](https://github.com/RPG-Maker-Translator/RPG-Maker-Translator/blob/master/3rdParty/rmxp_translator/README.txt) describes dumping database text into JSON editing files and applying it back using separate XP, VX, and VX Ace scripts. An example for VX, from a working data directory, is:

```text
ruby rmvx_translator.rb --dump=*.rvdata
```

Edit translation values, retaining their original counterparts. With a separate existing output directory, apply the edited JSON against the original data files:

```text
ruby rmvx_translator.rb --translate=*.rvdata --dest=../rebuilt
```

The writer's [argument parser](https://github.com/RPG-Maker-Translator/RPG-Maker-Translator/blob/master/3rdParty/rmxp_translator/base_translator.rb) uses `--dest` for output; the README's apply example mistakenly repeats `--dump`. The intermediate JSON is the translator's schema, not MV/MZ game data. Preserve original control files used to detect mismatches, and inspect custom Ruby scripts for UI and generated text outside ordinary database fields.

Ruby Marshal stores typed objects and references. Use the matching class definitions and serialization behavior; do not flatten objects or reconstruct an object graph from plain strings. Ruby warns that loading untrusted Marshal input can execute code, so inspect unknown distributions with suitable isolation rather than treating deserialization as inert text parsing. [Ruby Marshal](https://docs.ruby-lang.org/en/master/Marshal.html)

Keep map/event IDs, page conditions, command order, script names used as keys, and asset references. Locate compressed script entries through the generation's supported tool rather than rewriting opaque bytes. Determine whether the runtime prefers its archive over loose `Data` files before selecting the patch form; extracted replacements beside an active archive may not take effect.

Trace `Font` defaults and custom `Bitmap`/window drawing separately. A Windows-installed font is not automatically a portable patch resource; establish font registration or runtime loading for the shipped RGSS build. Images, tilesets, character sheets, windowskins, and audio retain engine-specific geometry and naming. Preserve their runtime generation rather than importing MV assets into an RGSS game.

## MV and MZ: locate the complete text set

The stock data includes actor/class/item/skill/equipment/enemy/state records, `System.json`, `MapInfos.json`, `MapNNN.json`, common events, and troop battle events. Preserve null slots, array positions, IDs, types, and object keys. Candidate display fields include names, descriptions, actor profiles, system terms, currency labels, and map display names. Author-facing names and note fields can also be program keys. [MV DataManager](https://github.com/rpgtkoolmv/corescript/blob/master/js/rpg_managers/DataManager.js)

Map commands occur in `events[id].pages[index].list`; common events have `list`, and troops have page command lists. Interpret `{code, indent, parameters}` by command type:

| Codes | Text boundary |
| --- | --- |
| `101` / `401` | Message header / lines; translate line parameter 0 and include MZ's separate speaker field |
| `102` / `402` | Choice labels / branches; preserve ordering, branch indexes, default and cancel behavior |
| `105` / `405` | Scrolling-text header / lines |
| `320`, `324`, `325` | Actor name, nickname, profile at parameter 1; actor ID remains parameter 0 |
| `108` / `408` | Comments that may be parsed by plugins |
| `355` / `655` | Executable JavaScript; only proven display literals are text |
| `356` / `357` | MV free-form / MZ structured plugin commands; retain identifiers and classify each argument |

Use the supplied handlers for customized versions. MZ added fields must not be guessed from MV array positions. [MV interpreter](https://github.com/rpgtkoolmv/corescript/blob/master/js/rpg_objects/Game_Interpreter.js), [MZ message commands](https://rpgmakerofficial.com/product/MZ_help-en/01_10_01.html), [MZ plugin commands](https://rpgmakerofficial.com/product/MZ_help-en/01_10_16.html)

Preserve message escapes such as `\V[n]`, `\N[n]`, `\P[n]`, `\G`, color/icon controls, waits and page behavior. JSON adds its own escaping layer: `"\\V[1]"` stores message text `\V[1]`. System messages also use slots such as `%1` and `%2`. Translate complete expressions while preserving the slot meanings. Plugin escape parsers can extend the stock grammar. [MV messages](https://rpgmakerofficial.com/product/MV_Help/page/01_10_01.html), [MZ terms](https://rpgmakerofficial.com/product/MZ_help-en/01_08_14.html)

Inspect enabled plugins, their order, parameters, custom data files, and UI drawing. Parameters may contain serialized JSON inside strings, and `note` tags can be parsed as metadata. Editor help translations do not translate runtime UI. Preserve each serialization layer and the plugin's lookup keys. [MV plugin specification](https://rpgmakerofficial.com/product/MV_Help/page/01_11_03.html)

## Fonts, other assets, and loading

**MV:** `fonts/gamefont.css` defines `GameFont`, but stock window font selection can choose a Chinese system-font list instead when the game's locale is Chinese. Trace `Window_Base.standardFontFace` and plugins before assuming one CSS change covers every window. [Font selection](https://github.com/rpgtkoolmv/corescript/blob/master/js/rpg_windows/Window_Base.js)

**MZ:** System 2 defines main/number font files, fallback, and size. Inspect the shipped font manager and `Game_System` accessors; do not apply MV's CSS recipe automatically. [MZ font settings](https://rpgmakerofficial.com/product/MZ_help-en/01_08_12_02.html)

For image/audio deployment encryption, select a reader and writer or an explicit supported unencrypted loading route. Changing encryption settings without converting the affected asset set can break unrelated images or audio. Preserve picture IDs, face and character sheet cells, tileset references, and animation associations. Movies and plugins can have separate resource paths. See [visual resources](../visual-resources.md) and [media resources](../media-resources.md).

Use the actual content root for replacement data and scripts. Preserve plugin order and account for wrapper archives and stale caches. Actor names and other text can be copied into runtime objects and saves; database edits may only affect newly initialized state. Do not overwrite player-authored names during migration. [MV actor initialization](https://github.com/rpgtkoolmv/corescript/blob/master/js/rpg_objects/Game_Actor.js)

Treat database loading, Chinese rendering, choice behavior, media, and claimed old-save compatibility separately under [patch delivery](../patch-delivery.md). A parsed data file establishes neither full text coverage nor runtime compatibility.
