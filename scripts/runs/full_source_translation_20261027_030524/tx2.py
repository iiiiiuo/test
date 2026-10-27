import sys, json
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[1], device="cpu", compute_type="int8", cpu_threads=4)
import wave,numpy as np; w=wave.open(sys.argv[2]); a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
segs,_ = m.transcribe(a, language="en", word_timestamps=True, vad_filter=False, beam_size=5, condition_on_previous_text=False, temperature=0)
res=[]
for s in segs:
    res.append(dict(start=s.start,end=s.end,text=s.text.strip(),lp=s.avg_logprob,nsp=s.no_speech_prob,words=[dict(w=w.word,s=w.start,e=w.end,p=w.probability) for w in s.words]))
    print(f"[{s.start:7.2f}-{s.end:7.2f}] lp={s.avg_logprob:.2f} nsp={s.no_speech_prob:.2f} {s.text.strip()}", flush=True)
json.dump(res, open(sys.argv[3],"w"), indent=0)
