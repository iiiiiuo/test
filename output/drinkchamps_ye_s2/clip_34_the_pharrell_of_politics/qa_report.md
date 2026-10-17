# Clip_34 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `328257d28fec2c0885884ccd384c46af2087c06dbb491e8256f83499445fa5e0`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 83.125 s, audio 83.125 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1993 (manifest 1993)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1993, "expected_frames": 1993, "video_duration_s": 83.124708, "audio_duration_s": 83.125, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 206, "asr_words": 208, "matched": 187, "match_ratio": 0.908, "matched_words_inside_their_caption": 0.963, "caption_onset_vs_first_word_s": {"n": 25, "median": -0.012, "max_abs": 1.402}}

## Critic rounds
- round 1: FAIL — 'Yeah.' caption carried JP of later 'I fuck with you'; 2.2 s uncaptioned interjection at 65.95-68.15 → L004 chunks override; CUTS 1718.13-1720.13 removing unapproved 'You're transcending'
- round 2: PASS — non-blocking: JP word order lags EN 58.7-66.1 → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items (scope: 2, 5, 7, 10; item 4 CHANGED_LINES = none; 1, 3, 4, 6, 8, 9 NOT IN SCOPE, no blocking problem noticed)
2. PASS - auto.json: 1080x1920, SAR 1:1, video 83.1247 s, audio 83.125 s, frames 1993 = expected 1993, no decode errors.
5. PASS - auto.json unmasked_hits empty; SRT/ASS show s**t, f**k, ni**a; Japanese not mechanically masked.
7. PASS - white bold Yu Gothic, black outline+shadow, EN above JP, centred, max 2 EN + 2 JP lines, inside frame and inside the sharp band (f_0015.71, f_0066.11, crops in qa/extra); matches ref_sheet geometry.
10. PASS - two Expl events, text verbatim from glossary draft: Clip_34_L002 "Tシャツ：“White Lives Matter”Tシャツ" (14.40-19.17 s, 4.8 s, starts with the caption showing "t-shirt", pos y=1188, below the 4-line EN/JP block that ends about y=1145, no overlap); Clip_34_L013 "Haro・GT：BMX自転車のブランド" (61.03-69.25 s, 8.2 s, starts at the JP caption with HaroとかGT, y=1138, below the 2-line block, no overlap). Same font, white fill, black outline/shadow, fs40, single line, no word split, inside y 438..1480.

Non-blocking notes
- A 20 ms gap in EN/JP captions at 66.13-66.15 s (at the jump cut) is the normal inter-caption gap; the Expl row stays on across it.

