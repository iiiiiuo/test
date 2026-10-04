# QA report: clip_06_hospital_stories

| Artifact | sha256 |
|---|---|
| final.mp4 | `e53a246dca7357e388fa1eda97daf8662a84735caf021cd0d43c3117d6a91ea0` |
| subtitles.ass | `a97f822ec283f453ea0362c2bac55b8d38fbc2ffe703f9e12b1a4818135400d3` |
| subtitles.srt | `674ca061e91f401147c385e45cd259cfc3bcdb4725cc92b678b207a8b483d052` |
| transcript.txt | `360e13819578dd7d5b5cb0b33883d5a8f186534b093338c217156e4c03bee6a0` |
| source_manifest.json | `283282c890667c0c4a4abb210dcdd0f716320c540d4d89de51ddb0de2124c995` |

QA'd render: `work/clips/clip_06_hospital_stories/render.mp4` sha256 `57b8c68c89f572c265882a03fc24a3ed6bb326e48b446cd7818e014083293944`; final.mp4 is a stream-copy remux (square-pixel flag only), decoded video+audio framemd5 identical: `ea3802855948f4dab561fb8b83eb1cec`.
Source frames: [[12713, 14046], [14113, 14409], [16389, 16932]] (half-open).

## Independent critic rounds (fresh context each)

- `work/qa/clip_06_hospital_stories_critic.md`: PASS

Final round verdict: PASS. Item verdicts (rubric 1-10) are in the critic files above; re-check rounds re-tested only the items affected by each fix and carried other PASS items forward.

Series checks: `output/shared/final_series_qa.md`, `output/shared/source_overlap_audit.md`, `work/qa/series_audit.json`.
Contact sheet: `work/clips/clip_06_hospital_stories/qa/pieces_contact.png`
