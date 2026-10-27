import json, sys
from lines import LINES, mask
RUN = "full_source_translation_20261027_105548"
D = f"/mnt/project-files/state/runs/{RUN}/"
VER = sys.argv[1] if len(sys.argv) > 1 else "v1"
CRITIC = sys.argv[2] if len(sys.argv) > 2 else "PENDING"
json.dump({"run_id": RUN, "version": VER,
  "source_sha256": "48ce9840119359f101e18265f9f7e1e48335797580931d65e030063ecfafecfe", "duration_s": 135.811814,
  "asr": {"full": ["faster-whisper medium.en (asr/asr_meden.json)", "large-v3 (asr/asr_lv3.json)"],
          "spans": "large-v3 / medium.en / small.en on disputed spans (asr/spans_*.log, spans2_*.log)",
          "cache_dir": f"/mnt/project-files/work/runs/{RUN}/asr/"},
  "note": "timestamps are ASR word-level estimates (s); EN is unmasked; en_display is the on-screen masked form",
  "unsubtitled": ["host backchannels 'yeah' ~33.5, ~39.1, ~42.3, ~103.0 s", "silence/pauses 59.9-61.1, 64.1-66.5, 95.1-97.0, 129.3-130.3 s"],
  "lines": [dict(id=i, start=s, end=e, speaker=sp, en=en, en_display=mask(en), jp=jp, confidence=c, note=n) for i,s,e,sp,en,jp,c,n in LINES]},
  open(D+"transcription.json","w"), ensure_ascii=False, indent=1)
def ts(x): return f"{int(x//60):02d}:{x%60:06.3f}"
o = [f"""# SOURCE_VIDEO 全編和訳レビュー（{VER}）

RUN_ID: `{RUN}`

## A. SOURCE INFORMATION

```
Source:
ScreenRecording_10-26-2026 15-15-33_1.mp4（2026-10-27 10:54 添付, sha256 48ce9840…fecfe）
※ 今回の依頼文の SOURCE_VIDEO.mp4 = この添付ファイルとして扱っています（プロジェクト直下の SOURCE_VIDEO.mp4 = Breakfast Club とは別物）

Source Duration:
135.812 s（コンテナ）/ 映像 135.788 s, 4903フレーム, HEVC, 可変フレームレート（60fps基準, 平均36.1fps）, 回転90°で表示 2556x1180 / 音声 AAC 44.1kHz stereo 135.788 s（開始 0.023 s）

Translation Coverage:
00:00.000 – 02:15.812

Translation Status:
PENDING HUMAN APPROVAL
```

内容: iPhoneの画面録画。ポッドキャスト（マイクに「GIVING」のロゴ）に出演した Snoop Dogg が、孫への接し方、自分の祖父と母の話をする。最後は女性ホストの質問の途中で終わる。BGMなし。

- 横長の番組映像の左右に黒帯があり、ほぼ全編 Snoop のアップ。最後の約5秒だけホストと2人の画になる。
- `1.lyrics.txt` はリポジトリ・input/・プロジェクトフォルダのどこにもなく、歌詞もない会話動画なので N/A。
- タイムスタンプはASRの単語タイミング（秒）。フレーム単位の調整はPHASE 2で行います。
- 信頼度: HIGH = 複数モデルが一致 / MED = 細部が不一致（意味は同じ）/ LOW = 聞き取りが確定できない。
- 下の EN は字幕に表示する形（伏せ字適用済み, s**t）。伏せ字なしの原文は transcription.json にあります。
- 固有名詞は英語表記（Snoop, Beverly, Snoopy, Bonanza）。動画内に解説行は出しません。
- 006〜010, 025〜037 は Snoop が孫・祖父・母・子供の頃の自分の声色をまねて再現している部分です。セリフは「」で区別しています。
- 字幕にしない音: ホストの相づち「yeah」（約33.5, 39.1, 42.3, 103.0秒）と、無音の間（59.9–61.1, 64.1–66.5, 95.1–97.0, 129.3–130.3秒）。

## B. COMPLETE ENGLISH / JAPANESE TRANSLATION
"""]
for i,s,e,sp,en,jp,c,n in LINES:
    o.append(f"### [{i}]\n\nTimestamp: {ts(s)} – {ts(e)}  \nSpeaker: {sp}  \nConfidence: {c}\n\nEN: {mask(en)}  \nJP: {jp}\n" + (f"\n> {n}\n" if n else ""))
o.append(open(f"/home/user/test/scripts/runs/{RUN}/review_tail.md").read().replace("{CRITIC}", CRITIC))
open(D+"translation_review.md","w").write("\n".join(o))
print("written", len(LINES))
