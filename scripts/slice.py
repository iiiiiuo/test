import json,sys
d=sys.argv[1]; spec=json.load(open(f"work/clips/{d}/spec.json")); FPS=30000/1001
out=[]
for a,b in spec["segments"]:
    ta,tb=a/FPS,b/FPS
    out.append(f"## source segment {ta:.2f}-{tb:.2f}s (frames {a}-{b})")
    for s in json.load(open('work/transcript.json'))['segments']:
        if s['end']>ta and s['start']<tb:
            out.append(f"{s['start']:.2f}-{s['end']:.2f} [{s['speaker_auto']} auto] {s['text']}"+(f"   (low-conf: {', '.join(s['low_conf_words'])})" if s['low_conf_words'] else ""))
open(f"work/clips/{d}/transcript_slice.txt","w").write("\n".join(out)+"\n")
