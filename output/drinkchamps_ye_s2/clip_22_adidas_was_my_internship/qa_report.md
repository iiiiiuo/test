# Clip_22 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `f845f5121c727db55bebb2ab89082ec9172eb8b9b2fab49465e356d51ab22935`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 95.554 s, audio 95.554 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 2291 (manifest 2291)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 2291, "expected_frames": 2291, "video_duration_s": 95.553791, "audio_duration_s": 95.554, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 276, "asr_words": 284, "matched": 266, "match_ratio": 0.964, "matched_words_inside_their_caption": 0.996, "caption_onset_vs_first_word_s": {"n": 34, "median": 0.0, "max_abs": 0.855}}

## Critic rounds
- round 1: PASS — none (note: JP names 3 s early at 73.81-77.03) → chunks override Clip_22_L019
- round 2: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json 1080x1920, SAR 1:1, video 95.554 s / audio 95.554 s (60 <= d < 120), 2291 frames = expected, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits = []; no curse words in the displayed English (SRT read in full); Japanese not mechanically masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - frames at 5, 9.9, 10.5, 80.39, 93.84 s: white bold Yu Gothic, black outline and shadow, EN above JP, centred, max 2 EN + 2 JP lines (4 lines), same size and position as the series reference, no clipping, readable on the bright yellow background.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
 - Text matches glossary_draft_s2.json verbatim: L001 Sway, L019 Bernard Arnault / ベゾス (two lines), L021 D'Usse (two lines); no word split by the line breaks.
 - Timing: Sway 1.61-10.28 s (8.7 s, starts with the caption that says "Sway"); Bernard Arnault 77.05-83.77 s (6.7 s, starts with the caption that says "Bernard Arnault"); D'Usse 89.74-95.53 s (5.8 s, starts with the caption that says "D'Usse"). All are 2 s or longer.
 - Layout: rows at y=1188 and y=1236, fs40. They sit below the EN/JP block (which ends at about y=1145) with no overlap, inside the sharp band (y 438..1480). Verified in frames 5, 9.9, 80.39 and 93.84 s.
 - Style: ASS Expl is Yu Gothic bold, white fill, black outline 3, shadow 2, the same as Sub. The render shows the same look as the EN/JP rows. It is correctly absent at 10.5 s, after the row ends.

Non-blocking notes
- The Sway row stays up about 4.9 s after its caption (which ends at 5.4 s) gives way to other lines. This is acceptable and was not flagged.

