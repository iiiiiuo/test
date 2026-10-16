# Clip_09 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `8ea513c487762b436b73b58c9d438f2d7273b36a656994bf66584c9b5f4e81b1`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 64.815 s, audio 64.815 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1554 (manifest 1554)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1554, "expected_frames": 1554, "video_duration_s": 64.81475, "audio_duration_s": 64.815, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 175, "asr_words": 188, "matched": 162, "match_ratio": 0.926, "matched_words_inside_their_caption": 0.951, "caption_onset_vs_first_word_s": {"n": 19, "median": -0.043, "max_abs": 1.623}}

## Critic rounds
- round 1: FAIL — ended on dangling "But it's funny," → end moved to after "...thousand back." (247.125 s); JP tail segment 笑えるよな dropped (approved segments only)
- round latest: PASS — none → frozen

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (non-blocking: JP/EN pairing is offset by one caption at 0-1.3s and 40.76-44.15s)
Fix: none

Items
1. Structure: PASS - starts on "Like, you know" right after a sample dip at ~182.18s (word boundary), ends after "...a couple hundred thousand back." (audio onset of next "But" at ~247.14s, clip ends 247.12s). Self-contained story (bills -> billionaire -> Shaq anecdote).
2. Duration/format: PASS - auto.json 1080x1920, SAR 1:1, video 64.815s / audio 64.815s, 1554 frames = expected, no decode errors.
3. Transcript accuracy: PASS - captions match HEARD lines (0.93 token match, 95% inside caption). Omitted "what I mean and" (0.7-2.1s) and ASR-only "because he was paying himself" (57.5-58.6s, not in turbo source ASR, likely ASR error) are not meaningful mismatches.
4. Translation fidelity: PASS - JP matches approved rows and meaning. Note the split places 「俺がYeの代弁者だ」 on "Like, you know," (0-1.3s) and ちゃんと見てなかったせいで on "lost hundreds of millions" (40.76-44.15s), one caption ahead of the EN; the next caption carries the matching EN, so the pair reads together. Not clearly wrong.
5. Masking: PASS - auto.json unmasked_hits = []; no listed words occur in the EN; JP not masked.
6. Timing/sync: PASS - median onset offset -0.04s; every sentence of foreground speech is captioned; shortest caption 1.3s (first), others >=1.5s. Gaps (26.05-27.12, 30.28-31.16, 47.65-49.56) are speech pauses/speaker change.
7. Typography/visuals: PASS - white bold Yu Gothic with black outline/shadow, EN above JP, centred, at the same vertical band as the reference, max 2 EN + 2 JP lines, no clipping (sheet_1/2, f_0064.73).
8. Framing: PASS - Ye and both hosts are centred in the sharp band with blurred fill above/below; changes occur only at shot changes (framing sheet and sheets).
9. Source usage: PASS - single interval part_3 frames [4371,5925) = 1554 frames; no padding or repetition; no join.

Non-blocking notes
- Caption 1 JP line uses fs50 vs fs54 for all other lines (subtitles.ass first Dialogue pair); barely visible.
- Caption 1 (0-1.3s) is short and the JP quote appears ~1.7s before it is spoken; consider moving the JP to the following caption if the approved rows allow.

