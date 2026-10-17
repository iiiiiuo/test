# Clip_33 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `d6ff20f0da4b7fd20ca98890789e0e872b703b3b79f1e857673dd096f5c649e9`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 83.709 s, audio 83.708 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 2007 (manifest 2007)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 2007, "expected_frames": 2007, "video_duration_s": 83.708625, "audio_duration_s": 83.708, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 239, "asr_words": 249, "matched": 234, "match_ratio": 0.979, "matched_words_inside_their_caption": 0.996, "caption_onset_vs_first_word_s": {"n": 22, "median": 0.104, "max_abs": 0.474}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json 1080x1920, SAR 1:1, video 83.709 s / audio 83.708 s, frames 2007 = expected 2007, no decode errors.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits = []; no unmasked listed words in SRT or ASS dialogue text; no mechanical asterisks in JP.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals vs reference: PASS - f_0043.35, e_50.5, e_79 show white bold Yu Gothic with black outline+shadow, centred, EN above JP at the same vertical position (y~950-1150) as the reference, max 2 EN + 2 JP lines, no clipping.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
 - Text matches glossary_draft_s2.json verbatim: L007 Kim (41.28-48.40, 7.1 s), L008 大統領になれる歳 (48.42-52.93, 4.5 s), L011 アーミッシュ (71.99-83.69, 11.7 s). Line breaks fall between phrases, no word or name split.
 - Each row starts with the caption showing the term (Kim at 41.28, 大統領 at 48.42, アーミッシュ at 71.99) and stays up while it is spoken.
 - Position y=1188/1236 (rendered ~1190-1270): below the JP row (ends ~1145), no overlap, inside the sharp band 438..1480; widest line (L011) spans x~165-915, inside the frame.
 - Style Expl: Yu Gothic bold, white fill, black outline, shadow, 40 px; visibly smaller than the 50-54 px EN/JP.

Non-blocking notes
- L011 explanation appears at 71.99 while "Amish" is spoken about 75 s (JP "アーミッシュの" is already on screen at 71.99); acceptable.

