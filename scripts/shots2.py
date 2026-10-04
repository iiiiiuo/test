import json, subprocess, numpy as np
N=22412; FPS=30000/1001
ts=[float(l.split("pts_time:")[1]) for l in open("work/cache/scenes_010.txt")]
fr=[round(t*FPS) for t in ts]
# cluster into transitions
cl=[]
for f in fr:
    if cl and f-cl[-1][1]<=15: cl[-1][1]=f
    else: cl.append([f,f])
spans=[]; prev=0
for a,b in cl:
    if a>prev: spans.append({"start_frame":prev,"end_frame_excl":a})
    if b>a:
        spans.append({"start_frame":a,"end_frame_excl":b+1,"transition":True}); prev=b+1
    else: prev=a
spans.append({"start_frame":prev,"end_frame_excl":N})
spans=[s for s in spans if s["end_frame_excl"]>s["start_frame"]]
def grab(f,w=96,h=54):
    t=f/FPS
    raw=subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-ss",f"{t:.4f}","-i","/mnt/project-files/SOURCE_VIDEO.mp4","-frames:v","1","-vf",f"scale={w}:{h}","-f","rawvideo","-pix_fmt","rgb24","-"],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(h,w,3).astype(float)
ex={"G":4.0,"W":35.0,"E":0.4,"W2":50.4,"H":42.17}
exv={k:grab(round(v*FPS)) for k,v in ex.items()}
def corr(a,b):
    a=a-a.mean(); b=b-b.mean(); return float((a*b).sum()/np.sqrt((a*a).sum()*(b*b).sum()))
for s in spans:
    if s.get("transition"): s["cls"]="T"; continue
    m=(s["start_frame"]+s["end_frame_excl"])//2
    v=grab(m); sc={k:round(corr(v,e),3) for k,e in exv.items()}
    s["scores"]=sc; s["cls"]=max(sc,key=sc.get)
    s["mid_frame"]=m
for s in spans:
    s["start_s"]=round(s["start_frame"]/FPS,3); s["end_s"]=round(s["end_frame_excl"]/FPS,3)
json.dump(spans,open("work/cache/shots.json","w"),indent=0)
for s in spans:
    if s["cls"]!="T": print(s["start_s"],s["end_s"],s["cls"],s["scores"])
