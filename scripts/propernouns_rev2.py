"""Rev 2 (user request 2026-10-15): proper nouns in Japanese use the English spelling; Cravo -> Quavo; パフ -> Puff Daddy."""
import re, glob, sys
M = [('フル・イェ','フルYe'),('Googleマップ','Google Maps'),('ジャレッド・クシュナー','Jared Kushner'),('ジャレッド','Jared'),
('スティーヴ・スタウト','Steve Stoute'),('スティーヴ','Steve'),('スタウト','Stoute'),('ラリー・フーヴァー','Larry Hoover'),
('デイヴ・シャペル','Dave Chappelle'),('シャペル','Chappelle'),('ドレイク','Drake'),('ジェイムス・ブレイク','James Blake'),('アルカ','Arca'),
('トラヴィス','Travis'),('コダック・ブラック','Kodak Black'),('バッド・バニー','Bad Bunny'),('シュプリーム','Supreme'),('バレンシアガ','Balenciaga'),
('ラルフ・ローレン','Ralph Lauren'),('サウジ','Saudi'),('イーロン','Elon'),('ダンジョン・ファミリー','Dungeon Family'),('ウータン・クラン','Wu-Tang Clan'),
('ウータン','Wu-Tang'),('トニー・スタークス','Tony Starks'),('ドン・C','Don C'),('ティンバー','Timbs'),('ワラビー','Wallabees'),('ニューヨーク','New York'),
('フリー','Free'),('クール・G・ラップ','Kool G Rap'),('ビッグ・パン','Big Pun'),('リック・ロス','Rick Ross'),('クリントン','Clinton'),('ジョン・レジェンド','John Legend'),
('ビッグ・ショーン','Big Sean'),('ボブ・アイガー','Bob Iger'),('キム','Kim'),('ノース','North'),('ビッグ・ボーイ','Big Boi'),('アウトキャスト','OutKast'),
('シャック','Shaq'),('テイクオフ','Takeoff'),('クラボ','Quavo'),('ツイッター','Twitter'),('モーセ','Moses'),('ピンプ・C','Pimp C'),('ザ・ストロークス','The Strokes'),
('ストロークス','Strokes'),('タッカー・カールソン','Tucker Carlson'),('ヴィクトリアズ・シークレット','Victoria\'s Secret'),('パフ','Puff Daddy'),('ウォルドーフ','Waldorf'),
('カリフォルニア','California'),('マイバッハ','Maybach'),('ヴァンズ','Vans'),('ヴァージル','Virgil'),('パテック','Patek'),('ルイ・ヴィトン','Louis Vuitton'),
('アディダス','Adidas'),('ナイキ','Nike'),('ベルナール・アルノー','Bernard Arnault'),('ベルナール','Bernard'),('アルノー','Arnault'),('アレクサンドル','Alexandre'),
('ジェフ・ベゾス','Jeff Bezos'),('ベゾス','Bezos'),('ラスベガス','Las Vegas'),('アマゾン','Amazon'),('キューバ','Cuba'),('スティーブ・ジョブズ','Steve Jobs'),
('ジョブズ','Jobs'),('ヴォリー','Vory'),('ワック100','Wack 100'),('スペースX','SpaceX'),('グライムス','Grimes'),('ジェイ・Z','Jay-Z'),('ファレル','Pharrell'),
('クインシー・ジョーンズ','Quincy Jones'),('J・コール','J. Cole'),('モス・デフ','Mos Def'),('コモン','Common'),('プレイボーイ','Playboy'),('イリーナ・シェイク','Irina Shayk'),
('グッチ','Gucci'),('レイ・カーツワイル','Ray Kurzweil'),('デムナ','Demna'),('ロスコーズ','Roscoe\'s'),('アッシャー','Usher'),('ドゥッセ','D\'Usse'),('ヘネシー','Hennessy'),
('アメリカ','America'),('ホワイトハウス','White House'),('インスタ','Instagram'),('イェ','Ye')]
K = '[ァ-ヴー・]'
tot = {}
# also: しかもパンはG・ラップに -> しかもBig PunはKool G Rapに (C05, manual)
for f in sorted(glob.glob('work/review_src_*.py')):
    t = open(f, encoding='utf-8').read()
    t = t.replace('Cravo', 'Quavo')
    for a, b in M:
        rx = re.compile(f'(?<!{K}){re.escape(a)}(?!{K})') if a[0] not in 'GJ' else re.compile(re.escape(a))
        t, n = rx.subn(b.replace('\\', '\\\\') if False else b.replace("'", "\\'") if False else b, t)
        tot[a] = tot.get(a, 0) + n
    open(f, 'w', encoding='utf-8').write(t)
print({k: v for k, v in tot.items() if v}); print('unused:', [k for k, v in tot.items() if not v])
