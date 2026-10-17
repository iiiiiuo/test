# Clip_28 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `0cb5125b77e9f6beb86ed423e7f4078520d8244cba0bac831020748c7896c293`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 64.648 s, audio 64.648 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1550 (manifest 1550)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1550, "expected_frames": 1550, "video_duration_s": 64.647916, "audio_duration_s": 64.648, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 241, "asr_words": 241, "matched": 226, "match_ratio": 0.938, "matched_words_inside_their_caption": 0.956, "caption_onset_vs_first_word_s": {"n": 27, "median": -0.078, "max_abs": 0.918}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items
1. Structure: NOT IN SCOPE
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 64.648 s / audio 64.648 s, 1550 frames = expected 1550, decode_errors empty.
3. Transcript: NOT IN SCOPE
4. Translation: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS. No f/s/b/ni/p-words in srt/ass; auto.json unmasked_hits = []; JP not masked.
6. Timing: NOT IN SCOPE
7. Typography/visuals: PASS. f_0003.84, f_0016.85, f_0039.94 vs ref_20: white bold Yu Gothic, black outline+shadow, EN above JP, centred, same position/size as reference; up to 2 EN + 2 JP lines, no clipping.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS. All 7 rows (L003, L004, L006, L007, L009, L011, L012) match glossary_draft_s2.json verbatim (line breaks only differ). Durations 3.7-8.4 s, each starts with the caption showing the term. Style Expl (Yu Gothic, white, outline 3, shadow 2). Rows at y 1138-1284 (about 1332 bottom), inside the sharp band 438..1480, below the 4-line EN/JP block (bottom about 1158 vs top 1188) with no overlap in the frames checked. No word/name split awkwardly (L006 breaks after the sentence, L011 and L012 at clause boundaries).

Non-blocking notes
- Gap between a 4-line EN+JP block and the Expl row is about 30 px, tight but not overlapping.

