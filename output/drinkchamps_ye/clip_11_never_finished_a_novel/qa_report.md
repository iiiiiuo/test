# Clip_11 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `61990de3dbc43403480bf4eb357de98224bd2286920fa233c8099ba90ecfbc65`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 85.919 s, audio 85.919 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 2060 (manifest 2060)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 2060, "expected_frames": 2060, "video_duration_s": 85.919166, "audio_duration_s": 85.919, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 226, "asr_words": 230, "matched": 220, "match_ratio": 0.973, "matched_words_inside_their_caption": 0.986, "caption_onset_vs_first_word_s": {"n": 30, "median": 0.084, "max_abs": 0.686}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json: 1080x1920, SAR 1:1, video 85.919 s, audio 85.919 s, 2060/2060 frames, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits = []; no listed word appears in the EN rows of subtitles.ass; JP rows are not mechanically masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - f_0001.00.png, extra/x_74.5.png and extra/x_76.95.png show white bold Yu Gothic with black outline and shadow, EN above JP, centred, at the same position and size as the previous render and the reference. The EN+JP block is at most 4 lines and nothing is clipped or outside the frame. Text stays readable on the bright yellow background.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
   - Text: both rows match glossary_draft_s1.json verbatim. Clip_11_L001 is "モーゼ：旧約聖書の預言者" and Clip_11_L016 is "天にいる父：キリスト教で神のこと". Each is a single line, so no word is split.
   - Timing: the L001 row runs 0.00-7.67 s (7.7 s) and covers both captions that show "Moses". The L016 row runs 73.89-76.97 s (3.1 s) and covers the caption "Your father and the Father above."
   - Layout: the row sits at y about 1188-1225, below the JP row, which ends about y 1145, so there is no overlap. It is inside the sharp band (438..1480).
   - Style: same font, white fill, black outline and shadow, at the smaller Expl size.

Non-blocking notes
- The L016 row ends at 76.97 s, 0.04 s (about 1 frame) into the next caption (starts 76.93 s). The row still shows during that one frame, over the unrelated "Now what has happened to the black community?" caption, as seen in x_76.95.png. It is essentially invisible. Ending the row at 76.51 s or 76.93 s would tidy it.
- The L016 row starts at 73.89 s, when the second "Your father and the Father above." caption appears. The same words were already on screen from 71.87 s, so the term shows about 2 s before its row. This is acceptable.

