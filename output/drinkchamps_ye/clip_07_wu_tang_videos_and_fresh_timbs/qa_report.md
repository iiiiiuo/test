# Clip_07 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `d765352bfc81c42ca8bed030ea14f9ce730ac703b3d6f6a716d49755c498b57d`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 63.188 s, audio 63.188 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1515 (manifest 1515)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1515, "expected_frames": 1515, "video_duration_s": 63.188125, "audio_duration_s": 63.188, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 197, "asr_words": 184, "matched": 156, "match_ratio": 0.792, "matched_words_inside_their_caption": 0.987, "caption_onset_vs_first_word_s": {"n": 20, "median": 0.034, "max_abs": 0.746}}

## Critic rounds
- round 1: PASS — none → none

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (minor: "fresh Timbs" at 41.23-43.63 omits heard "pair of"; "Free" name LOW-confidence)
Fix: none

## Items
1. Structure: PASS. Opens on host question "All right. Dungeon Family or Wu-Tang Clan?" (source "All right" at 1658.34; start 1658.114 only trims prior speech ending 1658.16, ~0.05 s tail at most). Ends on "You're correct." (speech ends ~1721.2; RMS near floor by 1721.30; next speech at 1721.75). Coherent question, answer, Timbs story, punchline.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 63.188 s, audio 63.188 s, 1515 frames = expected, decode_errors empty.
3. Transcript: PASS. sync.txt matches (Tony Starks, Wallabees, ni**as, "Free"). Only deviation: caption 41.23 "fresh Timbs" vs heard "fresh pair of Timbs" (meaning intact). "Yeah, yeah, yeah" (57.99) supported by audio energy 1716.0-1717.5 although render ASR missed it.
4. Translation: PASS. All 25 rows match approved rev3; no clear errors. L011 "Free" is a LOW-confidence name (flagged in the approved CSV), not a blocker.
5. Masking: PASS. "ni**as" masked at 38.49; auto.json unmasked_hits empty; JP not mechanically masked.
6. Timing/sync: PASS. Median caption onset vs first word 0.034 s; 98.7% matched words inside their caption. Shortest caption 0.82 s ("What? Come on, man.") is 3 words; acceptable. First caption shows at 0.056 s, about 0.18 s before the host's "All right" (while Ye laughs); harmless. Gaps (28.81-29.26, 35.71-37.17) are pauses, not speech.
7. Typography/visuals: PASS. White bold Yu Gothic with black outline/shadow, EN above JP, centred, same vertical band as ref_20.png, max 2 EN + 2 JP lines, no clipping (f_0000.05, f_0039.85 checked), readable on the bright yellow background.
8. Framing: PASS. Sharp centre band with blurred fill above and below, like the reference. Faces fully in frame at 0.05 s, 4.46 s, 33.82 s, 39.85 s, 61.56 s and 63.11 s. Crop changes occur at shot changes (Ye to host to Ye to third speaker).
9. Source usage: PASS. Single interval [39754, 41269) of part_2_2, 1515 frames, no joins, no padding or repetition. Audio segment same as video.

## Non-blocking notes
- Opening 0.5 s is a reaction shot of Ye laughing under the host's caption (the "no face" crop on frames 39754-39766). Natural, but it could start on the host.
- Captions at 22.38-28.81 (6.4 s) and 57.99-60.59 hold long text; readable but dense.
- Caption 41.23: consider "fresh pair of Timbs" for fidelity.

