# Clip_20 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `3feb1ec30e15a0f7a2cbfb1dbc1141ba0ace459ae2e0e37cc81007612b6e4f51`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 74.575 s, audio 74.574 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1788 (manifest 1788)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1788, "expected_frames": 1788, "video_duration_s": 74.5745, "audio_duration_s": 74.574, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 217, "asr_words": 214, "matched": 187, "match_ratio": 0.862, "matched_words_inside_their_caption": 0.92, "caption_onset_vs_first_word_s": {"n": 24, "median": 0.085, "max_abs": 5.605}}

## Critic rounds
- round latest: FAIL — D'Usse/Hennessy JP swapped across chunks → L004/L011 chunk overrides

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items (scope: 2, 5, 7, 10; item 4 CHANGED_LINES = none so not checked):
1. NOT IN SCOPE
2. PASS - auto.json: 1080x1920, SAR 1:1, video 74.5745 s, audio 74.574 s, 1788/1788 frames, no decode errors.
3. NOT IN SCOPE
4. NOT IN SCOPE (no changed lines)
5. PASS - auto.json unmasked_hits=[]; ASS shows s**t (4.84, 8.68) and f**k (41.23); sync.txt HEARD says shit/fuck so audio is uncensored; JP not mechanically masked; no other listed words in the captions.
6. NOT IN SCOPE
7. PASS - f_0007.33, f_0042.27 vs ref_20: white bold Yu Gothic, black outline+shadow, centred, EN above JP, max 2 EN + 2 JP lines, same vertical start (~y 950), no clipping, readable on the bright yellow background.
8. NOT IN SCOPE
9. NOT IN SCOPE
10. PASS - only Clip_20_L002 has an entry. Text "D'Usse：Jay-Zが共同所有していたコニャックのブランド" matches the draft verbatim (wrapped after たた, no word split). On screen 6.00-11.03 s (5.03 s); the D'Usse caption starts at 6.00 s. Style Expl, Yu Gothic bold, white fill, black outline and shadow, fs40, y 1188/1236. Frame f_0007.33 shows it below the JP row with a clear gap (JP bottom ~1145). Max EN+JP block bottom is ~1160 (4 rows at 948-1098), so no overlap in 6.00-11.03 s. Inside the sharp band (438-1480).

Non-blocking notes: the row stays up to 11.03 s, past the D'Usse caption (ends 8.66), which is fine for readability.

