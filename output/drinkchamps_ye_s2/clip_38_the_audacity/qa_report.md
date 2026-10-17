# Clip_38 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `678294ca826f7581d922915048fcb9de853ccdeffca14cd7bcd8d0963f5959f3`.

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
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json: 1080x1920, SAR 1:1, video 75.409 s, audio 75.408 s, 1808 frames = expected, no decode errors.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - only "s**t" (caption L003) in displayed EN; no unmasked shit/fuck/nigga/bitch/pussy in srt/ass; auto.json unmasked_hits empty; JP has no asterisks.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - f_0007.98.png, extra/f_61.0.png, extra/f_62.6.png: white bold Yu Gothic, black outline+shadow, EN above JP centred, same size/position as reference, max 2 EN + 2 JP lines (4 lines at 61.0 s), nothing clipped.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
 - Text matches glossary_draft_s2.json verbatim: Clip_38_L002 "Tucker Carlson：Fox Newsの司会者。/2022年10月にYeをインタビューした" (two lines, break after 。); Clip_38_L009 "White Lives Matter：Yeが着て物議を醸したTシャツ" (one line).
 - Timing: 6.17-13.41 s (7.2 s), starts with the Tucker Carlson caption; 60.25-65.67 s (5.4 s), starts with the White Lives Matter caption.
 - Position: Expl rows at y 1188/1236 (font 40), inside the sharp band 438..1480. Worst case, the 4-line EN/JP block at 61.0 s ends about y 1145, above the Expl top of about 1190, so no overlap.
 - Style: same font, white fill, black outline and shadow as Sub; width about 750 px, within the frame; no awkward word or name break.

Non-blocking notes
- Caption at 62.09-63.63 s ("that would have the audacity to have") has no JP row (auto.json captions_without_jp = Clip_38_L010). The JP for this line is on the next caption, and the pipeline reports the caption timing as identical to the previous render. Out of scope here.

