VERDICT: PASS
Blocking gaps: none
Largest gap: none
Fix: none

Scope: items 2, 4 (Clip_06_L009), 5, 7, 10. Items 1, 3, 6, 8, 9: NOT IN SCOPE (nothing blocking noticed).

2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 75.158 s, audio 75.158 s, frames 1802 = expected 1802, decode_errors empty.
4. Translation (L009, 22.98-29.62): PASS. "I'm forgiving. I forgive everybody. I forgive the Clintons." vs 俺は許す　全員許す　クリントン夫妻も許す; meaning matches, on the right moment (ASR: "Clintons" at 27.6 s).
5. Masking: PASS. auto.json unmasked_hits = []; no listed word is unmasked in the EN. "bum-ass" is not on the list. JP is not mechanically masked.
6 (spot check only). Expl events were checked against the ASR word times, see item 10.
7. Typography/visuals: PASS. f_0026.30.png and f_0045.69.png plus sheet_1.jpg: white bold Yu Gothic, black outline and shadow, centred, EN above JP, same size and position as the series; no clipping; max 2 EN + 2 JP lines (4 rows at most).
10. Term-explanation row: PASS.
- Text is verbatim vs glossary_draft_s1.json for L001, L002, L008, L009, L010, L011, L018 (only line breaks differ).
- Timing: L001 0.10-5.03 (4.9 s), L002 5.05-9.82, L008 20.96-24.94 ("Ross" heard 21.28), L009 24.96-29.62 ("Clintons" heard 27.6), L010 29.64-39.00, L011 41.56-49.82, L018 71.93-75.16. All are 3.2 s or longer.
- Placement: Expl y = 1120/1168 under 3 EN+JP rows, 1170/1218 under 4 rows, 1070 under 2 rows. Frames show no overlap with the EN/JP rows, and the row stays inside the sharp band (bottom about 1260, limit 1480).
- Style: Expl = Yu Gothic bold, 40 px, white fill, black outline, shadow (same as Sub).
- Line breaks fall at clause boundaries; no name is split.

Non-blocking notes
- L009 explanation starts at 24.96, about 2 s after the L009 caption (22.98), because the single Expl slot is held by the Ross note until 24.94. It is on screen while "Clintons" is spoken, so this is acceptable.
- The Ross note (L008) runs about 2 s past its speech, for the same reason.
