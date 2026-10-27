"""Refine caption starts: start of the voiced (250-3500 Hz) region that contains the medium.en first-word time,
bounded to [s-0.5, s+0.4] and never before the previous line's last-word end."""
import json, sys, numpy as np
sys.path.insert(0, sys.path[0]); from lines import LINES; from align import WT
W = "/mnt/project-files/work/runs/full_source_translation_20261027_105548/asr/"
e = np.load(W + "band_energy_db.npy")
def onset(s, prev_end):
    k0, k1 = int(max(s - 1.0, 0) * 100), int((s + 0.4) * 100)
    base = np.percentile(e[k0:k1], 5); thr = base + 15
    lo = max(int((s - 0.5) * 100), int(prev_end * 100) + 1, 0)
    k = int((s + 0.05) * 100)
    if e[k] > thr:                      # voiced at s: walk back to region start
        while k - 1 >= lo and e[k - 1] > thr: k -= 1
    else:                               # silent at s: first rise after s
        while k < k1 and not (e[k:k + 3] > thr).all(): k += 1
    return round(k / 100, 2)
res = {}; prev = 0
for l in LINES:
    f = WT[l[0]]["first"]
    res[l[0]] = onset(f, prev) if f > 0 else 0.0; prev = WT[l[0]]["last_end"] - 0.25  # medium.en word ends run late

if __name__ == "__main__":
    for l in LINES: print(l[0], WT[l[0]]['first'], res[l[0]], round(res[l[0]] - WT[l[0]]['first'], 2))
