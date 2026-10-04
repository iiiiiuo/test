# report shot cuts within 15 frames of each segment boundary (flash-frame risk)
import json,sys
spec=json.load(open(f"work/clips/{sys.argv[1]}/spec.json")); shots=json.load(open("work/cache/shots.json"))
cuts=[s["start_frame"] for s in shots]
for a,b in spec["segments"]:
    for c in cuts:
        if 0<c-a<=15: print(f"start {a}: cut at {c} (+{c-a} frames) -> consider start {c}")
        if 0<b-c<=15: print(f"end {b}: cut at {c} (-{b-c} frames) -> consider end {c}")
print("checked",spec["segments"])
