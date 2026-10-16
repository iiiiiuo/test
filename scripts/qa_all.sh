#!/bin/bash
# run automated QA for each clip as soon as its render is logged
cd /home/user/test
for i in $(seq -w 2 21); do
  c=Clip_$i
  until grep -q "$c rendered\|FAIL render $c" work/b/render_all.log; do sleep 10; done
  mkdir -p work/b/$c/qa; python3 scripts/source_context.py $c
  python3 scripts/qa_clip.py $c || echo "FAIL qa $c"
done
echo QADONE
