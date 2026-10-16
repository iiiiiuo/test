# Clip_33 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `3e47b274c2e83bcfedee6f47cd5867569077c7f0d957827d25f35b047b8868ee`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 83.709 s, audio 83.708 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 2007 (manifest 2007)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 2007, "expected_frames": 2007, "video_duration_s": 83.708625, "audio_duration_s": 83.708, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 239, "asr_words": 249, "matched": 234, "match_ratio": 0.979, "matched_words_inside_their_caption": 0.996, "caption_onset_vs_first_word_s": {"n": 22, "median": 0.104, "max_abs": 0.474}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items
1. Structure: PASS. Opens on Ye's "I'm always being honest" (audio is a low-energy pause at 1093.88, speech onset ~0.2s), ends on "Louis Vuitton." (source 1177.54, next thought "I still..." excluded); coherent single argument, standalone.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 83.7086s / audio 83.708s, 2007 frames = manifest, decode_errors empty.
3. Transcript: PASS. sync.txt match ratio 0.979; only meaningful difference is 12.36 caption "You know, I'm here, right?" where ASR also hears "what I'm saying? It's like" (trimmed filler); no meaning change.
4. Translation: PASS. All 23 captions carry JP; JP matches approved CSV and the English meaning (checked 2.56, 34.36, 48.42, 66.28, 81.61). Long approved JP lines are split across consecutive captions correctly.
5. Masking: PASS. auto.json unmasked_hits empty; no listed curse words in the text.
6. Timing/sync: PASS. Onset vs first heard word median 0.10s, max 0.47s; matched words inside own caption 99.6%; shortest caption ~1.9s; no uncaptioned foreground sentence (host "Yeah" at ~34s is captioned).
7. Typography: PASS. Frames f_0000.05/0004.90 and sheets show white bold Yu Gothic with black outline/shadow, EN above JP, centred, same vertical position and size as ref_sheet; max 2 EN + 2 JP lines; no clipping.
8. Framing: PASS. Ye and the host faces sit in the sharp centre band with blurred fill; crop changes only at shot changes (host to Ye at ~0.7s, Ye to host ~32s, back to Ye ~34s).
9. Source usage: PASS. Single interval part_5 frames [26226, 28233), half-open, 24000/1001, audio same range; no padding/freeze/repetition.

Non-blocking notes
- 0.0-0.7s shows the host's reaction shot while Ye's first line plays; reads as a natural reaction cut.
- First caption's JP shows only 俺はいつだって正直だ; the JP for "we'll get to that point" (その話はまたするとして) appears at the next caption (~0.6s after the English). Approved wording, split by design.

