VERDICT: FAIL
Blocking gaps: Item 4/6 captions 7-9 (12.25-18.81s): JP lines are shifted against EN; caption 8 EN "speak their truth off of D'Usse" shows JP ヘネシーで酔って (Hennessy), caption 7 EN (no brand yet) shows JP D'Usseで酔って言えよ, caption 9 EN "off of Hennessy" shows only 言うんじゃなくてな (evidence: subtitles.srt #7-9 vs sync.txt HEARD at 12.2-18.8s)
Largest gap: JP of the approved L004 block was split by line position, not by spoken phrase, so the D'Usse/Hennessy contrast (the clip's point) is displayed swapped on screen
Fix: Re-time/regroup JP for L004 (and check L011, 49.4-57.9s) so each JP phrase sits with its EN phrase: 12.25 "本音を言うなら" / 14.11 "D'Usseで酔って言えよ" / 16.35 "ヘネシーで酔って言うんじゃなくてな" (same approved wording, only moved across caption boundaries); re-render, re-check items 4/6/7 only

## Items
1. Structure: PASS. Starts at "Like, you at somebody's wedding" (source 213.7 "it adds to it like you at..." precedes, clean phrase start); ends on "A nightcap is well recommended, my friend." with the laugh, resolved. Standalone-understandable.
2. Duration/format: PASS. auto.json: 1080x1920, SAR 1:1, video 74.5745s, audio 74.574s, 1788/1788 frames, no decode errors.
3. Transcript accuracy: PASS. EN matches HEARD (differences only ASR errors: "do say" = D'Usse, "yay" = Ye). Caption 14 "I'm asking and calling for every..." is audio-marginal (HEARD "asking every black") but matches the approved low-conf row; not blocking.
4. Translation fidelity: FAIL. Meaning is fine as a whole, but captions 7-9 attach JP to the wrong moment (see above). Caption 20 "Go full Ye off the D'Usse. Go Ye!" shows only D'Usseで (fragment; "Go Ye!" untranslated); captions 21-22 JP are lighter but acceptable.
5. Masking: PASS. auto.json unmasked_hits = []; s**t x2, f**k visible in 17; JP not masked.
6. Timing/sync: FAIL (same defect). Onsets are close to speech (median 0.165s). Caption 20 (49.39) leads first "Go full Ye" (~50.0s) by ~0.6s, caption 23 (58.57) is ~0.5s after "But yeah" - acceptable. 31.74-34.45 uncaptioned: Ye pauses, hands clasped, laughing (frames 32.5/34), no sentence spoken: acceptable. JP/EN phrase misalignment in 12.25-18.81 as above.
7. Typography/visuals: PASS. White bold Yu Gothic, black outline/shadow, EN above JP, centred, same position as reference (sheet_1/2 vs ref_sheet); max 2 EN + 2 JP lines; no clipping (f_0050.72 checked). Caption 11 JP wraps mid-katakana (ブラックライブスマ/ター), cosmetic.
8. Framing: PASS. Faces in the sharp band with blurred fill; changes only at shot changes (manifest pieces 5165/6322/6378/6577/6700); host cutaway at 47-49s and N.O.R.E. at 58s are real shot changes.
9. Source usage: PASS. Single interval part_6 frames [5165,6953), 1788 frames, continuous, no padding/freeze/repetition (the repeated "Go full Ye" is spoken content).

## Non-blocking notes
- Caption 11 JP line break splits ブラックライブスマ|ター; consider breaking after the "…" or before ブラック.
- Caption 20 could carry "Go Ye!" meaning (e.g. D'Usseで / Yeになれ!) once regrouped.
