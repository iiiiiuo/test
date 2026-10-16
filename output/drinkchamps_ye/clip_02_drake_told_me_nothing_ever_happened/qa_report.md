# Clip_02 QA report

Final verdict: **PASS** (Fresh Clip Critic, independent context). Render sha256 `19723d69e7ae880cd482db048a882bbdd990ba748066c31849186acbbe3b15af`.

## Automated checks (final.mp4)
- 1080x1920 SAR 1:1, 24000/1001 fps, h264/aac 48000 Hz
- Video 74.116 s, audio 74.116 s (rule 60.0 <= d < 120.0: PASS)
- Frames: 1777 (manifest 1777)
- Decode/format: {"width": 1080, "height": 1920, "sar": "1:1", "fps": "24000/1001", "video_frames": 1777, "expected_frames": 1777, "video_duration_s": 74.115708, "audio_duration_s": 74.116, "v_start": "0.000000", "a_start": "0.000000", "rotation": null, "decode_errors": "", "PASS": true}
- Caption sync vs render ASR: {"caption_tokens": 197, "asr_words": 195, "matched": 187, "match_ratio": 0.949, "matched_words_inside_their_caption": 0.979, "caption_onset_vs_first_word_s": {"n": 21, "median": 0.094, "max_abs": 1.816}}

## Critic rounds
- round 1: FAIL — final shot framed on backdrop crest; opening edge → framing fix; start moved to quiet point before Yeah (large-v3 span re-check confirms Yeah)
- round 1: FAIL — L014 caption 3.8 s early over laughter → same timing rules (caption now 70.81)
- round latest: FAIL — final shot crop put laughing Ye at left edge (3/10 detections) → manual crop x=420 for frames 40930-41110 (framing_overrides.json)

## Final critic report

VERDICT: PASS
Blocking gaps: none
Largest gap: none (non-blocking: caption 1 shows "Yeah," that is not heard in the render, and the first spoken word "It's" starts at t=0.0 with full energy)
Fix: none

1. Structure: PASS. Opens on "it's so funny, though, because me and Drake..." and jumps at 6.30s to "so then Drake says to me, yo... no, I need to tell the story like this", then the Jared/Drake "nothing ever happened" story and punchline "When did I become Jared Kushner?" plus host reaction. Ends on a complete line ("You had me scared for a second"). The join (source 1598.93 to 1646.81) reads as Ye restarting his story; understandable standalone.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 74.116 s / audio 74.116 s, 1777 frames = expected 1777, no decode errors.
3. Transcript accuracy: PASS. 24 captions, 187/195 words matched, 97.9% inside their caption. Only differences: "Yeah," in caption 1 is not heard (see notes), "Stoute"/"Stout" spelling, "scared" vs "I was scared" (same meaning).
4. Translation fidelity: PASS. JP rows match the approved CSV (rev3) and the heard meaning; no missing or misplaced lines. Duplicate JP across captions 7/8 and 14/15 is the approved single JP for one sentence split in EN.
5. Masking: PASS. "f**k" at 21.73-24.84; unmasked_hits empty; JP "ヤった" translated from meaning, not mechanically masked.
6. Timing/sync: PASS. Median onset error 0.09 s; no caption under 1.3 s; uncaptioned spans are 10.37-12.75 (about 2 s of room-tone pause before "no, I need to tell the story") and 60.67-64.64 / 66.84-70.81 (loud laughter reactions, no foreground sentence). No uncaptioned full sentence.
7. Typography/visuals: PASS. sheet_1/2 vs ref_sheet: white bold Yu Gothic, black outline/shadow, EN above JP, centred, same vertical position (about y 365/720 on the sheet) as the reference, max 2 EN + 2 JP lines, no clipping.
8. Framing: PASS. Ye in the sharp centre band with full cap and face; host shot at ~63 s centred; blurred fill above and below like the reference; crop changes coincide with shot changes (frame 40845 punch-in, 40930 recentre).
9. Source usage: PASS. Manifest: part_1 frames [38185,38336) and [39484,41110), half-open, disjoint, audio ranges match video. Total 151+1626=1777 frames. No freeze or repetition; the 2 s pause and the laughter are source content.

Non-blocking notes
- Caption 1 displays "Yeah," but render audio starts directly with "It's" (ASR and the 0.0 s onset). The clip start (frame 38185) lands right on the word onset, so it is slightly abrupt. Drop "Yeah," from the EN, or start about 0.1-0.2 s earlier if source frames allow.
- Caption 11 JP wraps mid-word: "一応言っとくけ / ど、何もなかったから" (and caption 19 breaks after "一応言っとくけど、"). Prefer breaking after "けど、".
- 10.37-12.75 is a roughly 2 s near-silent pause inside the clip; it is a natural beat before the restart, but it could be trimmed by ~0.8 s without harming sync if the pace is wanted tighter.

