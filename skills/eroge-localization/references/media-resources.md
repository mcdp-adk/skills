# Media Resources

Use this reference when the requested scope includes voice, music, sound effects, video, or timed subtitles. Shared asset mapping and rebuild procedures are in [Asset Processing](asset-processing.md), while package claims belong in [Patch Delivery](patch-delivery.md). Media presence alone does not imply that translated voice or dubbing is requested.

## Read source streams before conversion

Identify which streams a container holds before converting it. ffprobe can report container and stream properties in machine-readable form:

    ffprobe -v error -show_format -show_streams -of json input.mkv

Check stream index, type, codec, language tags, channel count, sample rate, duration, start time, frame rate, dimensions, and subtitle type as applicable. ffprobe documents each stream and container separately; a filename extension does not establish codec or track layout. [ffprobe documentation](https://ffmpeg.org/ffprobe.html)

Compare source and candidate stream indexes instead of assuming that output index 1 refers to the same language or role as source index 1. Preserve language metadata when the game or player uses it to choose a track. If the runtime addresses media by a script key rather than container language, keep that mapping authoritative.

When FFmpeg conversion is suitable, choose streams explicitly. Its automatic mapping can select the highest-resolution video, the audio stream with most channels, and the first compatible subtitle stream; it can omit data and attachment streams. Do not rely on those defaults for a container with multiple tracks. [FFmpeg stream selection](https://ffmpeg.org/ffmpeg.html#Stream-selection)

For example, if the target specifically requires an AAC audio-only M4A and the input is one localized WAV take:

    ffmpeg -n -i localized.wav -map 0:a:0 -c:a aac -b:a 192k localized.m4a

The -n option refuses to overwrite an existing output. Change codec, bitrate, channel layout, sample rate, and container to match the actual loader. Re-probe the result; this conversion does not preserve external loop points or prove in-game playback. [FFmpeg main options](https://ffmpeg.org/ffmpeg.html#Main-options)

## Voice and sound

If replacement voice is in scope, map each take to its speaker, line, route, resource key, and playback event. Keep the approved spoken wording and pronunciation decisions with the recording. Preserve the resource name or update the target mapping deliberately. Check alternate takes and voiced choices where they exist.

Match the target's sample rate, channel layout, format, and playback convention. Preserve voice start/stop behavior, fades, silence, and tails that align with animation or the next line. A longer Chinese take may collide with input timing or another speaker; retiming is a project change, not an automatic consequence of translation. Listen in the surrounding mix and compare levels against adjacent lines.

For music and sound effects, change media only when it contains language-dependent material or the project explicitly requires an alternate. Preserve cue points, loop boundaries, fades, spatial placement, and mixing role. Loop points may be embedded, stored in a sidecar, or defined by script; converting the waveform alone may discard them. Verify the loop for clicks or gaps and retain the expected channel count when audio is streamed.

## Video and subtitles

First distinguish a separate subtitle track, a game-rendered overlay, image-based subtitles, and lettering burned into video. They have different edit paths. For image subtitles, changing the extracted text is insufficient; the runtime needs a supported text overlay or a replacement image/video.

For every timed cue, preserve its identity, timebase, start/end, speaker, position, and supported style. The HTML media model defines cues with start and end times; games may instead use frames, ticks, or script events, so follow the target format. [HTML text tracks](https://html.spec.whatwg.org/multipage/media.html#text-track-cues)

If the source stores cues in frames, retain the source frame rate when converting between frame numbers and seconds. Round to valid frame boundaries, then review short cues and adjacent cuts: time rounding can change which speaker a subtitle appears to belong to. Keep cue IDs stable when scripts refer to them.

Review overlap, gaps, reading time, scene cuts, line breaks, and simultaneous speech. Do not move a cue across a cut or speaker turn to solve an overflow. Confirm whether the requested captions include sound cues or speaker labels; do not add them to dialogue subtitles by assumption.

When replacing a video stream, preserve all required audio, subtitle, data, and attachment tracks as well as start timestamps, frame cadence, dimensions, aspect ratio, color properties, and synchronization. Re-encoding can change timestamps or frame timing. Review the resulting stream properties and play the affected scene at normal speed when runtime checking is in scope.

If only one stream needs replacement, map unchanged streams from the original and the new stream from its localized source, then choose codecs the target container supports. FFmpeg disables automatic stream selection once explicit mapping is used, so include every required stream deliberately. [FFmpeg mapping behavior](https://ffmpeg.org/ffmpeg.html#Stream-selection)

## Scope the media operation

Automatic stream selection, audio transcoding, and subtitle extraction are convenience operations, not evidence of complete media coverage. Keep language selection, missing-take fallback, replay/skip paths, and locale switching in view only where the changed media uses them. Do not synthesize or dub automatically; use supplied recordings or an agreed text-subtitle path.

Use [Patch Delivery](patch-delivery.md) for the distinction between static media inspection and observed playback.
