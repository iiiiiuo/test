# Clip_18 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `cc459848f12c2c279bf485a84f0bddcd40f9e060dfcda7b1f1ad0fce7b4c8949`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 72.322 s, audio 72.322 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1734 (manifest 1734)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1734, "expected_frames": 1734, "video_duration_s": 72.32225, "audio_duration_s": 72.322, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 247, "asr_words": 259, "matched": 238, "match_ratio": 0.964, "matched_words_inside_their_caption": 0.975, "caption_onset_vs_first_word_s": {"n": 28, "median": 0.022, "max_abs": 1.128}}

## Critic rounds
- round latest: FAIL — 0.47 s "You know what I'm saying?" with next sentence JP → L012 chunk override

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items (scope: 2, 5, 7, 10; item 4 CHANGED_LINES = none, not checked)
1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json: 1080x1920, SAR 1:1, video 72.322 s, audio 72.322 s, 1734/1734 frames, no decode errors.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (no changed lines)
5. Masking: PASS - auto.json unmasked_hits = []; no profanity in srt/ass/sync HEARD; Japanese not mechanically masked (clip has no listed masked words).
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - frames 4.67, 11.04, 27.0, 48.42, 50.5: white bold Yu Gothic, black outline+shadow, EN above JP, centred, same position (pos y 948 start) as reference ref_20.png; max 2 EN + 2 JP lines (4 lines max); nothing clipped, all inside sharp band.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
 - Text verbatim vs glossary_draft_s1.json: L001 (two terms, each on own line, 0.00-9.03 s), L003 Alexandre (9.05-19.09 s), L006 ジェフ・ベゾス (25.75-29.09 s), L012 マシンをぶっ壊す (45.73-52.19 s). All match; line breaks fall at 。 or between phrases, no word/name split.
 - Timing: each starts at the caption showing the term (L006 caption 25.75; L012 "break the machine" caption 45.73); durations 9.0, 10.0, 3.3, 6.5 s, all >= 2 s.
 - Layout: Expl style Yu Gothic 40 bold, white, black outline 3, shadow 2; lines at y 1138-1284 (text bottom about 1320), below EN/JP block (bottom about 1150 in worst 4-line case, 1100 for 3-line case) with visible gap, inside y 438..1480. Frames 4.67, 11.04, 27.0, 48.42, 50.5 confirm no overlap.

Non-blocking notes
- L012 explanation stays up to 52.19 s, past the spoken term (47.25 s), over a different speaker (frame 50.5); readable and approved, just lingers.
- L006 explanation sits close under the 3-line EN/JP block (about 40 px gap) but does not touch.

