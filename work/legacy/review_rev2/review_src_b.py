from review_src_a import E
CLIPS = {}

CLIPS['C05'] = [
 E([1, 2], 'Host / Ye', "Kool G Rap or Big Pun? — (Ye:) I like both.", "Kool G Rapか\nBig Punか\n（Ye）どっちも好き", "Pick-one game. Kool G Rap and Big Pun are New York rap legends.", "Large-v3 'I like both'; turbo 'I like boof'. 'Both' fits the next answer."),
 E([3], 'Host', "Take a shot.", "じゃあ一杯飲め", "Game rule: refusing to pick means taking a shot."),
 E([4, 5], 'Ye', "So, you know, God said for us to not compare each other amongst ourselves.", "神は\n互いを比べるなって\n言ってるだろ"),
 E([6, 7], 'Ye', "So when I compare the greatness of Kool G Rap and the greatness of Big Pun,", "だからKool G Rapの偉大さと\nBig Punの偉大さを比べるのは"),
 E([8], 'Ye', "which was inspired by Kool G Rap,", "しかもBig PunはKool G Rapに\n影響受けてるわけで"),
 E([9], 'Host', "Yeah.", "確かに"),
 E([10, 11], 'Ye', "it's not godly. You know what I'm saying?", "神の道に反するんだよ\nわかる？"),
 E([12], 'Ye', "I know Ross said God forgives, I don't.", "Rick Rossは\n「神は許すが俺は許さない」って\n言ってたけど", "Rick Ross album title 'God Forgives, I Don't' (2012)."),
 E([13], 'Ye', "I'm forgiving. I forgive everybody. I forgive the Clintons. I forgive", "俺は許す\n全員許す\nClinton夫妻も許す", "", "Turbo 'I'm forgiven'; large-v3 'I'm forgiving'."),
 E([14, 15], 'Ye', "John Legend for wearing them bum-ass sweaters. I forgive... I forgive him. He's forgiven.", "John Legendも許す\nあのダサいセーター着てたことをな\n許す…許してやる\nあいつは許された", "John Legend = singer, formerly close to Ye; they fell out over politics."),
 E([16], 'Ye', "Big Sean. May they all be forgiven. I forgive Big Sean", "Big Sean\nみんな許されますように\nBig Seanも許す", "Big Sean = rapper signed to Ye's G.O.O.D. Music."),
 E([17, 18], 'Ye', "for not being able to make the choice between braids or a beard. Choose one.", "編み込みか髭か\n決められなかったことをな\nどっちか選べよ", "Joke about Big Sean's look (braids together with a beard)."),
 E([19], 'Ye', "Um, I forgive, uh...", "あと許すのは…"),
 E([20], 'Host', "Who else is you again?", "他には誰？", "", "LOW: large-v3 'Who loves you again?'; turbo 'Who else is you again?'. Read as a host asking 'who else?'."),
 E([21], 'Host', "That's it?", "それで終わり？"),
 E([22], 'Ye', "Everybody. Everybody I ever... you know what I'm saying?", "全員だよ\n今までの全員\nわかるだろ"),
 E([23], 'Ye', "I forgive everyone.", "みんな許す"),
 E([24], 'Ye', "I forgive Bob Iger.", "Bob Igerも許す", "Bob Iger = Disney CEO."),
 E([25], 'Ye', "I forgive the left party.", "左派の政党も許す", "Clip ends here; the next sentence (not used) is a forgiveness line about 'the Jewish media'."),
]

CLIPS['C06'] = [
 E([1, 2], 'Ye', "Anybody that's ever been through a divorce, it's a difficult thing, you know, because your baby mama gonna play with you.", "離婚を経験した奴ならわかるけど\nキツいもんなんだよ\n子どもの母親に振り回されるから"),
 E([2, 3], 'Ye', "Like, when we did the Donda 2 thing,", "例えば『Donda 2』の\nイベントの時", "Donda 2 = Ye's 2022 album/live event in Miami.", "Large-v3 'the don the two thing'; turbo 'the Donda 2 thing'.", s='when we did the'),
 E([3, 4, 5], 'Ye', "uh, when my kids came on a plane, after they was on a plane, Kim texted me and said North's not on a plane.", "子どもたちが飛行機に乗ってきた時\nもう乗ってたのに\nKimから「Northは乗ってない」ってメールが来た", "North = Ye and Kim Kardashian's eldest daughter.", "Exact meaning of 'after they was on a plane' is unclear (possibly: the text came after they had already boarded).", s='uh when my kids'),
 E([6, 7], 'Ye', "And knowing my personality, you know what I'm saying, that could affect my show.", "俺の性格わかってたら\nそれでライブに\n影響出るってわかるだろ"),
 E([7, 8], 'Ye / Host', "So baby mamas across the world, not just me, like on some billionaire — (Host:) That's a Gemini shit. Yeah, I can attest to that.", "世界中の子どもの母親がそうなんだよ\n俺みたいな億万長者だけじゃなく\n（ホスト）それ双子座あるあるだな\nマジでわかる", "", "MEDIUM: the speaker of 'That's a Gemini shit / I can attest to that' is inferred (a host); Ye is a Gemini.", s='so baby mamas'),
 E([9, 10], 'Ye', "And like, but everybody goes through a lot of that type of... I just thought about, you know,", "でもみんな\nそういうのを経験するもんで\n俺がずっと思ってたのは"),
 E([11, 12, 13], 'Ye', "all the time when I thought me and Kim were going to get a divorce, like, throughout our relationship, I always thought about", "Kimと離婚するかもって\n思うたびに\n付き合ってる間ずっと\n頭に浮かんでたのが"),
 E([14, 15], 'Ye', "Big Boi, man. He really told me what it really was on 'I Choose You.'", "Big Boiだよ\n『I Choose You』で\n本当のことを教えてくれてた", "Big Boi of OutKast; 'I Choose You' is on Speakerboxxx (2003).", "ASR spells 'Big Boy'; context (OutKast) shows Big Boi."),
 E([16], 'Host / Ye', "Oh, it's about OutKast? I was thinking about Big Boy Radio.", "あ、OutKastの話か\nBig Boiのラジオかと思った", "A host mixes up Big Boi with radio host Big Boy.", "MEDIUM: speaker of this line inferred as a host."),
 E([17, 18, 19], 'Ye', "Like, your baby's mama's mama don't like me, they try to come to the studio, try to come and fight me and blah, blah,", "「お前の母親の母親は俺を嫌ってて\nスタジオに来てケンカ売ってくる」とかさ", "Paraphrase of OutKast lyrics ('Ms. Jackson' theme)."),
 E([19, 20], 'Host / Ye', "Oh, that's 'Sorry Ms. Jackson,' right? — Yeah, yeah, yeah.", "それって『Ms. Jackson』だろ？\nそう、そう", "", "Turbo 'and then he said sorry Miss Jackson right'. Could be Ye quoting the song rather than a host; MEDIUM.", s='oh thats sorry'),
 E([21, 22], 'Ye', "Okay, but then also he says, better pick the right one or pick the kiddies up.", "それに\n「相手はちゃんと選べ\nさもなきゃ子どもの送り迎えだ」\nって言ってる", "Paraphrased OutKast lyric about choosing the right partner.", "Large-v3 'or pick the kiddies up'; turbo 'to pick pick the kitties up'. Lyric wording unconfirmed."),
 E([23, 24, 25], 'Ye', "And the whole time, I'm like, this rap is just coming, rolling through my head like a mantra of what it, you know.", "その間ずっと\nそのラップが頭の中で\nマントラみたいに回ってたんだよ"),
 E([25, 26, 27], 'Ye', "So, and I still be in my head like, you know, maybe, you know, maybe one day our family could get back together.", "今でも頭の中では\nもしかしたらいつか\n家族がまた一緒になれるかもって\n思ってる", s='so and i still'),
]

CLIPS['C07'] = [
 E([1, 2, 3], 'Ye', "Like, you know, and I don't like somebody saying, well, I'm gonna be the voice of Ye, the only voice of Ye, the only manager of Ye.", "「俺がYeの代弁者だ」とか\n「Yeの唯一の声だ」\n「唯一のマネージャーだ」とか\n言われるのが嫌なんだよ", "Answer to a question about who runs Ye's business now.", "Opening 'like you know I mean' is filler; clip could start at 'I don't like'."),
 E([3, 4, 5], 'Ye', "Like, I look at every single bill I pay. I only pay bills on a Friday, and I look at every one,", "払う請求書は全部\n自分で目を通してる\n支払いは金曜だけ\n一枚ずつ確認してる", s='like i look at'),
 E([5, 6], 'Ye', "one by one by one by one.", "一枚ずつ、一枚ずつな", s='one by one by one'),
 E([6, 7, 8], 'Ye', "Like, I was thinking getting to be a billionaire would take me out of having to do work.", "億万長者になったら\nもう働かなくていいと\n思ってたんだけど", s='like i was thinking'),
 E([8, 9], 'Ye', "Now one of my biggest jobs is keeping my money,", "今じゃ一番の仕事は\n自分の金を守ることだよ", s='now one of my'),
 E([9, 10, 11], 'Ye', "because there's a lot of people that's on a full-time job to take my money, right?", "だって俺の金を取ることを\nフルタイムでやってる奴が\nいっぱいいるからな", s='because theres a lot'),
 E([11, 12], 'Ye', "And I've literally lost hundreds of millions of dollars by not looking close enough.", "ちゃんと見てなかったせいで\nマジで何億ドルも\n失ってきたんだよ", "'Hundreds of millions of dollars' = 数億ドル.", s='and ive literally'),
 E([13, 14, 15], 'Host', "So it reminded me of what Shaq said, when he had the deal and he had the studio in his crib,", "それで思い出したのが\nShaqの話でさ\n契約してた時\n家にスタジオがあったのに", "Host anecdote about Shaquille O'Neal's rap career.", "Speaker inferred as a host."),
 E([15, 16, 17], 'Host', "and when he got the check, he looked at what the label was charging him, and they were charging him for studio time.", "明細を見たら\nレーベルがスタジオ代を\n請求してたんだって", "", "Large-v3 has false starts ('the on the check because he was paying this'). Condensed to the clear meaning.", s='and when he got'),
 E([18, 19], 'Host', "He was like, the studio's at my crib! And then he got a couple hundred thousand back. But it's funny,", "「スタジオ俺ん家だぞ！」って\nで、数十万ドル取り返した\n笑えるよな", "", "Line ends on 'it's funny' (the next words 'he overlooked that easily' were cut at the clip end); consider ending at 'got a couple hundred thousand back'.", s='hes like'),
]

CLIPS['C08'] = [
 E([1, 2], 'Host', "We had Quavo and Takeoff here the other day.", "この前Quavoと\nTakeoffが来てたんだけど", "Takeoff (Migos) and an associate visited the show earlier.", "'Quavo' is the ASR spelling of a name; unverified."),
 E([3, 4], 'Host', "What they were saying? Real shit.", "何て言ってたと思う？\nマジな話"),
 E([5, 6, 7], 'Host', "They said, Quavo said that you asked to borrow his Twitter during the blockout. Is this true?", "Quavoが言うには\nあんたがアカウント停止中に\nあいつのTwitterを\n借りようとしたって\n本当？", "Ye's Twitter was locked in Oct 2022."),
 E([8, 9, 10], 'Ye', "Yeah. He said... he offered it. He said he offered it.", "ああ\nあいつが…\n貸すって言ってきたんだよ"),
 E([11, 12, 13, 14], 'Ye', "But, you know what I'm saying, I just said, let me take this time as just like a breather.", "でも\nこの時間はひと休みだと思おうって", e='a breather'),
 E([14, 15, 16], 'Ye', "They put me, like, it's a technical foul, right? Because, oh, here goes another thing.", "テクニカル・ファウル\n取られたようなもんだろ\n「またかよ」ってな", s='they put me'),
 E([17], 'Ye', "I feel like God put me on a little timeout.", "神様にちょっと\nタイムアウトを\n取らされた気がする"),
 E([17, 18, 19], 'Ye', "Yeah. Because my dad was like, I feel where you coming from, Ye, I understand,", "親父に言われたんだよ\n「言いたいことはわかる\nYe、理解はできる", s='yeah because my'),
 E([20, 21, 22], 'Ye', "but you got to be more sophisticated with your words. You have to be more sophisticated.", "でも言葉はもっと\n洗練させなきゃダメだ」って"),
 E([22, 23], 'Ye', "I agree with that. That was less sophisticated than I needed to be.", "その通りだと思う\nあれは必要以上に\n雑な言い方だった", "Refers to the tweet that got him locked out.", s='i agree'),
 E([23, 24], 'Host', "You said God texted you that?", "神様からメールが来たって？", "", "MEDIUM: who says this is inferred.", s='you said god'),
 E([24], 'Host', "No, his father.", "いや、親父さんだよ", s='no his'),
 E([24, 25], 'Ye', "Yeah, second to God, my dad. Yeah, yeah, yeah.", "そう、神の次に大事な\n俺の親父", s='yeah second'),
 E([25, 26, 27], 'Ye', "Because I know for a fact, um, you know, pissing off Jewish people and pissing off black people, I know that.", "ユダヤ人を怒らせて\n黒人も怒らせたって\nそれはちゃんとわかってる", "Ye acknowledging that his remarks angered both communities.", s='because i know for'),
]
