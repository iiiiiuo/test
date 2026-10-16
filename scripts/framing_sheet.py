"""One thumbnail per shot (the actual cropped band at mid-shot) for framing review."""
import json, sys, subprocess
from PIL import Image, ImageDraw
ROOT = '/home/user/test'
for CLIP in sys.argv[1:]:
    fr = json.load(open(f'{ROOT}/work/b/{CLIP}/framing.json'))
    clip = {c['clip_id']: c for c in json.load(open(f'{ROOT}/work/selected_clips.json'))}[CLIP]
    src = json.load(open(f'{ROOT}/work/sources.json'))[clip['source_id']]
    th = []
    for iv in fr['intervals']:
        for s in iv['shots']:
            f = iv['start_frame'] + (s['start'] + s['end']) // 2
            t = (src['start_pts'] + f * 1001) / 24000
            p = f'/tmp/claude-0/fs_{CLIP}_{f}.png'
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.4f}', '-i', f"/mnt/project-files/{src['file']}", '-frames:v', '1',
                            '-vf', f"crop={s['w']}:{s['h']}:{s['x']}:{s['y']},scale=300:290", p], check=True)
            im = Image.open(p); ImageDraw.Draw(im).text((4, 4), f"{s['start']}-{s['end']} {s['how'][:28]}", fill='red'); th.append(im)
    W = Image.new('RGB', (300 * min(6, len(th)), 290 * ((len(th) + 5) // 6)))
    for i, im in enumerate(th): W.paste(im, ((i % 6) * 300, (i // 6) * 290))
    W.save(f'{ROOT}/work/b/{CLIP}/framing_sheet.jpg', quality=85)
    print(CLIP, len(th))
