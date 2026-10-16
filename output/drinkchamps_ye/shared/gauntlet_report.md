# Gauntlet report

Loop: Builder → actual render → one Fresh Clip Critic (independent context, rubric `work/b/critic_rubric.md`) → targeted fix of the largest gap → re-render → re-check. PASS renders frozen by hash (`work/b/frozen.json`).

| Target | Round | Verdict | Largest gap / change | Fix |
|---|---|---|---|---|
| Clip_01 | 1 | FAIL | clip ended ~0.1 s before last word "ever" while caption showed it | systematic boundary audit of all 42 boundaries (scripts/boundary_check.py) -> 15 clips moved to quietest point between last included and first excluded word (scripts/refine_bounds.py, work/b/boundary_changes.json); Clip_01 host aside (LOW, untranslated) removed by jump cut |
| Clip_04 | 1 | FAIL | false face (backdrop crest) framing 43-52 s; LOW lines L015-L017 captioned as a guess | crest saturation filter + cluster consistency in framing; jump cut removing L015-L017 |
| Clip_02 | 1 | FAIL | final shot framed on backdrop crest; opening edge | framing fix; start moved to quiet point before Yeah (large-v3 span re-check confirms Yeah) |
| Clip_03 | 1 | FAIL | Ye cut at left edge (crest false face); caption led speech by 2 s; LOW last line not heard as written | framing fix; caption onset = first matched word; clip ends after That's crazy (L015 dropped) |
| Clip_01 | 2 | PASS | none | none |
| Clip_06 | 1 | FAIL | "I like both." 2.4 s early (Whisper glued onset of "I" to previous word); "I forgive" 1.6 s early | build_subs: onset moved to just before next heard word when gap >0.8 s; non-final chunk no longer held over long pause; pre-onset only after previous line |
| series | 0 |  | timing rule change in build_subs (affects all clips) |  |
| Clip_08 | 1 | PASS | none | none |
| Clip_07 | 1 | PASS | none | none |
| Clip_11 | 1 | PASS | none | none |
| Clip_06 | 2 | PASS | none (round 2) | none |
| Clip_09 | 1 | FAIL | ended on dangling "But it's funny," | end moved to after "...thousand back." (247.125 s); JP tail segment 笑えるよな dropped (approved segments only) |
| Clip_03 | 1 | FAIL | caption L007 1.75 s early; "Wait a second." uncaptioned (not in approved line) | jump cut 1824.905-1826.19 removes "Wait a second." |
| Clip_05 | 1 | FAIL | caption 9 2.5 s early over pause | build_subs: glued short-word onset fix + forced chunk break at >1 s pauses (snapped to punctuation) |
| Clip_04 | 1 | FAIL | "Stadium. Bad Bunny..." one 5.9 s caption ~3 s early | same pause-break rule (split "Stadium." / "Bad Bunny...") |
| Clip_02 | 1 | FAIL | L014 caption 3.8 s early over laughter | same timing rules (caption now 70.81) |
| Clip_10 | 1 | FAIL | wide shot 19252-19331 cut Ye off at right edge; caption "But..." 1.2 s early | manual 1.2x punch crop on Ye for that shot (work/b/framing_overrides.json); timing rules |
| series | 0 |  | build_subs timing v3: onsets checked against source audio energy (moved to sustained speech), glued-onset gap rule (no trailing punctuation), cross-ASR later onset for unique words >0.8 s apart, first chunk uses checked onset, pause breaks at punctuation, fragment merge; Clip_10_L004 display English repeat added (en_overrides) |  |
| Clip_03 | latest | PASS | none | frozen |
| Clip_04 | latest | PASS | none | frozen |
| Clip_05 | latest | PASS | none | frozen |
| Clip_09 | latest | PASS | none | frozen |
| Clip_14 | latest | PASS | none | frozen |
| Clip_16 | latest | PASS | none | frozen |
| Clip_17 | latest | PASS | none | frozen |
| Clip_21 | latest | PASS | none | frozen |
| Clip_02 | latest | FAIL | final shot crop put laughing Ye at left edge (3/10 detections) | manual crop x=420 for frames 40930-41110 (framing_overrides.json) |
| Clip_10 | latest | FAIL | JP for Jewish/black people shown 3-6 s early; "He offered it." repeat uncaptioned; "But" early | chunk override for L014 (EN-only lead-in), L004 window extended to 794.95, primary ASR pass chosen by match count |
| Clip_12 | latest | FAIL | end cut inside "away" | end moved to 1093.07 (frame 26207) |
| Clip_13 | latest | FAIL | end cut before final "right?" | end moved to 1474.48 (frame 35352) |
| Clip_15 | latest | FAIL | two uncaptioned host sentences; duplicate JP on "Yeah." | jump cuts 1171.355-1173.385 and 1184.17-1187.235; L005 chunk override |
| Clip_18 | latest | FAIL | 0.47 s "You know what I'm saying?" with next sentence JP | L012 chunk override |
| Clip_19 | latest | FAIL | IQ/EQ JP on wrong EN chunks | L010 chunk override |
| Clip_20 | latest | FAIL | D'Usse/Hennessy JP swapped across chunks | L004/L011 chunk overrides |

## Failed approaches
- cross-check with turbo ASR taking later onset: mis-aligned repeated words ("I forgive" x2), replaced by gap rule
- per-token cascading glue loop (moved whole phrases late, Clip_09); energy-only rule (laughter defeats it, Clip_02 L014)
