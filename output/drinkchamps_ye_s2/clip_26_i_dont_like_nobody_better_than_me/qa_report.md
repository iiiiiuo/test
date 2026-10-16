# Clip_26 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `dfc8cd6ed1b7131a08a1b4f9f251224fa0a20790c4eb2000b7b85c15d1063f8c`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 82.165 s, audio 82.165 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1970 (manifest 1970)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1970, "expected_frames": 1970, "video_duration_s": 82.165416, "audio_duration_s": 82.165, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 177, "asr_words": 184, "matched": 160, "match_ratio": 0.904, "matched_words_inside_their_caption": 0.95, "caption_onset_vs_first_word_s": {"n": 24, "median": -0.061, "max_abs": 2.581}}

## Critic rounds
- round 1: PASS — non-blocking: 'Right.' caption lags ~0.9 s at 60.01 → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (largest non-blocking: "Right." caption at 60.01-60.81 lags the spoken "Right" at ~59.1-59.4 by ~0.9s)
Fix: none

1. Structure: PASS. Opens on "Can we address this hat?" (speech onset ~0.14s, low-level noise before it, no clipped word per source audio). Ends on "I love the respect." (audio level still ~8000 at 81.7, decays by 82.1; source "Yeah" after is excluded). Jump cut at 27.94 ("...right now." then "So that...") reads naturally; sync.txt shows "so you can't say this right now" then "so that".
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 82.165 s, audio 82.165 s, 1970 frames = expected 1970, no decode errors.
3. Transcript: PASS. 160/184 ASR words matched; all caption text agrees with HEARD (differences are ASR noise: "Russia" for "Watch the Throne", "yay" for "Ye").
4. Translation: PASS. Approved rev2 wording used. JP verb-final split in L003 shows "政権に就ける時だ" during "that cares about us" (13-19.7s); acceptable as approved wording, not a clear error.
5. Masking: PASS. auto.json unmasked_hits empty; no listed curse words in the clip text; JP not masked.
6. Timing/sync: PASS. Onset median -0.06s vs first heard word, 95% matched words inside their caption. No caption under ~0.8s except brief "Right." / "2024..." fragments (0.8s, readable). No uncaptioned full foreground sentence; 64.0-68.3s is Ye's silent thinking pause after the VP question (meaningful pause, frame f_0064.36 shows him reacting).
7. Typography/visuals: PASS. White bold Yu Gothic, black outline+shadow, centred EN over JP, 2+2 lines max, position/size match ref_20.png and ref_sheet.jpg (f_0054.78, f_0073.60 checked); no overflow or clipping.
8. Framing: PASS. Faces in the sharp centre band with blurred fill above/below like the reference. Crop changes (3.46, 25.69, 27.94, 35.95, 43.46, 47.71, 61.27, 64.23, 71.49, 76.87) coincide with scene-detect cuts in the render.
9. Source usage: PASS. Single source part_3; two half-open intervals [44628,45298) and [45450,46750) = 670 + 1300 = 1970 frames; audio segments match video; no freeze, padding or repeats.

Non-blocking notes
- "2024..." caption (5.40-6.20) starts ~0.7s after the spoken "2024" (audio energy from ~4.7s).
- "Right." caption (60.01-60.81) lags the spoken "Right" at ~59.1-59.4; caption 17 ends at 59.34 so "Right" is heard just before its caption.
- JP line split in L003 puts "俺たちを気にかける人間を" on the "that is us" caption and "政権に就ける時だ" on "that cares about us"; consider re-timing the split only if a re-render happens anyway.

