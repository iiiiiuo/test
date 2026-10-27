"""Build EN+JP ASS/SRT for run full_source_translation_20261027_105548 from the approved translation (v1).
Style = frozen subtitle_style_spec v1 (no explanation row), same as runs _030524 / _070832.
Timing = medium.en word starts refined to the 250-3500 Hz voiced-region onset (onsets.py), with host-backchannel overrides."""
import json, re, sys
from PIL import ImageFont
RUN = "full_source_translation_20261027_105548"
S = f"/mnt/project-files/state/runs/{RUN}"; WK = f"/mnt/project-files/work/runs/{RUN}"
OUT = sys.argv[1]
FONT = ImageFont.truetype(f"{WK}/fonts/YuGothB.ttc", 54, index=0)
F_JP = ImageFont.truetype(f"{WK}/fonts/YuGothB.ttc", 50, index=0)
EN_K, JP_K = 0.767, 0.753  # libass ink width / PIL advance width (frozen series calibration)
wen = lambda t: FONT.getlength(t) * EN_K
wjp = lambda t: F_JP.getlength(t) * JP_K
appr = {l["id"]: l for l in json.load(open(S + "/approved_translation.json"))["lines"]}
DUR = 135.79  # last video frame pts 81468/600 = 135.78; audio ends 135.81
# (line id, EN chunk or None = approved EN, JP chunk or None = approved JP, start, last-word end)
sys.path.insert(0, sys.path[0]); from lines import LINES; from onsets import res as ON; from align import WT
OVR = {"016": 39.48, "043": 109.38, "037": 93.95, "012": 28.16}  # earlier energy = host "yeah" (016, 043) / breath (037) / host's "right" tail (012)
SAME = "SAME"  # chunk shows the line's full approved JP (EN split only, JP word order does not split cleanly)
SPLIT = {  # line id -> [(en chunk, jp chunk | SAME, start, last-word end), ...]; times = medium.en words + onset check
 "013": [("and let them know, because they", SAME, 29.92, 31.00), ("need to know who their grandfather is.", SAME, 32.20, 33.30)],  # natural pause 31.0-32.2
 "045": [("and from what we was encountering", "俺らが家の外で 出くわしてたことや", 113.86, 116.00), ("and the things we was seeing when we was outside of our home,", "見てたもんを考えたら", 116.06, 118.70)],
 "049": [("Do you feel like there's really a big difference", SAME, 130.25, 133.70), ("between children that grow up with both their parents...", SAME, 133.76, 135.79)],
}
E = []
for l in LINES:
    if l[0] in SPLIT: E += [(l[0],) + c for c in SPLIT[l[0]]]
    else: E.append((l[0], None, None, OVR.get(l[0], min(ON[l[0]], round(WT[l[0]]["first"], 2))), WT[l[0]]["last_end"] - 0.15))  # never later than the ASR word start
MASK = {"shit":"s**t","fuck":"f**k","fucking":"f**king","fucked":"f**ked","bitch":"b**ch","nigga":"ni**a","niggas":"ni**as","motherfucker":"motherf**ker"}
def mask(t): return re.sub(r"[A-Za-z]+", lambda m: MASK.get(m.group(0).lower(), m.group(0)) if m.group(0)[0].islower() else MASK.get(m.group(0).lower(), m.group(0)).capitalize() if m.group(0).lower() in MASK else m.group(0), t)
def wrap_en(t, maxw=760):
    if wen(t) <= maxw: return [t]
    w = t.split(); best = None
    for i in range(1, len(w)):
        a, b = " ".join(w[:i]), " ".join(w[i:])
        if wen(a) <= maxw and wen(b) <= maxw:
            score = abs(wen(a) - wen(b)) - (300 if a.endswith(",") else 0) + (150 if i == 1 or i == len(w) - 1 else 0) + (300 if w[i - 1].lower() in ("a", "an", "the", "of", "to", "in", "you", "we", "do", "you'd") else 0)
            if best is None or score < best[0]: best = (score, [a, b])
    assert best, t
    return best[1]
def wrap_jp(t, maxw=760):
    if not t: return []
    if wjp(t) <= maxw: return [t]
    p = t.split(" ")  # approved JP marks break points with spaces; pick the most balanced 2-line split
    c = [(" ".join(p[:i]), " ".join(p[i:])) for i in range(1, len(p))]
    c = [x for x in c if wjp(x[0]) <= maxw and wjp(x[1]) <= maxw]
    if c: return list(min(c, key=lambda x: abs(wjp(x[0]) - wjp(x[1]))))
    # no usable space: break after closing punctuation or a particle (display line break only, wording unchanged)
    c = [(t[:i], t[i:]) for i in range(2, len(t) - 1) if t[i - 1] in "」』？！、…をはがにでてともと" and t[i] not in "」』？！、…"]
    c = [x for x in c if wjp(x[0]) <= maxw and wjp(x[1]) <= maxw]; assert c, t
    return list(min(c, key=lambda x: abs(wjp(x[0]) - wjp(x[1])) - (400 if x[0][-1] in "」』？！、" else 0)))
ev = []
for lid, en, jp, s, e in E:
    assert appr[lid]["display"], lid
    ev.append(dict(id=lid, en=en if en is not None else appr[lid]["en"], jp=appr[lid]["jp"] if jp in (None, SAME) else jp, same=jp == SAME, s=s, e=e))
# chunks must reproduce approved text exactly; every displayed line used
for lid, l in appr.items():
    ch = [x for x in ev if x["id"] == lid]
    assert bool(ch) == l["display"], lid
    if ch:
        assert " ".join(x["en"] for x in ch) == l["en"], lid
        if any(x["same"] for x in ch): assert all(x["same"] for x in ch), lid
        else: assert " ".join(x["jp"] for x in ch) == l["jp"], lid
for i, x in enumerate(ev):
    nxt = ev[i + 1]["s"] - 0.02 if i + 1 < len(ev) else DUR
    x["end"] = round(min(max(x["e"] + 0.3, x["s"] + 1.0), nxt), 2)
    assert x["end"] > x["s"]
def st(t): ms = int(round(t * 1000)); return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"
def at(t): h=int(t//3600); m=int(t%3600//60); s=t%60; return f"{h}:{m:02d}:{s:05.2f}"
hdr = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Yu Gothic,50,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,2,8,60,60,950,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
out = [hdr.rstrip("\n")]; srt = []; timing = []
for n, x in enumerate(ev, 1):
    rows = [(r, 54) for r in wrap_en(mask(x["en"]))] + [(r, 50) for r in wrap_jp(x["jp"])]
    assert len(rows) <= 4, rows
    for r, fs in rows: assert (wen(r) if fs == 54 else wjp(r)) <= 760, r
    for k, (r, fs) in enumerate(rows):
        out.append(f"Dialogue: 0,{at(x['s'])},{at(x['end'])},Sub,,0,0,0,,{{\\an8\\pos(540,{948 + 50 * k})\\fs{fs}}}{r}")
    srt.append(f"{n}\n{st(x['s'])} --> {st(x['end'])}\n" + "\n".join(r for r, _ in rows) + "\n")
    timing.append(dict(event=n, line_id=x["id"], start=x["s"], end=x["end"], last_word_end=x["e"], en=x["en"], en_display=mask(x["en"]), jp=x["jp"]))
open(OUT + "/subtitles.ass", "w").write("\n".join(out) + "\n")
open(OUT + "/subtitles.srt", "w").write("\n".join(srt))
json.dump(dict(run_id=RUN, source_duration_s=DUR, method="caption start = voiced-region onset of the first word (medium.en word time refined with 250-3500 Hz energy, onsets.py); end = medium.en last word end - 0.15 + 0.3 s, min 1.0 s, never overlapping the next caption", not_subtitled=["host backchannels 'yeah'"], events=timing), open(OUT + "/lyric_timing.json", "w"), ensure_ascii=False, indent=1)
print(len(ev), "events")
