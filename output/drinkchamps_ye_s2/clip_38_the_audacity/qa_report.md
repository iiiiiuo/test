# Clip_38 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `a798ef9121093c3b9971cd43b7e61b534a7efd7ebd96d3b3fa4ad6a74e77aa29`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 75.409 s, audio 75.408 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1808 (manifest 1808)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1808, "expected_frames": 1808, "video_duration_s": 75.408666, "audio_duration_s": 75.408, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 197, "asr_words": 206, "matched": 187, "match_ratio": 0.949, "matched_words_inside_their_caption": 0.947, "caption_onset_vs_first_word_s": {"n": 25, "median": 0.015, "max_abs": 1.165}}

## Critic rounds
- round 1: PASS — note: same JP repeated on two consecutive captions → chunks override Clip_38_L010 (one JP segment per chunk)
- round 2: PASS — minor: 62.09 caption EN-only → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (minor: caption 62.09-63.63 "that would have the audacity to have" is EN-only; approved JP for L010 starts with the next caption)
Fix: none

1. Structure: PASS. Opens on the host question "So did you get, like, any calls?" (audio RMS low 1366.3-1367.3, no mid-word start); ends on "they've never seen this before." (energy dip ~1441.9, next speech "you know" starts ~1442.1), thought resolved; standalone and coherent.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 75.409 s / audio 75.408 s, 1808 frames = expected 1808, no decode errors.
3. Transcript accuracy: PASS. 26 captions match HEARD (95% word match); "four Black children" fits the context (ASR heard "for"); no meaningful mismatches.
4. Translation fidelity: PASS. JP rows match approved CSV rev2 for L001-L011; no clear errors; L010 JP "そういう度胸のな" is the approved wording.
5. Masking: PASS. "s**t" masked at 9.81 s; auto.json unmasked_hits empty; JP not mechanically masked.
6. Timing/sync: PASS. Onset median offset 0.015 s; caption 23.27 s leads "just" (23.74 s) by ~0.5 s, acceptable; no flash <1 s that is unreadable (shortest ~1.0 s, 70.77-71.79 and 62.09-63.63 are readable); no uncaptioned foreground sentence.
7. Typography/visuals: PASS. White bold Yu Gothic-style, black outline/shadow, EN above JP, centred, size/vertical position match ref_sheet (in the sharp band, lower-mid), max 2 EN + 2 JP lines, no clipping (f_0075.33.png, sheet_1/2).
8. Framing: PASS. Ye and the host framed in the centre band with head fully visible, blurred fill above/below as in the reference; crop changes coincide with shot changes (framing.json shots).
9. Source usage: PASS. Single interval part_6 frames [32765, 34573) = 1808 frames, half-open, one source; no padding, freeze or repetition; no joins.

Non-blocking notes
- Caption 62.09-63.63 has no JP line (approved JP for L010 begins at the following caption); consider moving the first JP line earlier if timing allows.
- The clip ends ~0.1 s before the next speaker words ("you know"); tight but clean.

