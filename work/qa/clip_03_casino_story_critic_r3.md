# clip_03_casino_story: Fresh Clip Critic, round 3 (scoped re-check)

Artifacts judged:
- render.mp4 sha256 8d9cc8dcf426c734494b0208cfe588bbdf56102864978eabcb5908d709c766ae (mtime 19:55:03)
- subtitles.ass sha256 c20956568b3544d4d870143764374a0ab0cd1fa07fd7ca8b5970eb35dcfe26b1
- subtitles.srt sha256 97a41f4e937756f330cbc38d0e55afe37539c211a6516d8ea3659ffef34e52ad

Probe: video 72.0386 s, audio 72.0380 s, 1080x1920.
Output-to-source map (from the manifest): seg3 out 18.986 = src 169.236; seg4 out 61.695 = src 214.247; seg5 out 69.536 = src 224.858.
Evidence frames: scratchpad c3r3/f_42.5.png, f_44.6.png, f_62.7.png, f_70.5.png. Word timings come from large-v3 with word_timestamps (scratchpad c3r3/words.py) and from scripts/check_span.py.

VERDICT: PASS

## Item 3 transcript accuracy: PASS
- src 191.50-193.92 (out 41.25-43.65), "No, no, no. I think probably, like, got spun off,". The audio gives No[191.58] no no, I think[192.02|0.81-0.97] probably like got[193.16|0.93] spun off[193.70-193.92]. "think" is confirmed in two independent runs (0.97 and 0.81), so the "fake" in the machine slice is not supported. The caption matches the speech. The frame f_42.5 shows the caption burned in.
- src 193.92-195.76 (out 43.67-45.51), "like, ten times, blah, blah, blah.". The audio gives like[193.92] 10 times blah blah blah[195.62], all at 0.92-1.00. It matches. Frame f_44.6.
- src 214.80-215.88 (out 62.25-63.33), "It's the Emmys!". Three runs heard "It's the Emmys" (Emmys 0.77/0.97/0.85). Window 214.25-214.85 contains only unintelligible noise ("All right" at 0.05), so no intelligible speech is left uncaptioned. Frame f_62.7.
- src 224.96 (out 69.64-72.04), "At that point, it ain't about the money. It's about the respect.". In the wide context window, "And" runs 224.76-225.08 (conf 0.25). It starts before the cut at 224.858, so inside the clip only a fragment of it is heard. In the clip-bounded window, the speech before "ain't" is unclear ("It" at 0.16). Dropping "And" is supported. "at that point" is at 1.00 in the wide window. Frame f_70.5.
- Regression diff (git HEAD vs current SRT): the only text changes are the three declared edits. Every other cue's text is identical (renumbered +1 after the split).

## Item 4 translation: PASS
- "It's the Emmys!" becomes エミー賞もんだな！ ("Emmy-worthy"). This keeps the sarcastic "that's acting/drama" joke in natural spoken Japanese.
- The split pair いやいや、たぶん / 10回くらいはぐらかされてさ reads as one natural Japanese sentence across the two cards, with the verb landing in the second. "got spun off" is rendered as はぐらかされて, which is faithful. "I think" is covered by たぶん.
- The JP for "At that point..." (そうなると金の問題じゃねぇ / リスペクトの問題なんだよ) is unchanged and still faithful.
- No stereotyped dialect and no asterisks in the JP.

## Item 6 timing: PASS
- Cue 19 onset 41.25 = src 191.50, and the first "No" is at 191.58 (0.08 s early). It ends at 193.90, matching the end of "off" at 193.92. Dwell 2.40 s.
- Cue 20 onset 43.67 = src 193.92, and "like" is at 193.92 (0.00). It ends at 195.76, where "blah" ends at 195.62. Dwell 1.84 s.
- Cue 30 onset 62.25 = src 214.80, and "It's" starts at about 214.96 (0.16 s early). It ends at 215.88, where speech ends at 215.80. Dwell 1.08 s.
- Cue 34 onset 69.64 = src 224.96, and "at" is at about 225.08 (0.12 s early). It ends at the clip end.
- There are no overlaps across all 34 cues, and the minimum dwell is 0.90 s (cue 24, unchanged).
- Non-blocking, undeclared change: cue 29 ("I'm like, leave him, bro.") now ends at 61.910 instead of 61.748. That runs 0.215 s (about 6 frames) past the seg3/seg4 cut at out 61.695, onto the next shot, and about 0.3 s past the end of the speech (src 211.84 = out 61.59). It is cosmetic, and there is no overlap with cue 30.

## Item 7 visuals (split captions and the edited cues): PASS
- f_42.5 shows EN "No, no, no. I think probably, like, got" / "spun off," with JP いやいや、たぶん below it.
- f_44.6 shows a single EN line and a single JP line.
- f_62.7 and f_70.5 render cleanly.
- All four frames use the same Sub style (Yu Gothic, bold -1, white, black outline 3, shadow 2), with EN above JP at the shared positions 948/998/1048/1098. Nothing clips or overflows.
- Minor: the wrap in cue 19 puts "got" at the end of line 1 and "spun off," alone on line 2. Readability is acceptable.

## Items 1, 2, 5, 8, 9, 10
- Items 1, 2, 5, 8 and 10 carry forward as PASS from the prior rounds. The footage is unchanged, and the duration was re-probed at 72.04 s (60 <= d < 120).
- Masking in the edited cues: none of them contains a curse word.
- Item 9 was out of scope.
