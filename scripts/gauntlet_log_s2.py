"""Append one critic round to work/b2/gauntlet.json: gauntlet_log_s2.py CLIP ROUND VERDICT [largest_gap] [fix] [failed_approach]"""
import json, sys
p = 'work/b2/gauntlet.json'; g = json.load(open(p))
a = sys.argv[1:] + [None] * 6
g.append({'target': a[0], 'round': int(a[1]), 'verdict': a[2], 'largest_gap': a[3] or 'none', 'fix': a[4] or 'none', 'failed_approach': a[5]})
json.dump(g, open(p, 'w'), indent=1)
