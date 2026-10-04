# third-opinion local transcription of a short span (no prompt), for resolving pass1/pass2 conflicts
import sys, subprocess, numpy as np
from faster_whisper import WhisperModel
a,b=float(sys.argv[1]),float(sys.argv[2]); size=sys.argv[3] if len(sys.argv)>3 else "large-v3"
m=WhisperModel(size, device="cpu", compute_type="int8", cpu_threads=4)
wav=subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-ss",str(a),"-t",str(b-a),"-i","work/cache/source_16k.wav","-f","s16le","-"],capture_output=True).stdout
audio=np.frombuffer(wav,np.int16).astype(np.float32)/32768
segs,_=m.transcribe(audio,language="en",word_timestamps=True,beam_size=10,condition_on_previous_text=False)
for s in segs:
    print(f"{a+s.start:7.2f}-{a+s.end:7.2f}", " ".join(f"{w.word.strip()}({w.probability:.2f})" for w in s.words))
