"""R95: is a T-generic point (u11,u13) (rationals) in any box of the author's re-verified inv_*.pkl or the
reviewer's own pickle?  usage: rundir mypkl 'u11,u13' ..."""
import sys, glob, pickle
from fractions import Fraction as Fr
sys.path.insert(0, __import__('os').path.dirname(__file__))
from review_m13b_enum import ok_family
boxes = {}
for fn in glob.glob(sys.argv[1] + '/inv_*.pkl'):
    for (fam, MT, r), P in pickle.load(open(fn, 'rb'))['boxes'].items(): boxes[(fam, MT, r)] = P
for N, (ns, D) in pickle.load(open(sys.argv[2], 'rb')).items():
    for f, P, (M, MT, rs) in D:
        for r in rs: boxes[(f, MT, r)] = P
def red(x, m): x = Fr(x); return x.numerator * pow(x.denominator, -1, m) % m
def vq(m, q):
    k = 0
    while m % q == 0: m //= q; k += 1
    return k
for pt in sys.argv[3:]:
    u = pt.split(','); hit = []
    for (f, MT, r), P in boxes.items():
        if MT == 1: continue
        if all((r - red(u[i], q ** vq(MT, q))) % q ** vq(MT, q) == 0 for i, q in enumerate((11, 13))):
            o = ok_family(f, P); assert o and r in o[2]
            hit.append((f, MT, P))
    print(pt, 'contained in', len(hit), 'boxes', hit[:5])
