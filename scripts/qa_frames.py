import json,sys,subprocess,os
d=f"work/clips/{sys.argv[1]}"; os.makedirs(f"{d}/qa",exist_ok=True)
m=json.load(open(f"{d}/source_manifest.json")); FPS=30000/1001
t=0; ts=[]
for p in m["pieces"]:
    n=p["end_frame_excl"]-p["start_frame"]; ts.append(t+n/FPS/2); t+=n/FPS
step=max(1,len(ts)//20+1)
ts=ts[::1][:24]
subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-y","-i",f"{d}/render.mp4","-vf",
  "select='"+"+".join(f"between(t,{x:.3f},{x+0.034:.3f})" for x in ts)+"',scale=270:480,drawtext=text='%{pts\\:hms}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1",
  "-vsync","vfr",f"{d}/qa/p_%02d.png"])
n=len([f for f in os.listdir(f"{d}/qa") if f.startswith("p_")])
subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-y","-framerate","1","-i",f"{d}/qa/p_%02d.png","-vf","tile=8x3:padding=4","-frames:v","1",f"{d}/qa/pieces_contact.png"])
print(n,"frames ->",f"{d}/qa/pieces_contact.png")
