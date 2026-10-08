"""Are I2/II1/I4 boxes ever 'new', i.e. not contained in a box of II3/I3/I1/II2 (engine data, all N)?
A box (MT, r) contains (MT2, r2) iff MT | MT2 and r2 = r mod MT.  usage: m13b_newbox.py rundir"""
import glob, pickle, sys
from collections import Counter
fams = {}
for fn in glob.glob(sys.argv[1] + '/inv_*.pkl'):
    for (fam, MT, r) in pickle.load(open(fn, 'rb'))['boxes']:
        fams.setdefault(fam, set()).add((MT, r))
PQ = set().union(*(fams.get(f, set()) for f in ('II3', 'I3', 'I1', 'II2')))
divs = sorted({MT for MT, _ in PQ})
cnt = Counter()
for f in ('I2', 'II1', 'I4'):
    for MT, r in fams.get(f, ()):
        inside = any(MT % D == 0 and (D, r % D) in PQ for D in divs if D <= MT)
        cnt[(f, inside)] += 1
print(cnt)
for f in ('I2', 'II1', 'I4'):
    for MT, r in sorted(fams.get(f, ())):
        if not any(MT % D == 0 and (D, r % D) in PQ for D in divs if D <= MT):
            print(f, MT, r, 'cell', r % 11 if MT % 11 == 0 else '*', r % 13 if MT % 13 == 0 else '*')
