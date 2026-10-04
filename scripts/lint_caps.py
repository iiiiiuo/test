import sys, importlib.util
from PIL import ImageFont
F="work/fonts/YuGothB.ttc"; fen=ImageFont.truetype(F,round(54*2048/2636)); fja=ImageFont.truetype(F,round(50*2048/2636))
d=sys.argv[1]
sp=importlib.util.spec_from_file_location("c",f"{d}/captions.py"); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
bad=0; prev=0
for s,e,en,ja in m.C:
    words=en.split(" "); lines=[""]
    for w in words:
        t=(lines[-1]+" "+w).strip()
        if fen.getlength(t)<=760: lines[-1]=t
        else: lines.append(w)
    jl=ja.split("|")
    if len(lines)>=2 and " " not in lines[-1]:
        pv=lines[-2].split(" "); cand=pv[-1]+" "+lines[-1]
        if len(pv)>1 and fen.getlength(cand)<=760: lines[-2]=" ".join(pv[:-1]); lines[-1]=cand
    if len(lines)>2: print("EN3",s,en); bad+=1
    for l in jl:
        if fja.getlength(l)>760: print("JPW",s,l); bad+=1
    if len(jl)>2: print("JP3",s,ja); bad+=1
    if s<prev: print("ORDER",s)
    prev=s
    for w in ["shit","fuck","bitch","nigga"]:
        if w in en.lower(): print("UNMASKED",s,en); bad+=1
for i in range(len(m.C)-1):
    if m.C[i+1][0]-m.C[i][0]<0.8: print("SHORT",m.C[i][0],m.C[i][2]); bad+=1
print("lint issues:",bad)
