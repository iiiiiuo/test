# QA report: clip_03_casino_story

| Artifact | sha256 |
|---|---|
| final.mp4 | `ab6a69859cf2facfa0fa04bcd3591cc65cbfbdeb1b82fffdce37d819199179b0` |
| subtitles.ass | `c20956568b3544d4d870143764374a0ab0cd1fa07fd7ca8b5970eb35dcfe26b1` |
| subtitles.srt | `97a41f4e937756f330cbc38d0e55afe37539c211a6516d8ea3659ffef34e52ad` |
| transcript.txt | `330585566ee46c8f60735ddc4ecd0052c6d424a517c894a2f225242d5fc0f926` |
| source_manifest.json | `3a2e27ba899f70936a18a0c0263efbdbd5c526eab8d7b4aa1293492fc4f85a3e` |

QA'd render: `work/clips/clip_03_casino_story/render.mp4` sha256 `8d9cc8dcf426c734494b0208cfe588bbdf56102864978eabcb5908d709c766ae`; final.mp4 is a stream-copy remux (square-pixel flag only), decoded video+audio framemd5 identical: `4e5257a86239d5b506e731b377b59146`.
Source frames: [[4290, 4794], [4867, 4932], [5072, 6352], [6421, 6656], [6739, 6814]] (half-open).

## Independent critic rounds (fresh context each)

- `work/qa/clip_03_casino_story_critic.md`: FAIL
- `work/qa/clip_03_casino_story_critic_r2.md`: FAIL
- `work/qa/clip_03_casino_story_critic_r3.md`: PASS

Final round verdict: PASS. Item verdicts (rubric 1-10) are in the critic files above; re-check rounds re-tested only the items affected by each fix and carried other PASS items forward.

Series checks: `output/shared/final_series_qa.md`, `output/shared/source_overlap_audit.md`, `work/qa/series_audit.json`.
Contact sheet: `work/clips/clip_03_casino_story/qa/pieces_contact.png`
