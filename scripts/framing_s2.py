"""Per-shot 9:16 framing for one clip: shot cuts from low-res frame differences, crop x from face detection.

Usage: python3 scripts/framing.py Clip_XX   -> work/b2/<clip>/framing.json
Crop window 1119x1080 (aspect of the 1080x1042 foreground band, frozen spec), x clamped to [0, 801].
"""
import json, sys, subprocess, os
import numpy as np, cv2

ROOT = '/home/user/test'
CLIP = sys.argv[1]
clip = {c['clip_id']: c for c in json.load(open(f'{ROOT}/work/s2/selected_clips.json'))}[CLIP]
src = json.load(open(f'{ROOT}/work/sources.json'))[clip['source_id']]
PATH = f"/mnt/project-files/{src['file']}"
sp = src['start_pts']
CW, XMAX = 1119, 1920 - 1119
PW, PH = 933, 900   # 1.2x punch window, same 1080:1042 aspect
cas_f = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cas_a = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
cas_p = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

def frames(t0, n, w, h, gray=True, step=1):
    vf = f'scale={w}:{h}' if step == 1 else f"select='not(mod(n\\,{step}))',scale={w}:{h}"
    cmd = ['ffmpeg', '-v', 'error', '-ss', f'{t0:.6f}', '-t', f'{n * 1001 / 24000:.6f}', '-i', PATH, '-vf', vf, '-fps_mode', 'passthrough',
           '-f', 'rawvideo', '-pix_fmt', 'gray' if gray else 'bgr24', '-']
    b = subprocess.run(cmd, capture_output=True, check=True).stdout
    c = 1 if gray else 3
    return np.frombuffer(b, np.uint8).reshape(-1, h, w, c) if c == 3 else np.frombuffer(b, np.uint8).reshape(-1, h, w)

def faces(img):
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); g = cv2.equalizeHist(g)
    out = []
    for cas, flip in ((cas_f, False), (cas_a, False), (cas_p, False), (cas_p, True)):
        gg = cv2.flip(g, 1) if flip else g
        for (x, y, w, h) in cas.detectMultiScale(gg, 1.1, 6, minSize=(64, 64)):
            if flip: x = g.shape[1] - x - w
            # ignore detections in the lower third (bottles / table) and tiny ones
            if y + h / 2 > g.shape[0] * 0.7: continue
            # reject the gold backdrop crest (highly saturated yellow), a recurring false positive (critics Clip_02/03/04)
            hsv = cv2.cvtColor(img[y:y + h, x:x + w], cv2.COLOR_BGR2HSV).reshape(-1, 3).mean(0)
            if hsv[1] > 140: continue
            out.append((x + w / 2, y + h / 2, w))
    # merge overlapping detections
    merged = []
    for f in sorted(out, key=lambda f: -f[2]):
        if all(abs(f[0] - m[0]) > m[2] * 0.6 for m in merged): merged.append(f)
    return merged

result = []
for iv in clip['intervals']:
    f0, f1 = iv['start_frame'], iv['end_frame_excl']; n = f1 - f0
    t0 = (sp + f0 * 1001) / 24000 - 0.0002
    small = frames(t0, n, 64, 36).astype(np.int16)
    d = np.abs(np.diff(small, axis=0)).mean(axis=(1, 2))
    cuts = [0] + [i + 1 for i in range(len(d)) if d[i] > 18 and d[i] > 3 * np.median(d[max(0, i - 12):i + 12])] + [n]
    # merge shots shorter than 12 frames into the previous shot
    shots = []
    for a, b in zip(cuts[:-1], cuts[1:]):
        if shots and b - a < 12: shots[-1][1] = b
        else: shots.append([a, b])
    STEP = 6
    big = frames(t0, n, 960, 540, gray=False, step=STEP)  # frame k*STEP of the interval
    out = []
    for a, b in shots:
        idx = [k for k in range(len(big)) if a <= k * STEP < b]
        if len(idx) > 12: idx = idx[::len(idx) // 12 + 1]
        idx = idx or [min(a // STEP, len(big) - 1)]
        allf = []
        for i in idx:
            allf += [(f, i) for f in faces(big[i])]
        # cluster detections by x; keep the cluster seen in the most sampled frames (consistency rejects false positives)
        clusters = []
        for f, i in sorted(allf, key=lambda z: -z[0][2]):
            for cl in clusters:
                if abs(cl['cx'] - f[0]) < 60: cl['m'].append((f, i)); break
            else: clusters.append(dict(cx=f[0], m=[(f, i)]))
        best = max(clusters, key=lambda cl: len({i for _, i in cl['m']}) * float(np.median([f[2] for f, _ in cl['m']]))) if clusters else None
        det = [f for f, _ in best['m']] if best and len({i for _, i in best['m']}) >= max(2, 0.3 * len(idx)) else []
        if det:
            cx = 2 * float(np.median([f[0] for f in det])); fw = 2 * float(np.median([f[2] for f in det]))
            cy = 2 * float(np.median([f[1] for f in det]))
            # reference-supported punch-in (frozen spec: 1.2x on wider shots) when the face is small in frame
            if fw < 300:
                w, h = PW, PH
                y = int(round(min(max(cy - 0.30 * PH, 0), 1080 - PH)))
            else:
                w, h, y = CW, 1080, 0
            x = int(round(min(max(cx - w / 2, 0), 1920 - w)))
            how = f'face cx={cx:.0f} cy={cy:.0f} w={fw:.0f} n={len(det)}/{len(idx)}'
        else:
            x = None; w, h, y = CW, 1080, 0; how = 'no face'
        out.append(dict(start=a, end=b, x=x, y=y, w=w, h=h, how=how))
    # fill shots without faces from nearest neighbour shot, else centre
    for i, s in enumerate(out):
        if s['x'] is None:
            nb = [o for o in out if o['x'] is not None]
            o = min(nb, key=lambda o: abs(o['start'] - s['start'])) if nb else None
            s.update(dict(x=o['x'], y=o['y'], w=o['w'], h=o['h']) if o else dict(x=XMAX // 2))
            s['how'] += ' -> neighbour/centre'
    result.append(dict(start_frame=f0, end_frame_excl=f1, shots=out))
    del big
os.makedirs(f'{ROOT}/work/b2/{CLIP}', exist_ok=True)
json.dump(dict(clip=CLIP, crop_w=CW, crop_h=1080, intervals=result), open(f'{ROOT}/work/b2/{CLIP}/framing.json', 'w'), indent=1)
print(CLIP, [(len(r['shots']), sum(1 for s in r['shots'] if 'no face' in s['how'])) for r in result])
