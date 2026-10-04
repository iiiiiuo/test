# QA report: clip_08_safe_alone

| Artifact | sha256 |
|---|---|
| final.mp4 | `7b2365d0a47551c9483f6ad4cad0f2c18512bf2e087d3cc1de31a93da30c6389` |
| subtitles.ass | `ee53e92f054db2c1461daf61dcb0b3aa7140bf4af2347a169eaf698db2ce3dbc` |
| subtitles.srt | `c321aa3ef4028f80cb118e03b801caaa83d98f907a52e1c9be0d9af4c209fed3` |
| transcript.txt | `5d5e4b3e989b8362c47a41cb072e0a829e4da774d457c8a71c24161c6eb03bdd` |
| source_manifest.json | `d1ce9c664b4d55802585d739b5415d1b5ccf454223231847cdfa42d58bccc7fa` |

QA'd render: `work/clips/clip_08_safe_alone/render.mp4` sha256 `3f781371f06ab0f3f308cf4b36e85b7033571ae6eb4ab82c6a77c2845777b0a8`; final.mp4 is a stream-copy remux (square-pixel flag only), decoded video+audio framemd5 identical: `1520a0f35df661c1ad5e5943160d2d25`.
Source frames: [[17194, 19459]] (half-open).

## Independent critic rounds (fresh context each)

- `work/qa/clip_08_safe_alone_critic.md`: FAIL
- `work/qa/clip_08_safe_alone_critic_r2.md`: FAIL
- `work/qa/clip_08_safe_alone_critic_r3.md`: PASS

Final round verdict: PASS. Item verdicts (rubric 1-10) are in the critic files above; re-check rounds re-tested only the items affected by each fix and carried other PASS items forward.

Series checks: `output/shared/final_series_qa.md`, `output/shared/source_overlap_audit.md`, `work/qa/series_audit.json`.
Contact sheet: `work/clips/clip_08_safe_alone/qa/pieces_contact.png`
