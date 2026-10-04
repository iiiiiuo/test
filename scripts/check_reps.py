import subprocess, numpy as np, sys, json
from faster_whisper import WhisperModel
spans=json.loads(sys.argv[1]); models=sys.argv[2].split(",")
for mname in models:
    m=WhisperModel(mname, device="cpu", compute_type="int8", cpu_threads=4)
    for a,b in spans:
        wav=subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-ss",str(a),"-t",str(b-a),"-i","work/cache/source_16k.wav","-f","s16le","-"],capture_output=True).stdout
        audio=np.frombuffer(wav,np.int16).astype(np.float32)/32768
        audio=np.concatenate([np.zeros(8000,np.float32),audio,np.zeros(8000,np.float32)])
        for temp in [0.0]:
            segs,_=m.transcribe(audio,language="en",word_timestamps=True,beam_size=10,condition_on_previous_text=False,vad_filter=False,temperature=temp)
            print(mname,a,b," ".join(f"{w.word.strip()}({w.probability:.2f})" for s in segs for w in s.words),flush=True)
