"""Render one 9:16 clip: frame-exact source intervals, per-shot crop band + blurred fill, burned bilingual ASS.

Usage: python3 scripts/render_clip.py Clip_XX  -> work/b2/<clip>/render.mp4, source_manifest.json
Frozen style: band 1080x1042 at y=438; background = same crop window, blurred, filling 1080x1920.
"""
import json, sys, subprocess, os, hashlib

ROOT = '/home/user/test'
CLIP = sys.argv[1]
OUT = f'{ROOT}/work/b2/{CLIP}'
clip = {c['clip_id']: c for c in json.load(open(f'{ROOT}/work/s2/selected_clips.json'))}[CLIP]
srcs = json.load(open(f'{ROOT}/work/sources.json'))
src = srcs[clip['source_id']]
PATH = f"/mnt/project-files/{src['file']}"
sp = src['start_pts']
fr = json.load(open(f'{OUT}/framing.json'))
ft = lambda f: (sp + f * 1001) / 24000
SEEK_PAD = 0.0002            # seek slightly before frame pts; audio trimmed by the same amount
PAD_SMP = round(SEEK_PAD * 48000)

inputs, fc, cat = [], [], []
manifest_v, manifest_a, pieces = [], [], []
for k, iv in enumerate(fr['intervals']):
    f0, f1 = iv['start_frame'], iv['end_frame_excl']; n = f1 - f0
    t0, t1 = ft(f0), ft(f1)
    a0 = round(t0 * 48000); a1 = round(t1 * 48000)
    ai = len(inputs) // 6   # audio input index for this interval
    inputs += ['-ss', f'{t0 - SEEK_PAD:.6f}', '-t', f'{t1 - t0 + 0.5:.6f}', '-i', PATH]
    S = len(iv['shots'])
    for j, s in enumerate(iv['shots']):
        vi = len(inputs) // 6   # one seeked input per shot: no large split buffers
        ts = ft(f0 + s['start'])
        inputs += ['-ss', f'{ts - SEEK_PAD:.6f}', '-t', f'{(s["end"] - s["start"]) * 1001 / 24000 + 0.5:.6f}', '-i', PATH]
        fc.append(f"[{vi}:v]trim=end_frame={s['end'] - s['start']},setpts=PTS-STARTPTS,"
                  f"crop={s['w']}:{s['h']}:{s['x']}:{s['y']},scale=1080:1042:flags=lanczos,setsar=1,split[f{k}_{j}][b{k}_{j}]")
        fc.append(f"[b{k}_{j}]scale=560:540,crop=304:540,boxblur=14:3,scale=1080:1920:flags=bicubic,setsar=1[bg{k}_{j}]")
        fc.append(f"[bg{k}_{j}][f{k}_{j}]overlay=0:438:shortest=1,setsar=1[v{k}_{j}]")
    fc.append(''.join(f'[v{k}_{j}]' for j in range(S)) + f'concat=n={S}:v=1:a=0[v{k}]')
    fc.append(f"[{ai}:a]aresample=48000,atrim=start_sample={PAD_SMP}:end_sample={PAD_SMP + (a1 - a0)},asetpts=PTS-STARTPTS[a{k}]")
    cat.append(f'[v{k}][a{k}]')
    manifest_v.append(dict(start_frame=f0, end_frame_excl=f1, start_pts=sp + f0 * 1001, end_pts_excl=sp + f1 * 1001,
                           start_s=round(t0, 6), end_s=round(t1, 6)))
    manifest_a.append(dict(start_sample_48k=a0, end_sample_48k_excl=a1, same_as_video_segment=True))
    for s in iv['shots']:
        pieces.append(dict(start_frame=f0 + s['start'], end_frame_excl=f0 + s['end'], crop=dict(w=s['w'], h=s['h'], x=s['x'], y=s['y']), basis=s['how']))
N = len(cat)
fc.append(''.join(cat) + f'concat=n={N}:v=1:a=1[vc][ac]')
fc.append(f"[vc]subtitles=filename={OUT}/subtitles.ass:fontsdir={ROOT}/work/fonts,format=yuv420p[vo]")
cmd = ['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(fc), '-map', '[vo]', '-map', '[ac]',
       '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-profile:v', 'high', '-r', '24000/1001', '-fps_mode', 'cfr',
       '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-movflags', '+faststart', f'{OUT}/render.mp4']
open(f'{OUT}/render_cmd.txt', 'w').write(' '.join(repr(c) if ' ' in c else c for c in cmd))
subprocess.run(cmd, check=True)
h = hashlib.sha256(open(f'{OUT}/render.mp4', 'rb').read()).hexdigest()
man = dict(clip=CLIP, candidate=clip['candidate'], title=clip['title'],
           source=dict(id=clip['source_id'], path=PATH, sha256=src['sha256'], fps='24000/1001', timebase='1/24000', start_pts=sp, pts_per_frame=1001),
           interval_convention='half-open [start_frame,end_frame_exclusive); pts=start_pts+frame*1001 (tb 1/24000)',
           video_segments=manifest_v, audio_segments=manifest_a,
           layers=[dict(type='foreground_band(1080x1042 @y438)+blurred_background', note='both layers from the same source frame; no auxiliary footage')],
           pieces=pieces, subtitles=dict(ass=f'{OUT}/subtitles.ass', sha256=hashlib.sha256(open(f'{OUT}/subtitles.ass', 'rb').read()).hexdigest()),
           translation=dict(approved_csv='review/s2/approved/translations_approved_s2_rev2.csv', revision=2, series=2),
           render=dict(path=f'{OUT}/render.mp4', sha256=h))
json.dump(man, open(f'{OUT}/source_manifest.json', 'w'), indent=1)
print(CLIP, 'rendered', h[:12])
