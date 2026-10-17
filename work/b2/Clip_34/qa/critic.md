VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Items (scope: 2, 5, 7, 10; item 4 CHANGED_LINES = none; 1, 3, 4, 6, 8, 9 NOT IN SCOPE, no blocking problem noticed)
2. PASS - auto.json: 1080x1920, SAR 1:1, video 83.1247 s, audio 83.125 s, frames 1993 = expected 1993, no decode errors.
5. PASS - auto.json unmasked_hits empty; SRT/ASS show s**t, f**k, ni**a; Japanese not mechanically masked.
7. PASS - white bold Yu Gothic, black outline+shadow, EN above JP, centred, max 2 EN + 2 JP lines, inside frame and inside the sharp band (f_0015.71, f_0066.11, crops in qa/extra); matches ref_sheet geometry.
10. PASS - two Expl events, text verbatim from glossary draft: Clip_34_L002 "Tシャツ：“White Lives Matter”Tシャツ" (14.40-19.17 s, 4.8 s, starts with the caption showing "t-shirt", pos y=1188, below the 4-line EN/JP block that ends about y=1145, no overlap); Clip_34_L013 "Haro・GT：BMX自転車のブランド" (61.03-69.25 s, 8.2 s, starts at the JP caption with HaroとかGT, y=1138, below the 2-line block, no overlap). Same font, white fill, black outline/shadow, fs40, single line, no word split, inside y 438..1480.

Non-blocking notes
- A 20 ms gap in EN/JP captions at 66.13-66.15 s (at the jump cut) is the normal inter-caption gap; the Expl row stays on across it.
