# Quality and Evidence

Use this reference to decide what a localization result establishes and what remains incomplete. Match checks to the requested task, affected mechanisms, and agreed quality target.

## Distinguish the evidence

| Evidence | Establishes | Does not establish |
| --- | --- | --- |
| Resource survey | Located sources, dependencies, and known gaps | Coverage of unexamined sources |
| Bilingual review | Meaning and format compared with the original in the reviewed range | Every in-game context or layout |
| Continuous Chinese reading | Coherence, voice, terminology, and readability across the read range | Fidelity without consulting Japanese |
| Parsing or compilation | Acceptance by that parser/compiler | Correct text selection or gameplay |
| Static glyph inspection | Character mappings in the inspected font | Runtime font use or readable layout |
| Runtime observation | Behavior of the candidate on the observed path and state | Other routes, versions, or saved states |
| Clean installation | The package can be applied under the recorded conditions | Compatibility beyond those conditions |

Linguistic checking inside the game addresses context and presentation that file-based editing can miss. It complements translation review. [IGDA's in-game localization review guidance](https://igda.org/news-archive/how-to-get-the-most-from-lqa-what-it-is-and-best-practices/)

## Establish content coverage

Compare the agreed scope with the source survey and maintained translations. Account separately for translated content, intentional retention, excluded work, unresolved readings, and inaccessible resources. Resolve unexpected omissions before claiming complete coverage.

Japanese-residue searches are discovery aids. They miss kanji-only labels and some generated text, and they also flag intentionally retained names. A low residue count is not an acceptance criterion by itself.

For completed translation work, finish the bilingual review and continuous Chinese reading described in [text and context](text-and-context.md). Record actual reviewed ranges; a summary or a few representative paragraphs do not constitute full review of a chapter. Revisit affected text after a changed terminology or characterization decision.

## Check the mechanisms that changed

| Change | Relevant checks |
| --- | --- |
| A local line | Meaning, context, control syntax, its display and any shared uses |
| A choice set | Distinct wording, branch mapping, cancellation behavior where applicable |
| A shared term | Applicable occurrences, excluded senses, and previous review status |
| An extractor or writer | Coverage, stable mapping, serialization, retained fields, and actual loading |
| A dynamic template | Meaningful conditions and substitution types as complete outputs |
| A font or shared style | Every affected display path, special characters, input range, and layout |
| An identifier or saved value | Consumers, new-game initialization, and relevant save/load behavior |
| Package contents or loading configuration | Clean installation, actual resource selection, and restoration |

Choose examples from independent mechanisms and their meaningful boundaries. Long and short text, absent and present names, numeric conditions, alternate styles, and route-specific variations are useful when those cases exist. An unchanged path can reuse evidence that still applies to the candidate; a new mechanism needs its own basis.

A check must inspect what it claims to inspect. If a custom checker is used as decisive evidence, establish that it accepts a valid case and detects the relevant defect. A successful process exit or an empty log alone cannot support a broader claim.

## Run without altering play data

Before launching a game, identify the test copy and its actual save, configuration, persistent-unlock, and synchronization locations. Copying the installation directory may leave external state shared with the user's play installation. Use a supported alternate data location or another adequate isolation method where needed.

Preserve the original and the user's progress. If the proposed run could change shared play state and adequate protection is unresolved, stop that run and continue independent authorized work. Ordinary external logs or caches are not by themselves a reason to block execution.

Use known chapter entry points, replay modes, or isolated test saves when useful. Record the entry state. A forced scene jump can show rendering while bypassing natural progression; distinguish those conclusions. When comparing a suspected pre-existing defect, use the same conditions on the unmodified release before attributing it to the original.

## Save compatibility

A save may retain names, translated strings, object values, script positions, or cached data. Loading it may bypass new initialization. Determine whether the affected value comes from a resource, a startup assignment, the save, or persistent system data.

Test the compatibility that is actually claimed: new game, saving and reloading with the patch, loading a supported earlier save, and any relevant replay or rollback path. A synthetic state supports only the scenario it represents. Without applicable old-save evidence, report that compatibility as unverified.

If migration is needed, trace references before changing fields, preserve unrelated progress, and work on backed-up test data. An accepted limitation should identify the affected save type and consequence rather than describe all saves as compatible or incompatible.

## Accept a patch against its agreed scope

Apply the actual candidate to a clean copy of the specified base release using the proposed instructions. A development directory with extra files or fallback settings cannot establish that the delivered package is sufficient.

| Aspect | Acceptance basis |
| --- | --- |
| Content | Agreed sources accounted for; included translations reviewed; deliberate retention distinguished from gaps |
| Presentation | Required characters supported and affected display paths observed with suitable Chinese forms and layout |
| Behavior | Affected choices, dynamic expressions, and claimed save/load compatibility checked |
| Package | Delivered files correspond to maintained inputs and checked candidate; installation has its required resources |
| Instructions | Base version, placement, language selection, restoration, compatibility, and remaining limitations match the package |

Acceptance covers the applicable mechanisms and agreed scope; it need not mean exploring every possible play sequence. If a required aspect remains incomplete, describe the concrete gap and options for finishing or reducing the scope. The user decides whether to accept a changed scope or limitation.

For a task that explicitly excludes verification, report the produced or inspected material and the missing evidence without claiming acceptance. Keep that task boundary distinct from the checks a future release would require.

## Keep conclusions traceable

Record the candidate or version, input state, method, observation, supported conclusion, and remaining gap. Link existing reports or source locations instead of duplicating them. File lists or hashes can help identify the object; they do not demonstrate meaning or runtime behavior.

After a correction, update the maintained source, regenerate affected output, and repeat affected checks. A documentation-only change need not invalidate unrelated runtime evidence. A tool failing before launch is neither a runtime pass nor automatic disproof of earlier applicable observations.

Use the [release notes template](../assets/templates/release-notes.md) to state the resulting support boundary in terms a player can use.
