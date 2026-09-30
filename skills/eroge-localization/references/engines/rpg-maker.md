# RPG Maker MV / MZ localization reference

Use this reference for Japanese-to-Simplified-Chinese work on an MV or MZ distribution. These stock-engine facts were researched on 2026-09-30; custom loaders and plugins can change them. The supplied game's loader and scripts resolve game-specific differences.

## Identify the runtime and the editable boundary

- Locate the game content root through `index.html`, its script references, and the desktop wrapper's `package.json` entry point. MV distributions commonly place content in `www/`; editor projects and some distributions place it directly beside `index.html`. Keep patch paths relative to the observed root.
- MV uses `js/rpg_core.js`, `rpg_managers.js`, `rpg_objects.js`, `rpg_scenes.js`, `rpg_sprites.js`, and `rpg_windows.js`; `js/plugins.js` lists plugins and `js/main.js` starts the game. The official [MV bootstrap][mv-bootstrap] shows the load chain.
- For MZ, look for the corresponding `js/rmmz_*.js` files and the runtime constants `Utils.RPGMAKER_NAME` and `Utils.RPGMAKER_VERSION`. These constants identify the loaded core; the [MZ API][mz-utils] documents them. Read their source declarations during investigation.
- Record the product, runtime version, and relevant file hashes separately. A custom core can keep an old version string, and a wrapper/NW.js version identifies the host rather than the engine.
- `Game.rpgproject` identifies an MV editor project; `game.rmmzproject` identifies an MZ editor project. Their absence in a shipped game does not disprove the runtime. The [MV menu][mv-menu] and [MZ menu][mz-menu] distinguish opening a project from deployment; MZ also supports updating a project's core independently.
- Native deployment encryption concerns image/audio assets; it does not establish that JSON or JavaScript is encrypted. Wrappers can additionally package files. Keep resource access and packaging decisions in [resources and patching](../resources-and-patching.md). [MV deployment][mv-deploy], [MZ deployment][mz-deploy]

## Text locations and structural boundaries

The stock MV loader reads `data/Actors.json`, `Classes.json`, `Skills.json`, `Items.json`, `Weapons.json`, `Armors.json`, `Enemies.json`, `Troops.json`, `States.json`, `Animations.json`, `Tilesets.json`, `CommonEvents.json`, `System.json`, and `MapInfos.json`; maps use `data/MapNNN.json`, with IDs padded to at least three digits. MZ uses the same principal data filenames, but its shipped loader remains authoritative for additions and schema differences. [MV DataManager][mv-data]

| Location | Candidate display text | Keep structural or consumer-dependent values intact |
| --- | --- | --- |
| `Actors.json` | `name`, `nickname`, `profile` | `id`, `classId`, equipment, image filenames and image indices. [Actor schema][actor] |
| `Skills.json` | `name`, `description`, `message1`, `message2` | Skill/type IDs, effects, costs and formulas. [Skill schema][skill] |
| Items, weapons, armor, enemies, classes, states | Player-facing names, descriptions and state messages where present | Numeric parameters, traits and references; classify fields by use rather than translating every string |
| `System.json` | `gameTitle`, `currencyUnit`; entries in `elements`, `skillTypes`, `weaponTypes`, `armorTypes`, `equipTypes` | Preserve positions and IDs in type arrays, including empty sentinel entries. [System schema][system] |
| `System.json.terms` | `basic`, `params`, `commands`, values in `messages` | Object keys such as `victory`; placeholders such as `%1`, `%2`. [Terms schema][terms], [MZ terms][mz-terms] |
| `MapNNN.json` | `displayName`; event dialogue below | Tile `data`, dimensions, event IDs/pages/conditions, transfer targets, image/audio names. [Map schema][map] |
| `MapInfos.json` | `name` only if it reaches the player's UI | Ordinarily map-tree metadata; preserve `parentId`, order and array slots. [MapInfo schema][mapinfo] |
| `CommonEvents.json` | Commands in each event's `list` | `id`, `switchId`, `trigger`; event `name` can be an author label or a plugin lookup key. [CommonEvent schema][common] |
| `Troops.json` | Battle-event page command lists | Members, enemy IDs, placement and page conditions |

Database entries and map events may use null array slots; keep them. Preserve JSON types, field names, IDs, array order and command order. Names that look like display text may also be compared by scripts: check such consumers before renaming them. A parsed JSON file is structurally readable, not automatically behaviorally safe to edit.

Map dialogue is under `events[eventId].pages[pageIndex].list`; common-event dialogue under `[commonEventId].list`; battle dialogue under `[troopId].pages[pageIndex].list`. An event command is `{code, indent, parameters}`; each `code` determines parameter meaning. [EventPage schema][page], [EventCommand schema][command]

## Event commands: translate payloads, preserve control flow

This table is grounded in the [MV interpreter][mv-interpreter]. For MZ, confirm the named handlers in the supplied `rmmz_objects.js`; plugin overrides can intercept them.

| Code | Meaning and localization boundary |
| --- | --- |
| `101` + `401` | Show Text header followed by text lines; translate `401.parameters[0]`, retaining the header's face/background/position settings |
| `102` + `402` | Choice labels in `102.parameters[0]`; retain order, branch index in `402.parameters[0]`, cancel/default settings and nesting |
| `105` + `405` | Scrolling-text settings followed by lines; translate `405.parameters[0]` |
| `320`, `324`, `325` | Actor name, nickname, profile: actor ID stays at parameter 0; textual value is parameter 1 |
| `108` / `408` | Comments and continuations: inspect plugin interpretation before changing |
| `355` / `655` | JavaScript and continuation: edit proven display literals while preserving executable syntax |
| `356` | MV plugin-command string: command/argument tokens can be identifiers |

MZ Show Text adds a speaker Name field; include it in extraction, independently from dialogue. Its Plugin Command chooses a plugin, command and arguments rather than MV's free command string. Inspect `command101` and `command357` for that distribution's serialized positions; retain plugin/command identifiers and translate only arguments proven to be display text. [MZ messages][mz-messages], [MZ advanced commands][mz-advanced]

Illustrative JSON fragment: only the dialogue changes; `code`, `indent` and variable reference remain intact.

| Version | Command object |
| --- | --- |
| Before | `{"code":401,"indent":0,"parameters":["所持金は\\V[1]です。"]}` |
| After | `{"code":401,"indent":0,"parameters":["现有金钱为\\V[1]。"]}` |

Do not insert or remove command objects merely to reflow Chinese. A line boundary, message boundary and branch boundary are different things. Reflow inside the existing message's text payloads first; page restructuring is a separate adaptation with control-flow implications.

## Escape codes and assembled text

| Stock message syntax | Preserve its role |
| --- | --- |
| `\V[n]`, `\N[n]`, `\P[n]`, `\G` | Variable value, actor name, party-member name, currency unit |
| `\C[n]`, `\I[n]`, `\{`, `\}` | Color, icon, larger/smaller text |
| `\\` | Literal backslash in the rendered message |
| `\$`, `\.`, `\|`, `\!`, `\>`, `\<`, `\^` | Gold window, timing, input waits and message display behavior |
| MZ `\PX[n]`, `\PY[n]`, `\FS[n]` | Text position and explicit font size; retain or deliberately adapt layout values |

The official [MV messages][mv-messages] and [MZ messages][mz-messages] define the stock escapes. Preserve ASCII backslashes/brackets and numeric arguments; Chinese punctuation must not replace control syntax. JSON `"\\V[1]"` represents message text `\V[1]`; escaping inside JavaScript introduces its own layer. Plugin escape codes require their actual parser's rules.

`%1`, `%2`, etc. in system messages are substitution slots. Translate the full template with each slot's meaning, then preserve the required slots. A hypothetical `%1を手に入れた！` can become `获得了%1！`; actual wording depends on what `%1` supplies. [MZ terms][mz-terms]

Follow dynamic text to its inputs: variable assignments, actor renaming, item names, template substitutions, concatenated JavaScript literals, choice generators and custom UI renderers. Translate display fragments with their assembled sentence in mind. For example, changing a variable's string without checking a later equality comparison can change a branch.

MZ official `TextScriptBase` can keep strings/scripts in plugin parameters and insert them with `\tx[...]` / `\js[...]`; `TextPicture` can render text through pictures; `UniqueDataLoading` can load additional JSON. These are concrete reasons why event dialogue alone is incomplete. Their identifiers and executable expressions remain logic. [Official MZ plugins][mz-plugins]

## Plugins, scripts and patch placement

- Plugin files live in `js/plugins/`; `js/plugins.js` supplies names, enabled status and configured parameters. Runtime parameters are strings in MV; plugins may parse serialized arrays/objects inside those strings. Preserve keys, parse each applicable layer, replace display values and serialize back at the same layers. [MV plugin specification][mv-plugin-spec]
- Plugin `@help`, `@desc` and editor-language comment blocks describe the editor interface; changing them does not translate the released game's runtime UI. `@param` names, plugin filenames and command names can be lookup keys. Trace the consuming code before changing a value. [MV plugin specification][mv-plugin-spec]
- `note` is not an unrestricted prose field: stock metadata parsing turns `<name:data>` into `meta.name`. Plugins can also parse comments, event names and raw notes themselves. Translate only known display-bearing values; retain tag names and delimiters. [MV DataManager][mv-data], [MV plugin specification][mv-plugin-spec]
- Retain enabled-plugin order. The stock MV manager loads enabled scripts in list order; method replacement/aliasing means later plugins can change earlier behavior. Place an adaptation after the specific implementation it extends when that dependency is established, and retain the original method's contract. [MV PluginManager][mv-plugin-manager]
- A minified bundle is still executable code. Prefer a supported text/configuration entry point or a small isolated adaptation when available; if direct bundle editing is necessary, change identified literals only, preserve syntax and record the exact original file/version. Compressed or encrypted containers require a separate known packaging path; readable source and opaque payloads are different boundaries.

## Chinese fonts and layout: MV and MZ differ

**MV:** `index.html` links `fonts/gamefont.css`; stock CSS registers `GameFont` from `mplus-1m-regular.ttf`. A bundled Chinese font can retain the `GameFont` family and change the CSS file URL. [MV bootstrap][mv-bootstrap], [MV font CSS][mv-font]

```css
@font-face {
  font-family: GameFont;
  src: url("zh-hans.ttf");
}
```

MV stock `Window_Base.standardFontFace()` chooses `SimHei, Heiti TC, sans-serif` when the system locale is Chinese and otherwise normally chooses `GameFont`; `resetFontSettings()` applies it to window contents. Changing locale can therefore bypass the bundled `GameFont`. Trace the actual font selection and plugin overrides before deciding whether CSS, a font-selection adaptation, or both are required. [MV Window_Base][mv-window], [MV Game_System][mv-system-runtime]

**MZ:** System 2 exposes Main Font Filename, Number Font Filename, Fallback Font and Font Size. Use the supplied build's configuration/loading path rather than copying MV's CSS recipe. For a runtime adaptation, inspect `Scene_Boot.loadGameFonts`, `FontManager.load`, `$dataSystem.advanced` and `Game_System.mainFontFace` / `numberFontFace` in the shipped scripts; these are targeted inspection points, not a promise about every customized build's implementation. [MZ System 2][mz-font]

Glyph coverage does not determine fit. Chinese dialogue, choices, item/help windows, name boxes, battle messages and plugin overlays can each use different metrics or rendering paths. See [fonts and layout](../fonts-and-layout.md) for fitting and font delivery decisions; preserve picture filenames even when translating picture-rendered text.

## Save semantics and evidence limits

MV separates JSON-backed `$data...` resources from runtime `$game...` objects. Save contents include system, switches, variables, self-switches, actors, party, map and player objects; actor setup copies database name/nickname/profile into runtime fields. An existing save can therefore retain Japanese actor text after `Actors.json` changes. Preserve player-authored names and state when designing any migration. [MV DataManager][mv-data], [MV Game_Actor][mv-actor-runtime]

MV's stock local saves use compressed `.rpgsave` files; browser storage uses separate keys. Save location depends on the wrapper and runtime, so copying the game folder does not prove save isolation. For MZ, inspect the supplied `StorageManager` and plugin overrides rather than assuming MV's formats or location. [MV StorageManager][mv-storage]

When patch verification is in scope, distinguish new-game initialization from loading existing state and record each verified path. Stock-engine knowledge does not establish a particular game's text coverage, save compatibility or Chinese rendering quality. Keep context records in [text and context](../text-and-context.md), and evidence scope in [quality and evidence](../quality-and-evidence.md).

[mv-bootstrap]: https://github.com/rpgtkoolmv/corescript/blob/master/template/index.html
[mv-menu]: https://rpgmakerofficial.com/product/MV_Help/page/01_04.html
[mz-menu]: https://rpgmakerofficial.com/product/MZ_help-en/01_04.html
[mz-utils]: https://developer.rpgmakerweb.com/rpg-maker-mz/Utils.html
[mv-deploy]: https://rpgmakerofficial.com/product/MV_Help/page/01_11_04.html
[mz-deploy]: https://rpgmakerofficial.com/product/MZ_help-en/01_11_03.html
[mv-data]: https://github.com/rpgtkoolmv/corescript/blob/master/js/rpg_managers/DataManager.js
[actor]: https://rpgmakerofficial.com/product/MV_Help/page/03_22.html
[skill]: https://rpgmakerofficial.com/product/MV_Help/page/03_48.html
[system]: https://rpgmakerofficial.com/product/MV_Help/page/03_50.html
[terms]: https://rpgmakerofficial.com/product/MV_Help/page/03_52.html
[mz-terms]: https://rpgmakerofficial.com/product/MZ_help-en/01_08_14.html
[map]: https://rpgmakerofficial.com/product/MV_Help/page/03_43.html
[mapinfo]: https://rpgmakerofficial.com/product/MV_Help/page/03_45.html
[common]: https://rpgmakerofficial.com/product/MV_Help/page/03_31.html
[page]: https://rpgmakerofficial.com/product/MV_Help/page/03_39.html
[command]: https://rpgmakerofficial.com/product/MV_Help/page/03_38.html
[mv-interpreter]: https://github.com/rpgtkoolmv/corescript/blob/master/js/rpg_objects/Game_Interpreter.js
[mv-messages]: https://rpgmakerofficial.com/product/MV_Help/page/01_10_01.html
[mz-messages]: https://rpgmakerofficial.com/product/MZ_help-en/01_10_01.html
[mz-advanced]: https://rpgmakerofficial.com/product/MZ_help-en/01_10_16.html
[mz-plugins]: https://rpgmakerofficial.com/product/MZ_help-en/01_11_05.html
[mv-plugin-spec]: https://rpgmakerofficial.com/product/MV_Help/page/01_11_03.html
[mv-plugin-manager]: https://github.com/rpgtkoolmv/corescript/blob/master/js/rpg_managers/PluginManager.js
[mv-font]: https://github.com/rpgtkoolmv/corescript/blob/master/template/fonts/gamefont.css
[mv-window]: https://github.com/rpgtkoolmv/corescript/blob/master/js/rpg_windows/Window_Base.js
[mv-system-runtime]: https://github.com/rpgtkoolmv/corescript/blob/master/js/rpg_objects/Game_System.js
[mz-font]: https://rpgmakerofficial.com/product/MZ_help-en/01_08_12_02.html
[mv-actor-runtime]: https://github.com/rpgtkoolmv/corescript/blob/master/js/rpg_objects/Game_Actor.js
[mv-storage]: https://github.com/rpgtkoolmv/corescript/blob/master/js/rpg_managers/StorageManager.js
