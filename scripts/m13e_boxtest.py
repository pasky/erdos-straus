"""m13e_boxtest.py — test a T-generic point x(u11,u13) against all engine boxes inv_*.pkl in a run dir
(boxes = (fam, M_T, r mod M_T) of every T-generic datum, m13b_invert.py).  x lies in the box iff
r = u11 mod 11^{v11(M_T)} and r = u13 mod 13^{v13(M_T)} (u given as rationals p/s: s*r = p).
usage: m13e_boxtest.py u11 u13 rundir [rundir...]   (u as p or p/s)"""
import glob, pickle, sys
from fractions import Fraction

def v(m, q):
    k = 0
    while m % q == 0:
        m //= q; k += 1
    return k

def inbox(MT, r, u11, u13):
    for q, u in ((11, u11), (13, u13)):
        Q = q ** v(MT, q)
        if Q > 1 and (u.denominator * r - u.numerator) % Q:
            return False
    return True

if __name__ == '__main__':
    u11, u13 = Fraction(sys.argv[1]), Fraction(sys.argv[2])
    nb = nf = 0; hits = []; Ns = []
    for d in sys.argv[3:]:
        for fn in sorted(glob.glob(d + '/inv_*.pkl')):
            D = pickle.load(open(fn, 'rb')); nf += 1; Ns.append(D['N'])
            for (fam, MT, r), P in D['boxes'].items():
                nb += 1
                if MT > 1 and inbox(MT, r, u11, u13):
                    hits.append((D['N'], fam, MT, r, P))
    print(f'point ({u11},{u13}): files {nf} (N max {max(Ns)}), boxes {nb}, hits {len(hits)}')
    for h in hits[:20]: print(' HIT', h)
