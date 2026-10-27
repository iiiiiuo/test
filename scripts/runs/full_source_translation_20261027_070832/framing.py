"""Per-shot x offset of the 1119x1080 crop window (frozen spec band), chosen from grid contact sheets.
Source presentation time [t0, t1) in seconds -> centre as a fraction of the 1920 px width.
All shots keep both hosts/guest in frame; Snoop's close-ups match the series guest close-up window."""
import json, sys
SHOTS = [
 (0.0, 5.37, 0.50, "wide: Charlamagne + Snoop (Snoop talks)"),
 (5.37, 36.0, 0.516, "Snoop close-up (zoom in 5.4-6.2)"),
 (36.0, 39.24, 0.50, "wide: both laugh (zoom out)"),
 (39.24, 43.11, 0.48, "whip to DJ Envy"),
 (43.11, 47.11, 0.52, "whip back to wide: Charlamagne + Snoop"),
 (47.11, 52.0, 0.50, "Snoop close-up (zoom 47.1-47.5)"),
]
W, CW = 1920, 1119
def x0(c): return int(round(min(max(c * W - CW / 2, 0), W - CW)))
expr = str(x0(SHOTS[-1][2]))
for t0, t1, c, _ in reversed(SHOTS[:-1]):
    expr = f"if(lt(t\\,{t1})\\,{x0(c)}\\,{expr})"
if __name__ == "__main__":
    json.dump([dict(t0=a, t1=b, centre=c, x0=x0(c), note=n) for a, b, c, n in SHOTS], open(sys.argv[1], "w"), indent=1)
    print(expr)
