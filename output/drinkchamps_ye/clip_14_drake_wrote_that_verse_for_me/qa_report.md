# Clip_14 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `9caada490330759f4bc0dcf51341e3e954a571a077aac2a1c52289bab0790f8e`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 61.770 s, audio 61.770 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1481 (manifest 1481)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1481, "expected_frames": 1481, "video_duration_s": 61.770041, "audio_duration_s": 61.77, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 199, "asr_words": 197, "matched": 187, "match_ratio": 0.94, "matched_words_inside_their_caption": 0.947, "caption_onset_vs_first_word_s": {"n": 21, "median": 0.02, "max_abs": 1.58}}

## Critic rounds
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items
1. NOT IN SCOPE
2. PASS - auto.json: 1080x1920, SAR 1:1, video 61.770 s, audio 61.77 s, 1481/1481 frames, no decode errors.
3. NOT IN SCOPE
4. PASS (Clip_14_L010, 47.07-51.68) - JP = ja_final (Drakeがそれを verseに仕上げて / ラップ全部書いたんだよ), reflowed to 2 JP lines; matches EN meaning (frame f_0049.38).
5. PASS - auto.json unmasked_hits empty; no fuck/shit/bitch/nigg/pussy in the SRT; JP not masked.
6. NOT IN SCOPE
7. PASS - frames f_0049.38, extra/e_15.5.png, extra/e_18.5.png: white bold Yu Gothic, black outline and shadow, EN above JP, centred, at the same position as the other captions, max 2 EN + 2 JP lines, inside the frame.
8. NOT IN SCOPE
9. NOT IN SCOPE
10. PASS - Expl row for Clip_14_L003 is the approved text verbatim ('『30 Hours』：2016年の' + 'アルバム『The Life of Pablo』の収録曲'). It shows 12.88-19.60 s (6.7 s), starting with the caption that shows '30 Hours' (the 12.88 caption has the term; the term is also in the 14.57 caption). Rows are at y=1188 and 1236, below the 4-line EN+JP block (ends about 1150), and inside the sharp band (438..1480). Same font, white fill, black outline and shadow, smaller size. The break falls after の, between phrases, so no word or name is split. Remains on screen to 19.60 during the L004 captions without overlap.

Non-blocking notes
- None.

