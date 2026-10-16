# Clip_11 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `d9a24657387e7cc9fab88b92621357290963d22b8ae35b36d1df07ad9c7b5d80`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 85.919 s, audio 85.919 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 2060 (manifest 2060)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 2060, "expected_frames": 2060, "video_duration_s": 85.919166, "audio_duration_s": 85.919, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 226, "asr_words": 231, "matched": 218, "match_ratio": 0.965, "matched_words_inside_their_caption": 0.991, "caption_onset_vs_first_word_s": {"n": 30, "median": 0.084, "max_abs": 0.676}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

## Items
1. Structure: PASS. Opens on "Like Moses had four chapters" (sync.txt 0.00; source_context shows "...moses like think about" just before, clip starts at a clean phrase). Ends on "but they've erased that, even that" (85.90), resolved thought; next source speech is a new topic (contracts). Standalone-understandable.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 85.919 s / audio 85.919 s, frames 2060 = expected 2060, no decode errors.
3. Transcript accuracy: PASS. HEARD lines match all 31 captions (match_ratio 0.965, 0.991 inside caption); the only differences are ASR errors ("wider", "fall", "somewhere") against turbo-ASR source context that reads "whiter", "father".
4. Translation fidelity: PASS. All 31 captions carry JP matching the English moment; no clear errors or misattachment (e.g. L26/L27 repeated "Your father and the Father above" split 自分の父親と / 天にいる父だよ, matches the repeated speech).
5. Masking: PASS. auto.json unmasked_hits = []; no listed curse words in the English; JP not mechanically masked.
6. Timing/sync: PASS. Median onset offset 0.084 s, max 0.676 s (one caption, no lag into the next sentence seen in sync.txt). Shortest captions "But see, look" (0.72 s) and "Some people are more..." (0.92 s) are short but one-liners/brief and readable. No uncaptioned foreground sentences (gap 76.51-76.93 is a pause).
7. Typography/visuals: PASS. White bold Yu Gothic-style text, black outline/shadow, EN above JP, centred, placed in the lower part of the sharp band at a position matching the reference sheet; max 2 EN + 2 JP lines; no clipping (f_0000.05, f_0043.46). Readable on the bright yellow and dark backgrounds.
8. Framing: PASS. Faces/heads centred in the 1080x1042 sharp band with blurred fill above/below, as in reference; framing changes coincide with shot changes (Ye / interviewer cuts). The interviewer reaction shot at ~43 s while Ye speaks is natural.
9. Source usage: PASS. Single interval part_3 frames [21216,23276) half-open, audio same range, one continuous cut; no padding, freeze or repetition (the repeated "Your father and the Father above" is real source repetition).

## Non-blocking notes
- Caption L12 (38.14-39.06) and L15 (43.88-44.60) are on screen under 1 s; legible but brisk.
- First four-line caption block (0-4.7 s) is long; within the 2+2 rule.

