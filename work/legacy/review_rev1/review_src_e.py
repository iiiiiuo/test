from review_src_a import E
CLIPS = {}

CLIPS['C23'] = [
 E([1, 2], 'Ye', "But right now in America, say, one of the laws that I would change is, it's illegal to collect rainwater in America.", "でも今のアメリカで\n俺が変えたい法律のひとつが\n雨水を集めるのが\n違法だってことだ", "Ye's claim. In reality most US states allow rainwater collection; a few restrict it. The translation keeps his claim as spoken.", "Factual accuracy of the claim is not ours to fix; flagging so the reviewer knows."),
 E([3], 'Host', "What? Illegal? It's illegal?", "は？違法？\n違法なの？"),
 E([4], 'Ye', "It's illegal to collect rainwater in America.", "アメリカじゃ雨水を集めるのは\n違法なんだよ"),
 E([5], 'Ye', "You go to every other country, they're collecting rainwater.", "他の国じゃ\nどこでも雨水を集めてる"),
 E([6], 'Ye', "You know, people are controlling the water.", "水を支配してる\n連中がいるんだよ"),
 E([7, 8, 9, 10], 'Ye', "You know, it's going to be fuck what t-shirt you wear, what political opinion, and who got beef with who. You ain't got no water,", "どんなTシャツ着てるかとか\n政治的な意見とか\n誰と誰がビーフしてるとか\nどうでもよくなる\n水がなかったら", "Reference to his 'White Lives Matter' shirt controversy.", "", e='got no water'),
 E([10, 11], 'Ye', "you ain't got no life. I'm trying to tell you.", "命もないんだよ\nそう言いたいわけ", s='you aint got no life', e='to tell you'),
 E([11, 12, 13], 'Ye', "Because, you know, a lot of people call me... they want to call me crazy.", "みんな俺のことを…\nイカれてるって\n言いたがるだろ", "Slow delivery with pauses (kept as meaningful pauses).", s='because', e='call me crazy'),
 E([13, 14], 'Ye', "It's like, it's like running a marathon.", "それって\nマラソンみたいなもんでさ", s='its', e='a marathon'),
 E([14, 15, 16], 'Ye', "If I got some short shorts on and a tank top, and I'm sweating hard as hell, um, running down the street, running the wrong way down a freeway,", "俺が短パンにタンクトップで\n汗だくになって\n高速道路を逆走してたら", s='if i got', e='down a freeway'),
 E([17], 'Ye', "then you're going to say that person is crazy.", "あいつイカれてるって\n言うだろ"),
 E([18, 19], 'Ye', "But if a hundred other people do it with me, then it's a marathon.", "でも100人が\n一緒に走ってたら\nそれはマラソンなんだよ", e='its a marathon'),
 E([19, 20], 'Host', "That's a good way to put it.", "うまいこと言うな", "", "Large-v3 'that's a good way to kill that'; turbo 'That's a good way to put it'.", s='thats'),
]

CLIPS['C24'] = [
 E([1, 2], 'Host', "Because as a person that, when we first seen the Gap deal, right, um, we understand that rich motherfuckers ain't going in the Gap.", "Gapとの契約を\n初めて見た時さ\n金持ちはGapなんか\n行かないってのは\nわかってたけど", "Yeezy Gap launched 2022."),
 E([3, 4, 5], 'Host', "But you know what, they was going in the Gap because of you. It was going. And they say 'powered by Balenciaga,' but then you walk into the store,", "あんたのおかげで\nみんなGapに行ったんだよ\n「Powered by Balenciaga」って\n書いてあるのに\n店に入ったら", "'Yeezy Gap Engineered by Balenciaga' was the line's branding.", "", s='but you know what', e='to the store'),
 E([6, 7, 8], 'Host', "and then the clothes is just on the floor. Is that degrading to somebody that's rich that want to come in there and support you?", "服がそのまま\n床に置いてある\nあれって応援しに来た\n金持ちに失礼じゃない？", "Yeezy Gap displayed clothes in large bags on the floor.", "MEDIUM: ASR 'this is closed that's just on the floor'; read as 'the clothes is just on the floor'."),
 E([9], 'Ye', "We should degrade the rich.", "金持ちなんか\n落としてやればいいんだよ"),
 E([10, 11], 'Ye', "Everybody is dirt. Everybody on the same level beneath God.", "みんな土だよ\n神の下では\nみんな同じレベル"),
 E([12, 13, 14], 'Ye / Host', "Because we'll hop over... (Host: That was a good one.)", "だって俺らは\nまたいで行くんだよ…", "", "LOW: crosstalk; large-v3 'That was all. That was very good.', turbo has nothing. Host reaction not translated.", e='was very good'),
 E([15, 16], 'Ye', "You know, we'll walk over a homeless person to get to the Gucci store.", "グッチの店に行くために\nホームレスをまたいで\n歩くんだから"),
 E([17, 18], 'Ye', "Ray Kurzweil said a utopia is possible where we're led by the least noble and the greediest people.", "レイ・カーツワイルは\n最も高潔じゃなく\n最も強欲な連中に\n率いられたユートピアが\nあり得るって言ってた", "Ray Kurzweil = futurist. Attribution and wording are Ye's.", "MEDIUM: the quote's meaning is ambiguous as spoken; translated literally. Ye repeats 'the world is led by the least noble and the most greedy' later in the interview."),
 E([19, 20], 'Ye', "I brought the head designer of Balenciaga, the greatest designer on our planet today, Demna.", "俺はバレンシアガの\nヘッドデザイナーを連れてきた\n今この星で最高のデザイナー\nデムナだ", "Demna = Balenciaga creative director."),
 E([21], 'Ye', "Demna is the Ye of clothing.", "デムナは\n服の世界のイェだ"),
 E([22], 'Ye', "Demna is the Drake of clothing.", "デムナは\n服の世界のドレイクだ"),
 E([23], 'Ye', "Drake is the greatest rapper ever.", "ドレイクは\n史上最高のラッパーだよ", "Notable because of their long feud."),
]

CLIPS['C25'] = [
 E([1], 'Host', "Taking God out of music, you said?", "音楽から神を\n取り除いたって？", "Recap of Ye's earlier point that R&B took God out of the music.", "", e='taking god out of music'),
 E([1, 2, 3], 'Ye', "Yeah. I remember I was at Roscoe's, you know, earlier this year, and I love Roscoe's and stuff,", "そう\n今年の初めに\nロスコーズに行ったんだけど\nロスコーズは好きなんだよ", "Roscoe's House of Chicken and Waffles (LA).", "", s='yeah i remember', e='roscoes stuff'),
 E([3, 4], 'Ye', "but they're playing the music, and it's like Usher saying, 'You got it bad.'", "でも店でかかってた曲が\nアッシャーの\n『You Got It Bad』で", "Usher's 2001 hit.", "", s='but theyre playing', e='you got it bad'),
 E([4, 5], 'Ye', "'You got it, you got it bad.'", "「お前は重症だ」ってさ", s='you got it you'),
 E([5], 'Ye', "Yeah, that messaging is not uplifting.", "そういうメッセージは\n前向きじゃないだろ", s='yeah that messaging'),
 E([5, 6], 'Host', "Some niggas got it bad.", "重症な奴も\nいるけどな", "Host joke.", "Speaker inferred.", s='some', e='got it bad'),
 E([6, 7], 'Ye', "Yeah, yeah. But there's... when we sing... God created music solely for the purpose of worshiping God.", "ああ\nでもな\n神は神を讃えるためだけに\n音楽を作ったんだよ", s='yeah yeah'),
 E([8, 9], 'Ye', "Now, if you listen to the majority of the music, it's not worshiping God. No, it's going into the dark holes.", "でも今の音楽の大半は\n神を讃えてない\n暗い穴に落ちていってる", e='dark holes'),
 E([9, 10, 11], 'Ye', "It's like, sweat to my... yeah, but it's saying, I want to fuck your bitch, I want to fuck your girlfriend,", "「お前の女とヤりたい」\n「お前の彼女とヤりたい」", "", "LOW: 'sweat to my...' fragment unclear in both models; the Japanese leaves it out.", s='its like'),
 E([12, 13], 'Ye', "I want to fuck your mom, like, it's like, and I want to do drugs while I'm fucking your mom.", "「お前の母親とヤりたい」\n「ヤりながらドラッグやりたい」\nとかさ"),
 E([13, 14, 15], 'Ye', "Like, it's, it just takes you into that, that place.", "そういう場所に\n連れていかれるんだよ", s='like its it', e='that that place'),
 E([14, 15, 16, 17, 18], 'Ye', "And God has... God has a place for us in a promised land that can't be defined by man. It's not the 40 acres that the oppressors can take away.", "でも神は\n俺らのために\n約束の地を用意してる\n人間には定義できない場所だ\n抑圧者が奪える\n40エーカーとは違う", "'40 acres (and a mule)' = broken post-Civil War promise of land to freed slaves.", "ASR '400 acres'; the historical phrase is '40 acres'. MEDIUM.", s='and god has'),
]

CLIPS['C26'] = [
 E([1, 2], 'Ye', "Like, you at somebody's wedding, and somebody get into a fight with a family member at the end.", "誰かの結婚式で\n最後に親戚と\nケンカになる奴いるだろ", "Context: Ye is talking about speaking his mind after drinking D'Usse, the cognac on the table."),
 E([3, 4], 'Ye', "And they say some real shit, but they ain't said it until they had the D'Usse.", "本音をぶちまけるけど\nそれもドゥッセを\n飲むまでは言わなかった", "D'Usse = cognac brand co-owned by Jay-Z, sponsor on the table.", "ASR 'do say' = D'Usse."),
 E([5], 'Ye', "They say some real shit.", "マジな本音をな"),
 E([6, 7, 8, 9], 'Ye', "And I'm telling you, the whole difference is, when people come and speak their truth, they need to speak their truth off of D'Usse. They don't need to speak their truth off of Hennessy.", "言っとくけど\n本音を言うなら\nドゥッセで酔って言えよ\nヘネシーで酔って\n言うんじゃなくてな", "Hennessy = rival cognac, long associated with hip-hop.", e='off of hennessy'),
 E([9, 10, 11, 12], 'Ye', "So I want to say today is, I need every single... and we can get back to the Black Lives Matter... but I need every single liquor store in the world to remove the Hennessy and put the D'Usse in it.", "だから今日言いたいのは\n…BLMの話には後で戻るけど\n世界中の酒屋から\nヘネシーを撤去して\nドゥッセを置いてほしい", "", "Mid-sentence aside about returning to the Black Lives Matter topic.", s='so i want to say', e='do say in it'),
 E([13], 'Ye', "I'm asking and calling for every...", "全員に呼びかける…", "", "Large-v3 'I'm asking a good day every'; turbo 'I'm asking and calling for every'.", s='im asking'),
 E([14], 'Ye', "I'm asking every black person,", "黒人のみんなに頼みたい"),
 E([15, 16], 'Ye', "when you want to drink and you want to go full the-uncle-that-don't-give-a-fuck level at the wedding,", "結婚式で飲んで\n何も気にしない\nおじさんレベルまで\n振り切りたい時は", "", "ASR 'go fool' = 'go full'."),
 E([17], 'Ye', "do it off the D'Usse. Don't do it off the Hennessy.", "ドゥッセでやれ\nヘネシーじゃなくて"),
 E([18], 'Ye', "Don't do it off the Hennessy.", "ヘネシーはやめとけ", e='off the hennessy'),
 E([18, 19, 20, 21], 'Ye', "Go full Ye off the D'Usse. Go Ye! Go full Ye off the D'Usse. Go full Ye off the D'Usse. Go full Ye off the D'Usse.", "ドゥッセで\nフルにイェになれ\nドゥッセでフル・イェだ", "A chant; Ye repeats it several times.", "Number of repetitions differs between models (large-v3 four, turbo five).", s='go full yay', e='yay off the duce but'),
 E([21, 22], 'Ye', "Let me just be clear real quick. Respect. Because this is the only time...", "ちょっとはっきりさせとくと\nリスペクトはしてるよ\nこれは今回だけ…", "", "MEDIUM: sentence trails off.", s='let me just', e='the only time'),
 E([22], 'Ye', "This is delicious. This D'Usse is good.", "これうまいな\nこのドゥッセいいわ", s='this is delicious'),
 E([23, 24], 'Ye', "Also for an evening nightcap. A nightcap is well recommended, my friend.", "夜の寝酒にもいい\n寝酒にオススメだぜ", "Joking ad-read tone."),
]
