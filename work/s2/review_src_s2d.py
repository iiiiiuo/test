# Series 2 review line sources, batch D (S15-S18).
from review_src_s2a import E
CLIPS = {}

CLIPS['S15'] = [
 E([1], 'Ye', "But every single Black artist need to be on Tidal.", "でも黒人アーティストは\n全員Tidalに\n入るべきなんだ", "Tidal = streaming service bought by Jay-Z in 2015; Ye had just mentioned artists signing with Apple Music's Larry Jackson instead."),
 E([2], 'Ye', "And every single Black artist need to wear Yeezy.", "黒人アーティストは全員\nYeezyを着るべきだ"),
 E([3, 4, 5], 'Ye', "And if Cedric, the head of Balenciaga, talk left or right to me, we need to be able to turn the switch off on Balenciaga.", "Balenciagaのトップの\nCedricが\n俺に妙な口をきいたら\nBalenciagaのスイッチを\n切れるようにしないと", "Cedric Charbit, Balenciaga CEO at the time. 'Talk left or right' = speak against him (left) or for him (right), per the next line."),
 E([6, 7], 'Ye', "And if he talk right to me and us, we turn the switch on.", "俺たちにまともな口をきくなら\nスイッチを入れる", "", "Large-v3 'turn the switch on', turbo 'turn a switch on'."),
 E([8, 9], 'Ye', "We have to come together as a bloc, as Claude Anderson said. We have to be a bloc.", "Claude Andersonが言ったように\n俺たちは一つの“ブロック”に\nならなきゃいけない", "Claude Anderson = economist, author of 'Powernomics', who argues Black Americans must act as an economic bloc.", e='be a block'),
 E([9, 10, 11, 12], 'Ye', "So this time, say, if I... don't... let's say, just in our wildest dreams, Ye doesn't become president.", "だから今回は\nもし俺が…\n万が一だぞ\nYeが大統領に\nなれなかったとしても", s='so this time'),
 E([13], 'Ye', "Hip-hop is a tribe by itself.", "ヒップホップは\nそれ自体が一つの部族なんだ", e='by itself'),
 E([13, 14, 15], 'Ye', "Yeah, so everyone is hip-hop. Also, we come together. That's it. That's a race itself.", "そう\nみんながヒップホップ\nだから一つになる\nそれだけだ\nそれ自体が一つの人種なんだ", "", "MEDIUM: speaker split of 1629-1642 s is inferred (Ye and N.O.R.E. overlap).", s='yeah so', e='a race itself'),
 E([16, 17], 'Host', "Hip-hop is a race. That's what I've been trying to tell you. Hip-hop has no color.", "ヒップホップは人種だって\n俺がずっと言ってるだろ\nヒップホップに肌の色はない", "", "MEDIUM: large-v3 'Hip-hop is a racist'; turbo 'hip-hop is a racist ... this is a race'. 'A race' fits the conversation. Review the audio around 1635.6 s."),
 E([18, 19, 20], 'Ye', "What are we doing with hip-hop? Hip-hop, if you say it's not a race, at least it's a people, just like how Jewish people are a people.", "ヒップホップで\n何をするかだ\n人種じゃないって言うなら\n少なくとも一つの“民”だ\nユダヤ人が一つの民であるようにな", "", "Large-v3 'just like how Jewish people are people', turbo 'just like our jewish people are people'."),
 E([21], 'Host', "Yeah, hip-hop against everybody.", "そう\nヒップホップ対全員だ"),
 E([22], 'Ye', "And we're making our people do our own thing?", "で、俺たちの仲間に\n自分たちのことを\nやらせるんだろ？", "", "Speaker inferred."),
 E([23], 'Host', "Yes.", "そうだ"),
 E([24, 25], 'Ye', "It's time for us to do it. A tremendous name.", "やる時が来たんだ\n“Tremendous”な名前だ", "", "MEDIUM: 'A tremendous name' is clear in large-v3 but its meaning here is unclear (possibly a nod to his 'Tremendous' line)."),
 E([26, 27], 'Ye', "I feel like Drink Champs is doing that immediately, right now. I feel like we're doing it right now.", "Drink Champsは\n今まさにそれをやってる\n俺たちは今やってるんだ", "", "Large-v3 'Dream Champs', turbo 'drink chance' = Drink Champs."),
]

CLIPS['S16'] = [
 E([1], 'Host', "Why are you wearing the Trump... excuse me...", "なんでTrumpの…\nいや、失礼", "Ye is wearing a 'Supreme Lives Matter'-style shirt."),
 E([2, 3], 'Ye', "It's not Trump. It's not Trump.", "Trumpじゃない\nTrumpじゃないって", "", "MEDIUM: turbo hears only the host's 'um' here; large-v3 'It's not Trump. It's not Trump.' Speaker inferred as Ye."),
 E([4], 'Host', "The Supreme Lives Matter.", "その\n“Supreme Lives Matter”", "", "Turbo 'the, um, the, um, the Supreme Lives Matter'."),
 E([5, 6, 7], 'Ye', "This is not Lives Matter. This is Tremaine. This is Tremaine.", "これは“Lives Matter”じゃない\nTremaineだよ\nTremaineだ", "Tremaine Emory, then creative director of Supreme, who criticized Ye publicly.", "Large-v3 'Tremaine', turbo 'Jermaine'; Tremaine Emory fits."),
 E([8], 'Ye', "This is my boy that's at Supreme now.", "今Supremeにいる\n俺の仲間"),
 E([9, 10, 11], 'Ye', "And the weird thing is, like, you know, he's a good guy. He's a good guy.", "妙な話だけどさ\nあいつはいい奴なんだ\nいい奴なんだよ"),
 E([12, 13, 14], 'Ye', "So you think about, like, Pete Davidson. I gave him a negative nickname, Skete Davidson.", "Pete Davidsonを考えてみろよ\nあいつには\n悪いあだ名をつけた\n“Skete Davidson”ってな", "Pete Davidson = comedian who dated Kim Kardashian; Ye called him 'Skete'.", "Large-v3 'skeet', turbo 'ski'; the nickname Ye used publicly is 'Skete'.", e='skeet davidson'),
 E([14, 15], 'Ye', "With Tremaine, I gave him something that was even more powerful. I Ye'd him up. I gave him Tremendous.", "Tremaineには\nもっと強いのをやった\nYe流に格上げして\n“Tremendous”ってあだ名をな", "'Tremendous' = Ye's nickname for Tremaine (also printed on his shirt).", s='with tremaine'),
 E([16, 17], 'Ye', "Right? And then we went in. We appropriate... we did a reverse appropriation of everything Supreme.", "で、乗り込んで\nSupremeの全部を\n“逆盗用”してやったんだ", "", "", s='right and then', e='everything supreme'),
 E([17, 18], 'Ye', "And I went to the studio with Ian Connor, right?", "Ian Connorと\nスタジオに入って", "Ian Connor = stylist and designer.", "Large-v3 'ian connor', turbo 'e and connor'.", s='and i went', e='connor right'),
 E([18, 19, 20], 'Ye', "And we went, Supreme is this... you know, it's a skate brand. It's the high school, right? You know what I'm saying?", "で、Supremeっていうのは\nスケートブランドで\n高校生のノリなんだよ", "", "Large-v3 'we went in is this'; turbo 'we went supreme is this'.", s='and we went', e='im saying'),
 E([20], 'Ye', "So it's like, we went in and flipped everything.", "だから乗り込んで\n全部ひっくり返したんだ", s='so its like'),
 E([21, 22], 'Ye', "This thing is, so the Tremendous movement is more... I don't want to call it a movement, because you don't move nowhere.", "これはさ\n“Tremendousムーブメント”…\nいや、ムーブメントとは呼びたくない\nどこにも動かないからな"),
 E([22, 23, 24], 'Ye', "That's like, the Tremendous idea is so much bigger than even a t-shirt, the other t-shirt I wore.", "“Tremendous”って発想は\nTシャツなんかより\nずっとデカい\n前に着たTシャツよりもな", "'The other t-shirt' = his 'White Lives Matter' shirt.", s='thats like'),
 E([24, 25], 'Ye', "Like, this is finna go crazy.", "これはヤバいことになるぞ", s='like this is', e='go crazy'),
 E([25, 26], 'Ye', "People are... love this, and they love, because you got Dov Charney. It's bigger than White Lives Matter.", "みんな気に入ってる\nDov Charneyが付いてるからな\nWhite Lives Matterよりデカい", "Dov Charney = founder of American Apparel and Los Angeles Apparel, who made the shirts with Ye.", "MEDIUM: large-v3 garbles the end ('duff charlie bigger than white that's my'); turbo 'you got Dove Charney. It's bigger than White Lives Matter.'", s='people are'),
]

CLIPS['S17'] = [
 E([1], 'Host', "So did you get, like, any calls?", "で、誰かから\n電話はあった？", "Context: after Ye's Tucker Carlson interview, did Black people call him to ask what's going on."),
 E([2, 3], 'Ye', "I mean, I'm getting calls at all times, but, yeah, I feel what you're saying, because Tucker Carlson did the interview.", "電話はいつも来てるよ\nでも言いたいことはわかる\nTucker Carlsonがインタビューしたから", "", "Large-v3 'Trevor Carlson'; turbo 'Tucker Carlson'."),
 E([4, 5, 6], 'Ye', "I just feel like there was people in the group, and shit, and the whole interview was just more like on some, like, a conversation about mental health.", "仲間内にもいろいろいて\nインタビュー全体が\nメンタルヘルスの話\nみたいになってたからな"),
 E([7], 'Ye', "And it's hard for, like...", "それって…", "", "Unfinished; turbo has 'And it's hard for like'."),
 E([8, 9], 'Host', "Is it a conversation about mental health? Is that real?", "メンタルヘルスの話なの？\nそれって本当？", "", "Speaker inferred as a host."),
 E([10, 11], 'Ye', "I just think that people don't know how to understand what they're dealing with now.", "みんな今\n何を相手にしてるのか\nわかってないんだと思う", e='dealing with now'),
 E([11, 12, 13, 14], 'Ye', "They've always saw Black people that were an athlete that would follow their contract, a rapper that would follow their contract, an actor that would follow their contract.", "今までの黒人は\n契約に従うアスリート\n契約に従うラッパー\n契約に従う俳優だった", s='theyve'),
 E([14, 15, 16, 17], 'Ye', "They never had to walk into the room and deal with a Black man that would have the audacity to give the most famous, most influential white woman in the world four Black children,", "部屋に入って\nこんな黒人を相手にしたことはない\n世界一有名で影響力のある\n白人女性に\n黒人の子どもを4人も\n授けるような度胸の男をな", "Kim Kardashian; Ye and Kim have four children.", "Both passes 'for black children' = 'four Black children'.", s='they never', e='for black children'),
 E([17, 18], 'Ye', "that would have the audacity to wear a red hat or a White Lives Matter t-shirt,", "赤い帽子や\nWhite Lives MatterのTシャツを\n着る度胸のある男", "Red hat = Trump MAGA cap.", s='that would have the audacity to wear'),
 E([19, 20], 'Ye', "that would have the audacity to have multiple hundred-thousand-square-foot, 57,000-square-foot warehouses, that would have the audacity.", "何千坪もの倉庫を\nいくつも持つ度胸のある男\nそういう度胸のな", "100,000 sq ft ≈ 9,300 m² (about 2,800 tsubo).", "Large-v3 'that would have to audacity'; turbo 'that would have the audacity'."),
 E([21, 22], 'Ye', "They've never dealt with it. So between Black people or white people, they've never seen this before.", "そんなの相手にしたことがないんだ\n黒人も白人も\nこんなの見たことがないんだよ"),
]

CLIPS['S18'] = [
 E([1], 'Ye', "And so let's be easy on everybody.", "だからみんなに\n優しくいこうぜ"),
 E([2, 3], 'Ye', "At the end of the day, we're all dirt beneath God, and we argue amongst each other.", "結局のところ\n俺たちはみんな\n神の前ではただの土くれで\n互いに言い争ってるだけなんだ"),
 E([4, 5], 'Ye', "But my job, as a Quincy Jones beneath... I'm not Moses. I'm Quincy Jones, right?", "でも俺の役目は…\n俺はモーゼじゃない\nQuincy Jonesなんだよ", "Quincy Jones = legendary producer/arranger. Moses = モーゼ per the series rule.", "Large-v3 'as a Quincy Jones beneath' is as spoken (unfinished thought)."),
 E([6, 7], 'Ye', "And we're playing all a symphony, but we're all playing on different notes.", "みんなで一つの交響曲を\n演奏してるけど\nそれぞれ違う音を\n弾いてるんだ", e='different notes'),
 E([7, 8, 9], 'Ye', "It's people that are there for greed. It's people there for... let's not say for the wrong reasons, but we're all here.", "欲のために\nいる奴もいる\n間違った理由とまでは\n言わないけど\nとにかくみんなここにいる", s='its people that'),
 E([10, 11, 12], 'Ye', "And God calls me to bring everybody together, everybody together: the left, the right, the racist, the non-racist, the Christians, the atheists, the straight, the trans, the this, the everybody.", "神は俺に\nみんなをまとめろって言ってる\n左も右も\n差別する奴もしない奴も\nクリスチャンも無神論者も\nストレートもトランスも\nとにかく全員"),
 E([13], 'Ye', "That's what God is calling.", "それが神のお告げなんだ"),
 E([15, 16], 'Ye', "I accept everyone together, because we're all, you know, we can't judge our sins.", "俺はみんなを受け入れる\n俺たちは\n罪を裁けないんだから", "", "Large-v3 adds 'Do you accept everybody together?' just before (1493 s); turbo has nothing there, so it is treated as an ASR artifact. Check the audio around 1493 s.", s='i accept'),
 E([17, 18, 19], 'Ye', "In God's eyes, looking at somebody's wife and killing somebody is the same level of sin. It's all the equal level of sin.", "神の目から見たら\n人の妻をいやらしい目で見るのも\n人を殺すのも\n同じ重さの罪だ\nどれも同じ罪なんだよ", "Echoes Matthew 5:28 ('whoever looks at a woman lustfully...')."),
 E([20, 21], 'Ye', "Looking at somebody's wife and killing somebody is the same level of sin.", "人の妻を見るのも\n人を殺すのも\n同じ罪なんだ"),
 E([22], 'Ye', "We should not be judged by man.", "人間に裁かれるべきじゃない"),
 E([23, 24], 'Ye', "We perform for an audience of one, and that's God.", "俺たちが演じてる相手は\nたった一人の観客\nそれが神だ"),
]
