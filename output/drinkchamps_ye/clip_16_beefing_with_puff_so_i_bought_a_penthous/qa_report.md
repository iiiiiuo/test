# Clip_16 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `a2d12ffb84027d8fdc20d71db596f3a756d9e242ccf4cce275c1c607c39249c8`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 64.564 s, audio 64.564 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1548 (manifest 1548)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1548, "expected_frames": 1548, "video_duration_s": 64.5645, "audio_duration_s": 64.564, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 207, "asr_words": 203, "matched": 187, "match_ratio": 0.903, "matched_words_inside_their_caption": 0.979, "caption_onset_vs_first_word_s": {"n": 19, "median": -0.013, "max_abs": 1.55}}

## Critic rounds
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

## Items
1. Structure: PASS. Opens on "Can I continue?" (source ctx 1820.76, after "Let's move on there"); ends on "you remember?" at 64.4s, just before the source moves to "puff is my idol" at 1885.63. Story is complete: Waldorf, billionaire, penthouse, Maybach, Puff stays rich.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 64.5645s / audio 64.564s, 1548 of 1548 frames, no decode errors.
3. Transcript: PASS. sync.txt HEARD matches the displayed English (match 0.903, 0.979 of matched words fall inside their caption). Differences are ASR noise ("Waldof", "made back the fleet"). Caption 22 "He wasn't rich at all times" (60.29-62.08): the render ASR hears "he was like this he", while the source ASR gives "he wasn't rich at all times". I could not re-check the audio locally (CPU contention), so this is unresolved. The line fits the span (about 1.8s) and the repeated "was like this" in the render ASR looks like a stutter, so it is not blocking.
4. Translation: PASS. Spot-checked all 23 captions against the approved CSV; no clear errors or misattached lines.
5. Masking: PASS. Displayed "s**t" (caption 12) and "ni**a's" (caption 21). auto.json shows unmasked_hits = []. The JP is not mechanically masked.
6. Timing: PASS. Median onset vs first word is -0.013s. Gaps without a caption (22.95-25.47 around 24.07, 44.12-48.95) are pauses or silence. No uncaptioned foreground sentence. The shortest caption, "Waldorf where?" (0.68s), is a 2-word line and is readable.
7. Typography: PASS. White bold Yu Gothic with black outline and shadow, EN above JP, centred, in the same vertical band as ref_20.png. Max 2 EN + 2 JP lines, nothing clipped (f_0030.60 checked). Readable on the bright yellow background.
8. Framing: PASS. Faces sit in the sharp band, with blurred fill above and below like the reference. Crop changes coincide with shot changes (framing_sheet).
9. Source usage: PASS. One interval, part_4 frames [43651,45199) = 1548 frames, which equals the render. No padding or repetition. The single interval means there are no joins.

## Non-blocking notes
- 0.0-0.17s shows Ye (4-frame source shot) while the host says "Can I continue?", and 1.5-6.4s shows the host while Ye speaks. This follows the source camera cuts.
- Caption 22 wording is unverified against the audio (see item 3).

