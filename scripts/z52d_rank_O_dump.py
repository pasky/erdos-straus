"""Dump sample items (master + avenue row) for manual audit. usage: dump.py i j"""
import json, sys, os
from z52d_rank_O_common import load_rows, load_master, OUT
s = json.load(open(os.path.join(OUT, 'negsample.json')))['mids']
rows = {r['mid']: r for r in load_rows()}; m = load_master()
i, j = int(sys.argv[1]), int(sys.argv[2])
for mid in s[i:j]:
    a = rows[mid]; t = m[mid]
    print(f"=== {mid} [{a['_batch']}] {t['title']}")
    print('CONN:', t['connection']); print('WHY:', t.get('why','')); print('FIRST:', t.get('first_step',''))
    for k in ('role','missing_theorem','yield','status','status_ref','barrier','next','note'):
        print(f'{k.upper()}:', a.get(k))
    print()
