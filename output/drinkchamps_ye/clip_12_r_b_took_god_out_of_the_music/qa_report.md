# Clip_12 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `41c7ee2d3e29e86ca2cf0dfb87db92a3dac1e6bbd0a3792a6c7b78c58623a4e2`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 65.524 s, audio 65.524 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1571 (manifest 1571)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1571, "expected_frames": 1571, "video_duration_s": 65.523791, "audio_duration_s": 65.524, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 176, "asr_words": 181, "matched": 165, "match_ratio": 0.938, "matched_words_inside_their_caption": 0.97, "caption_onset_vs_first_word_s": {"n": 20, "median": 0.066, "max_abs": 1.374}}

## Critic rounds
- round latest: FAIL — end cut inside "away" → end moved to 1093.07 (frame 26207)

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (minor: 0.07 s start margin, see notes)
Fix: none

Items
1. Structure: PASS. Opens on the host question "Taking God out of music, you said?" (source_context: prior "I was like-" is outside), resolves with the "40 acres ... take away" sentence; standalone, coherent.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 65.524 s / audio 65.524 s, 1571 frames = expected, decode errors empty.
3. Transcript accuracy: PASS. HEARD matches SUB throughout (97% of matched words inside their caption); "400 acres" in ASR is an ASR error, "40 acres" is correct in context and audio.
4. Translation fidelity: PASS. JP rows match approved rev3 CSV; no clear errors; no dropped lines.
5. Masking: PASS. ni**as, f**k, b**ch, f**king masked in EN (auto.json unmasked_hits empty); JP not mechanically masked.
6. Timing/sync: PASS. Median onset offset 0.07 s; no caption <1.3 s; gaps (18.75-19.71, 31.63-32.89, 55.36-57.19) are pauses/"hmm", not foreground sentences.
7. Typography/visuals: PASS. f_0065.44 and sheets: white bold Yu Gothic, black outline/shadow, EN over JP, centred, at same height as reference, max 2 EN + 2 JP lines, no overflow.
8. Framing: PASS. Faces sit in the sharp centre band with blurred fill above/below; crop changes align with speaker cuts (N.O.R.E./Ye).
9. Source usage: PASS. One interval part_3 frames [24636,26207), 1571 frames, no padding or repetition, no joins.

Non-blocking notes
- Audio energy rises continuously from ~1027.44 s while clip starts at 1027.527 s and ASR puts "Taking" at 1027.60; the first word may be ~0.08 s clipped, but render ASR still hears "taking god out of music".
- Ends 1093.05 s, just as "from us" begins (ASR 1092.90); the end is low energy (-26 dB) and reads as a complete sentence.
- At 1.29 s the host caption stays up for ~0.06 s over the first Ye frame (cut slightly precedes caption end).

