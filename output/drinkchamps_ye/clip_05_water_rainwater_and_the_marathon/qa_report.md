# Clip_05 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `af95628beae1b61c91120751fe9ee41c0734502e5683ea97b74f960f208bd12e`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 65.566 s, audio 65.565 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1572 (manifest 1572)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1572, "expected_frames": 1572, "video_duration_s": 65.5655, "audio_duration_s": 65.565, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 165, "asr_words": 166, "matched": 160, "match_ratio": 0.97, "matched_words_inside_their_caption": 0.938, "caption_onset_vs_first_word_s": {"n": 18, "median": -0.15, "max_abs": 2.37}}

## Critic rounds
- round 1: FAIL — caption 9 2.5 s early over pause → build_subs: glued short-word onset fix + forced chunk break at >1 s pauses (snapped to punctuation)
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: PASS. Starts at "But right now in America" right after the prior sentence ends (source_context 641.18); ends on "That's a good way to put it." then a brief reaction shot. Standalone coherent.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 65.5655 s, audio 65.565 s, 1572/1572 frames, no decode errors.
3. Transcript: PASS. sync.txt HEARD matches the captions; ASR match ratio 0.97. Only differences are trivial ("for who" vs "with who", "a street").
4. Translation: PASS. No clear errors; JP lines are attached to the correct moments.
5. Masking: PASS. "f**k" is masked in L7; auto.json unmasked_hits is empty; JP is not masked.
6. Timing/sync: PASS. Onsets sit within about 0.1-0.4 s of the first heard word (e.g. 27.73 vs "You" 27.67; 64.04 vs "that's" 63.93). No uncaptioned foreground sentence. Pauses at 25.7-27.7 s and 62.6-64.0 s are real silence (ASR word times).
7. Typography: PASS. sheet_1 and sheet_2 match the reference: white bold Yu Gothic, black outline, EN above JP, centred, at about the same height and size, max 2 EN + 2 JP lines, no clipping.
8. Framing: PASS. Faces are in the sharp band with blurred fill above and below. Framing changes only at shot changes (Ye, Envy, Jess, wide).
9. Source usage: PASS. One interval, frames [15371,16943), source part_2_2. Pieces are contiguous with no repetition or padding.

Non-blocking notes
- Final 0.07 s has no caption on a smiling reaction shot (acceptable).

