# QA report: clip_09_50_cent

| Artifact | sha256 |
|---|---|
| final.mp4 | `f47835f1ff0e8f9e8a7354a9fadde74c9b3d77467ac62737eafb4830f81b8d14` |
| subtitles.ass | `f7524cb7d3f680a0c1fb504ce1ae5e895bade2d58beef2c5b83632a42c5e5d69` |
| subtitles.srt | `8ef501be02f8d7fb96df14a847a79fca2d18aadfafa0a47147206581094ed82e` |
| transcript.txt | `97300e7d8922867fe60cef0b0aa0509afa6ad38ed7bb21b6f5914be3c2de87b5` |
| source_manifest.json | `98185edda6159a6cc101d8b12649118fe05d10eef832dadcfd698bdd3e9064bc` |

QA'd render: `work/clips/clip_09_50_cent/render.mp4` sha256 `d48312ad558f54ca73682513fc3c1c30e417ab0e3f6b1eb0c10962ce676b6867`; final.mp4 is a stream-copy remux (square-pixel flag only), decoded video+audio framemd5 identical: `68cb02c37050270e942a5c9b199bba18`.
Source frames: [[19460, 20250], [20274, 20398], [20457, 21556], [21646, 21697], [21857, 21909], [21955, 22052]] (half-open).

## Independent critic rounds (fresh context each)

- `work/qa/clip_09_50_cent_critic.md`: FAIL
- `work/qa/clip_09_50_cent_critic_r2.md`: FAIL
- `work/qa/clip_09_50_cent_critic_r3.md`: FAIL
- `work/qa/clip_09_50_cent_critic_r4.md`: PASS

Final round verdict: PASS. Item verdicts (rubric 1-10) are in the critic files above; re-check rounds re-tested only the items affected by each fix and carried other PASS items forward.

Series checks: `output/shared/final_series_qa.md`, `output/shared/source_overlap_audit.md`, `work/qa/series_audit.json`.
Contact sheet: `work/clips/clip_09_50_cent/qa/pieces_contact.png`
