#!/bin/bash
# Full-source 9:16 render: no cuts/speed change; spatial reframe + EN/JP subtitle burn-in only.
# Source: iPhone screen recording, HEVC VFR (timebase 1/600, 4903 frames), display-matrix rotation 90 (FFmpeg autorotates
# to 2556x1180). Frames keep their original PTS (passthrough, 1/600 encoder + track timebase). Audio is stream-copied
# (untouched AAC packets). The source audio edit list = 1033-sample empty edit + skip 2112; the copy is written as
# skip 1079, which decodes the same 1033 samples as digital zero, so every source sample keeps its presentation time.
set -e
RUN=full_source_translation_20261027_105548
SRC="/mnt/project-files/ScreenRecording_10-26-2026 15-15-33_1.mp4"
WK=/mnt/project-files/work/runs/$RUN; OUT=${1:-$WK/render.mp4}; ASS=${2:-/mnt/project-files/output/runs/$RUN/subtitles.ass}
D=$(dirname "$0")
X=$(python3 "$D/framing.py" "$WK/framing.json")
cp "$ASS" "$WK/subs_render.ass"
ffmpeg -v error -y -i "$SRC" -filter_complex \
"[0:v]crop=1222:1180:'$X':0,setsar=1,split[a][b];\
[a]scale=1080:1042:flags=lanczos[fg];\
[b]scale=2000:1932,crop=1080:1920,boxblur=28:3[bg];\
[bg][fg]overlay=0:438,subtitles=$WK/subs_render.ass:fontsdir=$WK/fonts,setsar=1,format=yuv420p[v]" \
-map "[v]" -map 0:a -c:v libx264 -preset slow -crf 18 -fps_mode passthrough -video_track_timescale 600 -enc_time_base:v 1/600 \
-c:a copy -movflags +faststart "$OUT"
