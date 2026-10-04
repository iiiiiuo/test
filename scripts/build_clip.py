#!/usr/bin/env python3
"""Build one clip from work/clips/<id>/spec.json -> work/clips/<id>/render.mp4 (+ subtitles.ass/.srt, source_manifest.json)."""
import json, sys, os, subprocess, hashlib
from PIL import ImageFont
SRC="/mnt/project-files/SOURCE_VIDEO.mp4"; FPSN,FPSD=30000,1001; SR=44100
FONT="work/fonts/YuGothB.ttc"
STYLE={"en_fs":54,"ja_fs":50,"top":948,"pitch":50,"maxw":760,"band_y":438,"band_h":1042}
CROPS={"G":dict(z=1.0,x0=430,y0=0),"E":dict(z=1.0,x0=610,y0=0),"H":dict(z=1.0,x0=700,y0=0),
       "WG":dict(z=1.2,x0=987,y0=150),"WL":dict(z=1.2,x0=0,y0=150)}
def f2t(f): return f*FPSD/FPSN
def run(c): subprocess.run(c,check=True)
def crop_box(c):
    ch=round(1080/c["z"]/2)*2; cw=round(ch*1080/1042/2)*2
    return cw,ch,min(c["x0"],1920-cw),min(c["y0"],1080-ch)
def main(cid):
    d=f"work/clips/{cid}"; spec=json.load(open(f"{d}/spec.json"))
    shots=json.load(open("work/cache/shots.json"))
    segs=spec["segments"]
    spk=spec.get("wide_speakers",[])  # [[t0,t1,"L"]] -> crop WL in wide shots during these source times
    over=spec.get("crop_overrides",[])  # [[f0,f1,"G"|..]]
    def cls_at(f):
        for o in over:
            if o[0]<=f<o[1]: return o[2]
        idx=[i for i,s in enumerate(shots) if s["start_frame"]<=f<s["end_frame_excl"]][0]
        s=shots[idx]
        trans=False
        if s["cls"]=="T":  # dissolve: outgoing shot's framing for first half, incoming for second half
            trans=True
            if f<(s["start_frame"]+s["end_frame_excl"])//2:
                j=idx-1
                while j>0 and shots[j]["cls"]=="T": j-=1
            else:
                j=idx+1
                while j<len(shots)-1 and shots[j]["cls"]=="T": j+=1
            s=shots[j]
        c=s["cls"]
        if c in("W","W2"):
            if trans: return "WG"
            t=f2t(f); c="WL" if any(a<=t<b for a,b,_ in spk) else "WG"
        return c
    pieces=[]
    for a,b in segs:
        cur=None
        for f in range(a,b):
            c=cls_at(f)
            if cur and cur[2]==c: cur[1]=f+1
            else:
                cur=[f,f+1,c]; pieces.append(cur)
    # merge tiny pieces (<12 frames) into previous piece
    merged=[]
    for p in pieces:
        if merged and p[1]-p[0]<12 and merged[-1][1]==p[0]: merged[-1][1]=p[1]
        else: merged.append(p)
    pieces=merged
    # subtitles
    def src2out(t):
        acc=0.0
        for a,b in segs:
            ta,tb=f2t(a),f2t(b)
            if ta-0.12<=t<=tb+0.12: return acc+min(max(t,ta),tb)-ta  # clamp onsets within 0.12 s of a segment edge
            acc+=tb-ta
        raise ValueError(f"time {t} outside segments")
    fen=ImageFont.truetype(FONT,round(STYLE["en_fs"]*2048/2636),index=0)
    fja=ImageFont.truetype(FONT,round(STYLE["ja_fs"]*2048/2636),index=0)
    def wrap_en(s):
        words=s.split(" "); lines=[""]
        for w in words:
            t=(lines[-1]+" "+w).strip()
            if fen.getlength(t)<=STYLE["maxw"]: lines[-1]=t
            else: lines.append(w)
        if len(lines)>=2 and " " not in lines[-1]:
            prev=lines[-2].split(" ")
            cand=prev[-1]+" "+lines[-1]
            if len(prev)>1 and fen.getlength(cand)<=STYLE["maxw"]: lines[-2]=" ".join(prev[:-1]); lines[-1]=cand
        if len(lines)>2: raise ValueError("EN caption needs >2 lines, split it: "+s)
        return lines
    def ja_lines(s):
        out=s.split("|")
        for l in out:
            if fja.getlength(l)>STYLE["maxw"]: raise ValueError("JP line too wide: "+l)
        return out
    def ts(t):
        cs=round(t*100); return f"{cs//360000}:{cs//6000%60:02d}:{cs//100%60:02d}.{cs%100:02d}"
    head=open("work/style/template_header.ass").read()
    ev=[]; srt=[]
    caps=spec["captions"]
    # timing: hold each caption up to 0.5s after its last word, never past the next caption's onset; min 0.8s
    times=[]
    for k,cap in enumerate(caps):
        t0=src2out(cap["s"]); t1=src2out(cap["e"])+0.5
        if k+1<len(caps): t1=min(t1,src2out(caps[k+1]["s"])-0.02)
        t1=min(max(t1,t0+0.8),src2out(f2t(segs[-1][1]))) if k+1==len(caps) else max(t1,min(t0+0.8,src2out(caps[k+1]["s"])-0.02))
        times.append((t0,t1))
    for k,cap in enumerate(caps):
        t0,t1=times[k]
        en=wrap_en(cap["en"]); ja=ja_lines(cap["ja"])
        y=STYLE["top"]
        for l in en:
            ev.append(f"Dialogue: 0,{ts(t0)},{ts(t1)},Sub,,0,0,0,,{{\\an8\\pos(540,{y})\\fs{STYLE['en_fs']}}}{l}"); y+=STYLE["pitch"]
        for l in ja:
            ev.append(f"Dialogue: 0,{ts(t0)},{ts(t1)},Sub,,0,0,0,,{{\\an8\\pos(540,{y})\\fs{STYLE['ja_fs']}}}{l}"); y+=STYLE["pitch"]
        def st(t):
            ms=round(t*1000); return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"
        srt.append(f"{k+1}\n{st(t0)} --> {st(t1)}\n{cap['en']}\n{cap['ja'].replace('|',chr(10))}\n")
    open(f"{d}/subtitles.ass","w").write(head+"\n".join(ev)+"\n")
    open(f"{d}/subtitles.srt","w").write("\n".join(srt))
    if os.environ.get('SUBS_ONLY'): print('subs ok'); return
    import shutil; shutil.rmtree(f"{d}/pieces",ignore_errors=True); os.makedirs(f"{d}/pieces",exist_ok=True)
    lst=open(f"{d}/pieces/list.txt","w")
    for i,(a,b,c) in enumerate(pieces):
        ts,te=(a-0.5)*FPSD/FPSN,(b-0.5)*FPSD/FPSN
        if c.startswith("MOVE:"):  # follow a source camera pan: linear crop x from xa to xb over the piece
            _,xa,xb=c.split(":"); cw,ch,_,y0=crop_box(CROPS["G"]); dur=(b-a)*FPSD/FPSN
            x0=f"'{xa}+({xb}-{xa})*min(t/{dur:.4f},1)'"
        else:
            cw,ch,x0,y0=crop_box(CROPS[c])
        vf=(f"trim=start={ts:.6f}:end={te:.6f},setpts=PTS-STARTPTS,crop={cw}:{ch}:{x0}:{y0},split[s1][s2];"
            f"[s1]scale=1080:{STYLE['band_h']}:flags=lanczos[fg];[s2]scale=2000:1932,crop=1080:1920,boxblur=28:3[bg];"
            f"[bg][fg]overlay=0:{STYLE['band_y']},setsar=1,format=yuv420p")
        out=f"{d}/pieces/p{i:03d}.mp4"
        run(["ffmpeg","-nostdin","-loglevel","error","-y","-copyts","-ss",f"{max(0,ts-3):.3f}","-i",SRC,"-filter_complex","[0:v]"+vf,
             "-an","-c:v","libx264","-preset","veryfast","-crf","12","-r",f"{FPSN}/{FPSD}","-frames:v",str(b-a),out])
        lst.write(f"file 'p{i:03d}.mp4'\n")
    lst.close()
    run(["ffmpeg","-nostdin","-loglevel","error","-y","-f","concat","-safe","0","-i",f"{d}/pieces/list.txt","-c","copy",f"{d}/video_nosub.mp4"])
    # audio: exact sample ranges per segment, 8ms fades at internal joins
    filt=[]; 
    for i,(a,b) in enumerate(segs):
        s0=round(f2t(a)*SR); s1=round(f2t(b)*SR); dur=(s1-s0)/SR
        fx=f"[0:a]atrim=start_sample={s0}:end_sample={s1},asetpts=PTS-STARTPTS"
        if i>0: fx+=",afade=t=in:d=0.008"
        if i<len(segs)-1: fx+=f",afade=t=out:st={dur-0.008:.6f}:d=0.008"
        filt.append(fx+f"[a{i}]")
    filt.append("".join(f"[a{i}]" for i in range(len(segs)))+f"concat=n={len(segs)}:v=0:a=1[aout]")
    run(["ffmpeg","-nostdin","-loglevel","error","-y","-i",SRC,"-filter_complex",";".join(filt),"-map","[aout]","-c:a","pcm_s16le",f"{d}/audio.wav"])
    run(["ffmpeg","-nostdin","-loglevel","error","-y","-i",f"{d}/video_nosub.mp4","-i",f"{d}/audio.wav",
         "-vf",f"subtitles={d}/subtitles.ass:fontsdir=work/fonts","-map","0:v","-map","1:a",
         "-c:v","libx264","-preset","medium","-crf","18","-profile:v","high","-pix_fmt","yuv420p","-r",f"{FPSN}/{FPSD}",
         "-c:a","aac","-b:a","192k","-ar","44100","-movflags","+faststart",f"{d}/render.mp4"])
    man={"clip":cid,"source":{"path":SRC,"sha256":"2bc9e4b5d7e07dce784dfdc99991c4b6de6b09d9adb9dd19bb2dec4795d0280f","fps":"30000/1001","timebase":"1/30000","pts_per_frame":1001},
         "interval_convention":"half-open [start_frame,end_frame_exclusive); pts=frame*1001 (tb 1/30000)",
         "video_segments":[{"start_frame":a,"end_frame_excl":b,"start_pts":a*1001,"end_pts_excl":b*1001,"start_s":round(f2t(a),6),"end_s":round(f2t(b),6)} for a,b in segs],
         "audio_segments":[{"start_sample_44k1":round(f2t(a)*SR),"end_sample_excl":round(f2t(b)*SR),"same_as_video_segment":True} for a,b in segs],
         "layers":[{"type":"foreground_band+blurred_background","note":"both layers derive from the same source frame at the same timestamp; no auxiliary footage"}],
         "pieces":[{"start_frame":a,"end_frame_excl":b,"framing":c,"crop":(dict(zip(["w","h","x","y"],crop_box(CROPS[c]))) if c in CROPS else {"pan_x":c})} for a,b,c in pieces],
         "edited_duration_frames":sum(b-a for a,b in segs)}
    json.dump(man,open(f"{d}/source_manifest.json","w"),indent=1)
    print(cid,"frames",man["edited_duration_frames"],"dur",round(f2t(man["edited_duration_frames"]),3),"pieces",len(pieces))
if __name__=="__main__": main(sys.argv[1])
