# Clip_15 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `12884c74991ff5e5336f30b9ba2df5c695af73c1ee56d00c6e34c7a2ad3eface`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 76.827 s, audio 76.827 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1842 (manifest 1842)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1842, "expected_frames": 1842, "video_duration_s": 76.82675, "audio_duration_s": 76.827, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 222, "asr_words": 229, "matched": 207, "match_ratio": 0.932, "matched_words_inside_their_caption": 0.986, "caption_onset_vs_first_word_s": {"n": 28, "median": 0.1, "max_abs": 0.63}}

## Critic rounds
- round latest: FAIL — two uncaptioned host sentences; duplicate JP on "Yeah." → jump cuts 1171.355-1173.385 and 1184.17-1187.235; L005 chunk override

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items (scope: 2, 5, 7, 10; item 4 not applicable, CHANGED_LINES = none)
1. Structure: NOT IN SCOPE
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 76.827 s, audio 76.827 s, 1842 frames = expected 1842, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (no changed lines)
5. Masking: PASS. auto.json unmasked_hits = []. A grep of ass/srt for pussy/shit/fuck/nigg/bitch finds nothing. EN shows "p**sy" (7 events, including "get-p**sy toe"). Japanese uses モテる/ヤってる, not mechanically masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS. Frames e_43.5, e_47.0, e_51.0 (extra/) against ref_20: white bold Yu Gothic, black outline and shadow, EN above JP, centred, same start y (~948) as the reference. Max 2 EN + 2 JP lines. Nothing clipped, all inside the sharp band, readable on the bright yellow background.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS.
 - Text matches glossary_draft_s1.json verbatim: Clip_15_L009 "350：Yeezy Boost 350。YeがAdidasと作ったスニーカー" (two lines, break between sentences) and Clip_15_L011 "Steve Stoute：音楽・広告業界の実業家".
 - Timing: the first runs 42.40-48.23 s (5.8 s). It starts with the "350s" caption and stays up through "So that was the whole point". The second runs 48.25-52.37 s (4.1 s) and covers the "Steve Stoute know" caption. Both are readable.
 - Position: style Expl is Yu Gothic bold, white, outline 3, shadow 2, 40 px. Rows are at y 1138/1186 and 1188, below the last EN/JP line (4-line caption ends about 1150) with a visible gap and no overlap, and above the y 1480 band limit.
 - No word or name is split by a line break.

Non-blocking notes
- The two explanations sit at slightly different y (first row 1138 for a 2-line EN/JP block, second 1188 for a 4-line block). This is intentional and does not collide.

