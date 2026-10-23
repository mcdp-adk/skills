# Engine Selection

Use this reference to identify the relevant engine guide and choose a modification route, including when the engine is not listed.

## Establish what runs and what it reads

1. Inventory the supplied release, including launchers, subdirectories, patches, configuration, plugins, and archives. Distinguish the launcher from the game process and bundled tools from the runtime.
2. Compare independent clues: executable metadata, adjacent libraries, configuration syntax, archive headers, script grammar, and resource directory structure. A renamed executable or familiar extension is only a lead.
3. Distinguish source projects from shipped output. An archive of compiled scripts is not an editable project; a readable script may still require a custom compiler or loader.
4. Identify the consumer of a representative resource: a script command, table lookup, object reference, file-open path, or decoding/rendering call. Follow the resolved resource through any patch layers or caches.
5. Record the release and engine evidence, relevant format variant, available reader, possible writer or replacement route, and the unresolved boundary. Use the project's existing records.

For native Windows components, inspect the executable's machine type before choosing tooling. The PE format separately describes on-disk offsets, relative virtual addresses, and process virtual addresses; they are not interchangeable patch locations. [Microsoft PE specification](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format)

## Choose the matching guide

These are documented method families, not promises that every game or resource under that name is supported. Open the guide whose clues match, then confirm its generation and input conditions.

| Family | Guide and distinguishing investigation |
| --- | --- |
| KiriKiri / KAG | [Scripts and storage](engines/kirikiri-kag.md): KAG/TJS, XP3 variants, resource lookup and overrides |
| NScripter / ONScripter | [Scripts and archives](engines/nscripter-onscripter.md): script encoding, archive tools, interpreter differences |
| TyranoScript | [Scenario and web resources](engines/tyranoscript.md): language support, tags, project assets and packaged applications |
| Siglus | [Scene scripts](engines/siglus-scripts.md): scene containers, compiled text and resource associations |
| RealLive | [Bytecode and resources](engines/reallive-bytecode.md): scenario archive, compiler compatibility and runtime extensions |
| BGI / Ethornell | [Scenario and system resources](engines/bgi-ethornell.md): distinct script formats, image encoding and archives |
| AliceSoft System families | [Generation-specific tools](engines/alicesoft-systems.md): System 3.x versus later AIN and asset formats |
| WOLF RPG Editor | [Maps and databases](engines/wolf-rpg.md): format generation, protection, common events and database text |
| Unity | [Project and runtime assets](engines/unity-runtime.md): localization tables versus shipped bundles and Mono/IL2CPP |
| RPG Maker | [Generations and resources](engines/rpg-maker-generations.md): XP/VX/VX Ace versus MV/MZ |
| Ren'Py | [Translation and resources](engines/renpy-resources.md): translation identifiers, compiled scripts, archives and display resources |

## Select by available mechanism

| Available boundary | Prepared approach | Question that decides feasibility |
| --- | --- | --- |
| Native localization in this release | Maintain locale tables and localized resource references | Does the shipped code actually select those tables and assets? |
| Editable scripts or structured data | Parse display fields and preserve executable structure | Can the corresponding writer preserve identities and references? |
| Packed assets with usable replacement lookup | Extract needed assets, edit, and supply the expected overrides | Which location wins at runtime, including existing patches? |
| Compiled scripts with supported import/compiler | Preserve the program while rebuilding text-bearing records | Does the writer support this opcode/layout/version? |
| Closed formats but accessible load/display code | Adapt the narrow program boundary | Can the replacement preserve context, lifetime, encoding, and behavior? |
| Unknown mechanism | Investigate one representative resource and its consumer | What exact missing fact prevents a valid output route? |

Use [asset processing](asset-processing.md) for the resource path and [program adaptation](program-adaptation.md) when the loader or display path must change. Different resources within one game can need different approaches.

## Investigate an unlisted engine or variant

Start with the earliest unresolved boundary, rather than trying an arbitrary sequence of unpackers:

- **Unknown container:** inspect signatures and its index structure; compare offsets, lengths, compression and filenames with a documented reader. Check nested containers after outer extraction. A high-entropy block alone does not distinguish compression from encryption.
- **Readable resources, unknown content:** trace a distinctive visible phrase or known asset reference into scripts, tables, images, or program data. Search likely encodings and assembled fragments; a failed plain-text search is not proof that text is absent.
- **Successful extraction, no writer:** inspect whether the engine loads loose overrides or alternate assets. A different container writer is useful only if its format matches. Otherwise investigate the loading code before editing a large corpus.
- **Successful build, unchanged display:** inspect the chosen path, patch priority, cached or compiled copies, and locale selection. Establish which bytes are actually read.
- **Loaded but incorrect output:** separate decode/parse failure, missing assets, lost references, layout, and scene-state behavior; these require different repairs.

A browser such as GARbro can inspect many visual-novel formats and optionally convert images/audio during extraction. Its own documentation notes that extension-based type labels can be wrong and some encrypted formats require title-specific selection. Preserve a raw extraction when conversion would discard rebuilding information; confirm writing support separately. [GARbro operation guide](https://github.com/morkt/GARbro)

Record new reusable format knowledge separately from the title's filenames, keys, offsets, and scene choices. A successful method for one release is evidence for that release; a family-wide claim needs a documented compatibility basis.
