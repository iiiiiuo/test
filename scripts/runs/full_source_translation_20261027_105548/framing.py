"""Per-shot x offset of the 1222x1180 crop window (frozen series band aspect 1119:1080) inside the 2096x1180
programme picture (screen-recording bars: picture spans x 230..2325 of the 2556x1180 rotated frame).
Shot cuts from scene detection; centres from Haar face positions (faces.json) as a fraction of the 2096 px width."""
import json, sys
SHOTS = [
 (0.0, 6.989, 0.45, "Snoop close-up"),
 (6.989, 8.404, 0.0, "two-shot: left edge so speaking Snoop (left) and host both stay in frame (critic r1)"),
 (8.404, 24.929, 0.45, "Snoop close-up"),
 (24.929, 26.344, 0.0, "two-shot: left edge so speaking Snoop (left) and host both stay in frame (critic r1)"),
 (26.344, 28.141, 0.45, "Snoop close-up"),
 (28.141, 29.222, 0.0, "two-shot: left edge so speaking Snoop (left) and host both stay in frame (critic r1)"),
 (29.222, 66.001, 0.45, "Snoop close-up"),
 (66.001, 67.133, 0.0, "two-shot: left edge so speaking Snoop (left) and host both stay in frame (critic r1)"),
 (67.133, 96.406, 0.45, "Snoop close-up"),
 (96.406, 97.654, 0.0, "two-shot: left edge so speaking Snoop (left) and host both stay in frame (critic r1)"),
 (97.654, 130.852, 0.45, "Snoop close-up"),
 (130.852, 135.116, 0.0, "two-shot: host asks the question; left edge keeps Snoop in frame too"),
 (135.116, 999, 0.50, "iOS Control Center (screen recording being stopped) - part of the source"),
]
PX, W, CW = 230, 2096, 1222
def x0(c): return PX + int(round(min(max(c * W - CW / 2, 0), W - CW)))
expr = str(x0(SHOTS[-1][2]))
for t0, t1, c, _ in reversed(SHOTS[:-1]):
    expr = f"if(lt(t\\,{t1})\\,{x0(c)}\\,{expr})"
if __name__ == "__main__":
    json.dump([dict(t0=a, t1=b, centre=c, x0=x0(c), note=n) for a, b, c, n in SHOTS], open(sys.argv[1], "w"), indent=1)
    print(expr)
