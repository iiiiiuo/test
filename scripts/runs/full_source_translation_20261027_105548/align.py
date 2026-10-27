"""Map each approved line's first/last word to medium.en word times (difflib alignment over the whole transcript)."""
import json, re, difflib, sys
sys.path.insert(0, sys.path[0]); from lines import LINES
W = "/mnt/project-files/work/runs/full_source_translation_20261027_105548/asr/"
mw = [w for g in json.load(open(W + "asr_meden.json")) for w in g["words"]]
n = lambda x: re.sub(r"[^a-z0-9]", "", x.lower().replace("going", "gonna").replace("say", "said"))
mt = [n(w[2]) for w in mw]
lt, owner = [], []
for k, l in enumerate(LINES):
    for t in l[4].split():
        if n(t): lt.append(n(t)); owner.append(k)
sm = difflib.SequenceMatcher(None, lt, mt, autojunk=False)
m = {}
for b in sm.get_matching_blocks():
    for i in range(b.size): m[b.a + i] = b.b + i
WT = {}
for k, l in enumerate(LINES):
    idx = [i for i, o in enumerate(owner) if o == k and i in m]
    words = [(lt[i], mw[m[i]][0], mw[m[i]][1]) for i in [j for j, o in enumerate(owner) if o == k] if i in m]
    WT[l[0]] = dict(first=mw[m[idx[0]]][0], last_end=mw[m[idx[-1]]][1], words=words, first_is_first=idx[0] == min(i for i, o in enumerate(owner) if o == k))
if __name__ == "__main__":
    for l in LINES: x = WT[l[0]]; print(l[0], l[1], l[2], "->", round(x["first"], 2), round(x["last_end"], 2), "" if x["first_is_first"] else "FIRST WORD UNMATCHED")
