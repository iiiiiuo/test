# QA report: clip_05_shot_seven_times

| Artifact | sha256 |
|---|---|
| final.mp4 | `6a5ae37c3953d20fa9ec837b0b06e54ef434cd9674b30154e732d5cead733664` |
| subtitles.ass | `cb11936e22988ba7bf2348c2ab9a0c05819c759318e0145474c746b2fa2eada7` |
| subtitles.srt | `c326ca6a1ca359ae896c79cf91c2edf10c3a2d0293827c5c79667fb015c10063` |
| transcript.txt | `40a9a082e254ccb90a831208a7a5c6665705b340699a614ccbddff0d343dedf7` |
| source_manifest.json | `81a73c0cf979c890b6577fc365fcad73ef6659e7684507015fb58d9d1a449eca` |

QA'd render: `work/clips/clip_05_shot_seven_times/render.mp4` sha256 `31a24356421adc283a38b32512437374540bda698f143d749c0cd0a543b33215`; final.mp4 is a stream-copy remux (square-pixel flag only), decoded video+audio framemd5 identical: `3b3c45e1cc0460e5c074869ce43dde21`.
Source frames: [[10490, 12587]] (half-open).

## Independent critic rounds (fresh context each)

- `work/qa/clip_05_shot_seven_times_critic.md`: PASS

Final round verdict: PASS. Item verdicts (rubric 1-10) are in the critic files above; re-check rounds re-tested only the items affected by each fix and carried other PASS items forward.

Series checks: `output/shared/final_series_qa.md`, `output/shared/source_overlap_audit.md`, `work/qa/series_audit.json`.
Contact sheet: `work/clips/clip_05_shot_seven_times/qa/pieces_contact.png`
