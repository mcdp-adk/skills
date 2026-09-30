# Unity projects and shipped runtimes

## Identify serialization, backend, and text framework

Confirm Unity from executable/data layout and serialized-file metadata. Record engine
version, platform, architecture, and whether the title uses Mono or IL2CPP. On Windows,
managed game assemblies under `<Game>_Data/Managed` suggest Mono; `GameAssembly.dll`
and IL2CPP metadata suggest IL2CPP. Confirm from multiple artifacts or runtime logs.
Identify UGUI, TextMesh Pro (TMP), legacy/custom text, and the game's scenario system.

Unity does not prescribe one dialogue format. Text may live in TextAssets, JSON/CSV,
ScriptableObjects, localization tables, bundles, managed code, or external data.
With the original project, retain `.meta` GUIDs and use its Unity/package versions.
With a shipped build, recovered assets are inspection/reconstruction inputs, not an
equivalent original project with a guaranteed rebuild path.

## Available project: integrate through its data model

For a title using Unity Localization, add a Simplified Chinese locale and retain
shared entry identities while editing String Tables. Its
[String Table model](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/StringTables.html)
separates shared keys from per-locale text; preserve Smart String placeholders and
formatting logic. [CSV import/export](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/CSV.html)
is a supported editing surface, not a reason to replace IDs with source sentences.

Use [Asset Tables](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/AssetTables.html)
for localized sprites, textures, audio, or other assets when the project already uses
that mechanism. Entries reference assets through GUIDs and Addressables. Preserve
asset identity or update references deliberately, then rebuild content/catalogs using
the project configuration. A replacement PNG alone does not update an Asset Table.

For custom dialogue, keep scenario IDs, choice destinations, voice keys, formatting
parameters, and code-owned values distinct. Import translations into the existing
schema, then use the original project to rebuild scripts and assets together.

## Shipped build: resource editing route

[AssetRipper](https://github.com/AssetRipper/AssetRipper) can analyze/export supported
Unity files, with support quality varying by version. Use it to locate readable
TextAssets and dependencies; a successful export does not establish round-trip writing.
[UABEA](https://github.com/nesrak1/UABEA) provides serialized-file/AssetBundle reading
and writing. Select a writer that handles the title's serialization and asset types.

1. Associate each editable item with file/bundle, object path ID, type, and references.
   For TextAssets, retain internal format and encoding; for MonoBehaviours, establish
   the field schema before changing string data.
2. Export the needed objects, translate display text, and reimport into a working copy.
   Preserve object references, bundle dependencies, and external resource streams.
3. Save with a compatible writer and retain required compression and layout. Bundles
   under `StreamingAssets/aa` may belong to Addressables; changed bytes can invalidate
   catalog CRC/hash data. Establish a supported content/catalog update together.

A text dump omits strings assembled by code and may contain unused assets. Confirm
the game actually consumes a selected object before treating it as the translation
source. Use [asset processing](../asset-processing.md) for object-to-output mapping.

## Shipped build: runtime replacement route

BepInEx package selection depends on backend, OS, and architecture; its
[Mono](https://docs.bepinex.dev/master/articles/user_guide/installation/unity_mono.html)
and [IL2CPP](https://docs.bepinex.dev/master/articles/user_guide/installation/unity_il2cpp.html)
instructions are separate. Pair the plugin with a compatible loader version and
confirm successful loading in `BepInEx/LogOutput.txt` before diagnosing text hooks.

[XUnity.AutoTranslator](https://github.com/bbepis/XUnity.AutoTranslator) can use local
translation files, replace some textures, and adjust supported text components.
For a reviewed offline translation, disable automatic endpoints with `Endpoint=` and
ship curated entries. Map context collisions and dynamic fragments deliberately;
rendered text keys alone may lose speaker, route, or placeholder identity.

Its UGUI font override and TMP font fallback/override are different settings. TMP
can require a font AssetBundle built for the target; an arbitrary TTF file is not a
universal TMP replacement. Texture dumping is discovery only: retain generated
identities, edit the intended image, verify replacement, then disable dumping for
delivery. IL2CPP hooks and custom text renderers have documented or title-specific
gaps. Audio/video replacement generally needs another resource or custom hook route.

## Fonts, visual assets, and delivery consequences

For TMP, add a Chinese glyph corpus to the generated atlas or provide compatible
[fallback font assets](https://docs.unity3d.com/Packages/com.unity.textmeshpro@4.0/manual/FontAssetsFallback.html).
Check fallback availability and font/material references, rather than assuming the
source font file guarantees glyphs in a static atlas. Adjust layouts for names,
choices, scrolling help, backlog, and rich text without stripping formatting tags.

For raster UI, preserve atlas regions, Sprite rectangles/pivots/borders, alpha, and
material usage. For AudioClips and VideoClips, preserve external stream bindings and
the title's codec/timing requirements. Review
[visual resources](../visual-resources.md) and [media resources](../media-resources.md)
when changing those assets. Localized data tables need their own schema-aware import.

Choose native asset changes or a runtime-dependent package per resource. Record
which game build and loader/plugin combination each replacement targets. Runtime
acceptance requires actual consumption and Chinese rendering; custom protection, missing schemas,
unsupported hooks, and Addressables updates remain distinct unresolved capabilities.
