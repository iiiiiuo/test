# Clip_29 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `e101e6b19d659a55fbf90f5645d455f6146ec32c851e0c305cc8f2be8e1d3f13`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 73.991 s, audio 73.990 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1774 (manifest 1774)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1774, "expected_frames": 1774, "video_duration_s": 73.990583, "audio_duration_s": 73.99, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 248, "asr_words": 258, "matched": 242, "match_ratio": 0.976, "matched_words_inside_their_caption": 0.967, "caption_onset_vs_first_word_s": {"n": 25, "median": 0.036, "max_abs": 0.614}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: PASS. Starts at "Think about, like, True Love" (source 1327.37s, after host aside); ends on "...her birthday, possibly." (1400.92s) with a 0.4s tail; single coherent monologue.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 73.990583s / audio 73.99s, 1774 frames = manifest, no decode errors.
3. Transcript: PASS. 97.6% ASR match; no meaningful mismatches in sync.txt (differences are filler only).
4. Translation: PASS. JP matches the English at each moment; no clear errors.
5. Masking: PASS. unmasked_hits empty; no masked words needed; JP not mechanically masked.
6. Timing/sync: PASS. Median onset offset 0.036s; the 0.614s max is the intentional split at 50.79-54.98 (0.33s gap, repeated JP "結局のところ、あいつは…"). No long uncaptioned speech, no too-short captions.
7. Typography: PASS. White bold, outlined, EN above JP, centred, 2 EN + 2 JP max, same size/position as reference (sheet_1/2 vs ref_sheet); no clipping.
8. Framing: PASS. Face in the sharp band with blurred fill; crop changes only at shot changes (frames 1124 and 1157, host shot ~46.9-48.3s).
9. Source usage: PASS. One interval [31824,33598) from part_4, no padding or repetition.

Non-blocking notes
- The JP line "結局のところ、あいつは…" repeats across the split caption at 50.79 and 54.16; acceptable.

