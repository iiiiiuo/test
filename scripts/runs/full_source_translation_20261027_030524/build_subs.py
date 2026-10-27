"""Build EN+JP ASS/SRT for the full-source run from the approved translation.
Style = frozen subtitle_style_spec v1 (no explanation row). Timing = medium.en / large-v3
word onsets checked against 250-3500 Hz energy; see TIMING notes in lyric_timing.json."""
import json, sys
from PIL import ImageFont
RUN = "full_source_translation_20261027_030524"
S = f"/mnt/project-files/state/runs/{RUN}"; WK = f"/mnt/project-files/work/runs/{RUN}"
OUT = sys.argv[1]
FONT = ImageFont.truetype(f"{WK}/fonts/YuGothB.ttc", 54, index=0)
F_JP = ImageFont.truetype(f"{WK}/fonts/YuGothB.ttc", 50, index=0)
# libass ink width / PIL advance width, from the frozen series calibration (work/b/calib_widths.json)
EN_K, JP_K = 0.767, 0.753
wen = lambda t: FONT.getlength(t) * EN_K
wjp = lambda t: F_JP.getlength(t) * JP_K
appr = {l["id"]: l for l in json.load(open(S + "/approved_translation.json"))["lines"]}
DUR = 130.714
# (line id, EN chunk or None = full approved EN, JP chunk or None = full approved JP, start, last-word end)
E = [
("001",None,None,2.90,3.80),("002",None,None,4.48,5.08),("003",None,None,5.40,5.62),
("004",None,None,5.96,6.62),("005",None,None,6.82,6.94),("006",None,None,7.46,8.62),
("007",None,None,8.84,9.12),("008",None,None,9.20,10.18),("009",None,None,10.30,11.30),
("010",None,None,11.56,12.46),("011",None,None,15.32,16.80),("012",None,None,17.02,19.00),
("013",None,None,19.04,19.26),("014",None,None,20.46,21.40),
("015+016","That's crazy.\nPull it off.","ヤバいな\nカバー取って",21.44,22.20),
("017",None,None,25.75,27.25),
("019","Travis, for reals, though,","Travis、マジな話",36.74,37.80),
("019","it all comes together when you see this interior.","この内装見たら全部しっくりくるんだ",37.86,39.80),
("020",None,None,52.28,54.06),("021",None,None,55.64,56.40),
("022","We took the exact factory pattern","純正とまったく同じパターンにしたから",57.10,58.80),
("022","so it still looks like the factory SV.","ちゃんと純正のSVに見えるんだ",58.90,60.70),
("023",None,None,61.10,61.50),("024",None,None,65.00,65.65),
("025",None,None,68.50,70.80),("026",None,None,72.30,73.66),
("027",None,None,75.55,77.20),("028",None,None,77.45,78.90),("029",None,None,79.40,82.20),
("030",None,None,82.90,84.25),("031",None,None,84.44,85.10),("032",None,None,89.30,91.65),
("033",None,None,91.68,91.95),("034",None,None,92.64,93.40),("035",None,None,94.28,95.06),
("036",None,None,95.18,95.90),("037",None,None,97.30,97.62),("038",None,None,98.25,98.75),
("039",None,None,99.85,100.34),
("040","So Travis just came, he picked up his Lambo,","Travisが来て Lamboを受け取って",107.90,110.70),
("040","and he's happy.","喜んでくれたよ",110.86,111.45),
("041",None,None,112.30,114.05),
("042","I kind of gave him a couple sneak peeks",None,115.00,116.60),
("042","of what it was gonna look like,",None,116.70,117.75),
("043","but then I was like, you know what,",None,117.82,118.62),
("043","I want this thing to be a surprise",None,118.70,119.88),
("044","because in pictures you can't really see","写真じゃこの色の本当の感じは",119.90,122.15),
("044","what this color looks like.","わからないからね",122.20,123.20),
("045","So today he got to see it for the first time,","で、今日初めて実物を見て",123.74,125.60),
("045","and he loved it.","すごく気に入ってくれた",125.68,126.75),
]
MASK = {"shit":"s**t","fuck":"f**k","fucking":"f**king","fucked":"f**ked","bitch":"b**ch","nigga":"ni**a","niggas":"ni**as"}
def mask(t):
    import re
    return re.sub(r"[A-Za-z]+", lambda m: MASK.get(m.group(0).lower(), m.group(0)), t)
def wrap_en(t, maxw=760):
    if "\n" in t: return t.split("\n")
    if wen(t) <= maxw: return [t]
    w = t.split(); best = None
    for i in range(1, len(w)):
        a, b = " ".join(w[:i]), " ".join(w[i:])
        if wen(a) <= maxw and wen(b) <= maxw:
            score = abs(wen(a) - wen(b)) - (120 if a.endswith(",") else 0) + (150 if i == 1 or i == len(w) - 1 else 0) + (300 if w[i - 1].lower() in ("a", "an", "the", "of", "to") else 0)
            if best is None or score < best[0]: best = (score, [a, b])
    assert best, t
    return best[1]
ev = []
for k, (lid, en, jp, s, e) in enumerate(E):
    ids = lid.split("+")
    en = en if en is not None else appr[ids[0]]["en"]
    jp = jp if jp is not None else appr[ids[0]]["jp"]
    for i in ids: assert appr[i]["display"], i
    ev.append(dict(ids=ids, en=en, jp=jp, s=s, e=e))
# check that chunks reproduce approved text exactly
for lid in sorted({i for x in ev for i in x["ids"]}):
    ens = " ".join(x["en"].replace("\n", " ") for x in ev if lid in x["ids"] and len(x["ids"]) == 1)
    if ens: assert ens == appr[lid]["en"], (lid, ens)
    jps = []
    for x in ev:
        if lid in x["ids"] and len(x["ids"]) == 1 and x["jp"] not in jps: jps.append(x["jp"])
    if jps: assert "\n".join(jps).replace("\n", "") == appr[lid]["jp"].replace("\n", ""), (lid, jps)
# timing: hold up to 0.5 s after last word, min 0.8 s, never overlapping next
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
    rows = [(r, 54) for r in wrap_en(mask(x["en"]))] + [(r, 50) for r in x["jp"].split("\n")]
    assert len(rows) <= 4, rows
    for r, fs in rows: assert (wen(r) if fs == 54 else wjp(r)) <= 760, r
    for k, (r, fs) in enumerate(rows):
        out.append(f"Dialogue: 0,{at(x['s'])},{at(x['end'])},Sub,,0,0,0,,{{\\an8\\pos(540,{948 + 50 * k})\\fs{fs}}}{r}")
    srt.append(f"{n}\n{at(x['s']).replace('.', ',')}0 --> {at(x['end']).replace('.', ',')}0\n" + "\n".join(r for r, _ in rows) + "\n")
    timing.append(dict(event=n, line_ids=x["ids"], start=x["s"], end=x["end"], last_word_end=x["e"], en=x["en"], en_display=mask(x["en"]), jp=x["jp"]))
open(OUT + "/subtitles.ass", "w").write("\n".join(out) + "\n")
open(OUT + "/subtitles.srt", "w").write("\n".join(srt))
json.dump(dict(run_id=RUN, source_duration_s=DUR, method="caption start = first-word onset (medium.en span pass, cross-checked with large-v3 and 250-3500 Hz energy); end = last word end + 0.5 s, min 0.8 s, never overlapping the next caption", not_subtitled=["018 (approved: no subtitle)"], events=timing), open(OUT + "/lyric_timing.json", "w"), ensure_ascii=False, indent=1)
print(len(ev), "events")
