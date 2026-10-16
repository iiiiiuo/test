# Clip_27 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `18037f9b78a2ddab9ba49408f5b370a12b8a62917df1e2512731e6435e1b0e2b`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 66.858 s, audio 66.858 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1603 (manifest 1603)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1603, "expected_frames": 1603, "video_duration_s": 66.858458, "audio_duration_s": 66.858, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 230, "asr_words": 229, "matched": 189, "match_ratio": 0.822, "matched_words_inside_their_caption": 0.894, "caption_onset_vs_first_word_s": {"n": 16, "median": -0.098, "max_abs": 2.898}}

## Critic rounds
- round 1: FAIL — 0.40 s flash caption 'But it's like,' at 55.57 → chunks override Clip_27_L012 (one caption)
- round 2: FAIL — opens inside 'Because'; ends while 'manner' sounding → hand windows start 657.98-658.06, end 724.86-724.94
- round 3: PASS — non-blocking: framing shows host 0.6-4.4 s → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (non-blocking: 0.6-4.4 s shows the host on screen while the caption reads as the main speaker's line; speaker identity unverified)
Fix: none

## Items
1. Structure: PASS. Source speech begins 658.15 (clip starts 658.03, no mid-word cut) and ends 724.78 (clip ends 724.89) on "think like in that manner", a resolved ending. Coherent argument: own factories, Maybach fleet, "until we make our own cars", legal BMF. Opening "Because why not we just do it ourself..." is a slightly dangling connective but is a self-contained rhetorical point.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 66.858 s, audio 66.858 s, 1603 frames = expected 1603, no decode errors.
3. Transcript accuracy: PASS. Sync.txt HEARD matches the displayed English throughout; mismatches are ASR errors only ("anybody" vs "nobody ... anywhere", "dip" vs "do", "the max" vs "the master", "Ye-bachs" heard as "yaybacks"). Source-context lines agree.
4. Translation fidelity: PASS. All 23 captions match the approved CSV rows L001-L013 (dropped_lines empty); no clear errors, JP attached to the right moments (e.g. 15.46-20.08 Warren Buffett split across two captions, 50.29 "Ye-bach").
5. Masking: PASS. auto.json unmasked_hits empty; "s**t" displayed at 43.49 and 50.29; JP not mechanically masked.
6. Timing/sync: PASS. Median caption onset vs first heard word -0.10 s; matched words inside own caption 89%. No gaps with foreground speech uncaptioned (30.12-30.50 is a pause/hesitation). Shortest captions: 1.04 s (20.10, 6 words) and 1.57 s (21.16) are readable at speech pace.
7. Typography/visuals: PASS. Frames f_0001.00, f_0016.41, f_0036.32, f_0065.86 show white bold Yu Gothic with black outline/shadow, EN above JP, centred, first line top ~y=950 as in the spec and ref_20.png, max 2 EN + 2 JP lines, widest EN line ~710 px (<760 px), no clipping, readable on the white shirt and bright backgrounds.
8. Framing: PASS. Sharp 1080x1042 band at y=438 with blurred fill above/below, same as reference. Faces are centred in the band for all three shots (cuts at 0.63 s and 4.9 s coincide with real shot changes per framing.json: Ye wide, host, Ye tight); no head cut-off beyond note below.
9. Source usage: PASS. One interval part_4 frames [15777, 17380), half-open, single source, 1603 frames; no padding, freezes or repetition; no joins.

## Non-blocking notes
- 0.26-4.4 s: the caption (labelled as the main speaker's words in the approved CSV) plays over the host, who is gesturing with moving lips; at 0.05-0.6 s Ye is on screen looking left with mouth closed. I could not verify by ear/pitch whether this stretch is a cutaway to the host listening or the host speaking. Content and captions match the audio either way; if the speaker is not Ye, the "俺たち" register still reads naturally.
- f_0000.05: cap top sits at the very top edge of the sharp band for the first 15 frames (0.6 s); brief.

