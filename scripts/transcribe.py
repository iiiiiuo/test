import sys, json, time
from faster_whisper import WhisperModel
import wave, numpy as np
model_dir, wav, out = sys.argv[1], sys.argv[2], sys.argv[3]
threads = int(sys.argv[4]) if len(sys.argv) > 4 else 4
clip = sys.argv[5] if len(sys.argv) > 5 else None  # "start,end" seconds
m = WhisperModel(model_dir, device="cpu", compute_type="int8", cpu_threads=threads)
t0 = time.time()
kw = dict(language="en", word_timestamps=True, vad_filter=True, beam_size=5,
          condition_on_previous_text=False, vad_parameters=dict(min_silence_duration_ms=500))
w = wave.open(wav); sr = w.getframerate(); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
off = 0.0
if clip:
    cs, ce = map(float, clip.split(",")); a = a[int(cs*sr):int(ce*sr)]; off = cs
segs, info = m.transcribe(a, **kw)
res = []
for s in segs:
    res.append(dict(start=round(s.start+off, 3), end=round(s.end+off, 3), text=s.text.strip(),
                    avg_logprob=round(s.avg_logprob, 3), no_speech_prob=round(s.no_speech_prob, 3),
                    words=[dict(w=w.word, s=round(w.start+off, 3), e=round(w.end+off, 3), p=round(w.probability, 3)) for w in (s.words or [])]))
    print(f"[{s.start+off:8.2f}-{s.end+off:8.2f}] {s.text.strip()}", flush=True)
json.dump(dict(model=model_dir, wav=wav, clip=clip, elapsed=round(time.time() - t0, 1), segments=res), open(out, "w"), indent=0, ensure_ascii=False)
print("ELAPSED", time.time() - t0, file=sys.stderr)
