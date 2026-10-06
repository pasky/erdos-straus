"""R86 from-scratch replay of Thm 5.1 certificates using the R86 family solver (not the author's
or the earlier reviewer's code). Targets: residues t mod L, (t,L)=1, t mod 840 a square class,
(t/13)=-1 [main], plus (t/11)=+1 [np]."""
import json, sys
from math import gcd
from fractions import Fraction as Fr
sys.path.insert(0, 'scripts')
from review_r86_families import sol, in_class, admissible

def leg(a, p): a %= p; return 0 if a == 0 else (1 if pow(a, (p-1)//2, p) == 1 else -1)
SQ = {1, 121, 169, 289, 361, 529}
for fn in ['data/mordell/cert_r13_np_240240.json', 'data/mordell/cert_r13_main_720720.json']:
    d = json.load(open(fn)); L = d['L']; np_ = d['variant'] == 'np'
    cls = [(c[0], tuple(c[1])) for c in d['classes']]
    for fam, k in cls:
        assert admissible(fam, k), (fam, k)
        M = 4*k[0]*k[1]*k[2] if fam in ('I2', 'I3', 'II3') else (k[2] if fam == 'II2' else 4*k[0]*k[1])
        assert L % M == 0, ('modulus does not divide L', fam, k, M)
    unc = []; tg = 0
    for t in range(1, L):
        if gcd(t, L) != 1 or t % 840 not in SQ or leg(t, 13) != -1: continue
        if np_ and leg(t, 11) != 1: continue
        tg += 1
        hit = [c for c in cls if in_class(c[0], c[1], t)]
        if not hit: unc.append(t); continue
        co, xyz = sol(hit[0][0], hit[0][1], t)
        assert all(v.denominator == 1 and v > 0 for v in co) and Fr(4, t) == sum(1/Fr(v) for v in xyz)
    print(fn, "targets", tg, "uncovered", unc, "== listed:", sorted(unc) == sorted(d['exceptions']))
