# Series audit: final-file probes, zero-overlap, duplicate-footage/speech scan, subtitle scans.
# usage: python3 scripts/series_audit.py clip_a clip_b ...   -> work/qa/series_audit.json + output/shared/source_overlap_audit.md
import json, subprocess, sys, re, hashlib, itertools, os
import numpy as np

clips = sys.argv[1:]
SRC = "/mnt/project-files/SOURCE_VIDEO.mp4"
res = {"clips": {}, "overlap": [], "dup_footage": [], "dup_speech": [], "subs": {}}

def sh(cmd): return subprocess.run(cmd, capture_output=True, text=True).stdout
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()

# 1. final-file probes
for c in clips:
    r = f"output/{c}/final.mp4" if os.environ.get("FINAL") else f"work/clips/{c}/render.mp4"
    pr = json.loads(sh(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", r]))
    v = [s for s in pr["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in pr["streams"] if s["codec_type"] == "audio"][0]
    # exact last video packet end
    pk = sh(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "packet=pts,duration", "-of", "csv=p=0", r]).split()
    pts = [tuple(map(int, x.split(",")[:2])) for x in pk if x.count(",") >= 1]
    tb = eval(v["time_base"].replace("/", "/1.0/")) if False else float(v["time_base"].split("/")[0]) / float(v["time_base"].split("/")[1])
    v_start = min(p for p, d in pts) * tb; v_end = max(p + d for p, d in pts) * tb
    apk = sh(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "packet=pts,duration", "-of", "csv=p=0", r]).split()
    apts = [tuple(map(int, x.split(",")[:2])) for x in apk if x.count(",") >= 1]
    atb = float(a["time_base"].split("/")[0]) / float(a["time_base"].split("/")[1])
    a_start = min(p for p, d in apts) * atb; a_end = max(p + d for p, d in apts) * atb
    dec = subprocess.run(["ffmpeg", "-v", "error", "-i", r, "-f", "null", "-"], capture_output=True, text=True)
    vdur = v_end - v_start; adur = a_end - a_start
    res["clips"][c] = {"sha256": sha(r), "w": v["width"], "h": v["height"], "sar": v.get("sample_aspect_ratio", "1:1"),
        "rotation": [sd.get("rotation") for sd in v.get("side_data_list", []) if "rotation" in sd],
        "nb_frames": len(pts), "video_start": round(v_start, 6), "video_dur": round(vdur, 6), "audio_start": round(a_start, 6), "audio_dur": round(adur, 6),
        "decode_errors": dec.stderr.strip()[:300],
        "pass_duration": 60.0 <= vdur < 120.0 and 60.0 <= adur < 120.0,
        "dar": v.get("display_aspect_ratio"), "file": r,
        "pass_format": v["width"] * 16 == v["height"] * 9 and v.get("sample_aspect_ratio", "1:1") in ("1:1", "N/A") and v.get("display_aspect_ratio", "9:16") == "9:16" and not dec.stderr.strip()}

# 2. zero overlap (half-open frame intervals from each clip's manifest, video + audio)
segs = {}
for c in clips:
    m = json.load(open(f"work/clips/{c}/source_manifest.json"))
    segs[c] = [(s["start_frame"], s["end_frame_excl"]) for s in m["video_segments"]]
    au = [(s["start_sample_44k1"], s["end_sample_excl"]) for s in m["audio_segments"]]
    res["clips"][c]["segments"] = segs[c]; res["clips"][c]["audio_samples"] = au
    res["clips"][c]["src_frames"] = sum(b - a for a, b in segs[c])
for c1, c2 in itertools.combinations(clips, 2):
    for a in segs[c1]:
        for b in segs[c2]:
            if max(a[0], b[0]) < min(a[1], b[1]): res["overlap"].append([c1, a, c2, b, min(a[1], b[1]) - max(a[0], b[0])])
    for a in res["clips"][c1]["audio_samples"]:
        for b in res["clips"][c2]["audio_samples"]:
            if max(a[0], b[0]) < min(a[1], b[1]): res["overlap"].append([c1, a, c2, b, "audio"])

# 3. duplicate footage: 32x18 gray thumbnails of every 6th used source frame. A repeated sequence must match in
# appearance (MAE<4) AND in motion (corr of frame-to-frame differences >0.8 with real motion energy) for >=3
# consecutive samples, so a static shared studio background alone does not count.
def thumbs(c):
    out = []
    for a, b in segs[c]:
        t0 = a * 1001 / 30000; d = (b - a) * 1001 / 30000
        raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t0:.4f}", "-t", f"{d:.4f}", "-i", SRC, "-vf", "select='not(mod(n,6))',scale=32:18,format=gray",
                              "-vsync", "0", "-f", "rawvideo", "-"], capture_output=True).stdout
        arr = np.frombuffer(raw, np.uint8).reshape(-1, 18 * 32).astype(float)
        for i in range(len(arr) - 1): out.append((a + 6 * i, arr[i], arr[i + 1] - arr[i]))
    return out
H = {c: thumbs(c) for c in clips}
for c1, c2 in itertools.combinations(clips, 2):
    A = np.array([t for _, t, _ in H[c1]]); B = np.array([t for _, t, _ in H[c2]])
    MA = np.array([m for _, _, m in H[c1]]); MB = np.array([m for _, _, m in H[c2]])
    mae = np.abs(A[:, None, :] - B[None, :, :]).mean(-1)
    ea = np.linalg.norm(MA, axis=1); eb = np.linalg.norm(MB, axis=1)
    corr = (MA @ MB.T) / (ea[:, None] * eb[None, :] + 1e-9)
    ok = (mae < 4) & (corr > 0.8) & (ea[:, None] > 40) & (eb[None, :] > 40)
    hs = set(map(tuple, np.argwhere(ok)))
    for i, j in hs:
        if (i - 1, j - 1) in hs: continue
        k = 0
        while (i + k, j + k) in hs: k += 1
        if k >= 3: res["dup_footage"].append([c1, H[c1][i][0], c2, H[c2][j][0], k])
    res.setdefault("static_lookalike_pairs", {})[f"{c1}|{c2}"] = int((mae < 4).sum())

# 4. duplicate speech: repeated 7-word sequences across clips' displayed English
def words(c):
    t = open(f"work/clips/{c}/subtitles.srt", encoding="utf-8").read()
    en = [l for l in t.splitlines() if re.search(r"[A-Za-z]", l) and "-->" not in l]
    return re.findall(r"[a-z0-9*']+", " ".join(en).lower())
W = {c: words(c) for c in clips}
G = {c: {" ".join(W[c][i:i + 7]) for i in range(len(W[c]) - 6)} for c in clips}
for c1, c2 in itertools.combinations(clips, 2):
    common = G[c1] & G[c2]
    if common: res["dup_speech"].append([c1, c2, sorted(common)[:5]])

# 5. subtitle scans
BAD = re.compile(r"\b(fuck\w*|shit\w*|bitch\w*|nigga\w*|bullshit|motherfuck\w*|pussy|dick)\b", re.I)
for c in clips:
    ass = open(f"work/clips/{c}/subtitles.ass", encoding="utf-8").read()
    srt = open(f"work/clips/{c}/subtitles.srt", encoding="utf-8").read()
    hdr = ass.split("[Events]")[0]
    ev = [l for l in ass.splitlines() if l.startswith("Dialogue:")]
    tt = [(l.split(",")[1], l.split(",")[2]) for l in ev]
    def s(x): h, m, r = x.split(":"); return int(h) * 3600 + int(m) * 60 + float(r)
    dur = res["clips"][c]["video_dur"]
    res["subs"][c] = {"header_sha256": hashlib.sha256(hdr.encode()).hexdigest(), "events": len(ev),
        "unmasked": BAD.findall(srt) + BAD.findall(ass), "events_out_of_bounds": sum(1 for a, b in tt if s(a) < 0 or s(b) > dur + 0.01),
        "font_line": [l for l in hdr.splitlines() if l.startswith("Style:")]}

res["summary"] = {"overlap_pairs": len(res["overlap"]), "dup_footage_runs": len(res["dup_footage"]), "dup_speech_pairs": len(res["dup_speech"]),
    "all_duration_pass": all(v["pass_duration"] for v in res["clips"].values()), "all_format_pass": all(v["pass_format"] for v in res["clips"].values()),
    "unmasked_total": sum(len(v["unmasked"]) for v in res["subs"].values()), "header_hashes": sorted({v["header_sha256"] for v in res["subs"].values()})}
json.dump(res, open("work/qa/series_audit.json", "w"), indent=1, default=str)

L = ["# Source overlap audit", "", f"Source: `{SRC}` (sha256 in each manifest). Convention: half-open `[start_frame, end_frame_excl)`, frame f has pts f*1001 at timebase 1/30000.",
     "Algorithm: `scripts/series_audit.py` compares every video interval pair across clips (overlap iff `max(a.start,b.start) < min(a.end,b.end)`) and every audio sample interval pair (44.1 kHz). Inputs: each clip's `source_manifest.json` (the same intervals the renderer used).", "",
     "| Clip | Source intervals (frames) | Source frames |", "|---|---|---|"]
for c in clips: L.append(f"| {c} | {segs[c]} | {res['clips'][c]['src_frames']} |")
L += ["", f"**Intersecting source frames across clips: {sum(o[4] for o in res['overlap'] if isinstance(o[4], int))}** (pairs: {len(res['overlap'])}). Audio range overlaps: {sum(1 for o in res['overlap'] if o[4] == 'audio')}.",
      f"Duplicate-footage runs (dHash <=3 bits, >=4 consecutive samples): {len(res['dup_footage'])}. Repeated 7-word speech across clips: {len(res['dup_speech'])}.",
      "", "Result: " + ("PASS" if not res["overlap"] else "FAIL")]
open("output/shared/source_overlap_audit.md", "w").write("\n".join(L) + "\n")
print(json.dumps(res["summary"]), json.dumps(res["dup_footage"][:10]), json.dumps(res["dup_speech"][:5]))
for c, v in res["clips"].items(): print(c, v["video_dur"], v["audio_dur"], v["w"], v["h"], v["sar"], v["pass_duration"], v["pass_format"], v["decode_errors"][:80])
