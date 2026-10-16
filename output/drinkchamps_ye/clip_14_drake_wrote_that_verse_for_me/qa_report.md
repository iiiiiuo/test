# Clip_14 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `4acd372b4212c164e852c969d50ea40adaf778b4be380961fdc4a0c51f900520`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 61.770 s, audio 61.770 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1481 (manifest 1481)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1481, "expected_frames": 1481, "video_duration_s": 61.770041, "audio_duration_s": 61.77, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 199, "asr_words": 199, "matched": 183, "match_ratio": 0.92, "matched_words_inside_their_caption": 0.951, "caption_onset_vs_first_word_s": {"n": 20, "median": 0.06, "max_abs": 1.58}}

## Critic rounds
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (non-blocking: opening has only the ~0.1 s tail of "Right" audible under the "Right?" caption)
Fix: none required; optional: start ~8-10 frames earlier (needs a fresh reservation) or drop "Right?" from caption 1.

1. Structure: PASS. Opens at "Right? We get on our jealousy stuff"; coherent Drake/"Victoria's Secret line" story with a resolved payoff ("wrote the whole rap", "how much easier my life would be... but..."); ends with Ye laughing after the host's "but...". source_context.txt and sync.txt agree.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 61.770 s, audio 61.77 s, 1481/1481 frames, no decode errors.
3. Transcript accuracy: PASS. The 23 captions match the HEARD lines. Differences are ASR noise only (interested/interesting, "Keep it real" for "Like, yeah, but").
4. Translation fidelity: PASS. JP follows the approved rev3 rows and the moment each caption sits on. The split of 「Victoria's Secretの / ショーは緊張したけど… is awkward across the pause but not wrong.
5. Masking: PASS. auto.json unmasked_hits is empty. The clip has no listed profane words, and the JP is not masked.
6. Timing/sync: PASS. Median onset offset is 0.06 s and 95% of matched words fall inside their caption. The gap 21.70-23.89 holds only "um / I / I had" hesitation (ASR 21.16-23.96), so no full sentence is uncaptioned. Shortest caption is 1.15 s ("I had, like,").
7. Typography/visuals: PASS. sheet_1/2 and f_0034.62.png: white bold Yu Gothic with black outline and shadow, EN above JP, centred, at about 50-59% of frame height like the reference, at most 2 EN + 2 JP lines, no clipping.
8. Framing: PASS. Ye's face is in the sharp centre band with blurred fill above and below, matching the reference. The host cutaway at ~33 s is framed correctly and the change happens at a shot change.
9. Source usage: PASS. One interval of part_4, frames [8230,9711) = 1481 frames, matching the render. Three crop pieces change at 9019 and 9057 with no visible jump. No padding, freezes or repetition.

Non-blocking notes
- Opening: the render's first 0.1 s is the tail of "right" (68 to 57 dB), and the real onset of "we" is at about 0.3 s. The "Right?" caption shows over almost no audible word.
- The 21.70-23.89 stretch is blank. It reads as a natural hesitation.

