# Clip_24 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `3177d397aab5e1b15570fddcb8822d33c36aecd82cbc678770705d55c671dc40`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 65.482 s, audio 65.482 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1570 (manifest 1570)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1570, "expected_frames": 1570, "video_duration_s": 65.482083, "audio_duration_s": 65.482, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 195, "asr_words": 197, "matched": 187, "match_ratio": 0.959, "matched_words_inside_their_caption": 0.973, "caption_onset_vs_first_word_s": {"n": 23, "median": -0.034, "max_abs": 1.694}}

## Critic rounds
- round 1: FAIL — L002 shown 1.1 s early over uncaptioned 'I ain't gonna lie, I've been' → interval 2 start moved to 'since' (frame 35657)
- round 2: FAIL — L012 JP order inverted vs EN (46.43-50.77) → chunks override Clip_24_L012
- round 3: PASS — non-blocking: 44.03 fragment EN-only → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

## Items
1. Structure: PASS. Opens on "Okay, let me talk about Balenciaga" (Ye, f_0000.05.png), host shot at 1.54 for "Since you did the last interview, I've been Balenciaga", then a Ye answer through to "too much trauma economy" (ends on a completed clause; source continues "you know I'm not gonna...", cut at 1561.27 after the phrase). Both jump cuts (8.55 and 1.54) read naturally and are covered by shot or caption changes. Source audio dips to 0.05 to 0.07 RMS at 1494.20 and 1504.30, so those cuts are clean.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 65.482 s, audio 65.482 s, 1570 of 1570 frames, no decode errors.
3. Transcript accuracy: PASS. HEARD matches the displayed English at 96% (matched words inside their caption: 97%). The one difference is "y'all" (3.73) against HEARD "yeah" (p=0.54, low confidence). It matches the approved row, and the intent is unaffected.
4. Translation fidelity: PASS. All 16 approved rows are in place and attached to the right moments. L012 was not dropped; it is split across three captions.
5. Masking: PASS. "s**t" at 50.79. auto.json shows no unmasked hits. The Japanese is not mechanically masked.
6. Timing/sync: PASS. Median caption onset against first heard word is -0.03 s. The one outlier (max_abs 1.69 s) is the "Balenci-Yalla" line, where ASR mis-times a repeated "balenciaga". No caption is shorter than 1.26 s. Gaps with no caption are 8.32 to 9.47 (Ye smiling; no speech to caption, only reaction) and 17.07 to 18.35 (pause).
7. Typography/visuals: PASS. White bold Yu Gothic-style text with black outline and shadow, EN above JP, centred, at the same lower-band position as ref_sheet.jpg. 2 EN plus 2 JP lines at most, with no overflow or clipping, and it reads on the bright white shirt.
8. Framing: PASS. The sharp 1080x1042 centre band is over a blurred fill. Ye's face is centred with headroom (f_0000.05.png), the host is in the middle of the band at 1.63, and crops change only at shot changes.
9. Source usage: PASS. There are three disjoint half-open ranges from part_1: [35384,35421), [35657,35825) and [36068,37433). Video and audio ranges are identical. There is no padding, freeze or repetition.

## Non-blocking notes
- 44.03 to 46.41 (L012 first fragment, "So even if, say, say, say, we wanted to, like,") shows English only. The Japanese appears with the continuation at 46.43. Acceptable as a sentence fragment, but the fragment is on screen for 2.4 s with no Japanese.
- The first 0.17 s of the clip has speech under the video before the first caption. The first word "okay" starts at about 0.0 (ASR p=0.04). The source has loud audio before the cut at 1475.81, so a trace of the preceding lyric may be present. It is not audible as a distinct word in the evidence.
- The cut at 1.54 (source 1477.35) lands in continuous speech, with energy that continues straight into the next word. It is abrupt, but the shot switches to the host at the same moment.

