"""O172 KUDLA_ES §2: the Kudla-support (genus-level) majorant of the Type II slice count.

For a slice (c,d) and odd n put N = 1 + 4c^2 d n. For each divisor f | N (f' = N/f) let T'_f = [[f,1],[1,f']] and
Diff_f = Ram_fin((-f, -f(ff'-1))) (Hilbert symbols, computed directly).
  ES_{c,d}(n) = #{f | N : f = -1 (mod 4cd)}                          (Type II certificates of the slice, ordered f)
  G_{c,d}(n)  = #{f | N : Diff_f subset of Odd(n)},  Odd(n) = {l : v_l(n) odd}   (Kudla-supported "at n")
Claims checked: ES <= G termwise (Thm 1.4), G = 0 at odd squares (oddness of Diff), and the ratio ES/G at primes.
Run: PYTHONPATH=scripts uv run python scripts/kud_genus_majorant.py PMAX CDMAX
"""
import sys
from math import isqrt
from collections import Counter
from sympy import factorint, divisors, primerange
from geo_common import hilbert

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
CD = int(sys.argv[2]) if len(sys.argv) > 2 else 12


def ram_fin(A, B):
    ps = set(factorint(abs(A))) | set(factorint(abs(B))) | {2}
    return frozenset(q for q in ps if hilbert(A, B, q) == -1)


def slice_counts(n, c, d):
    N = 1 + 4 * c * c * d * n
    odd = {l for l, v in factorint(n).items() if v % 2}
    es = g = viol = 0
    for f in divisors(N):
        D = ram_fin(-f, -f * (N - 1))
        inG = D <= odd
        isES = (f + 1) % (4 * c * d) == 0
        g += inG
        es += isES
        viol += (isES and not inG)
    return es, g, viol


slices = [(c, d) for c in range(1, CD + 1) for d in range(1, CD + 1) if c * d <= CD]
tot = Counter()
for p in primerange(5, PMAX):
    for c, d in slices:
        es, g, v = slice_counts(p, c, d)
        tot['ES primes'] += es; tot['G primes'] += g; tot['viol'] += v
        tot['slices(p) with G>0'] += (g > 0); tot['slices(p) with ES>0'] += (es > 0); tot['slices(p)'] += 1
for m in range(3, isqrt(PMAX * 20) + 1, 2):
    for c, d in slices:
        es, g, v = slice_counts(m * m, c, d)
        tot['ES squares'] += es; tot['G squares'] += g; tot['viol'] += v
print(f"primes 5..{PMAX}, odd squares up to {PMAX*20}, slices c*d <= {CD} ({len(slices)})")
print(dict(tot))
