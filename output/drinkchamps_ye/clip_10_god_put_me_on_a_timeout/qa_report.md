# Clip_10 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `74eecdfd8c530cf542e83d9885d8962db6f46f4a993d319791474fd3888cdd1c`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 71.613 s, audio 71.613 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1717 (manifest 1717)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1717, "expected_frames": 1717, "video_duration_s": 71.613208, "audio_duration_s": 71.613, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 178, "asr_words": 187, "matched": 170, "match_ratio": 0.955, "matched_words_inside_their_caption": 0.988, "caption_onset_vs_first_word_s": {"n": 25, "median": 0.09, "max_abs": 0.78}}

## Critic rounds
- round 1: FAIL — wide shot 19252-19331 cut Ye off at right edge; caption "But..." 1.2 s early → manual 1.2x punch crop on Ye for that shot (work/b/framing_overrides.json); timing rules
- round latest: FAIL — JP for Jewish/black people shown 3-6 s early; "He offered it." repeat uncaptioned; "But" early → chunk override for L014 (EN-only lead-in), L004 window extended to 794.95, primary ASR pass chosen by match count

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json 1080x1920, SAR 1:1, video 71.613 s, audio 71.613 s, 1717/1717 frames, no decode errors.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits empty; ASS shows "Real s**t."; no other listed words appear in the ASS; JP not mechanically masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - f_0010.16.png and f_0014.28.png show white bold Yu Gothic with black outline and shadow, centred, EN above JP, at the same vertical position as ref_20.png; max 2 EN + 2 JP lines; no clipping.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term explanation row: PASS - one row (Clip_10_L003) in ASS style Expl, 8.29-16.51 s (8.2 s). The text matches glossary_draft_s1.json verbatim: "アカウント停止：2022年10月、Yeの投稿が問題視されTwitterアカウントが凍結された". It is split over two lines at y=1188 and y=1236 with no word broken. It covers both L003 caption events (8.29-12.03 and 12.05-16.51). Judged from render frames f_0010.16.png (inside the first event) and f_0014.28.png (inside the second); both show the row. It sits at about y 1190-1275, below the JP row (about y 1100-1145) with a clear gap and inside the sharp band 438..1480. Same font, white fill, black outline and shadow, smaller size. No extra frames were needed.

Non-blocking notes: none

