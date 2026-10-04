# QA report: clip_07_trauma_misunderstood

| Artifact | sha256 |
|---|---|
| final.mp4 | `f74ac01b3f98a249d704d6bee9a5bbeb9d5eba6e3a4b2f50dbc0ccf237fcddb3` |
| subtitles.ass | `74c1a20fcfc6d7b55af335cbe2334384bd651587d3c90446ce98e5edd444cc0b` |
| subtitles.srt | `564c479f272c219e5420a47dc196cbb8079be9a10b3dd69a2e87e58e9cc9668f` |
| transcript.txt | `5b0c54460de9f130cf9305c62dcd0b97ba9f8d97bfefd661a2c766237cca35c6` |
| source_manifest.json | `2b4bdab2e1ee06ec8b5a37d1fa833979e9085ef0ec0379e27b643b0dca7ea35e` |

QA'd render: `work/clips/clip_07_trauma_misunderstood/render.mp4` sha256 `1256d0a8e0389b2edbd51152b8d601f23b114b65de4a7fa122c1145f50b29e75`; final.mp4 is a stream-copy remux (square-pixel flag only), decoded video+audio framemd5 identical: `9a0bf782018313e24df04852b582fb24`.
Source frames: [[14477, 15253], [15339, 16370]] (half-open).

## Independent critic rounds (fresh context each)

- `work/qa/clip_07_trauma_misunderstood_critic.md`: PASS

Final round verdict: PASS. Item verdicts (rubric 1-10) are in the critic files above; re-check rounds re-tested only the items affected by each fix and carried other PASS items forward.

Series checks: `output/shared/final_series_qa.md`, `output/shared/source_overlap_audit.md`, `work/qa/series_audit.json`.
Contact sheet: `work/clips/clip_07_trauma_misunderstood/qa/pieces_contact.png`
