"""Write source ASR context (20 s before/after each interval) for critic review of start/end naturalness."""
import json, sys
ROOT = '/home/user/test'
CLIP = sys.argv[1]
clip = {c['clip_id']: c for c in json.load(open(f'{ROOT}/work/s2/selected_clips.json'))}[CLIP]
segs = json.load(open(f"{ROOT}/work/asr/{clip['source_id']}.turbo.json"))['segments']
out = [f"# {CLIP} source context ({clip['source_file']}), turbo ASR. '>>' = inside a used interval, '  ' = outside (not in the clip)"]
for iv in clip['intervals']:
    a, b = iv['start_s'], iv['end_s']
    out.append(f"\n## interval {a:.2f}-{b:.2f}s (frames {iv['start_frame']}-{iv['end_frame_excl']})")
    for s in segs:
        if s['end'] < a - 20 or s['start'] > b + 20: continue
        mid = (s['start'] + s['end']) / 2
        tag = '>>' if a <= mid <= b else '  '
        out.append(f"{tag} {s['start']:8.2f}-{s['end']:8.2f} {s['text'].strip()}")
open(f'{ROOT}/work/b2/{CLIP}/qa/source_context.txt', 'w').write('\n'.join(out) + '\n')
