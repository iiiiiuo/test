"""Per-shot horizontal centre of the 1119x1080 crop window (frozen spec band), chosen from 2 fps contact sheets.
Source time ranges [t0, t1) in seconds -> centre as a fraction of the 1920 px width."""
import json, sys
SHOTS = [
 (0.0, 4.137, 0.48, "intro car, Travis enters"),
 (4.137, 8.675, 0.55, "Ryan greets, hug, both talk"), (8.675, 12.579, 0.60, "walk in: Travis + Ryan; shop photos"),
 (12.579, 15.916, 0.55, "covered car"), (15.916, 23.724, 0.56, "Travis + Ryan at the cover"),
 (23.724, 29.730, 0.50, "Travis walks / reacts at red wall"), (29.730, 40.274, 0.50, "car exterior details"),
 (40.274, 43.510, 0.56, "Travis + Ryan at the car"), (43.510, 52.219, 0.50, "interior details"),
 (52.219, 54.988, 0.45, "Travis by car"), (54.988, 61.828, 0.50, "seats / steering wheel"),
 (61.828, 63.730, 0.40, "Travis close-up"), (63.730, 68.368, 0.50, "car profile / rear"),
 (68.368, 71.605, 0.55, "Travis dances at red wall"), (71.605, 73.607, 0.64, "Ryan + Travis at the door"),
 (73.607, 76.710, 0.50, "dash / car profile"), (76.710, 81.215, 0.45, "Travis by the car"),
 (81.215, 85.352, 0.45, "Travis interview"), (85.352, 92.192, 0.52, "Travis + Ryan hug, Ryan by the car"), (92.192, 96.697, 0.50, "Travis interview"),
 (96.697, 101.969, 0.52, "Travis + Ryan by the door / walk"), (101.969, 104.037, 0.42, "car wash"),
 (104.037, 110.611, 0.42, "car in the lot"), (110.611, 114.214, 0.48, "Ryan to camera"),
 (114.214, 119.486, 0.50, "car drives off"), (119.486, 124.358, 0.48, "Ryan to camera"),
 (124.358, 127.361, 0.40, "Travis close"), (127.361, 131.0, 0.50, "group photo"),
]
W, CW = 1920, 1119
def x0(c): return int(round(min(max(c * W - CW / 2, 0), W - CW)))
expr = str(x0(SHOTS[-1][2]))
for t0, t1, c, _ in reversed(SHOTS[:-1]):
    expr = f"if(lt(t\\,{t1})\\,{x0(c)}\\,{expr})"
if __name__ == "__main__":
    json.dump([dict(t0=a, t1=b, centre=c, x0=x0(c), note=n) for a, b, c, n in SHOTS], open(sys.argv[1], "w"), indent=1)
    print(expr)
