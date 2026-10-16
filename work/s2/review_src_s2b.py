# Series 2 review line sources, batch B (S05-S09).
from review_src_s2a import E
CLIPS = {}

CLIPS['S05'] = [
 E([1], 'Host', "Can we address this hat? What does the 2024 mean?", "この帽子の話をしようか\n「2024」って\nどういう意味？", "Ye is wearing a cap reading '2024', his announced presidential run.", e='2024 mean'),
 E([1, 2, 3], 'Ye', "2024... the run.", "2024は…\n出馬だよ", s='2024', e='run'),
 E([3, 4, 5, 6], 'Ye', "It's time for us to rise up. It's time for us to put somebody in office that is us, that cares about us,", "俺たちが立ち上がる時だ\n俺たちの側の人間を\n俺たちを気にかける人間を\n政権に就ける時だ", s='its', e='cares about us'),
 E([6, 7], 'Ye', "that serves God and serves the people. That's what 2024 means.", "神に仕え\n人々に仕える人間をな\nそれが2024の意味だ", "", "Large-v3 repeats 'Twenty four means twenty'; turbo 'That's what 2024 means'.", s='that serves', e='2024'),
 E([8], 'Host', "So you can't say this right now.", "じゃあ今は\nまだ言えないってことか", "", "Large-v3 'you can't', turbo 'we can't'. Speaker inferred as a host.", s='so so you'),
 E([9, 10], 'Host', "So that... Ye might be against... But what if Trump runs?", "ってことは…\nYeが対抗するのは…\nでもTrumpが出たら？", "", "MEDIUM: the host's first half is fragmentary in both passes ('So that that that the yay might be against').", s='so that'),
 E([11, 12], 'Ye', "No, that's... He might. Yeah.", "いや、それは…\n出るかもな", "", "MEDIUM: large-v3 'No, that's all in 24. He might. Yeah'; turbo 'No, that's, oh, he might, yeah.' Kept to the shared words.", e='yeah'),
 E([12, 13], 'Ye', "I think that's what America's been waiting for.", "Americaはそれを\n待ってたんだと思うよ", s='i', e='waiting for'),
 E([14], 'Host', "You against Trump?", "Trumpと対決？"),
 E([15], 'Host', "Yeah. Who you voting for?", "そう\nあんたは誰に投票する？", "", "Speaker split inferred: the 'Yeah' may be Ye's answer.", s='yeah'),
 E([16], 'Ye', "That's a good one.", "いい質問だな"),
 E([17, 18, 19], 'Ye', "I'm not even going to lie, man. I'm a fan of a lot of people, but, you know, respectfully, I don't like nobody better than me.", "ウソはつかないよ\nファンな人はたくさんいる\nでも悪いけど\n俺より好きな奴はいない"),
 E([20, 21], 'Host', "Right. If he asked you to be VP, would you?", "なるほど\nもしTrumpに副大統領を頼まれたら\nやる？", "VP = vice president.", s='right'),
 E([22, 23, 24], 'Ye', "Yeah. Absolutely. If that was a piece that's like me, let's say, Watch the Throne then.", "ああ、もちろん\nそれは俺にとって\n『Watch the Throne』みたいなもんだ", "Watch the Throne = Ye and Jay-Z's 2011 joint album, where Ye was the junior partner in Jay-Z's eyes.", "MEDIUM: 'If that was a piece that's like me' is unclear in both passes; the gist is the Watch the Throne comparison."),
 E([25, 26], 'Host', "Well, you thought he was the VP on Watch the Throne? I thought you was equals, co-president.", "『Watch the Throne』では\nJayが副大統領だったって？\n対等な共同大統領だと思ってたわ", "", "MEDIUM: large-v3 'he was the VP ... I thought that was his co-president'; turbo 'I thought I was equals co-president'. Merged reading."),
 E([27, 28, 29], 'Ye', "But still, that's my elder. That's my senior. That's the person with more experience. I love the respect.", "でもやっぱり\nあの人は俺の先輩\n経験も上だ\nその敬意が大事なんだよ", "Ye means Jay-Z.", "Large-v3 'that's the first one more experience'; turbo 'a person with more experience'."),
]

CLIPS['S06'] = [
 E([1], 'Host', "No, man, come on.", "おいおい、待てよ", "", "Speaker inferred."),
 E([2, 3], 'Ye', "What was the question? You had a good question I want to answer, though.", "質問なんだっけ？\nいい質問だったから\n答えたいんだよ"),
 E([4, 5, 6], 'Host', "No, we were just talking about that moment when you showed the porn to the executives, and now we're talking about your sneaker.", "いや、さっきまで\n重役にポルノを見せた話をしてて\n今はあんたのスニーカーの話", "Refers to Ye's account (told later in the episode) of playing an adult video in an Adidas meeting."),
 E([7, 8], 'Ye', "Yeah. At Adidas, at this point, I should be the person that says, Nori, get a sneaker.", "そう\n今のAdidasなら\n「Nori、お前のスニーカー作れ」って\n俺が言える立場のはずなんだ", "Nori = N.O.R.E., the host."),
 E([9], 'Ye', "That's right. I should be the person that delegates.", "そう\n俺が采配を振るう\n立場のはずなんだよ"),
 E([10], 'Ye', "But instead, they gave it to Stella McCartney's husband.", "なのにその役は\nStella McCartneyの旦那に\n回された", "Stella McCartney's husband = Alasdhair Willis, Adidas creative director at the time."),
 E([11, 12, 13], 'Ye', "And I'm not going to speak no ill on Stella McCartney's husband, because I'm cool with her, uh, with his father-in-law. You know, that's my man, you know what I'm saying?", "Stella McCartneyの旦那を\n悪く言うつもりはないよ\nあいつの義父とは仲がいいからな\n俺の仲間なんだよ", "Father-in-law = Paul McCartney."),
 E([14, 15, 16], 'Ye', "That man stood next to me. We went into the studio. We did all day.", "あの人は俺の隣に立ってくれた\n一緒にスタジオに入って\n一日中やったんだ"),
 E([17, 18], 'Ye', "We did 'Only One.' We did 'FourFiveSeconds.'", "『Only One』も\n『FourFiveSeconds』も\n一緒に作った", "Two 2014-15 songs Ye made with Paul McCartney.", "Large-v3 'We did only one. We did four or five seconds.' = the song titles."),
 E([19, 20], 'Ye', "Like, me and Paul McCartney got joints. You know what I'm saying?", "俺とPaul McCartneyは\n曲を一緒にやってるんだよ\nわかるだろ？"),
 E([21, 22, 23], 'Ye', "So that's the reason why, Adidas, you really found you a Virgil in Stella McCartney's husband, and a person that I'm going to give a hug no matter what.", "だからAdidasは\nStella McCartneyの旦那に\n自分たちのVirgilを見つけたわけだ\n俺が何があってもハグする相手をな", "Virgil Abloh, Ye's longtime collaborator who became Louis Vuitton's menswear director; Ye frames these hires as companies finding their own insider.", "Large-v3 'Virgil and Stella McCartney's husband'; 'in' fits the meaning better. Interpretation, not a hearing problem."),
 E([24, 25, 26], 'Ye', "So because that's the way it is. It's like, even at war, even in John Wick, even with Neo, it's ones that they just have to pass on.", "そういうもんなんだよ\n戦争でも\nJohn WickでもNeoでも\n見逃さなきゃいけない相手がいる", "John Wick / Neo (The Matrix) = Keanu Reeves characters.", e='have to pass on'),
 E([26, 27, 28], 'Ye', "So it's just like Stella McCartney's husband. Because he's Stella McCartney's husband, part of the reason why he became Stella McCartney's husband,", "Stella McCartneyの旦那もそう\nStella McCartneyの旦那だから\nそれもあの人と結婚した\n理由の一つなんだろうけど", s='so', e='became stella mccartneys husband'),
 E([28, 29], 'Ye', "he get a pass from Ye. And you get a pass from Ye.", "Yeからは見逃してもらえる\nお前も見逃してもらえる", s='hed get', e='you get a pass from yay'),
 E([30], 'Ye', "You get a pass from the culture, right?", "カルチャーから\n見逃してもらえるんだよ"),
]

CLIPS['S07'] = [
 E([1, 2], 'Ye', "Because why not we just do it ourself and not be mad at nobody? Jewish, nobody Chinese, nobody black, nobody,", "だって俺たちで\nやればいいだけだろ\n誰にも腹を立てずに\nユダヤ人にも中国人にも\n黒人にも", "", "MEDIUM: turbo hears 'nobody Jewish, nobody Chinese'; large-v3 has 'but i think' in place of 'Jewish'. Review the audio around 662 s.", e='nobody black nobody'),
 E([3], 'Ye', "anywhere. We got to get like the Chinese world.", "どこの誰にもな\n中国みたいに\nならなきゃいけない", s='anywhere', e='chinese world'),
 E([3, 4, 5], 'Ye', "We got it on point. We got to get our own factories.", "あそこはしっかりしてる\n自分たちの工場を\n持たなきゃダメだ", "", "Large-v3 repeats 'we gotta get like a point'.", s='we got', e='own factories'),
 E([5, 6, 7], 'Ye', "We got to put it together, whether it's like, you know what I'm saying, like, look at, like, Warren Buffett's factory or something.", "形にしなきゃいけない\nたとえばWarren Buffettの\n工場みたいにさ", s='you gotta put', e='or something'),
 E([7, 8], 'Ye', "It's got to, like, when you walk in, you got to feel. That's the reason why.", "入った瞬間に\n感じるものがないとダメなんだ\nそれが理由だよ", s='its kind of', e='the reason why'),
 E([8, 9, 10], 'Ye', "One of the things is, like, when me and Puffy was, like, going back and forth on Instagram or text,", "たとえばさ\n俺とPuff DaddyがInstagramや\nメールでやり合ってた時", "Puffy = Puff Daddy (Diddy).", s='one of the things', e='or text'),
 E([10, 11, 12], 'Ye', "I went and changed my... I was on the car service. I'm like, I want to just do Maybach fleets for the whole... for everybody.", "俺はハイヤーを\n変えたんだよ\n全員分Maybachの車隊に\nしたくてさ", "", "Large-v3 'i wouldn't change my', turbo 'I went and changed my'.", s='i wouldnt change'),
 E([12, 13, 14], 'Ye', "You know what I'm saying? I'm getting my, like, my people in a higher, you know, position and stuff like that.", "わかるだろ？\n仲間をもっと上の\n立場にしたいんだよ", s='im saying', e='stuff like that'),
 E([14, 15, 16], 'Ye', "I got two Maybachs type shit. I got like four, you know what I'm saying? Our fleet done to pull up.", "Maybachを2台とか\n4台とか持ってて\nうちの車隊で\n乗りつけるんだよ", "", "MEDIUM: 'I got like four, you're saying, our fleet don to pull up' (large-v3) / 'four years and our fleet down to pull up' (turbo). Gist kept.", s='i got two', e='to pull up'),
 E([16, 17, 18], 'Ye', "This is back to back to back to back to back, back, back, back... Ye-bachs and shit,", "後ろにずらっと\n何台も何台も…\n“Ye-bach”だよ", "", "MEDIUM: large-v3 'right yay backs and shit' (a Ye/Maybach pun, 'Ye-bachs'?); turbo only repeats 'back'. Review the audio around 709-711 s.", s='this is back'),
 E([18, 19], 'Ye', "until we make our own cars. You know, until we make our own cars.", "自分たちの車を作るまでは\n自分たちの車を作るまではな", "", "Large-v3 'cards' = cars.", s='until we make', e='you know until we make our own cards'),
 E([19, 20, 21], 'Ye', "But it's like, we're not really maximizing who we are.", "でもまだ俺たちは\n自分たちの力を\n出し切れてない", s='but its like', e='who we are'),
 E([21, 22, 23], 'Ye', "We're not limited to the master. We get with a legal BMF, you know, we have to think, like, in that manner.", "主人に縛られる必要はない\n合法版のBMFみたいに\nそういう考え方を\nしなきゃいけない", "BMF = Black Mafia Family, the Detroit drug and hip-hop organization (subject of the TV series 'BMF'); 'legal BMF' = the same organizing power, legitimately.", "Large-v3 'we're the legal bmf', turbo 'get with a legal BMF'.", s='were not limited'),
]

CLIPS['S08'] = [
 E([1, 2, 3], 'Ye', "Think about, like, True Love. Like, my kids... we listen to True Love at Kim's house, which used to be my house,", "『True Love』で考えてみろよ\nKimの家で\n子どもたちと聴くんだ\n元は俺の家だけどな", "'True Love' = 2022 song by Ye and XXXTentacion. Kim = Kim Kardashian, Ye's ex-wife.", e='be my house'),
 E([3, 4], 'Ye', "but we listened to True Love in front of the kids,", "子どもの前で\n『True Love』を聴いてたら", s='but uh we', e='of the kids'),
 E([4, 5], 'Ye', "and Chicago be like, you said Chicago, you said Chicago!", "Chicagoが\n「Chicagoって言った！\nChicagoって言った！」って", "Chicago = Ye's daughter, named in the song.", s='and chicago', e='said chicago you said chicago'),
 E([5, 6, 7, 8], 'Ye', "So I was big on, on Donda, that even though I was beefing with my baby mama, that I wouldn't say anything that I couldn't play in front of the kids.", "『Donda』では\n元妻と揉めてても\n子どもの前で流せないことは\n言わないって決めてた", "Donda = Ye's 2021 album.", "Large-v3 repeats 'baby mama i'm my baby mama'.", s='so i was big'),
 E([8, 9], 'Ye', "That's the consciousness that I had to have as a leader in all of my content.", "それがリーダーとして\nあらゆる作品で\n持たなきゃいけない\n意識なんだよ", s='that thats'),
 E([9, 10, 11], 'Ye', "So even right now, I say, okay, it's adult content, right? This is a grown, grown conversation. It's a grown conversation", "だから今だって\n「これは大人のコンテンツだ」\nって言ってる\n大人の、大人の話なんだよ", s='so even right'),
 E([11, 12, 13], 'Ye', "that I ran into at age five, but it's still a grown-up conversation to me, right?", "5歳の時に\n出くわした話だけど\n俺にとってはやっぱり\n大人の話なんだ", "Ye has said he first saw pornography at age five.", "Large-v3 'and i ran into at age five'.", s='and i ran'),
 E([13, 14], 'Ye', "So I played this for grown-ups in the Adidas meeting.", "だから大人向けに\nAdidasの会議で流したんだよ", s='so i played', e='meeting'),
 E([14, 15, 16], 'Ye', "I said, look, we have to do this, because culture... it ain't no culture if you have a party and it ain't no girls there.", "俺は言った\n「これは必要なんだ\nパーティーに女の子がいなかったら\nそれはカルチャーじゃない」", s='i said look'),
 E([16, 17], 'Host', "That's not cultural. Yeah, that ain't.", "カルチャーじゃないな\nそうだよ", "", "Speaker inferred; may be Ye continuing.", s='thats not cultural', e='they aint'),
 E([17, 18, 19], 'Ye', "Right. And this is the reason why Drake runs the culture, right? Because at the end of the day, he's at the time...", "そう\nだからDrakeが\nカルチャーを仕切ってるんだよ\n結局のところ、あいつは…", "", "Large-v3 'he's at the time' is unclear; left as an unfinished thought.", s='right and'),
 E([19, 20, 21], 'Ye', "It don't matter, it don't matter if I could take over Fashion Week for, you know, two weeks or whatever.", "俺がファッションウィークを\n2週間乗っ取ろうが\n関係ない", s='it dont matter', e='or whatever'),
 E([21, 22], 'Ye', "It's like, Drake runs the culture at the end of the day,", "結局カルチャーを\n仕切ってるのはDrakeなんだ", s='its like drake'),
 E([22, 23, 24], 'Ye', "because the culture, at the end of the day, is about finding a nice young Libra that you could connect with on her birthday, possibly.", "だってカルチャーってのは\n誕生日の天秤座の\n若い子と仲良くなれるかって\nことだからな", "Joke aimed at a woman in the studio celebrating her birthday (a Libra, mentioned earlier in the show).", s='because the culture'),
]

CLIPS['S09'] = [
 E([1, 2, 3], 'Host', "This is the thing. You could say all this stuff. You could say Tuskegee and people don't even know what that is.", "ここが大事なんだけど\nいろいろ言うのはいい\nでも「Tuskegee」って言っても\nみんな知らないんだよ", "Tuskegee syphilis study (1932-72): the US Public Health Service withheld treatment from Black men. Ye had just compared his family situation to it.", e='what that is'),
 E([3, 4, 5], 'Ye', "Right. Hold on. Hold on.", "そうだな\n待て待て", "", "MEDIUM: overlapping voices; the split of 'Right / Hold on / No, I know / Hold up' between Ye and the host is inferred.", s='right', e='hold on hold on'),
 E([4, 5], 'Host', "No, I know. Hold up.", "いや、わかってる\n待って", s='no i know', e='hold up'),
 E([5, 6], 'Host', "And they just think you're throwing things out there, and they're like, yeah, he's just saying things.", "みんな「適当に言ってる」\n「口から出まかせだ」って\n思っちゃうんだよ", s='and they just'),
 E([7, 8], 'Host', "But if people do the research, if you can articulate what Tuskegee... what really happened, which is legit, it really happened,", "でもみんなが調べたら\nTuskegeeで\n実際に何があったか説明できたら\nあれは本当にあったことだから", "", "Large-v3 'articulate what Tuskegee what really happened'; turbo 'what Tuskegee happened'."),
 E([9, 10], 'Host', "it's not a conspiracy theory. The government did this to people.", "陰謀論じゃない\n政府が実際に\nやったことなんだ"),
 E([11, 12, 13], 'Host', "Then you can get people on the side of what you're saying. It all becomes about articulation and history, because history is real.", "そうすれば\nみんな味方してくれる\n大事なのは伝え方と歴史\n歴史は事実だからな"),
 E([14, 15], 'Host', "And that's what I think. Sometimes I think we as Americans, we have no history anymore.", "俺はそう思う\nアメリカ人には\nもう歴史がないんじゃないかって"),
 E([16, 17], 'Host', "We're not learning history, real history. Teaching history, it's all done, it's gone.", "歴史を学んでない\n本当の歴史をな\n歴史の授業なんて\nもう消えちまった", e='its gone'),
 E([17, 18, 19], 'Host', "And we need to bring that back, and bring it back in the right way, where people articulate what really happened.", "それを取り戻さなきゃ\n正しいやり方でな\n何が本当にあったか\nちゃんと伝えられるように", s='and', e='really happens'),
 E([19, 20, 21, 22, 23], 'Ye', "What you guys are doing, what's different right here, because as you're talking, I felt, I was like, wow, there wouldn't have been no way for me to become president without coming to Drink Champs.", "お前らがやってることは\nここが違うんだよ\n話を聞いてて思った\n「Drink Champsに来なかったら\n大統領にはなれなかった」って", s='what you guys'),
 E([23], 'Ye', "When you were talking right now, like...", "今の話を聞いてて…", s='when you were'),
 E([24, 25], 'Ye', "you know, what you... the way you articulated it, because it's very important that we stay in constant communication.", "その伝え方だよ\n俺たちがずっと\n話し合い続けることが\nすごく大事なんだ", "", "Large-v3 'you know who you're saying what you the way you articulated it'; false starts dropped."),
 E([26, 27, 28, 29], 'Ye', "That's what the enemy wants us to do. They don't want us to talk. Like the slave ships, right? They cut our tongues and told us not to talk to each other.", "敵の狙いはそこなんだ\n俺たちに話させたくない\n奴隷船と同じだよ\n舌を切って\n互いに話すなって言った", "Ye means the enemy wants the opposite: to stop Black people talking. Slave-ship image as Ye states it.", "Large-v3 'I told us that to talk'; turbo 'and told us not to talk to each other'."),
]
