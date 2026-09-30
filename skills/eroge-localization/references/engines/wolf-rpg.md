# WOLF RPG Editor: structured data and resource loading

Use this reference for a confirmed WOLF distribution. `Game.exe`, `Data/BasicData/`, maps ending in `.mps`, and `.wolf` containers are useful combined evidence; inspect executable version information and the data format before selecting a writer.

## Separate release boundaries

| Release family | Localization implication |
| --- | --- |
| Older 2.x data/runtime | Historical parsers and encoding assumptions; do not assume Unicode |
| 3.00 onward | Unicode engine; still needs a Chinese-capable font and compatible data writer |
| 3.50 onward | Additional encryption format and Pro individual-file `.wolfx` support |

The official release history identifies 3.00 as the Unicode transition. Record editor and shipped runtime versions separately; converting editable older data is a migration, not a transparent text patch. [Official release information](https://silversecond.com/WolfRPGEditor/)

Version 3.50 adds a new encryption scheme; a tool supporting older `.wolf` data does not thereby support the new scheme. Pro `.wolfx` files add an individual-resource layer with loader priority and key-dependent access. Preserve the runtime's decryption relationship, including font handling, rather than renaming encrypted resources into ordinary files. [3.50 release changes](https://silversecond.com/WolfRPGEditor/old_releaselog/ReleaseLog07.html), [individual encryption](https://silversecond.com/WolfRPGEditor/Help/02_file_crypt_pro.html)

## Find the editable data

| Location | Candidate display content | Keep intact |
| --- | --- | --- |
| `Data/BasicData/Game.dat` | Title and font settings | Runtime settings and resource references |
| `CommonEvent.dat` | Common-event messages and generated UI | Event numbers, arguments, variables, and calls |
| Database `.dat` / `.project` pairs | Names, descriptions, interface terms | Schema, record IDs, types, and lookup relationships |
| Map `.mps` | Event dialogue, choices, text pictures | Map/event IDs, tiles, conditions, and command structure |
| Text/CSV resources | External messages and tables | Delimiters, keys, and filenames used by consumers |

String conditions and assignments can be extracted too; they are not automatically display text. Preserve operands used for comparisons or dispatch, and inspect text-picture commands separately from image-picture commands. Historical wolftrans implements readers and writers for maps, common events, database pairs, and game settings. [Data handling implementation](https://raw.githubusercontent.com/elizagamedev/wolftrans/master/lib/wolftrans/patch_data.rb)

## Choose a writer suited to the data

For supported 3.00+ data, the optional official translation support tool offers a concrete route:

1. Select the game's executable to establish the input data root and choose Simplified Chinese as the output language.
2. Extract the XLSX mapping; retain location codes and the original column, editing the translation column.
3. Create the tool's language output folders, then apply the translations to those folders.

The tool outputs a separate translated distribution. Its mapping can include file-reference strings, but it does not automatically rename the actual image/audio files. Confirm that the intended protected data is readable and writable with the selected tool edition; engine version alone does not establish format support. [Official support tool scope and operations](https://silversecond.com/WOLF_Translation_tool/Manual.html)

Historical [wolftrans](https://github.com/elizagamedev/wolftrans) is an alternative reader/writer for some older data, explicitly described as early and unstable. Its three arguments are the source game, translation patch directory, and generated output directory. **It deletes an existing output directory.** If selecting it, reserve a new dedicated output path that does not exist; never use the original game or a shared work directory as that argument. Do not infer 3.x or `.wolfx` support from its legacy coverage. [Maintainer warning](https://raw.githubusercontent.com/elizagamedev/wolftrans/master/README.md)

Keep each string's map/event/database location with its translation. If a reader can extract a newer format but lacks its writer, use editable authoring data or a supported writer; plaintext extraction alone cannot produce engine data.

## Text controls and Chinese layout

Preserve variable/control syntax and distinguish actual line breaks from editor notation. Representative native controls include `\f[n]` font size, `\c[n]` color, `\font[n]` font selection, `\sp[n]` speed, `\r[A,B]` ruby, and `<C>`/`<R>`/`<L>` alignment. Games can add common-event conventions around them. [Official text effects](https://silversecond.com/WolfRPGEditor/Guide/EFFECT_006.html)

Choice formatting can carry into later choices; do not assume each label resets font/color settings. Keep choice order and branch references while adjusting labels and explicit resets. [Choice command behavior](https://silversecond.com/WolfRPGEditor/Help/04ev_select.html)

Select the font by the engine's expected font name, not merely the filename. The official material guide permits bundled TTF/TTC files in the game root or unencrypted Data; OTF support starts in 3.230. Include glyphs needed by dialogue, ruby, numbers, symbols, and retained Japanese. [Font/material requirements](https://silversecond.com/WolfRPGEditor/Help/06material.html)

## Images, media, and packaging

Keep picture dimensions, character/tile grids, animation frames, alpha, and button relationships while replacing embedded text. The material guide recommends 32-bit PNG with alpha and Ogg audio; converting arbitrary files to those formats does not preserve the game's references or timing automatically. [Material formats](https://silversecond.com/WolfRPGEditor/Help/06material.html)

Trace spoken lines to voice files and common-event playback logic. Preserve filenames unless their database/event consumers change together. Process subtitles, video, and timing separately through [media resources](../media-resources.md).

Editor packaging can combine Data into `Data.wolf` or encrypt subdirectories separately; observe the distribution's actual arrangement. Rebuild with a compatible editor/writer or use a demonstrated loader entry point, retaining keys for protected resources. [Editor packaging options](https://silversecond.com/WolfRPGEditor/Help/01control.html), [patch delivery](../patch-delivery.md)
