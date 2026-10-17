# Clip_08 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `a019ff5ee8bb3fddf78274927ff11ec7cdd19326fb58eef2a7a67d781c1bfe95`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 80.706 s, audio 80.705 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1935 (manifest 1935)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1935, "expected_frames": 1935, "video_duration_s": 80.705625, "audio_duration_s": 80.705, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 252, "asr_words": 248, "matched": 225, "match_ratio": 0.893, "matched_words_inside_their_caption": 0.964, "caption_onset_vs_first_word_s": {"n": 24, "median": 0.001, "max_abs": 0.938}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items (scope: 2, 4 [no changed lines], 5, 7, 10)
1. NOT IN SCOPE
2. PASS - auto.json: 1080x1920, SAR 1:1, video 80.706 s / audio 80.705 s (60 <= d < 120), 1935 frames = expected, decode_errors empty.
3. NOT IN SCOPE
4. PASS (no changed lines; nothing to judge)
5. PASS - auto.json unmasked_hits [], ASS grep shows only "s**t" (24.06 caption); Japanese not mechanically masked ("それ双子座あるあるだな").
6. NOT IN SCOPE
7. PASS - frames f_0022.01, f_0044.21, f_0047.38, f_0053.89 vs ref_20.png: white bold Yu Gothic, black outline+shadow, EN above JP, centred, same top-row y (~948-975), max 2 EN + 2 JP lines (4-line frame at 22.01 ends ~y1140), inside sharp band 438..1480, no clipping, readable on bright and dark backgrounds.
8. NOT IN SCOPE
9. NOT IN SCOPE
10. PASS - three explanation rows, all verbatim vs glossary_draft_s1.json (L008, L009, L011; L011 split into two lines after "。", no word split):
 - L008 "Big Boi：ヒップホップデュオOutKastのメンバー" 39.84-44.51 (4.67 s), starts with caption "Big Boi, man."; judged from frame f_0044.21 (in span): single line, y~1208, no EN/JP on screen in that gap, within band.
 - L009 "Big Boy：ロサンゼルスの人気ラジオDJ" 44.53-48.39 (3.86 s), starts with caption "Oh, it's about OutKast? ... Big Boy Radio"; judged from f_0045.84/f_0047.38 (in span): y~1208 vs JP row bottom ~1095, no overlap, within band.
 - L011 "『Ms. Jackson』：OutKastの2000年のヒット曲。/元恋人の母親への謝罪がテーマ" 53.23-60.34 (7.11 s), starts with the "Sorry Ms. Jackson" caption; judged from f_0053.89 (in span): two lines y~1208/1255, no overlap with EN/JP (bottom ~1040), within band (<1480).
 All use Expl style: Yu Gothic Bold 40, white fill, black 3 px outline, 2 px shadow (ASS style line), smaller than JP (50), matching rendered look.

Non-blocking notes
- At 44.11-44.53 the L008 row stays up while no EN/JP is shown (0.4 s gap); harmless.
- With 4-line EN+JP blocks the clearance to the explanation row (y1188) is ~40 px; none of the three explanation spans coincides with a 4-line block here.

