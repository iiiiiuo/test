# Clip candidate map

Source: SOURCE_INTERVIEW (747.81 s). Units: work/semantic_map.json. Unused units: U03 (bridge, dependent), U05 (dependent aftermath, 36 s), U13 (outro).

| ID | source intervals (s) | est. dur | topic | opening/setup + ending | standalone | confidence risk | quality | overlap conflicts | status | reason |
|---|---|---|---|---|---|---|---|---|---|---|
| C01 | 0.03-61.00 | 61.0 | Grown up now / headlines | 'How you been?' -> 'Courthouse... album on the way' | standalone | UNTRANSLATABLE: 53.9-61.0 transcribed 5 different ways across 4 model runs | MEDIUM | none | rejected | without the disputed ending only 53 s of coherent material remains (<60 s); extending would take frames from C02 |
| C02 | 61.00-135.28 | 74.3 | Offset owes me 10K | host question -> 'kudos to you, bro' | standalone | MEDIUM: fast speech, pass2-resolved | HIGH | none | accepted | clear question+story+punchline; 74s |
| C03 | 143.30-229.82 | 86.5 | Casino/strip club story | 'Was y'all in the casino together?' -> 'I'm the biggest b**ch' | standalone (Offset referred to as 'he') | MEDIUM | HIGH | C03b | accepted | vivid story with resolution; 86.5s in acceptable band |
| C03b | 135.28-267.24 | 132.0 | Casino + aftermath |  |  |  | MEDIUM | C03, C04b | rejected | >120s; splitting gives C03; U05 alone too short |
| C04 | 267.68-349.84 | 82.2 | Beef with A Boogie & Offset | 'Is the beef too far to squash?' -> 'this shit look a little sad' | standalone | LOW | HIGH | C04b | accepted | complete Q&A; 82s |
| C04b | 257.28-349.84 | 92.6 | Offset cool? + beef |  |  |  | MEDIUM | C03b, C04 | rejected | 92.6s; extra opener rambles; C04 tighter |
| C05 | 350.12-423.80 | 73.7 | Shot 7 times, healing alone | 'Have you fully healed?' -> 'some of them was going through me' | standalone | LOW | HIGH | none | accepted | strong; 74s |
| C06 | 424.36-480.76, 547.38-571.92 | 80.9 | Hospital stories | 'How long to get up?' -> 'I ain't fry like that' | standalone | MEDIUM: one cut joining two hospital anecdotes | HIGH | C07b | accepted | U08 alone 56s (<60); U10 alone 25s; same-topic join, chronological |
| C07 | 482.00-546.06 | 64.1 | Trauma & being misunderstood | 'Does trauma change people?' -> album title meaning | standalone | LOW | HIGH | C07b | accepted | 64s |
| C07b | 482.00-571.92 | 89.9 | Trauma + neck bullet |  |  |  | MEDIUM | C06, C07 | rejected | would strand U08 (<60s); topic shift |
| C08 | 573.88-649.22 | 75.3 | Safe alone | 'You spend a lot of time alone' -> 'different tune in five years / hopefully' | standalone | LOW | HIGH | none | accepted | 75s |
| C09 | 649.34-735.56 | 86.2 | 50 Cent | 'You talked with 50?' -> 'troll me right now' | standalone | MEDIUM: 719-731 age phrase | HIGH | none | accepted | 86s complete thread |

## Final accepted clips (actual source frame intervals, half-open)

| Clip | Source intervals (s) | Duration (s) |
|---|---|---|
| clip_02_offset_owes_10k | 61.13-119.49, 122.96-135.27 | 70.671 |
| clip_03_casino_story | 143.14-159.96, 162.40-164.56, 169.24-211.95, 214.25-222.09, 224.86-227.36 | 72.039 |
| clip_04_beef_offset | 267.63-349.98 | 82.349 |
| clip_05_shot_seven_times | 350.02-419.99 | 69.970 |
| clip_06_hospital_stories | 424.19-468.67, 470.90-480.78, 546.85-564.96 | 72.472 |
| clip_07_trauma_misunderstood | 483.05-508.94, 511.81-546.21 | 60.294 |
| clip_08_safe_alone | 573.71-649.28 | 75.576 |
| clip_09_50_cent | 649.32-675.67, 676.48-680.61, 682.58-719.25, 722.25-723.96, 729.30-731.03, 732.57-735.80 | 73.840 |

Unused material and reasons: U03 bridge 135.28-143.1 (depends on the C02 and C03 context; too short alone), U05 231.4-267.24 (aftermath that depends on C03; 36 s, too short alone, and adding it to C03 exceeds 120 s), U13 outro (no content). LOW-confidence or unresolvable spans were cut inside clips; see each clip's translation_notes.md.
Durations outside the 61-75 s preference band: clip_07 60.29 s (the natural answer ends there; no adjacent unused material), clip_04 82.35 s (a complete Q&A; trimming would cut the resolution), clip_08 75.58 s (ends on the natural closing line).
