import json, numpy as np, onnxruntime as ort, kaldi_native_fbank as knf, wave
from sklearn.cluster import AgglomerativeClustering
w=wave.open("work/cache/source_16k.wav"); sig=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)
sess=ort.InferenceSession("work/models/wespeaker_r34.onnx")
def emb(a,b):
    x=sig[int(a*16000):int(b*16000)]
    o=knf.FbankOptions(); o.frame_opts.dither=0; o.mel_opts.num_bins=80; o.frame_opts.samp_freq=16000
    f=knf.OnlineFbank(o); f.accept_waveform(16000,x.tolist()); f.input_finished()
    F=np.array([f.get_frame(i) for i in range(f.num_frames_ready)],np.float32)
    F=F-F.mean(0)
    e=sess.run(None,{"feats":F[None]})[0][0]; return e/np.linalg.norm(e)
T=json.load(open("work/cache/transcript.json"))["segments"]
words=[x for s in T for x in s["words"]]
# windows over speech: 1.5s windows, hop .75 where words exist
wins=[]; t=0; end=words[-1]["e"]
while t<end:
    ws=[x for x in words if x["s"]<t+1.5 and x["e"]>t]
    sp=sum(min(x["e"],t+1.5)-max(x["s"],t) for x in ws)
    if sp>0.6: wins.append((t,t+1.5))
    t+=0.5
E=np.array([emb(a,b) for a,b in wins])
np.save("work/cache/diar_emb.npy",E); json.dump(wins,open("work/cache/diar_wins.json","w"))
for k in [3,4,5,6]:
    lab=AgglomerativeClustering(n_clusters=k,metric="cosine",linkage="average").fit_predict(E)
    print(k,np.bincount(lab))
