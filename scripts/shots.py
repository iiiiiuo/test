import re, json, subprocess, cv2, numpy as np
N=22412
cuts=[0]+[int(re.search(r"pts:\s*(\d+)",l).group(1))//1001 for l in open("work/cache/scenes_raw.txt")]
cuts=sorted(set(cuts))+[N]
shots=[]
casc=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
for i in range(len(cuts)-1):
    a,b=cuts[i],cuts[i+1]
    faces=[]
    for f in [a+(b-a)//4, a+(b-a)//2, a+3*(b-a)//4]:
        t=f*1001/30000
        raw=subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-ss",f"{t:.4f}","-i","/mnt/project-files/SOURCE_VIDEO.mp4","-frames:v","1","-vf","scale=960:540","-f","rawvideo","-pix_fmt","gray","-"],capture_output=True).stdout
        if len(raw)!=960*540: continue
        g=np.frombuffer(raw,np.uint8).reshape(540,960)
        fs=casc.detectMultiScale(g,1.1,6,minSize=(40,40))
        faces.append([[int(x*2),int(y*2),int(w*2),int(h*2)] for x,y,w,h in fs])
    shots.append({"i":i,"start_frame":a,"end_frame_excl":b,"start_s":round(a*1001/30000,3),"dur_s":round((b-a)*1001/30000,2),"faces":faces})
json.dump(shots,open("work/cache/shots.json","w"))
print(len(shots))
