"""Cross-review (Opus): re-evaluate z78_deep's budget with the P5 per-parent
step applied to a set that really is a union of depth-2 cylinders.

z78_deep evaluates step(3, lv, ...) with lv = nonsq - L1 - P3 - Q3.  After Q3
(depth-3 boxes) the alive set is NOT a union of depth-2 parents, so the
per-parent bound "kills <= 2 ceil(T/r^2) children per alive parent" does not
imply loss <= lv * 2ceil/r.  The valid order is: L1, P3 (depth <= 2), then the
P5 step on A' = nonsq - L1 - P3, then subtract Q3 en bloc.
Run from repo root: PYTHONPATH=scripts uv run --offline --no-project python -B scripts/z78_xr_p5order.py
"""
import z78_deep as Z
from z78_deep import *

def budget_fixed(r):
    parts = zbudget(r)
    if r in qrows: parts[2] = min(parts[2], F(qrows[r]+q3[r][0]+2*q3[r][3], r**3))
    if r in qsleft: parts[2] = min(parts[2], F(qsleft[r]+qshit[r]+q3[r][0]+2*q3[r][3], r**3))
    def step(depth, lower, old, k, splits):
        W = r**depth; best = lower-old; N = r**k
        for E, s, c in splits:
            T = (N//E+1)//2; per = 2*ceildiv(T, W//r)
            best = max(best, lower-F(s+c, W), lower*(1-F(min(per, r), r))-F(s, W))
        return max(F(0), best)
    if r in small:
        return None
    A1 = F(r-1, 2*r)-parts[0]-parts[1]          # union of depth<=2 cylinders
    old = parts[3]; ss = p5[r]
    if r in five:
        ss = five[r]; old = min(old, F(shiftcap(r, 5, ss), r**3))
    x = step(3, A1, old, 5, [(r*r << j, s, r**3) for j, s in enumerate(ss)]) if A1 >= 0 else A1-old
    parts[3] = A1-x
    lv = x-parts[2]                              # then Q3 en bloc
    ps = F(0)
    for k in range(7, 801, 2):
        n = r**k; b = n.bit_length()
        if b > 800: break
        D = (k+1)//2; W = r**D
        old = F(bound(P, n), W) if b >= 48 else F(1)
        if lv <= 0: ps += old; lv -= old; continue
        splits = []
        if b in layers:
            cut, v = layers[b]; splits = [(1 << (cut+i), packed(1 << b, cut+i), c) for i, c in enumerate(v)]
        splits += local.get((r, k), [])
        if k == 7 and r in p7:
            splits = [(E, min(s, p7[r][E.bit_length()-1]) if E.bit_length()-1 < len(p7[r]) else s, c) for E, s, c in splits]
        x = step(D, lv, old, k, splits); ps += lv-x; lv = x
    parts[4] = ps
    return parts

if __name__ == '__main__':
    primes = [r for r in L if 211 < r < 7219]
    fail = []; rows_ = []
    for r in primes:
        a = budget2(r); b = budget_fixed(r)
        va, vb = sum(a), sum(b); half = F(r-1, 2*r)
        if vb >= half: fail.append(r)
        rows_.append((r, va, vb, a, b))
    print('corrected-order failures', *fail)
    mx = max(fail); ok = [t for t in rows_ if t[0] > mx]
    print('corrected: last failure', mx, 'first pass after', min(t[0] for t in ok),
          'max ppm after', max(ppm(t[2]) for t in ok))
    for r, va, vb, a, b in rows_:
        if r in (907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997) or r == mx:
            half = F(r-1, 2*r)
            print(r, 'nonsq_ppm_floor', (half*10**6).numerator//(half*10**6).denominator,
                  'author', ppm(va), *[ppm(x) for x in a], '| corrected', ppm(vb), *[ppm(x) for x in b],
                  '| margin_corr_exact', float((half-vb)*10**6))
