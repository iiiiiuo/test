# Source overlap audit

Source: `/mnt/project-files/SOURCE_VIDEO.mp4` (sha256 in each manifest). Convention: half-open `[start_frame, end_frame_excl)`, frame f has pts f*1001 at timebase 1/30000.
Algorithm: `scripts/series_audit.py` compares every video interval pair across clips (overlap iff `max(a.start,b.start) < min(a.end,b.end)`) and every audio sample interval pair (44.1 kHz). Inputs: each clip's `source_manifest.json` (the same intervals the renderer used).

| Clip | Source intervals (frames) | Source frames |
|---|---|---|
| clip_02_offset_owes_10k | [(1832, 3581), (3685, 4054)] | 2118 |
| clip_03_casino_story | [(4290, 4794), (4867, 4932), (5072, 6352), (6421, 6656), (6739, 6814)] | 2159 |
| clip_04_beef_offset | [(8021, 10489)] | 2468 |
| clip_05_shot_seven_times | [(10490, 12587)] | 2097 |
| clip_06_hospital_stories | [(12713, 14046), (14113, 14409), (16389, 16932)] | 2172 |
| clip_07_trauma_misunderstood | [(14477, 15253), (15339, 16370)] | 1807 |
| clip_08_safe_alone | [(17194, 19459)] | 2265 |
| clip_09_50_cent | [(19460, 20250), (20274, 20398), (20449, 21556), (21646, 21697), (21732, 21909), (21955, 22052)] | 2346 |

**Intersecting source frames across clips: 0** (pairs: 0). Audio range overlaps: 0.
Duplicate-footage runs (dHash <=3 bits, >=4 consecutive samples): 2. Repeated 7-word speech across clips: 0.

Result: PASS
