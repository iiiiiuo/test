import json, math
FPS=30000/1001
def fr(t): return round(t*FPS)
units=[
 ("U01",0.0,61.0,"Settling into adulthood; crash-out reputation; headlines; leaving courthouse, 'album on the way'"),
 ("U02",61.06,135.28,"Host asks why he invites drama (Offset gambling, Kai Cenat streams); Offset owes him 10K, calls him a bum; whole industry in his DMs"),
 ("U03",135.28,143.1,"Bridge: Charlamagne follow-up 'y'all cool like that to say here's 10K?'"),
 ("U04",143.3,229.82,"Casino story: he lent 10K, Offset begging regular ladies for cash, made it rain in strip club; 'it's about respect'"),
 ("U05",231.4,267.24,"Worried what others think? 'most I did was call him a bum'; 10K in the air; could you and Offset be cool"),
 ("U06",267.68,349.84,"Is beef too far to squash? A Boogie come give me a hug; Offset hug too; feel bad for Offset's gambling, 'look a little sad'"),
 ("U07",350.12,423.8,"Healed from being shot 7 times? PTSD wore off; no therapy, isolated; maybe 8-9 shots, mad holes"),
 ("U08",424.36,480.76,"Out of coma, got on feet, almost fought the doctor, 'he spanked you out' hospital gown joke"),
 ("U09",480.76,546.06,"Does trauma change people? changed in front of the world; misunderstood; album name They Just Ain't You"),
 ("U10",546.32,571.92,"Removed bullet from neck while awake with numbing cream; 'Rambo' joke"),
 ("U11",573.88,649.22,"Feels safe alone; friends a liability; different from average person; 'singing a different tune in five years'"),
 ("U12",649.34,735.56,"50 Cent: shooting parallel, Many Men remix, different paths, too old for trolling"),
 ("U13",736.0,747.81,"Outro/sign-off and network bumper (non-content)"),
]
json.dump({"source":"SOURCE_INTERVIEW sha256 2bc9e4b5…0280f","coverage":"0.000-747.814 s fully assigned","units":[{"id":u,"start_s":a,"end_s":b,"summary":s} for u,a,b,s in units]},open("work/semantic_map.json","w"),indent=1)
cands=[
 dict(id="C01",units=["U01"],iv=[[0.034,61.0]],topic="Grown up now / headlines",open_end="'How you been?' -> 'Courthouse... album on the way'",standalone="standalone",risk="MEDIUM: end phrase disputed across passes (album on the way)",q="MEDIUM",status="reserved",reason="natural interview opener; 61s"),
 dict(id="C02",units=["U02"],iv=[[61.0,135.28]],topic="Offset owes me 10K",open_end="host question -> 'kudos to you, bro'",standalone="standalone",risk="MEDIUM: fast speech, pass2-resolved",q="HIGH",status="reserved",reason="clear question+story+punchline; 74s"),
 dict(id="C03",units=["U04"],iv=[[143.3,229.82]],topic="Casino/strip club story",open_end="'Was y'all in the casino together?' -> 'I'm the biggest b**ch'",standalone="standalone (Offset referred to as 'he')",risk="MEDIUM",q="HIGH",status="reserved",reason="vivid story with resolution; 86.5s in acceptable band"),
 dict(id="C03b",units=["U03","U04","U05"],iv=[[135.28,267.24]],topic="Casino + aftermath",open_end="",standalone="",risk="",q="MEDIUM",status="rejected",reason=">120s; splitting gives C03; U05 alone too short"),
 dict(id="C04",units=["U06"],iv=[[267.68,349.84]],topic="Beef with A Boogie & Offset",open_end="'Is the beef too far to squash?' -> 'this shit look a little sad'",standalone="standalone",risk="LOW",q="HIGH",status="reserved",reason="complete Q&A; 82s"),
 dict(id="C04b",units=["U05","U06"],iv=[[257.28,349.84]],topic="Offset cool? + beef",open_end="",standalone="",risk="",q="MEDIUM",status="rejected",reason="92.6s; extra opener rambles; C04 tighter"),
 dict(id="C05",units=["U07"],iv=[[350.12,423.8]],topic="Shot 7 times, healing alone",open_end="'Have you fully healed?' -> 'some of them was going through me'",standalone="standalone",risk="LOW",q="HIGH",status="reserved",reason="strong; 74s"),
 dict(id="C06",units=["U08","U10"],iv=[[424.36,480.76],[547.38,571.92]],topic="Hospital stories",open_end="'How long to get up?' -> 'I ain't fry like that'",standalone="standalone",risk="MEDIUM: one cut joining two hospital anecdotes",q="HIGH",status="reserved",reason="U08 alone 56s (<60); U10 alone 25s; same-topic join, chronological"),
 dict(id="C07",units=["U09"],iv=[[482.0,546.06]],topic="Trauma & being misunderstood",open_end="'Does trauma change people?' -> album title meaning",standalone="standalone",risk="LOW",q="HIGH",status="reserved",reason="64s"),
 dict(id="C07b",units=["U09","U10"],iv=[[482.0,571.92]],topic="Trauma + neck bullet",open_end="",standalone="",risk="",q="MEDIUM",status="rejected",reason="would strand U08 (<60s); topic shift"),
 dict(id="C08",units=["U11"],iv=[[573.88,649.22]],topic="Safe alone",open_end="'You spend a lot of time alone' -> 'different tune in five years / hopefully'",standalone="standalone",risk="LOW",q="HIGH",status="reserved",reason="75s"),
 dict(id="C09",units=["U12"],iv=[[649.34,735.56]],topic="50 Cent",open_end="'You talked with 50?' -> 'troll me right now'",standalone="standalone",risk="MEDIUM: 719-731 age phrase",q="HIGH",status="reserved",reason="86s complete thread"),
]
for c in cands:
    c["est_s"]=round(sum(b-a for a,b in c["iv"]),1)
json.dump({"candidates":cands,"unused_units":{"U03":"follow-up bridge, depends on U02/U04, 8s","U05":"aftermath remarks depend on casino story; 36s, no same-topic extension without exceeding limits or overlapping frozen picks","U13":"outro/bumper, not content"}},open("work/clip_candidates.json","w"),indent=1,ensure_ascii=False)
rows=["| ID | source intervals (s) | est. dur | topic | opening/setup + ending | standalone | confidence risk | quality | overlap conflicts | status | reason |","|---|---|---|---|---|---|---|---|---|---|---|"]
for c in cands:
    conf=[o["id"] for o in cands if o is not c and any(max(a,x)<min(b,y) for a,b in c["iv"] for x,y in o["iv"])]
    rows.append(f"| {c['id']} | {', '.join(f'{a:.2f}-{b:.2f}' for a,b in c['iv'])} | {c['est_s']} | {c['topic']} | {c['open_end']} | {c['standalone']} | {c['risk']} | {c['q']} | {', '.join(conf) or 'none'} | {c['status']} | {c['reason']} |")
import os; os.makedirs("output/shared",exist_ok=True)
open("output/shared/clip_candidate_map.md","w").write("# Clip candidate map\n\nSource: SOURCE_INTERVIEW (747.81 s). Units: work/semantic_map.json. Unused units: U03 (bridge, dependent), U05 (dependent aftermath, 36 s), U13 (outro).\n\n"+"\n".join(rows)+"\n")
print("\n".join(rows))
