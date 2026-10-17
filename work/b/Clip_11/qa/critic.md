VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

1. Structure: NOT IN SCOPE
2. Duration/format: PASS - auto.json: 1080x1920, SAR 1:1, video 85.919 s, audio 85.919 s, 2060/2060 frames, decode_errors empty.
3. Transcript accuracy: NOT IN SCOPE
4. Translation fidelity: NOT IN SCOPE (CHANGED_LINES = none)
5. Masking: PASS - auto.json unmasked_hits = []; no listed word appears in the EN rows of subtitles.ass; JP rows are not mechanically masked.
6. Timing/sync: NOT IN SCOPE
7. Typography/visuals: PASS - f_0001.00.png, extra/x_74.5.png and extra/x_76.95.png show white bold Yu Gothic with black outline and shadow, EN above JP, centred, at the same position and size as the previous render and the reference. The EN+JP block is at most 4 lines and nothing is clipped or outside the frame. Text stays readable on the bright yellow background.
8. Framing: NOT IN SCOPE
9. Source usage: NOT IN SCOPE
10. Term-explanation row: PASS
   - Text: both rows match glossary_draft_s1.json verbatim. Clip_11_L001 is "モーゼ：旧約聖書の預言者" and Clip_11_L016 is "天にいる父：キリスト教で神のこと". Each is a single line, so no word is split.
   - Timing: the L001 row runs 0.00-7.67 s (7.7 s) and covers both captions that show "Moses". The L016 row runs 73.89-76.97 s (3.1 s) and covers the caption "Your father and the Father above."
   - Layout: the row sits at y about 1188-1225, below the JP row, which ends about y 1145, so there is no overlap. It is inside the sharp band (438..1480).
   - Style: same font, white fill, black outline and shadow, at the smaller Expl size.

Non-blocking notes
- The L016 row ends at 76.97 s, 0.04 s (about 1 frame) into the next caption (starts 76.93 s). The row still shows during that one frame, over the unrelated "Now what has happened to the black community?" caption, as seen in x_76.95.png. It is essentially invisible. Ending the row at 76.51 s or 76.93 s would tidy it.
- The L016 row starts at 73.89 s, when the second "Your father and the Father above." caption appears. The same words were already on screen from 71.87 s, so the term shows about 2 s before its row. This is acceptable.
