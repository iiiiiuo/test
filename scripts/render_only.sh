#!/bin/bash
# subs + render + QA using existing framing.json (framing already reviewed via framing_sheet.jpg)
cd /home/user/test
for c in "$@"; do
  python3 scripts/build_subs.py $c > /dev/null || { echo "FAIL subs $c"; continue; }
  python3 scripts/render_clip.py $c || { echo "FAIL render $c"; continue; }
  [ -d work/b/$c/qa ] && { rm -rf work/b/$c/qa_prev; mv work/b/$c/qa work/b/$c/qa_prev; }; mkdir -p work/b/$c/qa
  python3 scripts/source_context.py $c && python3 scripts/qa_clip.py $c || echo "FAIL qa $c"
done
echo BATCHDONE
