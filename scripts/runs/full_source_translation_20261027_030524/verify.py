"""Hard checks on the actual render: streams, duration, frame/PTS identity, audio identity/sync, subtitle text vs approval."""
import json, subprocess, sys, numpy as np, re
RUN = "full_source_translation_20261027_030524"
SRC = "/mnt/project-files/uploads/hearth/7e1ad6f4-32c8-492c-b8b3-032c4a7f9beb"
OUT = sys.argv[1]; ASS = sys.argv[2]
def probe(p, sel):
    return subprocess.run(["ffprobe","-v","error","-select_streams",sel,"-show_entries","packet=pts","-of","csv=p=0",p],capture_output=True,text=True).stdout.split()
def pcm(p):
    raw = subprocess.run(["ffmpeg","-v","error","-i",p,"-vn","-ac","1","-ar","48000","-f","f32le","-"],capture_output=True).stdout
    return np.frombuffer(raw, np.float32)
r = {}
vs, vo = sorted(map(int, probe(SRC,"v"))), sorted(map(int, probe(OUT,"v")))
r["video_frames"] = [len(vs), len(vo)]; r["video_pts_identical"] = vs == vo
s, o = pcm(SRC), pcm(OUT)
n = min(len(s), len(o)); r["audio_samples"] = [len(s), len(o)]
# lag by cross-correlation on 10 s windows across the whole file
lags = []
for t in range(5, int(n / 48000) - 10, 15):
    a = s[t*48000:(t+10)*48000]; b = o[t*48000-2400:(t+10)*48000+2400]
    c = np.correlate(b, a, "valid"); lags.append(int(np.argmax(c)) - 2400)
r["audio_lag_samples_per_15s"] = lags
k = max(set(lags), key=lags.count); ss = s[:n - abs(k)]; oo = o[k:n] if k >= 0 else o[:n + k]
m = min(len(ss), len(oo)); res = oo[:m] - ss[:m]
r["audio_residual_snr_db"] = round(float(10 * np.log10((ss[:m]**2).sum() / (res**2).sum())), 1)
fmt = json.loads(subprocess.run(["ffprobe","-v","error","-show_entries","stream=codec_type,width,height,sample_aspect_ratio,duration,start_time:format=duration","-of","json",OUT],capture_output=True,text=True).stdout)
r["streams"] = fmt["streams"]; r["format_duration"] = fmt["format"]["duration"]
# subtitle text vs approved translation
appr = json.load(open(f"/mnt/project-files/state/runs/{RUN}/approved_translation.json"))["lines"]
txt = [re.sub(r"\{[^}]*\}", "", l.split(",", 9)[9]).strip() for l in open(ASS) if l.startswith("Dialogue")]
jp_all = "".join(t for t in txt if re.search(r"[぀-ヿ一-鿿]", t))
missing = [l["id"] for l in appr if l["display"] and l["jp"].replace("\n", "") not in jp_all.replace("ナシだ", "ナシだ")]
r["jp_lines_missing_or_altered"] = missing
r["annotation_style_present"] = "Expl" in open(ASS).read()
r["unmasked_curse_in_display"] = [t for t in txt if re.search(r"\b(shit|fuck\w*|bitch|nigga\w*)\b", t, re.I)]
print(json.dumps(r, ensure_ascii=False, indent=1))
