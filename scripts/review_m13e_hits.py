"""R107: own re-test of x** = (2,15) and x* = (2,2) against every box stored in O107's inv_N.pkl files, and
the level bookkeeping (all T-units 1<N<=13^9 present; none in (13^9, 11^10)).  usage: review_m13e_hits.py DIR..."""
import sys, glob, pickle
def inbox(MT, r, u11, u13):
    for q, u in ((11, u11), (13, u13)):
        k = 0; t = MT
        while t % q == 0: t //= q; k += 1
        if (r - u) % q**k: return False
    return True
units = sorted(11**i * 13**j for i in range(12) for j in range(12) if 1 < 11**i * 13**j < 11**10)
print('T-units <= 13^9:', sum(u <= 13**9 for u in units), '; in (13^9, 11^10):', [u for u in units if u > 13**9])
seen = {}; nb = 0; h15 = []; h2 = set()
for d in sys.argv[1:]:
    for fn in glob.glob(f'{d}/inv_*.pkl'):
        A = pickle.load(open(fn, 'rb')); seen[A['N']] = A['nsol']
        for (fam, MT, r), P in A['boxes'].items():
            nb += 1
            if MT == 1 or inbox(MT, r, 2, 15): h15.append((A['N'], fam, MT, r, P))
            if MT == 1 or inbox(MT, r, 2, 2): h2.add((fam, P))
print('levels present:', len(seen), 'missing:', [u for u in units if u <= 13**9 and u not in seen])
print('ES solutions', sum(seen.values()), 'box entries (per level, summed)', nb)
print('x** hits:', h15); print('x* data:', sorted(h2))
