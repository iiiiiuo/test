import json, sys, importlib.util
FPS=30000/1001
fr=lambda t: round(t*FPS)
d=sys.argv[1]; ivs=json.loads(sys.argv[2]); extra=json.loads(sys.argv[3]) if len(sys.argv)>3 else {}
spec_=importlib.util.spec_from_file_location("c",f"{d}/captions.py"); m=importlib.util.module_from_spec(spec_); spec_.loader.exec_module(m)
spec={"segments":[[fr(a),fr(b)] for a,b in ivs],"captions":[{"s":s,"e":e,"en":en,"ja":ja} for s,e,en,ja in m.C]}
spec.update(extra)
json.dump(spec,open(f"{d}/spec.json","w"),ensure_ascii=False,indent=0)
print(spec["segments"], sum(b-a for a,b in spec["segments"])/FPS)
