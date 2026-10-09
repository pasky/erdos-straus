"""m13e_closest.py — near misses: boxes that miss x(u11,u13) by the smallest factor.  For a box (fam, M_T, r):
agreement a_q = min(v_q(M_T), v_q(r - u_q)); miss = prod_q q^(v_q(M_T) - a_q) (= 1 iff the box contains the point);
'depth' = 11^a_11 * 13^a_13 = the precision to which the box agrees with the point.
usage: m13e_closest.py u11 u13 rundir [rundir...]"""
import glob, pickle, sys
from fractions import Fraction
from m13e_boxtest import v
u = {11: Fraction(sys.argv[1]), 13: Fraction(sys.argv[2])}
rows = {}
for d in sys.argv[3:]:
    for fn in glob.glob(d + '/inv_*.pkl'):
        D = pickle.load(open(fn, 'rb'))
        for (fam, MT, r), P in D['boxes'].items():
            if MT == 1:
                continue
            miss = depth = 1
            for q in (11, 13):
                e = v(MT, q)
                if e == 0:
                    continue
                t = u[q].denominator * r - u[q].numerator
                a = min(e, v(t, q) if t else e)
                miss *= q ** (e - a); depth *= q ** a
            key = (fam, MT, r)
            if key not in rows or D['N'] < rows[key][0]:
                rows[key] = (D['N'], miss, depth, P)
best = sorted(rows.items(), key=lambda kv: (kv[1][1], -kv[1][2]))[:12]
print(f'point ({u[11]},{u[13]}): {len(rows)} boxes')
for (fam, MT, r), (N, miss, depth, P) in best:
    print(f' miss={miss:<6} depth={depth:<10} M_T={MT:<12} N={N:<11} {fam} {P}')
print(' max depth among all boxes:', max(rows.values(), key=lambda t: t[2])[1:3])
