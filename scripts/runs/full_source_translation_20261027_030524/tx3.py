import sys, wave, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[1], device="cpu", compute_type="int8", cpu_threads=4)
w=wave.open(sys.argv[2]); a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
for span in sys.argv[3:]:
    s,e=map(float,span.split(','))
    segs,_=m.transcribe(a[int(s*16000):int(e*16000)],language="en",beam_size=5,vad_filter=False,condition_on_previous_text=False,temperature=0,word_timestamps=True)
    for g in segs: print(f"{span}: [{g.start+s:.2f}-{g.end+s:.2f}] {g.text.strip()} | "+" ".join(f"{x.word.strip()}({x.probability:.2f})" for x in g.words))
