# Clip_13 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `57aa32038246b874c4a092a4edcd8734e159b671e45d45be9133485114ee6719`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 78.996 s, audio 78.995 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1894 (manifest 1894)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1894, "expected_frames": 1894, "video_duration_s": 78.995583, "audio_duration_s": 78.995, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 261, "asr_words": 288, "matched": 249, "match_ratio": 0.954, "matched_words_inside_their_caption": 0.98, "caption_onset_vs_first_word_s": {"n": 28, "median": 0.077, "max_abs": 0.727}}

## Critic rounds
- round latest: FAIL — end cut before final "right?" → end moved to 1474.48 (frame 35352)

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

## Items
1. Structure: PASS. Opens on "I always thought" (ASR 1395.74s, preceded by "Yeah, yeah" outside the cut); ends on "You understand that, right?" (source 1473.55-1474.43, clip end 1474.47) with the point resolved; reads standalone.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 78.996 s, audio 78.995 s, 1894/1894 frames, decode_errors empty.
3. Transcript accuracy: PASS. Match ratio 0.954 and 98% of matched words inside their captions. Differences are ASR errors or filler only (e.g. "very not close" heard vs "polo", "Drink Chance").
4. Translation fidelity: PASS. All 29 captions match approved rev3 rows with no dropped lines. Quote marks and the split of long JP lines across consecutive captions track the speech.
5. Masking: PASS. auto.json unmasked_hits is empty and no listed words occur; the JP is not masked.
6. Timing/sync: PASS. Onset median 0.077 s. The max of 0.727 s is the 69.73-70.26 gap, which is the speaker's real pause (source 1464.70-1465.51). No uncaptioned foreground sentence. The shortest caption is 0.88 s ("It didn't work for me", a short sentence) and still readable.
7. Typography/visuals: PASS. sheet_1 and f_0078.92 against ref_sheet: white bold Yu Gothic, black outline and shadow, EN above JP, centred, same size and position as the reference, at most 2 EN + 2 JP lines, no overflow.
8. Framing: PASS. Single continuous piece (one crop 1119x1080); face and cap sit in the sharp band with the blurred fill above and below. The speaker leans and moves slightly but is never cut off.
9. Source usage: PASS. One interval, part_3 frames [33458, 35352), with video and audio from the same range. No padding, freeze or repetition.

## Non-blocking notes
- Caption 6 (0.20 s gap, 1.2 s duration, "you know, they did it,") carries the JP for the full thought, so JP runs slightly ahead of EN across captions 6-8. Reads fine.

