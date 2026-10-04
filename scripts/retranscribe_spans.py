# Local re-transcription of low-confidence spans (cache defect: run-on/low-prob words). Second opinion only.
import json, subprocess, numpy as np, sys
from faster_whisper import WhisperModel
spans=json.loads(sys.argv[1]); out_path=sys.argv[2]
m=WhisperModel("large-v3", device="cpu", compute_type="int8", cpu_threads=4)
prompt="The Breakfast Club radio interview with Charlamagne Tha God, DJ Envy and Jess. Talking about Offset, Kai Cenat, A Boogie, 50 Cent, gambling, the strip club. You feel me? Bro, y'all, nigga."
res=[]
for a,b in spans:
    wav=subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-ss",str(a),"-t",str(b-a),"-i","work/cache/source_16k.wav","-f","s16le","-ac","1","-ar","16000","-"],capture_output=True).stdout
    audio=np.frombuffer(wav,np.int16).astype(np.float32)/32768
    segs,_=m.transcribe(audio,language="en",word_timestamps=True,beam_size=5,initial_prompt=prompt,condition_on_previous_text=True,vad_filter=False)
    for s in segs:
        res.append({"start":round(a+s.start,2),"end":round(a+s.end,2),"text":s.text,"avg_logprob":s.avg_logprob,"words":[{"s":round(a+w.start,2),"e":round(a+w.end,2),"w":w.word,"p":round(w.probability,3)} for w in s.words]})
        print(f"{a+s.start:7.2f}-{a+s.end:7.2f} {s.text}",flush=True)
json.dump(res,open(out_path,"w"),indent=0)
print("DONE")
