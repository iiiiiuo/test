# QA report: clip_02_offset_owes_10k

| Artifact | sha256 |
|---|---|
| final.mp4 | `f635277be8c2fd3610d9558ce430a8a203f25f4f413cd19389cd32a266e749a8` |
| subtitles.ass | `384ae99fce720dfafc474847306bd6b546d8fcd12c7d5580a4a63bb73ff41764` |
| subtitles.srt | `d893a5e5b84f841edff35850c224af40804df011f8283b765ff675b6903419c6` |
| transcript.txt | `5d48e0e3335c017d7cf7e1514cd0713386fc9209feafc5dfdf9c4e15adae9a83` |
| source_manifest.json | `d268c6b0d5ae1aaae19a63cbe5551ed1c91c5b9a36644e8b13604d9eb3130ddc` |

QA'd render: `work/clips/clip_02_offset_owes_10k/render.mp4` sha256 `5339c5bf453f76073a6b9f3448965294ec7b13580104ebe3017fd0c766e4f37b`; final.mp4 is a stream-copy remux (square-pixel flag only), decoded video+audio framemd5 identical: `d0f7df46ebb4c5ee15b968612cf51780`.
Source frames: [[1832, 3581], [3685, 4054]] (half-open).

## Independent critic rounds (fresh context each)

- `work/qa/clip_02_offset_owes_10k_critic.md`: FAIL
- `work/qa/clip_02_offset_owes_10k_critic_r2.md`: PASS

Final round verdict: PASS. Item verdicts (rubric 1-10) are in the critic files above; re-check rounds re-tested only the items affected by each fix and carried other PASS items forward.

Series checks: `output/shared/final_series_qa.md`, `output/shared/source_overlap_audit.md`, `work/qa/series_audit.json`.
Contact sheet: `work/clips/clip_02_offset_owes_10k/qa/pieces_contact.png`
