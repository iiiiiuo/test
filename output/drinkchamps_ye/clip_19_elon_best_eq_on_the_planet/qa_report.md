# Clip_19 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `20f9cd07dd44bbd38e050b9a9e3e1621784f1f3aba55021ebb3ed37e309995c6`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 75.993 s, audio 75.992 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1822 (manifest 1822)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1822, "expected_frames": 1822, "video_duration_s": 75.992583, "audio_duration_s": 75.992, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 246, "asr_words": 245, "matched": 229, "match_ratio": 0.931, "matched_words_inside_their_caption": 0.965, "caption_onset_vs_first_word_s": {"n": 26, "median": 0.025, "max_abs": 0.545}}

## Critic rounds
- round latest: FAIL — IQ/EQ JP on wrong EN chunks → L010 chunk override

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items
1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json: 1080x1920, SAR 1:1, video 75.993 s / audio 75.992 s, 1822 frames = manifest, no decode errors.
3. Transcript: NOT IN SCOPE
4. Translation: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits empty; frame at 56 s shows "s**t?"; JP not masked.
6. Timing: NOT IN SCOPE
7. Typography/visuals: PASS - frames 10.5, 30, 56 s: white bold Yu Gothic, black outline+shadow, EN above JP, centred, same size/position as ref_20; 4-line blocks stay in frame.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS - 5 Expl events match glossary_draft_s1.json verbatim (L003 Ralph Lauren 8.16-15.03 = 6.9 s; L004 Vory/Wack 100 15.05-20.32 = 5.3 s; L007 Grimes 27.44-32.21 = 4.8 s; L008 EQ 33.58-37.18 = 3.6 s; L012 Kim 53.72-59.34 = 5.6 s). Each starts with the caption showing the term. Rows at y 1188/1236 (fs40), below the last JP line (y 1098), inside 438..1480. Same font/white/outline/shadow. Line breaks fall at clause boundaries ("当時の / マスクのパートナー"); terms on separate lines for L003/L004.

Non-blocking notes
- None.

