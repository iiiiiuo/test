# Gauntlet report

Loop: Builder → actual render → one Fresh Clip Critic (independent context, rubric `work/b2/critic_rubric.md`) → targeted fix of the largest gap → re-render → re-check. PASS renders frozen by hash (`work/b2/frozen.json`).

| Target | Round | Verdict | Largest gap / change | Fix |
|---|---|---|---|---|
| Clip_22 | 1 | PASS | none (note: JP names 3 s early at 73.81-77.03) | chunks override Clip_22_L019 |
| Clip_23 | 1 | FAIL | final word 'about' cut ~0.25 s early; 'fit in' clipped at join | hand end windows 1143.08-1143.14 and 1197.24-1197.30 (frames 27408, 28706) |
| Clip_22 | 2 | PASS | none | none |
| Clip_24 | 1 | FAIL | L002 shown 1.1 s early over uncaptioned 'I ain't gonna lie, I've been' | interval 2 start moved to 'since' (frame 35657) |
| Clip_23 | 2 | PASS | none | none |
| Clip_25 | 1 | PASS | note: opening trims ~0.2 s of 'And I' | interval 1 start moved to 1108.40-1108.46 window |
| Clip_24 | 2 | FAIL | L012 JP order inverted vs EN (46.43-50.77) | chunks override Clip_24_L012 |
| Clip_26 | 1 | PASS | non-blocking: 'Right.' caption lags ~0.9 s at 60.01 | none |
| Clip_24 | 3 | PASS | non-blocking: 44.03 fragment EN-only | none |
| Clip_27 | 1 | FAIL | 0.40 s flash caption 'But it's like,' at 55.57 | chunks override Clip_27_L012 (one caption) |
| Clip_28 | 1 | PASS | none | none |
| Clip_29 | 1 | PASS | none | none |
| Clip_27 | 2 | FAIL | opens inside 'Because'; ends while 'manner' sounding | hand windows start 657.98-658.06, end 724.86-724.94 |
| Clip_25 | 2 | PASS | non-blocking: low-level tail of 'and' in first 0.35 s | none |
| Clip_27 | 3 | PASS | non-blocking: framing shows host 0.6-4.4 s | none |
| Clip_31 | 1 | PASS | none | none |
| Clip_30 | 1 | FAIL | opens on uncaptioned tail 'thing is' (0-0.25 s) | start window 51.62-51.78 (frame ~1238) |
| Clip_32 | 1 | PASS | none | none |
| Clip_33 | 1 | PASS | none | none |
| Clip_30 | 2 | PASS | non-blocking: 0.06 s tail of 'is,' at open | none |
| Clip_34 | 1 | FAIL | 'Yeah.' caption carried JP of later 'I fuck with you'; 2.2 s uncaptioned interjection at 65.95-68.15 | L004 chunks override; CUTS 1718.13-1720.13 removing unapproved 'You're transcending' |
| Clip_35 | 1 | FAIL | 1.8 s uncaptioned repeated sentence at 41.93-43.75; next caption early | jump cut 638.43-641.52 + display EN 'the whole time' (L009) |
| Clip_36 | 1 | PASS | non-blocking: caption 10 ~1.2 s early over applause | none |
| Clip_37 | 1 | PASS | cosmetic: caption 4 onset ~1.9 s before words (host stutter) | none |
| Clip_34 | 2 | PASS | non-blocking: JP word order lags EN 58.7-66.1 | none |
| Clip_38 | 1 | PASS | note: same JP repeated on two consecutive captions | chunks override Clip_38_L010 (one JP segment per chunk) |
| Clip_35 | 2 | PASS | non-blocking: abrupt audio drop at join 41.70 | none |
| Clip_39 | 1 | FAIL | JP 'I'm not Moses' shown 4 s early under previous EN chunk | chunks override Clip_39_L003 |
| Clip_38 | 2 | PASS | minor: 62.09 caption EN-only | none |
| Clip_39 | 2 | PASS | cosmetic: ~0.5 s uncaptioned 'you know saying' at start | none |

## Failed approaches
- auto/hand window ended inside glued word about (1196.82-1197.02)
- start window 51.39-51.55 (energy dip before 'is,') put the uncaptioned 'is' in the clip
