# Series 2 review line sources, batch A (S01-S04). Same format as work/review_src_a.py:
# E(auto-line numbers in work/s2/lines_auto/<clip>.json, speaker, verified English (unmasked), Japanese draft, context, uncertainty, s, e).
def E(nums, spk, en, ja, ctx='', unc='', s=None, e=None):
    return dict(nums=nums, spk=spk, en=en, ja=ja, ctx=ctx, unc=unc, s=s, e=e)

CLIPS = {}

CLIPS['S01'] = [
 E([1, 2], 'Host', "I want to start because, you know, the very famous interview was you and Sway, right?", "まず聞きたいのは\nあの有名なSwayとの\nインタビューのことなんだけど", "Ye's 2013 Sway in the Morning interview ('You ain't got the answers, Sway!')."),
 E([3, 4], 'Host', "And then you saying that you wanted to be like Ralph, or you wanted to be up there with that caliber.", "あんたはRalphみたいになりたい\nあのレベルに行きたいって\n言ってたよな", "Ralph = Ralph Lauren.", "Large-v3 'want', turbo 'wanted'; same meaning."),
 E([5, 6], 'Host', "And now it's like you are Ralph. You are that caliber.", "で、今じゃあんたが\nRalphそのもの\nあのレベルにいる"),
 E([7, 8], 'Host', "And then I guess what I'm trying to say is, so that's where we get confused.", "だから何が言いたいかっていうと\nそこで俺らは\n混乱するわけよ"),
 E([9], 'Host', "Did Sway have the answers?", "Swayは答えを\n持ってたのか？", "Callback to Ye's famous line 'You ain't got the answers, Sway!'"),
 E([10], 'Host', "I think you already admitted Sway had the answers.", "Swayが正しかったって\nもう認めてたよな", "", "MEDIUM: large-v3 'admitted Sway had the answers', turbo 'admitted the way he had the answer'. Large-v3 fits the context; speaker inferred as a host."),
 E([11, 12, 13, 14], 'Host', "But I guess that's where we get confused with the Adidas part of it, because that's how you became a billionaire, right? Through the Yeezy.", "でもAdidasの件で\n混乱するんだよ\nあんたが億万長者になれたのは\nYeezyのおかげだろ？", "", "Large-v3 adds a false start ('like didn't like'); turbo reads 'Through the Yeezy' where large-v3 has 'the easy'.", e='through the easy'),
 E([15], 'Host', "So, like, what was the discrepancy with Adidas?", "じゃあAdidasとは\n何が食い違ったんだ？"),
 E([16, 17], 'Ye', "You know, I just didn't have the relationships with the factories at that time.", "当時の俺には\n工場とのつながりが\nなかったんだよ"),
 E([18, 19], 'Ye', "And I was managing a lot of ideas, like I was, you know, a new dad.", "アイデアもいっぱい抱えてて\n父親になったばかりで"),
 E([20], 'Ye', "I was newly married.", "結婚したばかりで"),
 E([21, 22], 'Ye', "I had a bunch of team, like a big team of designers with me.", "デザイナーの大きなチームも\n抱えてた"),
 E([23, 24], 'Ye', "And we hadn't established who we were. We were still fighting to get our respect in fashion.", "まだ自分たちが何者か\n確立できてなくて\nファッション界で認められようと\nもがいてた"),
 E([25], 'Ye', "So there's a lot of fights at the same time.", "だから同時に\nいろんな戦いがあった"),
 E([26, 27], 'Ye', "So we had to go and basically, like, intern almost up under these companies.", "だから要は\nそういう企業の下で\nインターンするしかなかった"),
 E([28], 'Host', "Because you interned for Louis Vuitton at one time, right?", "Louis Vuittonで\nインターンしてたもんな？", "", "Turbo 'at once'; large-v3 'at one time, right?'."),
 E([29], 'Ye', "Yeah, Louis Vuitton, Fendi.", "そう、Louis Vuitton、Fendi"),
 E([30], 'Ye', "And we interned, in a way, at Adidas.", "で、Adidasでも\nある意味インターンしてた"),
 E([31, 32], 'Ye', "Like, the licensing deal was my internship to become, you know, more in that Bernard Arnault, Bezos, Elon territory,", "あのライセンス契約は\nBernard Arnaultとかベゾスとかイーロンの\n領域に行くための\n俺のインターンだったんだよ", "Bernard Arnault = LVMH chairman. Bezos/Elon in katakana per the series naming rule.", "Both passes say 'my intern'; rendered as 'my internship' in meaning."),
 E([33, 34], 'Ye', "and just understanding how, you know, how money works. Like, this is first generation.", "金がどう回るのかを\n理解するためのな\nこれは第一世代なんだよ", s='and just understanding', e='this is first generation'),
 E([35, 36], 'Ye', "Like, you can say, like, look at, like, Jay with the D'Usse. This is first generation of wealth, those infrastructures, right?", "たとえばJayとD'Usseを見ろよ\nこれは富の第一世代なんだ\nそういうインフラのな", "Jay-Z co-owned the cognac brand D'Usse (spelled D'Usse in this series).", "Large-v3 'do say' = D'Usse."),
]

CLIPS['S02'] = [
 E([1], 'Ye', "You know, they done fuck with me too long.", "あいつら\n長いこと俺を\nナメすぎたんだよ"),
 E([2, 3], 'Ye', "Every time they say my name wrong, it's like they calling me Cassius. My name Ali.", "名前を間違えて呼ばれるたびに\nCassiusって呼ばれてる気分\n俺の名前はAliだ", "Muhammad Ali, born Cassius Clay, rejected his birth name; Ye legally changed his name from Kanye West to Ye."),
 E([4, 5], 'Ye', "If I change my name, you respect that I changed my name. It shows you the level of disrespect.", "名前を変えたなら\nそれを尊重しろよ\nどれだけナメてるかって話だ"),
 E([6], 'Ye', "Every time they say one of my outfits are bizarre,", "俺の服を毎回\n「奇抜」って書くくせに"),
 E([7, 8], 'Ye', "when the last time you read a headline and they called me a billionaire?", "見出しで俺を\n「億万長者」って書いてたのを\n最後に見たのはいつだ？"),
 E([9, 10], 'Ye', "For three years, Forbes wouldn't say I was a billionaire. It's all to diminish me, so y'all wouldn't listen to me.", "3年間Forbesは\n俺を億万長者と認めなかった\n全部俺を小さく見せて\nお前らが耳を貸さないようにするためだ"),
 E([11], 'Ye', "So, say, when I did the Ye and Drake show, right?", "で、俺とDrakeの\nライブをやった時な", "The December 2021 Free Larry Hoover benefit concert."),
 E([12, 13], 'Ye', "It's so funny, I look up and it say Ye, D-R-K, right there.", "笑えるんだけど\n見上げたら\n「Ye、D-R-K」って書いてあって", "Ye reads the marquee 'YE + DRAKE' as 'Ye DRK'.", "MEDIUM: large-v3 'say yay drk', turbo 'it say Yay, D-R-K'. The exact sign wording is unclear."),
 E([13, 14], 'Ye', "But, uh, I just... it's just a similarity to it.", "なんか…\n似てるってだけなんだけど", "", "Turbo also hears a host line here ('Oh, that's how you see it'); not clear in large-v3.", s='but uh i just', e='similarity to it'),
 E([14], 'Host', "Are you dyslexic like me?", "俺みたいに\n失読症なのか？", "", "MEDIUM: only turbo has this host question; large-v3 hears 'like me i'm not'. Review the audio around 1137.5 s.", s='like me', e='im not'),
 E([14, 15], 'Ye', "Yeah, absolutely. Gemini, dyslexic, left-handed, made to be right-handed so I could fit in.", "ああ、もちろん\n双子座で失読症\n左利きなのに\n周りに合わせて右利きにされた", s='yeah absolutely'),
 E([16], 'Ye', "Think about, like, Nike.", "Nikeを考えてみろよ"),
 E([17, 18], 'Ye', "Nike is as popular as Apple, but it's company number 321. Apple's number one.", "NikeはAppleと同じくらい人気なのに\n企業ランキングは321位\nAppleは1位だ", "", "Ye's figure ('number 321') is his own claim, kept as spoken."),
 E([19, 20], 'Ye', "Nike's on defense. It's not on offense.", "Nikeは守りの会社なんだよ\n攻めじゃない"),
 E([21], 'Ye', "Right? Because niggas love Nike.", "だろ？\nみんなNikeが大好きだからな", "In-group 'niggas' = people/Black people here; masked in displayed English."),
 E([22, 23, 24], 'Ye', "Right? So Nike is used for political influence, because it's not about the money you make. It's about the position you have.", "だからNikeは\n政治的な影響力に使われる\n稼ぐ金じゃなくて\nどんな立場にいるかが大事なんだ"),
 E([25, 26], 'Ye', "So when they signed me to Gap, it wasn't to raise a stock price.", "だからGapが俺と契約したのも\n株価を上げるためじゃない"),
 E([27, 28, 29], 'Ye', "It was to be able to, like, tell the Fortune 500 companies that do deals with China, to tell them, hey, Gap has influence in the underserved communities.", "中国と取引してる\nFortune 500の企業に\n「Gapは低所得層の地域に\n影響力がある」って\n示すためだった"),
 E([30], 'Ye', "That was what the deal was about.", "あの契約は\nそういうことだったんだよ"),
]

CLIPS['S03'] = [
 E([1], 'Host', "Okay, let me talk about Balenciaga.", "よし、Balenciagaの話をさせてくれ", "Follows Ye singing his lyric 'Balenciaga for all your friends'."),
 E([2, 3], 'Host', "Since you did the last interview, I've been Balenciaga, y'all. You know my nickname is Yalla.", "前回のインタビュー以来\n俺はずっとBalenciagaなんだよ\n俺のあだ名はYallaだろ", "Host (N.O.R.E.) is wearing Balenciaga.", "MEDIUM: nickname heard as 'Yala' (large-v3) / 'yalla' (turbo); spelling uncertain.", s='ive been since'),
 E([4], 'Host', "So now they call me Balenci-Yalla.", "だから今じゃ\nBalenci-Yallaって呼ばれてる"),
 E([5, 6], 'Ye', "Balenciaga has the best design because they have the best designer, period.", "Balenciagaのデザインが最高なのは\n最高のデザイナーがいるからだ\nそれだけ", "The designer = Demna, Balenciaga's creative director at the time.", e='period'),
 E([6], 'Host', "And that's not you?", "それはあんたじゃないの？", s='and thats not you'),
 E([7], 'Ye', "I'm more like a Steve Jobs type.", "俺はどっちかっていうと\nスティーブ・ジョブズタイプ"),
 E([8, 9], 'Ye', "You know, you say to Steve, like, yo, you don't even program.", "スティーブに「お前プログラム\n書かないじゃん」って言うようなもんだ", e='program'),
 E([9, 10, 11], 'Ye', "You know, I would never disrespect a designer that been to school and that can cut and have dedicated their whole life, and call myself a designer.", "学校に通って\n型紙も切れて\n人生を捧げてきたデザイナーを差し置いて\n自分をデザイナーだなんて\n絶対に名乗らない", s='you know i would never'),
 E([12], 'Ye', "I'm more an imagineer.", "俺はむしろ\n「イマジニア」なんだよ", "'Imagineer' = imagine + engineer (Disney's term)."),
 E([13, 14], 'Ye', "I'm a visionary, and I place the pieces of our culture together.", "ビジョンを描いて\n俺たちのカルチャーの\nピースを組み合わせる", e='together'),
 E([14, 15], 'Ye', "Even right now, you know, I want to bring joy and laughter.", "今だってさ\n喜びと笑いを届けたいんだよ", s='even right now', e='and laughter'),
 E([15, 16, 17], 'Ye', "So even if, say, say, say, we wanted to, like, look at the interview and we have a conversation after and say, look, do we need this first segment?", "たとえばこのインタビューを見返して\n「最初のパートって\n要る？」って\n話し合ったとしても", s='so even if', unc="Large-v3 'conversation out'; heard as 'after' in meaning (a later review of the footage)."),
 E([18, 19], 'Ye', "Let's just do the shit that's like, you know, it's controversial, because people ain't going to really name names.", "物議を醸すやつは\nそのままでいい\nだってみんな\nはっきり名前は出さないから", "", "MEDIUM: large-v3 'people are going to really name names', turbo 'people ain't gonna really name names'; the meaning flips. Review the audio around 1549.5 s."),
 E([20, 21], 'Ye', "But it's funny still. I think about that.", "でもやっぱり笑えるんだよ\nそう思う"),
 E([22, 23], 'Ye', "It's like, we need joy. It's too much pain.", "俺たちには喜びが必要だ\n痛みが多すぎる"),
 E([24, 25], 'Ye', "You know, it's too much anger, and it's too much trauma economy.", "怒りも多すぎるし\n「トラウマ経済」が\nデカすぎる", "'Trauma economy' = Ye's phrase for media/politics profiting from Black trauma."),
]

CLIPS['S04'] = [
 E([1, 2], 'Ye', "I want to change something I said. I am the leader. Now let me change that. I am a leader,", "さっき言ったことを訂正したい\n「俺が“その”リーダーだ」って言ったけど\n言い直す\n俺は“一人の”リーダーだ"),
 E([2, 3], 'Ye', "and there's a new leader being born every day,", "そして毎日\n新しいリーダーが生まれてる", s='and theres a new', e='born every day'),
 E([3, 4], 'Ye', "and there's leaders locally that will hear this, that can play this.", "地元にもリーダーがいて\nこれを聞いて\n流してくれる", s='and theres leaders', e='can play this'),
 E([4, 5, 6], 'Ye', "Leaders of their school, leaders of their boys club, leaders of their church, leaders of their crew, leaders of their crew,", "学校のリーダー\nボーイズクラブのリーダー\n教会のリーダー\n仲間内のリーダー", "", "Large-v3 'churches', turbo 'church'.", s='leaders of their school', e='leaders of their crew'),
 E([6, 7, 8], 'Ye', "and that's another word for crew: leaders of their gang.", "仲間っていうのは\n言い換えれば\nギャングのリーダーだ", s='and thats another'),
 E([8, 9], 'Ye', "You see what I'm saying? Gang has, like, a negative connotation, but by removing the gang leaders...", "わかるか？\nギャングって言葉は\n悪いイメージがあるけど\nギャングのリーダーを排除すると…", s='you see', e='the gang leaders'),
 E([9, 10], 'Host', "Gangs originated in Chicago.", "ギャングの発祥は\nChicagoだよな", "", "MEDIUM: turbo hears the host say 'Gangs is originated in Chicago'; large-v3 merges it into Ye's line ('originally in chicago'). Speaker inferred.", s='originally', e='chicago'),
 E([10, 11], 'Ye', "Yeah, exactly. By removing the gang leaders, you're removing the leaders.", "そう、その通り\nギャングのリーダーを排除すれば\nリーダーそのものを\n排除することになる", s='yeah', e='the leaders'),
 E([11, 12], 'Ye', "And that was something, and that fucked up the world, right? Because those gang leaders would organize.", "それが世界を\nめちゃくちゃにしたんだよ\nギャングのリーダーは\n人をまとめてたからな", s='and that was something', e='would organize'),
 E([12, 13], 'Ye', "Right there, you know what I'm saying? Gangster Disciples saved my life in Chicago.", "そういうこと\nChicagoでは\nGangster Disciplesが\n俺の命を救ってくれた", "Gangster Disciples = Chicago street organization co-founded by Larry Hoover.", s='right there'),
 E([13, 14], 'Ye', "I'm here because of Gangster Disciples.", "俺がここにいるのは\nGangster Disciplesのおかげだ", s='i', e='gangster disciples'),
 E([15, 16], 'Ye', "And I am exactly who Larry Hoover wanted to see come out of the organization that he created.", "俺はまさに\nLarry Hooverが\n自分の作った組織から\n出てきてほしかった人間なんだよ", "Larry Hoover = imprisoned co-founder of the Gangster Disciples; Ye and Drake held a 2021 benefit concert for his release."),
 E([17], 'Ye', "Took out leaders, took out structure.", "リーダーを消して\n組織を壊したんだ"),
 E([18], 'Ye', "Nothing fucks with a Drink Champs interview, right?", "Drink Champsのインタビューに\n勝るもんはないよな"),
 E([19], 'Host', "No, no, no.", "いやいや", "", "Turbo hears only 'right' here; short interjection, speaker inferred."),
 E([20, 21], 'Ye', "Because, you know, when I go to Tucker Carlson, they're just like... it's not the same.", "Tucker Carlsonに出ても\nなんか…\nやっぱ違うんだよ", "Ye was interviewed on Tucker Carlson's Fox News show in October 2022.", "Turbo 'they're just like so same'; large-v3 'It's not the same.'", s='because you know'),
 E([22, 23, 24, 25], 'Ye', "They're just so marveled by the fact of the brilliance. They're not respecting the brilliance. They're more like shocked and, like, marveled by it. It's like hilarious to them. It's like, that squirrel can jet-ski!", "あっちは俺の才能に\nただ驚いてるだけで\nリスペクトはしてない\nショック受けて\n面白がってるだけ\n「このリス、水上スキーできるぞ！」\nみたいな感じ", "'Squirrel can jet-ski' = Ye's image of being treated as a novelty act."),
]
