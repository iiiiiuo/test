# QA report: clip_04_beef_offset

| Artifact | sha256 |
|---|---|
| final.mp4 | `b9615f0f0d1a4a14e6501ebca6091d83c5fd8a67a32ffdf5a8c0af796b021352` |
| subtitles.ass | `720bd60f5beb191ef78c2656c8b280fbe87f63d2ceadafd81cac507d4d6cc1ed` |
| subtitles.srt | `999097a71bd4d3f1f03a18e53d93d58d1ebd7dffb8254afd8732391dfe26e5bc` |
| transcript.txt | `82804bbd83c19ab8bdf801344e9c2184b593f6a7a26744c3d0591a1c95aac735` |
| source_manifest.json | `0c7cc13a0e13244d9760e435669e6cfd4be89f19f292f418c4564f1af5bb3503` |

QA'd render: `work/clips/clip_04_beef_offset/render.mp4` sha256 `bb677a51bcae40e32cb1f85c2e748f7c48482174835cf9194133b9477d09be5e`; final.mp4 is a stream-copy remux (square-pixel flag only), decoded video+audio framemd5 identical: `5fe847616b08aaf5b0df1606bc2a247e`.
Source frames: [[8021, 10489]] (half-open).

## Independent critic rounds (fresh context each)

- `work/qa/clip_04_beef_offset_critic.md`: FAIL
- `work/qa/clip_04_beef_offset_critic_r2.md`: PASS

Final round verdict: PASS. Item verdicts (rubric 1-10) are in the critic files above; re-check rounds re-tested only the items affected by each fix and carried other PASS items forward.

Series checks: `output/shared/final_series_qa.md`, `output/shared/source_overlap_audit.md`, `work/qa/series_audit.json`.
Contact sheet: `work/clips/clip_04_beef_offset/qa/pieces_contact.png`
