"""Build EN+JP ASS/SRT for the Snoop Dogg full-source run from the approved translation.
Style = frozen subtitle_style_spec v1 (no explanation row), same as run full_source_translation_20261027_030524.
Timing = large-v3 word timestamps; 006/008/009/011/012 starts moved to measured voice onsets (critic round 1)."""
import json, re, sys
from PIL import ImageFont
RUN = "full_source_translation_20261027_070832"
S = f"/mnt/project-files/state/runs/{RUN}"; WK = f"/mnt/project-files/work/runs/{RUN}"
OUT = sys.argv[1]
FONT = ImageFont.truetype(f"{WK}/fonts/YuGothB.ttc", 54, index=0)
F_JP = ImageFont.truetype(f"{WK}/fonts/YuGothB.ttc", 50, index=0)
EN_K, JP_K = 0.767, 0.753  # libass ink width / PIL advance width (frozen series calibration)
wen = lambda t: FONT.getlength(t) * EN_K
wjp = lambda t: F_JP.getlength(t) * JP_K
appr = {l["id"]: l for l in json.load(open(S + "/approved_translation.json"))["lines"]}
DUR = 50.984  # presented video end: 1528 frames x 1001/30000 (139 edit-list-discarded frames excluded)
# (line id, EN chunk or None = approved EN, JP chunk or None = approved JP, start, last-word end)
E = [
("001",None,None,0.00,1.96),("002",None,None,1.96,3.04),("003",None,None,3.10,3.76),
("004",None,None,4.42,7.22),("005",None,None,7.22,8.24),("006",None,None,8.96,11.28),
("007",None,None,11.36,11.94),
("008",None,None,12.58,15.02),  # one event: a split at 13.22 left a 0.62 s caption (critic r2 note)
("009",None,None,15.84,16.94),("010",None,None,17.14,18.24),("011",None,None,18.72,21.10),
("012",None,None,22.84,23.46),("013",None,None,23.64,24.94),("014",None,None,24.94,25.66),
("015",None,None,25.90,27.24),("016",None,None,27.44,29.70),
("017","You ask me that one more time,","もう一回それ聞いてきたら",30.76,32.10),
("017","I'm gonna hit you in the head with a football.","アメフトのボールで頭ぶん殴るぞ",32.18,33.32),
("018",None,None,33.50,34.28),("019",None,None,34.94,36.18),
("020",None,None,39.30,40.90),("021",None,None,41.00,43.34),
("022",None,None,43.36,43.80),("023",None,None,43.94,44.86),("024",None,None,44.96,45.78),
("026",None,None,46.56,47.42),("027",None,None,48.00,48.36),("028",None,None,48.78,50.62),
]
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
    c = [x for x in c if wjp(x[0]) <= maxw and wjp(x[1]) <= maxw]; assert c, t
    return list(min(c, key=lambda x: abs(wjp(x[0]) - wjp(x[1]))))
ev = []
for lid, en, jp, s, e in E:
    assert appr[lid]["display"], lid
    ev.append(dict(id=lid, en=en if en is not None else appr[lid]["en"], jp=jp if jp is not None else appr[lid]["jp"], s=s, e=e))
# chunks must reproduce approved text exactly; every displayed line used
for lid, l in appr.items():
    ch = [x for x in ev if x["id"] == lid]
    assert bool(ch) == l["display"], lid
    if ch:
        assert " ".join(x["en"] for x in ch) == l["en"], lid
        assert " ".join(x["jp"] for x in ch) == l["jp"], lid
for i, x in enumerate(ev):
    nxt = ev[i + 1]["s"] - 0.02 if i + 1 < len(ev) else DUR
    x["end"] = round(min(max(x["e"] + 0.5, x["s"] + 0.8), nxt), 2)
    assert x["end"] > x["s"]
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
    srt.append(f"{n}\n{at(x['s']).replace('.', ',')}0 --> {at(x['end']).replace('.', ',')}0\n" + "\n".join(r for r, _ in rows) + "\n")
    timing.append(dict(event=n, line_id=x["id"], start=x["s"], end=x["end"], last_word_end=x["e"], en=x["en"], en_display=mask(x["en"]), jp=x["jp"]))
open(OUT + "/subtitles.ass", "w").write("\n".join(out) + "\n")
open(OUT + "/subtitles.srt", "w").write("\n".join(srt))
json.dump(dict(run_id=RUN, source_duration_s=DUR, method="caption start = first-word onset (large-v3 word timestamps); end = last word end + 0.5 s, min 0.8 s, never overlapping the next caption", not_subtitled=["025 (approved: no subtitle)"], events=timing), open(OUT + "/lyric_timing.json", "w"), ensure_ascii=False, indent=1)
print(len(ev), "events")
