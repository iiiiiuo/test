import json, sys, time
from faster_whisper import WhisperModel
t=time.time()
m=WhisperModel("large-v3", device="cpu", compute_type="int8", cpu_threads=4)
segs,info=m.transcribe("work/cache/source_16k.wav", language="en", word_timestamps=True, beam_size=5, vad_filter=False, condition_on_previous_text=False)
out=[]
for s in segs:
    out.append({"start":s.start,"end":s.end,"text":s.text,"avg_logprob":s.avg_logprob,"no_speech_prob":s.no_speech_prob,
      "words":[{"s":w.start,"e":w.end,"w":w.word,"p":round(w.probability,3)} for w in s.words]})
    print(f"{s.start:7.2f}-{s.end:7.2f} {s.text}", flush=True)
json.dump({"model":"faster-whisper large-v3 int8 cpu","source_sha256":"2bc9e4b5d7e07dce784dfdc99991c4b6de6b09d9adb9dd19bb2dec4795d0280f","segments":out},open("work/cache/transcript.json","w"),ensure_ascii=False,indent=0)
print("DONE",time.time()-t)
