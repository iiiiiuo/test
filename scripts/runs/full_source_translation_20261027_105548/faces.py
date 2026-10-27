"""Sample faces (Haar) at 4 fps in the 2096x1180 content area; print per-shot face centre x (fraction of content width)."""
import cv2, subprocess, numpy as np, json, sys
S = "/mnt/project-files/ScreenRecording_10-26-2026 15-15-33_1.mp4"
raw = subprocess.run(["ffmpeg","-v","error","-i",S,"-vf","fps=4,crop=2096:1180:230:0,scale=1048:590,format=gray","-f","rawvideo","-"],capture_output=True).stdout
a = np.frombuffer(raw, np.uint8).reshape(-1, 590, 1048)
c = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
out = []
for i, f in enumerate(a):
    fs = c.detectMultiScale(f, 1.1, 6, minSize=(70, 70))
    out.append([round(i / 4, 2), [[round((x + w / 2) / 1048, 3), round(w / 1048, 3)] for x, y, w, h in fs]])
json.dump(out, open(sys.argv[1], "w"))
