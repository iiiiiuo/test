"""Hard checks on the actual render: streams, duration, frame/PTS identity, frame content order, audio identity/sync,
subtitle text vs approval, masking."""
import json, subprocess, sys, numpy as np, re
RUN = "full_source_translation_20261027_105548"
SRC = "/mnt/project-files/ScreenRecording_10-26-2026 15-15-33_1.mp4"
OUT = sys.argv[1]; ASS = sys.argv[2]
sh = lambda *a: subprocess.run(list(a), capture_output=True).stdout
def pts_s(p):
    tb = sh("ffprobe","-v","error","-select_streams","v","-show_entries","stream=time_base","-of","csv=p=0",p).decode().strip()
    a, b = map(int, tb.splitlines()[0].strip(",").split("/"))
    return [round(int(x.strip(",")) * a / b, 4) for x in sh("ffprobe","-v","error","-select_streams","v","-show_entries","packet=pts","-of","csv=p=0",p).decode().split() if x.strip(",")]
def pcm(p): return np.frombuffer(sh("ffmpeg","-v","error","-i",p,"-vn","-f","f32le","-"), np.float32).reshape(-1, 2)  # native 44.1 kHz stereo
r = {}
vs = sorted(t for t in pts_s(SRC) if t >= 0); vo = sorted(pts_s(OUT))
r["video_frames_presented_src_out"] = [len(vs), len(vo)]; r["video_pts_identical"] = vs == vo
# content: output fg band (scaled to 64x60) vs source crop window, frame by frame
X = sh("python3", f"{sys.path[0]}/framing.py", "/dev/null").decode().strip()
g = lambda args: np.frombuffer(sh(*args), np.uint8).reshape(-1, 60, 64).astype(float)
src = g(["ffmpeg","-v","quiet","-i",SRC,"-an","-vf",f"crop=1222:1180:'{X}':0,scale=64:60,format=gray","-fps_mode","passthrough","-f","rawvideo","-"])
out = g(["ffmpeg","-v","quiet","-i",OUT,"-an","-vf","crop=1080:1042:0:438,scale=64:60,format=gray","-fps_mode","passthrough","-f","rawvideo","-"])
rows = slice(0, 28)  # top half of the band (above the subtitle area at y>=948)
d = [float(np.abs(out[i][rows] - src[i][rows]).mean()) for i in range(min(len(src), len(out)))]
shift = {k: float(np.mean([np.abs(out[i][rows] - src[i + k][rows]).mean() for i in range(10, len(out) - 10, 7)])) for k in (-2, -1, 0, 1, 2)}
r["frame_content_mean_abs_diff"] = dict(n=len(d), mean=round(float(np.mean(d)), 2), max=round(max(d), 2), by_offset={k: round(v, 2) for k, v in shift.items()})
s, o = pcm(SRC), pcm(OUT); r["audio_samples_src_out"] = [len(s), len(o)]
# source: 1033-sample empty edit (silence) before its first decoded sample; output: those 1033 samples are decoded zeros
lead = len(o) - len(s); r["audio_output_lead_samples"] = lead; r["audio_output_lead_peak"] = float(np.abs(o[:lead]).max()) if lead > 0 else None
r["audio_source_empty_edit_samples"] = 1033
r["audio_bit_identical_after_lead"] = bool(lead >= 0 and np.array_equal(o[lead:], s))
r["audio_packets_md5_src_out"] = [sh("ffmpeg","-v","error","-i",p,"-map","0:a","-c","copy","-f","md5","-").decode().strip() for p in (SRC, OUT)]
fmt = json.loads(sh("ffprobe","-v","error","-show_entries","stream=codec_type,width,height,sample_aspect_ratio,duration,start_time:format=duration","-of","json",OUT))
r["streams"] = fmt["streams"]; r["format_duration"] = fmt["format"]["duration"]
appr = json.load(open(f"/mnt/project-files/state/runs/{RUN}/approved_translation.json"))["lines"]
txt = [re.sub(r"\{[^}]*\}", "", l.split(",", 9)[9]).strip() for l in open(ASS) if l.startswith("Dialogue")]
jp_all = "".join(t.replace(" ", "") for t in txt if re.search(r"[぀-ヿ一-鿿]", t))
r["jp_lines_missing_or_altered"] = [l["id"] for l in appr if l["display"] and l["jp"].replace(" ", "") not in jp_all]
r["jp_not_in_approval"] = [t for t in txt if re.search(r"[぀-ヿ一-鿿]", t) and not any(t.replace(" ", "") in l["jp"].replace(" ", "") for l in appr)]
r["annotation_style_present"] = "Expl" in open(ASS).read()
r["unmasked_curse_in_display"] = [t for t in txt if re.search(r"(shit|fuck|bitch|nigga)", t, re.I)]
print(json.dumps(r, ensure_ascii=False, indent=1))
