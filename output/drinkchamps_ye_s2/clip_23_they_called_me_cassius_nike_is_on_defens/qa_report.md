# Clip_23 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `fc245faf456620bfb0e02c3c6f0eab3ec473d622caa71f0b15c045e5e4fe21b8`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 86.253 s, audio 86.253 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 2068 (manifest 2068)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 2068, "expected_frames": 2068, "video_duration_s": 86.252833, "audio_duration_s": 86.253, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 243, "asr_words": 262, "matched": 227, "match_ratio": 0.934, "matched_words_inside_their_caption": 0.956, "caption_onset_vs_first_word_s": {"n": 28, "median": -0.071, "max_abs": 1.003}}

## Critic rounds
- round 1: FAIL — final word 'about' cut ~0.25 s early; 'fit in' clipped at join → hand end windows 1143.08-1143.14 and 1197.24-1197.30 (frames 27408, 28706)
- round 2: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: PASS. Starts in silence 0.41s before "You know" (source energy: speech onset 1096.84s, clip start 1096.43s). Ends on "That was what the deal was about." with a sentence-final energy drop at 1197.28s. The jump cut at 46.71s joins "so I could fit in" to "Think about like Nike" and reads naturally, with a topic shift and no meaning distortion.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 86.2528s, audio 86.253s, 2068 of 2068 frames, no decode errors.
3. Transcript accuracy: PASS. sync.txt HEARD lines match the displayed English; the differences are ASR errors (Ali/Mali, Gemini/jim, Ye/yay) and the masked words.
4. Translation fidelity: PASS. No clear errors. The splits on L027 and L028 ("中国と取引してる" and "Fortune 500の企業に「Gapは低所得層の地域に") follow the approved rows.
5. Masking: PASS. "f**k" (cap 1) and "ni**as" (cap 22) are masked, with no unmasked hits in auto.json. The Japanese is not masked.
6. Timing/sync: PASS. Caption onset vs first heard word has median -0.07s. 95.6% of matched words fall inside their caption. All 30 captions are at least 1.2s long. There are no uncaptioned foreground sentences.
7. Typography/visuals: PASS. Compared with ref_sheet.jpg: white bold Yu Gothic with black outline and shadow, EN above JP, centred at the same vertical band, max 2 EN + 2 JP lines, nothing clipped, readable on the bright yellow background.
8. Framing: PASS. Ye is centred and sharp in the middle band with blurred fill above and below. Cutaways to the host (about 40.9s, 42-43s, 46.8s) are properly framed. The framing change is at shot changes only.
9. Source usage: PASS. Two half-open intervals from part_1, frames 26288-27408 and 27758-28706, with no overlap or repetition. There is no padding or freeze.

Non-blocking notes
- The first caption appears at 0.32s, about 0.09s before the speech onset at 0.41s of the clip, which is not noticeable.
- The jump-cut audio at 46.71s ends tightly at 1143.142s. The energy dip is clean.

