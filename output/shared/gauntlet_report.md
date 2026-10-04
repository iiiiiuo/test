# Gauntlet report

Loop: Builder → actual render → one Fresh Clip Critic (independent context, rubric items 1-10) → targeted fix → scoped re-check. Every critic file is under `work/qa/`.

| Target | Round | Factual change | Evidence | Verdict | Largest gap | Fix / strategy | Result |
|---|---|---|---|---|---|---|---|
| style template | calib | froze shared ASS template v1 | work/qa/calibration_critic.md | PASS | none | none | frozen |
| clip_02 | r1 | first build | clip_02_offset_owes_10k_critic.md | FAIL | framing: a camera pan at 57.8-58.4 s pushes the guest out of the crop | added a MOVE crop override (x 430→800) for src frames 3555-3581; corrected JP for "in blood" | → r2 |
| clip_02 | r2 | crop pan + JP edit | clip_02_offset_owes_10k_critic_r2.md | PASS | none | none | frozen |
| clip_03 | r1 | first build | clip_03_casino_story_critic.md | FAIL | "It's the image" was misheard; the speech is "It's the Emmys" | caption fix verified with 3 models; dropped an inaudible "And"; split a 3-line caption | → r2 |
| clip_03 | r2 | captions edited | clip_03_casino_story_critic_r2.md | FAIL | the render still had the old subtitles (spec.json was not regenerated) | root cause: build reads spec.json, so make_spec now always runs after caption edits; "fake" corrected to "I think" (3 models) | → r3 |
| clip_03 | r3 | spec regenerated and re-rendered | clip_03_casino_story_critic_r3.md | PASS | none | none | frozen |
| clip_04 | r1 | first build | clip_04_beef_offset_critic.md | FAIL | a 0.30 s caption and 4 flash frames at the start | merged and re-split the captions; start moved to frame 8021; added the SHORT lint and boundary_check | → r2 |
| clip_04 | r2 | captions + start | clip_04_beef_offset_critic_r2.md | PASS | none | none | frozen |
| clip_05 | r1 | first build | clip_05_shot_seven_times_critic.md | PASS | none | none | frozen |
| clip_06 | r1 | first build | clip_06_hospital_stories_critic.md | PASS | none | none | frozen |
| clip_07 | r1 | first build | clip_07_trauma_misunderstood_critic.md | PASS | none | none | frozen |
| clip_08 | r1 | first build | clip_08_safe_alone_critic.md | FAIL | an invented "I'm alone." caption | replaced with the spoken "Yeah." | → r2 |
| clip_08 | r2 | caption text | clip_08_safe_alone_critic_r2.md | FAIL | caption about 0.7 s early | re-timed the captions to measured onsets | → r3 |
| clip_08 | r3 | caption timing | clip_08_safe_alone_critic_r3.md | PASS | none | none | frozen |
| clip_09 | r1 | first build | clip_09_50_cent_critic.md | FAIL | guessed words in "Yeah, you feel me?" plus clipped words at two joins | dropped 728.13-728.76; moved the segment-3 start; "I would not..." | → r2 |
| clip_09 | r2 | joins moved | clip_09_50_cent_critic_r2.md | FAIL | the join still cut mid-sound (cut points came from word timestamps) | new hypothesis: choose cuts from 10-20 ms RMS minima; dropped 727.50-729.30 | → r3 |
| clip_09 | r3 | RMS-based cuts | clip_09_50_cent_critic_r3.md | FAIL | "does" is co-articulated with the next unresolvable utterance, so no clean end point exists | third hypothesis: drop the whole span 725.74-727.50 | → r4 |
| clip_09 | r4 | span dropped | clip_09_50_cent_critic_r4.md | PASS | none | none | frozen |
| series | 1 | final files (stream-copy remux, SAR flag only) | work/qa/series_audit.json, series_critic.md | PASS | none | none | complete |
