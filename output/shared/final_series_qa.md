# Final series QA

Verdict: **PASS** (independent series reviewer, `work/qa/series_critic.md`; automated audit, `work/qa/series_audit.json`).

| Clip | Video s | Audio s | 1080x1920 SAR 1:1 DAR 9:16 | Source frames | final.mp4 sha256 | Per-clip QA |
|---|---|---|---|---|---|---|
| clip_02_offset_owes_10k | 70.671 | 70.693 | yes | 2118 | `f635277be8c2fd36…` | PASS (`work/qa/clip_02_offset_owes_10k_critic_r2.md`) |
| clip_03_casino_story | 72.039 | 72.061 | yes | 2159 | `ab6a69859cf2facf…` | PASS (`work/qa/clip_03_casino_story_critic_r3.md`) |
| clip_04_beef_offset | 82.349 | 82.372 | yes | 2468 | `b9615f0f0d1a4a14…` | PASS (`work/qa/clip_04_beef_offset_critic_r2.md`) |
| clip_05_shot_seven_times | 69.970 | 69.993 | yes | 2097 | `6a5ae37c3953d20f…` | PASS (`work/qa/clip_05_shot_seven_times_critic.md`) |
| clip_06_hospital_stories | 72.472 | 72.495 | yes | 2172 | `e53a246dca7357e3…` | PASS (`work/qa/clip_06_hospital_stories_critic.md`) |
| clip_07_trauma_misunderstood | 60.294 | 60.316 | yes | 1807 | `f74ac01b3f98a249…` | PASS (`work/qa/clip_07_trauma_misunderstood_critic.md`) |
| clip_08_safe_alone | 75.576 | 75.598 | yes | 2265 | `7b2365d0a47551c9…` | PASS (`work/qa/clip_08_safe_alone_critic_r3.md`) |
| clip_09_50_cent | 73.840 | 73.863 | yes | 2213 | `f47835f1ff0e8f9e…` | PASS (`work/qa/clip_09_50_cent_critic_r4.md`) |

- Zero overlap: 0 intersecting video or audio interval pairs across all clips. See `output/shared/source_overlap_audit.md`.
- Duplicate footage: 2 automated flags (clip_04 vs clip_05, the same static DJ Envy camera). The reviewer checked them visually: different moments, not duplicates.
- Repeated hooks or setups: none. Automated 7-word repeat scan across the displayed English found 0; the reviewer compared the openings and setups.
- Subtitles: one shared ASS header across all 8 clips (sha256 `f62020aac164d1df…`, Yu Gothic Bold from `work/fonts/YuGothB.ttc`). Unmasked curse words in the displayed text: 0. No Japanese asterisks.
- Export: each final.mp4 is a stream-copy remux of the QA'd render that only sets the square-pixel flag. Decoded video and audio framemd5 are identical (recorded in each qa_report.md).
- Coverage: every semantic unit has a disposition (`output/shared/clip_candidate_map.md`). No viable unreserved candidate remains.

## Limitations
- C01 (the opening 0-61 s) was rejected: its ending phrase could not be transcribed reliably, and the remaining 53 s is below the 60 s minimum.
- Short unclear spans were cut inside clips 02, 03, 06, 07 and 09 rather than guessed. They are listed in each translation_notes.md.
- Non-blocking reviewer notes: clip_02 starts 70 ms before "Maybe" (still intelligible); clip_07 opens with an uncaptioned low-confidence "Listen,".

## Shared copy
- Copied to `/mnt/project-files/output/`. The project file store inserts a 5,875-byte `uuid` metadata box into each MP4, so byte hashes there differ from the ones above. Decoded video and audio framemd5 of all 8 shared copies match the exported files: verified.
