# Calibration Critic Verdict (independent)

Artifacts: render /home/user/test/work/clips/calib/render.mp4; subs subtitles.ass; font fonts/YuGothB.ttc (sha256 d923a57f...b2, face "Yu Gothic Bold", weight 700).
Reference normalized x1.5 (720x1280 -> 1080x1920). Measurements: white-pixel-adjacent-to-black-outline row profiles.

| Item | Ref (norm.) | Test | Result |
|---|---|---|---|
| Font identity/weight | Yu Gothic Bold shapes | Same glyph shapes (Latin g/y/k/J, kana) side by side; TTC face Yu Gothic Bold 700; no fallback glyphs seen | PASS |
| White fill / black outline / black shadow | yes | yes | PASS |
| EN above JP stacking | yes | yes | PASS |
| EN glyph band height | 39 px (r_8/r_30/r_50) | 39 px (f_1/f_3/f_9) | PASS (0%) |
| JP glyph band height | 33-36 px | 32-34 px | PASS (within 8%) |
| Line pitch | 48-51 px | 47-50 px | PASS |
| First-line top | y 956-959 | y 957 | PASS (<0.1% H) |
| Horizontal centering | EN/JP centers ~539-545 | f_9 EN center 539.5; f_3 JP line center 537 | PASS (within 10 px) |
| Wrap width | EN lines up to ~800-830 px wide | up to ~770 px wide; 2-line EN wraps similar | PASS |
| Layout (sharp band ~438-1480 over blurred fill) | yes | sharp band 438-1480 visible f_3 | PASS |
| Clipping/garbled glyphs | none | none | PASS |
| Readability | good | good | PASS |

Non-blocking note (outside styling scope, for translation/masking QA): test masks "f**king" while CLAUDE.md example list uses "f*cking"; confirm masking form against the reference-derived list.
Comparison crop: scratchpad cmp.png (ref r_50 top vs test f_9 bottom).

VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none
