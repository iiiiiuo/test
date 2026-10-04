# Series QA critic (fresh independent context)

VERDICT: PASS

| Clip | final.mp4 sha256 (prefix) |
|---|---|
| clip_02_offset_owes_10k | f635277be8c2fd36 |
| clip_03_casino_story | ab6a69859cf2facf |
| clip_04_beef_offset | b9615f0f0d1a4a14 |
| clip_05_shot_seven_times | 6a5ae37c3953d20f |
| clip_06_hospital_stories | e53a246dca7357e3 |
| clip_07_trauma_misunderstood | f74ac01b3f98a249 |
| clip_08_safe_alone | 7b2365d0a47551c9 |
| clip_09_50_cent | f47835f1ff0e8f9e |

Evidence frames: work/qa/series_frames/ (dup_montage.png, style_montage.png, cmp.png, ends.png, row_clip_*.png)

## A duplicate footage: PASS
Extracted source frames 8160/8189/8220 (clip_04) and 10670/10700/10730 (clip_05) -> dup_montage.png. Same fixed DJ Envy camera angle (same set dressing, logo, props), but head pose, gaze, mouth and hand position differ (8189: facing camera-left/front, mid-word; 10670: head turned left, different expression; 10730: head lowered/turned). Different moments of a static camera, not repeated content. Transcripts at those times differ (clip_04 beef question 273 s vs clip_05 healing question 356-358 s). Source intervals disjoint ([8021,10489) vs [10490,12587)).

## B repeated hook/setup: PASS
Hooks: 02 "Maybe you just got here now... drama with Offset" (61.06 s); 03 "Was y'all in the casino together?" (143.30); 04 "Is the beef too far ... to squash?" (267.68); 05 "Have you fully healed ... shot seven times?" (350.12); 06 "How long did it take you to get up and start moving?" (424.36); 07 "Do you think trauma changes people or reveals...?" (484.22); 08 "You just said that you spent a lot of time alone." (573.88); 09 "You had a conversation with 50..." (649.34). All distinct questions/setups; audit reports 0 repeated 7-word speech spans. Thematic adjacency (02/03 Offset 10K; 05/06/07 shooting aftermath; 07/08 "think differently from the ground up") is subject matter only, no repeated speech/setup.

## C series style: PASS
style_montage.png (one frame at t=15 s from each clip + ref r_8/r_30/r_50) and cmp.png (clip_05 vs r_30 at matched scale): all 8 clips use the same layout as reference (blurred same-frame fill top/bottom, 16:9-ish centre band), captions centred at the same vertical position across clips and matching the reference, bold white Gothic with black outline+shadow, EN above JP, similar scale/line height, 2-line EN wrap max, JP 1-2 lines. All ASS headers identical (single header hash f62020aa..., Style Yu Gothic 50 bold, outline 3, shadow 2). Framing keeps faces in band at all sampled frames.

## D localization consistency: PASS
srt scan across 8 clips: masked forms only s**t, f**k, f**king, f**ked, bulls**t, ni**a, ni**as/Ni**as - identical two-asterisk forms everywhere, matching subtitle_style_spec.md list. Unmasked EN curse words: 0. Japanese lines with asterisks: 0/397. Japanese register casual plain-form throughout (desu/masu polite endings 0; one hit "俺ですらさ" is not polite form).

## E readiness: PASS (advisories non-blocking)
ends.png: first/last ~3 s of each clip - no black, freeze or padded frames; every clip opens on its hook question and ends on a completed line (02 "kudos to you, bro"; 03 "it's about the respect"; 04 "look a little sad, you know what I mean?"; 05 "mad holes and shit"; 06 "on some Rambo shit"; 07 "very different to the average person"; 08 "Hopefully so. You feel me?"; 09 "troll me right now"). Tail gaps after last word 0.01-0.38 s; next source speech is not included.
- Advisory clip_02 00:00.00: cut at src 61.13 s vs word "Maybe" 61.06 s; local faster-whisper large-v3 on the render's first 1.2 s still reads "Maybe" (p=0.77) - onset intact enough, not blocking.
- Advisory clip_07 00:00.00-00:01.17: 1.17 s before first cue contains a low-confidence "Listen," (ASR p=0.32; disappears under a prompt) that is unsubtitled; already noted by per-clip critic as low-conf and passed. Natural lead-in, not padding. Optional: trim start to ~src 484.10 s (out ~1.05 s) if a cleaner open is wanted (still >= 60 s? current 60.29 s -> would drop to ~59.2 s, so do NOT trim; keep as is).

## F format: PASS
ffprobe: all 8 final.mp4 1080x1920, SAR 1:1, DAR 9:16. Durations (s): 02 70.6706, 03 72.0386, 04 82.3490, 05 69.9700, 06 72.4724, 07 60.2936 (video stream 60.293567, audio 60.292993), 08 75.5755, 09 73.8404 - all within [60.0, 120.0).

Blocking gaps: none
Largest gap: none
Fix: none
