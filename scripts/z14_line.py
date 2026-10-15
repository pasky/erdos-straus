# z14_line.py — coverage of an l-line through a point: mu_l = c varies (c mod l^A), all other coordinates fixed to `base`.
# Classes: D_q, II2 (a,d,q) and I3 (c,d,q) with PRIME f = q <= QMAX (4ad, 4cd <= AMAX), and the z14_win windows.
# For a class with period P = l^a P' (l ∤ P') the restriction to the line depends on c mod l^a only.
# Usage: PYTHONPATH=scripts uv run python scripts/z14_line.py c0 k l A base QMAX AMAX
import sys
from math import gcd
from sympy import primerange, n_order, factorint
from sympy.ntheory.modular import crt
from z14_win import make_windows, window_period, fires
c0, k, l, A, base, QMAX, AMAX = map(int, sys.argv[1:8])
LA = l ** A
cov = [None] * LA


def mu_mod(P, c):
    """the line point's residue mod P (l-part from c, rest = base)."""
    a = 0; Pp = P
    while Pp % l == 0: Pp //= l; a += 1
    s, _ = crt([l ** a, Pp], [c % l ** a, base % Pp]) if Pp > 1 else (c % l ** a, 0)
    return int(s), a


def mark(P, test, name):
    a = 0; Pp = P
    while Pp % l == 0: Pp //= l; a += 1
    if a > A: return
    for c0_ in range(l ** a):
        s, _ = mu_mod(P, c0_)
        if test(s + P * 1000):
            for c in range(c0_, LA, l ** a):
                if cov[c] is None: cov[c] = (name, P)


pairs2 = [(a, d) for a in range(1, AMAX // 4 + 1) for d in range(1, AMAX // (4 * a) + 1)]
for q in primerange(3, QMAX):
    if c0 % q == 0: continue
    o = n_order(4, q)
    if l not in factorint(o): continue
    def nq(s): return (c0 * pow(4, s, q) + k) % q
    if k % q: mark(o, lambda s: nq(s) == 0, 'D%d' % q)
    if q % 4 == 3:
        R2 = {(-4 * a * a * d) % q for a, d in pairs2 if (q + 1) % (4 * a * d) == 0}
        if R2: mark(o, lambda s: nq(s) in R2, 'II2:%d' % q)
W = make_windows(c0, k, 14, 10 ** 8, WMAX=10, T1MAX=40)
for w in W:
    P = window_period(w)
    mark(P, lambda s: fires(w, s, c0, k), 'W%d' % w['m'])
unc = [c for c in range(LA) if cov[c] is None]
print('line l=%d base=%d: uncovered %d / %d residues mod %d^%d' % (l, base, len(unc), LA, l, A), unc[:20])
