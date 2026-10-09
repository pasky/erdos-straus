"""R107: own recount of Comp 3.2 (C_3 part) and Comp 3.3 (smallest miss) from O107's inv_N.pkl files.
usage: review_m13e_c3.py DIR..."""
import sys, glob, pickle
def v(m, q):
    k = 0
    while m % q == 0: m //= q; k += 1
    return k
pt = {11: 2, 13: 15}
first = {}
for d in sys.argv[1:]:
    for fn in glob.glob(f'{d}/inv_*.pkl'):
        A = pickle.load(open(fn, 'rb'))
        for b in A['boxes']:
            if b not in first or A['N'] < first[b]: first[b] = A['N']
meet = []; minmiss = None
for (fam, MT, r), N in first.items():
    ok = True; mass = 1.0; miss = 1
    for q in (11, 13):
        k = v(MT, q)
        if (r - pt[q]) % q**min(k, 3): ok = False
        if k > 3: mass /= q**(k - 3)
        a = 0
        while a < k and (r - pt[q]) % q**(a + 1) == 0: a += 1
        miss *= q**(k - a)
    if ok: meet.append((N, fam, MT, r, mass))
    if minmiss is None or miss < minmiss[0]: minmiss = (miss, fam, MT, r, N)
print('distinct boxes', len(first), '; meeting C_3:', len(meet), 'total mass %.3g' % sum(m[-1] for m in meet))
for m in sorted(meet): print('  ', m)
print('smallest miss', minmiss)
