import json, numpy as np
p1=json.load(open("work/cache/transcript.json"))["segments"]
p2=json.load(open("work/cache/transcript_pass2.json"))+json.load(open("work/cache/transcript_pass2b.json"))
spans=[[54,150],[150,232],[255,350],[360,424],[424,480],[480,547],[547,625],[625,692],[692,746]]
inp2=lambda t:any(a<=t<b for a,b in spans)
segs=[dict(s,src_pass=1) for s in p1 if not inp2((s["start"]+s["end"])/2)]+[dict(s,src_pass=2) for s in p2]
segs.sort(key=lambda s:s["start"])
lab=np.load("work/cache/diar_lab.npy"); W=json.load(open("work/cache/diar_wins.json"))
names={0:"GUEST",1:"CHARLAMAGNE",2:"DJ_ENVY",3:"HOST_F?"}
out=[]
for s in segs:
    idx=[i for i,(a,b) in enumerate(W) if a<s["end"] and b>s["start"]]
    c=np.bincount(lab[idx],minlength=4) if idx else np.zeros(4,int)
    low=[w["w"].strip() for w in s["words"] if w["p"]<0.5]
    out.append({"start":round(s["start"],2),"end":round(s["end"],2),"text":s["text"].strip(),"pass":s["src_pass"],
      "speaker_auto":names[int(c.argmax())] if c.sum() else "?","speaker_conf":round(float(c.max()/c.sum()),2) if c.sum() else 0,
      "low_conf_words":low,"words":s["words"]})
json.dump({"source_sha256":"2bc9e4b5d7e07dce784dfdc99991c4b6de6b09d9adb9dd19bb2dec4795d0280f",
 "method":"faster-whisper large-v3 int8 full pass (cond_prev=False); spans "+str(spans)+" replaced by local pass2 (cond_prev=True, context prompt) due to run-on/low-prob defect; speakers: wespeaker r34 onnx embeddings + spectral clustering (k=4), auto labels, verified per clip",
 "segments":out},open("work/transcript.json","w"),ensure_ascii=False,indent=0)
print(len(out))
