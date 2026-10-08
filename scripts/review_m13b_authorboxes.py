"""R95: re-verify every box in the author's inv_*.pkl (fam,MT,r)->P with the reviewer's literal ET classes,
then recompute (2,2)-cell coverage from the verified boxes.  usage: rundir k"""
import sys, glob, pickle
import numpy as np
sys.path.insert(0, __import__('os').path.dirname(__file__))
from review_m13b_enum import ok_family
boxes = set(); bad = 0; tot = 0
for fn in glob.glob(sys.argv[1] + '/inv_*.pkl'):
    for (fam, MT, r), P in pickle.load(open(fn, 'rb'))['boxes'].items():
        tot += 1; o = ok_family(fam, P)
        if not o or o[1] != MT or r not in o[2]: bad += 1; print('BAD', fam, MT, r, P); continue
        boxes.add((MT, r))
print('author boxes', tot, 'failed reverification', bad)
for k in map(int, sys.argv[2:]):
    R = 11**k * 13**k; S = R // 143; cov = np.zeros(S, dtype=bool)
    for MT, r in boxes:
        if MT == 1 or R % MT: continue
        for v in range(r % MT, MT * 143, MT):
            if v % 143 == 2: break
        else: continue
        L = MT * 143 // np.gcd(MT, 143); cov[(v - 2) // 143::L // 143] = True
    print(f'k={k}: (2,2) cell uncovered {(~cov).sum()}/{S} = {(~cov).sum()/S:.4f}')
