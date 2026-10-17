# Clip_30 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `d1a025a3752392513f999b4e286e54f84977d1df9b9893ae88f231c3799255c1`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 94.761 s, audio 94.761 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 2272 (manifest 2272)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 2272, "expected_frames": 2272, "video_duration_s": 94.761333, "audio_duration_s": 94.761, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 247, "asr_words": 257, "matched": 245, "match_ratio": 0.992, "matched_words_inside_their_caption": 0.922, "caption_onset_vs_first_word_s": {"n": 28, "median": -0.334, "max_abs": 1.494}}

## Critic rounds
- round 1: FAIL — opens on uncaptioned tail 'thing is' (0-0.25 s) → start window 51.62-51.78 (frame ~1238)
- round 2: PASS — non-blocking: 0.06 s tail of 'is,' at open → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items
1. Structure: NOT IN SCOPE
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 94.761 s, audio 94.761 s (60 <= d < 120), 2272 frames = manifest/expected, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS. No profanity in any caption (en_unmasked scan) and no unmasked hits in srt/ass/auto.json; Japanese contains no asterisks.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS. ASS style Sub = Yu Gothic Bold, white, black outline 3 + shadow 2; EN above JP, centred, max 2 EN + 2 JP lines (auto max_lines 4); frames f_0004.44 and f_0008.01 and sheet_2 show no clipping, readable on busy background.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS. Only glossary entry for this clip is Clip_30_L001; ASS Expl text (two lines) equals the draft verbatim ("Tuskegee：1932〜72年、米公衆衛生局が黒人男性の / 梅毒を治療せずに経過観察した人体実験"); shown 3.08-10.32 s (7.24 s), starting with the caption that shows "Tuskegee"; at y 1188/1236 (inside 438..1480), JP row ends about y 1130 so no overlap in f_0004.44 / f_0008.01; Expl style = Yu Gothic Bold white, outline 3, shadow 2, fs40; line break falls between phrases, no word split.

Non-blocking notes
- The Expl row stays up through captions at 5.82-8.76 s (different lines) as well; it is readable and does not collide, so left as is.

