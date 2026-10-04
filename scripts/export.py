# Export a frozen clip to output/<id>/ without re-encoding.
# final.mp4 = stream-copy remux of render.mp4 that only sets the square-pixel flag (SAR 1:1, DAR 9:16);
# decoded video+audio frames are verified identical (framemd5) to the QA'd render.
# usage: python3 scripts/export.py <clip_id>
import json, sys, os, shutil, subprocess, hashlib, importlib.util, re
c = sys.argv[1]; src = f"work/clips/{c}"; dst = f"output/{c}"; os.makedirs(dst, exist_ok=True)
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def fmd5(p):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-map", "0", "-f", "framemd5", "-"], capture_output=True, text=True).stdout
    return hashlib.md5("\n".join(l for l in out.splitlines() if not l.startswith("#")).encode()).hexdigest()
st = json.load(open("work/state.json")); rec = [x for x in st["clips"] if x["id"] == c][0]
assert rec["status"] == "frozen", "clip not frozen"
assert sha(f"{src}/render.mp4") == rec["render_sha256"], "render changed since freeze"
subprocess.run(["ffmpeg", "-v", "error", "-i", f"{src}/render.mp4", "-map", "0", "-c", "copy", "-bsf:v", "h264_metadata=sample_aspect_ratio=1/1",
                "-aspect", "9:16", "-movflags", "+faststart", "-y", f"{dst}/final.mp4"], check=True)
a, b = fmd5(f"{src}/render.mp4"), fmd5(f"{dst}/final.mp4"); assert a == b, "decoded frames differ"
for f in ["subtitles.ass", "subtitles.srt", "source_manifest.json"]: shutil.copyfile(f"{src}/{f}", f"{dst}/{f}")
# transcript.txt: verified caption text, unmasked, with SOURCE timestamps
sp = importlib.util.spec_from_file_location("cap", f"{src}/captions.py"); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
UNMASK = {"s**t": "shit", "f**k": "fuck", "f**king": "fucking", "f**ked": "fucked", "b**ch": "bitch", "ni**a": "nigga", "ni**as": "niggas", "bulls**t": "bullshit"}
def unmask(t): return re.sub(r"[A-Za-z]*\*\*[A-Za-z]*", lambda mm: UNMASK.get(mm.group(0).lower(), mm.group(0)) if mm.group(0).islower() else UNMASK.get(mm.group(0).lower(), mm.group(0)).capitalize(), t)
L = [f"# {c} - unmasked English speech, SOURCE timestamps (s) of /mnt/project-files/SOURCE_VIDEO.mp4", "# speech in source spans not listed in source_manifest.json was cut; '...' marks a fragment too unclear to transcribe", ""]
for s, e, en, ja in m.C: L.append(f"[{s:8.2f} - {e:8.2f}] {unmask(en)}")
open(f"{dst}/transcript.txt", "w").write("\n".join(L) + "\n")
assert "**" not in open(f"{dst}/transcript.txt").read(), "unmask failed"
# qa_report.md
q = ["# QA report: " + c, "", "| Artifact | sha256 |", "|---|---|"]
for f in ["final.mp4", "subtitles.ass", "subtitles.srt", "transcript.txt", "source_manifest.json"]: q.append(f"| {f} | `{sha(f'{dst}/{f}')}` |")
q += ["", f"QA'd render: `{src}/render.mp4` sha256 `{rec['render_sha256']}`; final.mp4 is a stream-copy remux (square-pixel flag only), decoded video+audio framemd5 identical: `{a}`.",
      f"Source frames: {json.load(open(f'{src}/source_manifest.json'))['video_segments'] and [[s['start_frame'], s['end_frame_excl']] for s in json.load(open(f'{src}/source_manifest.json'))['video_segments']]} (half-open).", "",
      "## Independent critic rounds (fresh context each)", ""]
for p in rec["qa"]:
    t = open(p).read(); v = re.search(r"VERDICT:\s*(PASS|FAIL)", t)
    q.append(f"- `{p}`: {v.group(1) if v else '?'}")
last = open(rec["qa"][-1]).read()
items = re.findall(r"^\s*(\d+)\s+([a-z ]+?)\s+(PASS|FAIL)", open(rec["qa"][0]).read(), re.M)
q += ["", "Final round verdict: " + re.search(r"VERDICT:\s*(PASS|FAIL)", last).group(1) + ". Item verdicts (rubric 1-10) are in the critic files above; re-check rounds re-tested only the items affected by each fix and carried other PASS items forward.",
      "", "Series checks: `output/shared/final_series_qa.md`, `output/shared/source_overlap_audit.md`, `work/qa/series_audit.json`.", "Contact sheet: `" + f"{src}/qa/pieces_contact.png`"]
open(f"{dst}/qa_report.md", "w").write("\n".join(q) + "\n")
rec["export"] = {"dir": dst, "final_sha256": sha(f"{dst}/final.mp4"), "framemd5": a}
tmp = "work/state.json.tmp"; json.dump(st, open(tmp, "w"), indent=1, ensure_ascii=False); os.replace(tmp, "work/state.json")
print(c, "exported", rec["export"]["final_sha256"][:12], "framemd5 match")
