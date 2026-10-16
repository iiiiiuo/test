#!/bin/bash
# large-v3 re-pass on candidate spans (local re-analysis only)
cd /home/user/test
python3 - <<'PY'
import json,subprocess,os
sp=json.load(open('work/s2/candidate_spans.json'))
for cid,(p,s,e) in sp.items():
    out=f'work/asr/{cid}.large.json'
    if os.path.exists(out): continue
    subprocess.run(['python3','scripts/transcribe.py','/root/models/large-v3',f'work/audio/{p}.wav',out,'4',f'{s},{e}'],stdout=open(f'work/asr/{cid}.large.log','w'),stderr=subprocess.STDOUT)
    subprocess.run(['cp',out,'/mnt/project-files/work/asr/'])
PY
