#!/bin/bash
# subs + render + QA using existing framing.json (framing already reviewed via framing_sheet.jpg)
cd /home/user/test
for c in "$@"; do
  python3 scripts/build_subs_s2.py $c > /dev/null || { echo "FAIL subs $c"; continue; }
  python3 scripts/render_clip_s2.py $c || { echo "FAIL render $c"; continue; }
  [ -d work/b2/$c/qa ] && { rm -rf work/b2/$c/qa_prev; mv work/b2/$c/qa work/b2/$c/qa_prev; }; mkdir -p work/b2/$c/qa
  python3 scripts/source_context_s2.py $c && python3 scripts/qa_clip_s2.py $c || echo "FAIL qa $c"
done
echo BATCHDONE
