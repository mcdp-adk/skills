# Program Adaptation

Use this reference when localization must change scripts, compiled resources, loading behavior, runtime display code, or an executable. Shared text representation rules are in [Text Resources](text-resources.md); resource extraction and rebuild choices are in [Asset Processing](asset-processing.md). This file focuses on program-level adaptation, especially runtime hooks and native modifications.

## Find the active text path

Identify the exact release, architecture, runtime, and code/data files it loads. Trace one displayed string from storage through decoding, formatting, and the final renderer. Static string search can find literal candidates but misses compressed, encrypted, generated, or split strings. Follow references, method calls, script commands, or runtime logs when needed; confirm the path that actually supplies the visible text.

Distinguish raw source text, decoded text, a completed template, and rendered objects. Locate the narrowest function that still has enough context to distinguish speaker, scene, route, UI role, and locale. A global replacement by Japanese spelling can affect unrelated lines, names, menus, and generated text.

Before scaling an approach, establish one complete write path: native locale entry, loose-file override, compiler/repacker, runtime substitution, or executable modification. Extraction or disassembly alone has no write-back path. When runtime work is in scope, confirm the target loader consumes the rebuilt or overlaid resource before describing it as an adaptation method.

## Make managed hooks bounded

For a managed runtime, identify the exact method signature and overload. Inspect parameters, return type, instance state, invocation thread, and callers before choosing a prefix, postfix, or replacement. Use a match key with enough context—such as resource ID plus UI role or speaker/route—not a broad text-only lookup. Pass through unknown strings unchanged.

Avoid recursive calls into the hooked method. Keep translation lookup deterministic and bounded; do not perform file I/O or wait on remote work in a frequently called render method. Account for repeated, nested, and concurrent calls: avoid mutable global “current line” state, guard shared caches, and preserve the original behavior on misses or exceptions. Remove only the hook instance's own patches during unload.

HarmonyX documents prefix/postfix patch behavior, coexistence with other patches, and limitations of supported runtimes; BepInEx documents the loader and its Mono/IL2CPP distinctions. Treat those as implementation options, not universal support. [HarmonyX](https://github.com/BepInEx/HarmonyX/wiki) · [BepInEx](https://docs.bepinex.dev/master/)

## Treat native hooks as ABI work

For native code, confirm the target architecture, calling convention, function signature, argument and return representation, and instruction boundary before detouring. A wrong ABI can corrupt the stack or registers even when the hook appears to run. Windows x64 passes its first integer or pointer arguments in RCX, RDX, R8, and R9, but other architectures and runtimes differ. Use the target's ABI rather than copying an example. [Microsoft x64 calling convention](https://learn.microsoft.com/en-us/cpp/build/x64-calling-convention?view=msvc-170)

Trace pointer ownership and lifetime for both incoming text and replacement text. Determine whether a string is borrowed, mutable, reference-counted, or owned by the caller; keep replacement storage alive for as long as the consumer may read it. Do not return a pointer to a temporary buffer or free memory through the wrong allocator. Preserve encoding and explicit length conventions at the boundary.

Hooks may run on render, audio, or worker threads. Keep shared translation state thread-safe, avoid blocking the render path, and prevent re-entry if the original function can call the hooked path again. If the call context does not identify a line reliably, use a resource-level mapping or leave the input unchanged rather than guessing.

If translation lookup fails before the original call, pass through the original arguments. Preserve exceptions from the original method unless the adaptation intentionally changes that behavior; retrying a call that already ran can duplicate its side effects.

## Change scripts, bytecode, or binaries

For editable scripts, alter only proven text-bearing operands and retain control flow. For bytecode, verify that a compatible compiler or structural patcher exists; preserve branch targets, instruction widths, tables, and version-specific records. A readable decompilation is not automatically recompilable.

For native binary edits, prefer a format-aware resource or code patch. If executable instructions must change, verify instruction boundaries, relative references, relocation behavior, memory protection, and integrity/signature checks. Build and update any affected lengths, offsets, checksums, compression sizes, or indices through a format-aware writer. Variable-length text can move later data; follow the specific format rules in [Text Resources](text-resources.md).

When a native hook uses a trampoline, preserve the displaced instructions and ensure branches/calls still reach the intended destinations after relocation. Keep hook installation and removal paired, and avoid patching a function while another thread can execute partially written instructions.

Assess an engine or runtime change against the target's resources, bytecode, plugin interfaces, save formats, and renderer. A newer or alternate runtime may enable a needed locale path but can change compatibility; record the selected version and verify the affected game behavior.

## Bound the result

A hook loading successfully proves injection, not that all dialogue or UI paths use that method. A rebuilt archive proves a writer produced output, not that the shipped reader selected it. Keep evidence scoped to the changed call sites, resource families, and target version; use [Patch Delivery](patch-delivery.md) for package-level conclusions.

If only extraction works, state that translation preparation is possible but a write-back or runtime loading mechanism remains missing. If a hook changes text but cannot supply required fonts, images, or media, treat those as separate resource dependencies rather than claiming the localized game is complete.
