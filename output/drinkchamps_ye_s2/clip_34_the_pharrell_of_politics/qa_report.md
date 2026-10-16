# Clip_34 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `56f684ea752e2ae117fd75e7b92cf1dc0674c40eeed8f299292d18ee505ce8c2`.

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
Largest gap: none (JP for the long Harley-Davidson/BMX sentence is split across 3 captions in Japanese word order, so JP lags EN content at 58.7-66.1s; non-blocking)
Fix: none

1. Structure: PASS. Opens on host's "Like, this real s**t..." right after "Go ahead" (audio starts at the "Like"); coherent Q&A (plight -> producer -> Pharrell -> BMX/nerd), ends on "We love you. We're ruling the world right now." (source 1737.22, sentence complete, next source line is a separate "Yeah, that's what I'm saying").
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 83.125s / audio 83.125s, frames 1993 = expected 1993, decode_errors empty.
3. Transcript: PASS. sync.txt matches source ASR; differences are ASR noise ("I can see you" vs heard "consider", "Is this for me?" before "I'm the first time" is not shown, minor).
4. Translation: PASS. JP matches approved CSV rows; L004 "Yeah." intentionally has no JP. Meaning correct throughout.
5. Masking: PASS. s**t x3, f**k, ni**a masked in EN; auto.json unmasked_hits empty; JP not mechanically masked.
6. Timing/sync: PASS. Median onset offset -0.01s; no caption under 0.45s except the "Pharrell." single-word 0.45s caption (49.35-49.80, spoken single word, acceptable); no uncaptioned foreground sentence.
7. Typography/visuals: PASS. sheet_1/2 vs ref_sheet: white bold Yu Gothic, black outline/shadow, EN above JP, centred at same height (~y 950-1050), max 2 EN + 2 JP lines, no clipping, readable on bright yellow background.
8. Framing: PASS. Faces centred in sharp band with blurred fill; crop changes align with speaker/shot changes (Ye close-ups, host shot at 3-10s and 14-17s).
9. Source usage: PASS. part_5, two half-open intervals [39610,41193) and [41241,41651), gap 48 frames = intentional jump cut; join at 66.02s lands in a speech pause (RMS lull 65.3-66.0s), resumes "a Haro GT" naturally, meaning intact; no padding/repetition (the repeated "Pharrell" is spoken content).

Non-blocking notes
- 58.75-66.13s: JP for one long EN sentence is distributed in Japanese order (hat / bike / "first Black person" last), so the JP on screen does not line up word-for-word with the EN beneath it; reads coherently in sequence.
- Caption 21 ("riding on a, you know,") runs ~0.1s past the jump cut at 66.02s.

