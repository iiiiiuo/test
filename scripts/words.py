import json,sys
a,b=float(sys.argv[1]),float(sys.argv[2])
for s in json.load(open('work/transcript.json'))['segments']:
  if s['end']>a and s['start']<b:
    print(f"{s['start']:.2f}-{s['end']:.2f} {s['speaker_auto'][:4]}: "+" ".join(f"{w['w'].strip()}@{w['s']:.2f}{'?' if w['p']<0.5 else ''}" for w in s['words']))
