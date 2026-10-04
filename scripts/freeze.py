# freeze a PASSed clip: record hashes + reserve intervals in ledger/state (atomic writes), verify zero overlap
import json,sys,hashlib,os,datetime
def sha(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()
def wjson(p,o):
    tmp=p+".tmp"; json.dump(o,open(tmp,"w"),indent=1,ensure_ascii=False); os.replace(tmp,p)
cid=sys.argv[1]; verdicts=sys.argv[2:]
d=f"work/clips/{cid}"; man=json.load(open(f"{d}/source_manifest.json"))
L=json.load(open("work/source_timeline_ledger.json")) if os.path.exists("work/source_timeline_ledger.json") else {}
L.setdefault("source","SOURCE_INTERVIEW sha256 2bc9e4b5d7e07dce784dfdc99991c4b6de6b09d9adb9dd19bb2dec4795d0280f")
L["convention"]="half-open [start_frame,end_frame_exclusive), frame k pts=k*1001 @1/30000; audio = identical time ranges"
L.setdefault("committed",{})
new=[(v["start_frame"],v["end_frame_excl"]) for v in man["video_segments"]]
for other,ivs in L["committed"].items():
    if other==cid: continue
    for a,b in new:
        for x,y in ivs:
            if max(a,x)<min(b,y): sys.exit(f"OVERLAP with {other}: {a,b} vs {x,y}")
L["committed"][cid]=[list(x) for x in new]
L["updated"]=datetime.datetime.utcnow().isoformat()+"Z"
wjson("work/source_timeline_ledger.json",L)
S=json.load(open("work/state.json"))
S.setdefault("clips",[]); S["clips"]=[c for c in S["clips"] if c.get("id")!=cid]
S["clips"].append({"id":cid,"status":"frozen","render":f"{d}/render.mp4","render_sha256":sha(f"{d}/render.mp4"),
  "subtitles_ass_sha256":sha(f"{d}/subtitles.ass"),"spec_sha256":sha(f"{d}/spec.json"),"manifest":f"{d}/source_manifest.json",
  "style_version":"frozen v1 (output/shared/subtitle_style_spec.md)","qa":verdicts,"frames":man["edited_duration_frames"]})
S["used_source_ranges"]=[{"clip":k,"intervals":v} for k,v in L["committed"].items()]
S["updated"]=L["updated"]
wjson("work/state.json",S)
print("frozen",cid,new)
