"""R107: compare the box sets of O107's run (m13e_es + m13e_inv, /tmp/o107/run*/inv_N.pkl) with the
independent R95 pipeline (review_m13b_enum.py: plain-Python divisor ES enumeration + reviewer-derived
inversion + literal ET classes) at chosen levels N.  Also reports whether x** = (2,15) / x* = (2,2) lie in
any independent box.  usage: review_m13e_cmp.py RUNDIR N1 N2 ..."""
import sys, pickle, os
sys.path.insert(0, os.path.dirname(__file__))
from review_m13b_enum import es, invert

def inbox(MT, r, u11, u13):
    for q, u in ((11, u11), (13, u13)):
        k = 0; t = MT
        while t % q == 0: t //= q; k += 1
        if (r - u) % q**k: return False
    return True

import glob
rd = sys.argv[1]
UA, UB = set(), set()
for N in map(int, sys.argv[2:]):
    S = es(N)
    raw = set()
    for fn in glob.glob(f'{rd}/es_{N}_*.txt'):
        for line in open(fn):
            if not line.startswith('#'): raw.add(tuple(map(int, line.split())))
    assert raw == {(x, y) for x, y, z in S}, ('ES solution sets differ', N)
    B = set()
    for s in S:
        for fam, P, (M, MT, rs) in invert(N, s):
            for r in rs: B.add((fam, MT, r))
    A = pickle.load(open(f'{rd}/inv_{N}.pkl', 'rb'))
    Ab = set(A['boxes']); UA |= Ab; UB |= B
    hit = lambda bs, u: sorted(b for b in bs if inbox(b[1], b[2], *u))
    print(f"N={N}: ES indep {len(S)} vs author {A['nsol']}; boxes indep {len(B)} author {len(Ab)}; "
          f"indep-author {len(B - Ab)} author-indep {len(Ab - B)}; x** hits indep {hit(B, (2, 15))}; "
          f"x* hits indep {hit(B, (2, 2))}", flush=True)
    for b in sorted(B ^ Ab)[:5]: print('  DIFF', b, b in B)
print(f"UNION over listed levels: indep {len(UB)} author {len(UA)}; indep-author {len(UB - UA)}; author-indep {len(UA - UB)}")
for b in sorted(UA - UB)[:10]: print('  author-only', b)
# author-only boxes: genuine?  canonical ES level of the stored datum (own formulas, review_m13e_parity)
from review_m13b_enum import ok_family
from review_m13e_parity import es_level_and_check
from collections import Counter
P_of = {}
for N in map(int, sys.argv[2:]):
    for k, P in pickle.load(open(f'{rd}/inv_{N}.pkl', 'rb'))['boxes'].items(): P_of.setdefault(k, P)
levels = set(map(int, sys.argv[2:])); cn = Counter()
for b in sorted(UA - UB):
    fam, MT, r = b; P = P_of[b]; ok = ok_family(fam, P)
    assert ok and ok[1] == MT and r in ok[2], ('author box not literal', b, P, ok)
    Nc = es_level_and_check(fam, P)
    cn['canonical level in list (BAD)' if Nc in levels else 'canonical level outside list'] += 1
    if Nc in levels: print('  MISSED BY INDEP?', b, P, Nc)
print('author-only boxes (all literal ET boxes):', dict(cn))
