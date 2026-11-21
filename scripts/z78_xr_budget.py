"""z78 cross-review (Opus): independent re-evaluation of the per-prime ledger.

(1) Own re-implementation of the z78_deep step chain (P5 step on the depth-2 set,
    i.e. corrected order), using the author's integer tables as inputs and the
    inherited SE/ZL `bound` (libm-dependent rows) unchanged.
(2) Variant with the EXACT depth-3 union (L1,P3,Q3,P5) from z78_xr_exact.c, for
    the primes whose data/z78/xreview/exact_<r>.txt exists.
Every comparison exact rational.  Run from root: PYTHONPATH=scripts ... z78_xr_budget.py
"""
import re
from pathlib import Path
from fractions import Fraction as F
from z77_combine import L, bound, P, Q, ppm
from z78_combine import zbudget, shiftcap, p5, q3
from z76_lift import ceildiv
import z78_deep as D
from z78_pack import packed

def higherP(r, lv):
    """Loss from P_K, K>=7, starting from a lower bound lv on the mass of an
    inverse-stable union of depth-3 cylinders.  Returns (loss, final lv)."""
    loss = F(0)
    for k in range(7, 801, 2):
        n = r**k; b = n.bit_length()
        if b > 800: break
        Dp = (k+1)//2; W = r**Dp
        old = F(bound(P, n), W) if b >= 48 else F(1)
        if lv <= 0:
            loss += old; lv -= old; continue
        sp = []
        if b in D.layers:
            cut, v = D.layers[b]
            for i, c in enumerate(v):
                E = 1 << (cut+i); s = packed(1 << b, cut+i)
                if k == 7 and r in D.p7 and cut+i < len(D.p7[r]): s = min(s, D.p7[r][cut+i])
                sp.append((E, s, c))
        for E, s, c in D.local.get((r, k), []):
            j = E.bit_length()-1; assert E == 1 << j
            if k == 7 and r in D.p7 and j < len(D.p7[r]): s = min(s, D.p7[r][j])
            sp.append((E, s, c))
        best = lv-old
        for E, s, c in sp:
            T = (n//E+1)//2; per = 2*ceildiv(T, W//r)
            best = max(best, lv-F(s+c, W), lv*(1-F(min(per, r), r))-F(s, W))
        x = max(F(0), best); loss += lv-x; lv = x
    return loss, lv

def ledger(r):
    z = zbudget(r)  # [L1, P3, Q3, P5, P>=7 (replaced), Q>=5, tails]
    half = F(r-1, 2*r)
    q3b = z[2]
    if r in D.qrows: q3b = min(q3b, F(D.qrows[r]+q3[r][0]+2*q3[r][3], r**3))
    if r in D.qsleft: q3b = min(q3b, F(D.qsleft[r]+D.qshit[r]+q3[r][0]+2*q3[r][3], r**3))
    A2 = half-z[0]-z[1]                      # union of depth<=2 cylinders
    ss = D.five.get(r, p5[r]); old5 = min(z[3], F(shiftcap(r, 5, ss), r**3))
    best = A2-old5
    for j, s in enumerate(ss):
        T = (r**5//(r*r << j)+1)//2; per = 2*ceildiv(T, r*r)
        best = max(best, A2*(1-F(min(per, r), r))-F(s, r**3))
    after5 = max(F(0), best)
    lv = after5-q3b
    hp, _ = higherP(r, lv)
    parts = [z[0], z[1], q3b, A2-after5, hp, z[5], z[6]]
    return parts, half

def exact_ledger(r, path):
    t = path.read_text().split()
    g = dict(zip(t[0::2], t[1::2]))
    l1, p3m, q3m, p5m = (int(g[k]) for k in ('L1', 'P3marg', 'Q3marg', 'P5marg'))
    assert l1 == L[r][-1]
    z = zbudget(r); half = F(r-1, 2*r)
    ex = [F(l1, r), F(p3m, r*r), F(q3m, r**3), F(p5m, r**3)]
    lv = half-sum(ex)
    hp, _ = higherP(r, lv)
    return ex+[hp, z[5], z[6]], half

if __name__ == '__main__':
    primes = [r for r in L if 211 < r < 7219]
    fails = []; worst = None
    for r in primes:
        parts, half = ledger(r); v = sum(parts)
        if v >= half: fails.append(r)
        elif fails and r > max(fails):
            pass
        if r in (911, 919, 929) or (r > 911 and (worst is None or v-half > worst[0])):
            if r > 911 and (worst is None or v-half > worst[0]): worst = (v-half, r, parts)
        if r in (911, 919, 929):
            print('own-ledger', r, 'total_ppm', ppm(v), 'parts_ppm', *[ppm(x) for x in parts],
                  'margin_ppm', float((half-v)*10**6))
    print('own-ledger failures (211<r<7219):', len(fails), 'largest', max(fails))
    print('own-ledger tightest prime >911:', worst[1], 'margin_ppm', float(-worst[0]*10**6))
    for pth in sorted(Path('data/z78/xreview').glob('exact_*.txt')):
        r = int(re.findall(r'\d+', pth.name)[0]); parts, half = exact_ledger(r, pth); v = sum(parts)
        print('exact-depth3-ledger', r, 'total_ppm', ppm(v), 'parts_ppm', *[ppm(x) for x in parts],
              'pass' if v < half else 'FAIL', 'margin_ppm', float((half-v)*10**6))
