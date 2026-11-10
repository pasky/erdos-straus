# z70 LOOSE item 4, follow-up diagnostic: is the reduction of the negative-Pell solution (T, U) modulo small odd primes q
# uniform on the conic T^2 - p U^2 = -1 (mod q)?  (For the small shared drift of the controls against the local null.)
# Primes p = 1 (mod 8) in [P0, P1]; per (q, p mod q): chi-square of the observed (T mod q, U mod q) vs uniform on the conic.
import sys
from collections import Counter, defaultdict
sys.path.insert(0, 'scripts')
from z70_loose_pell import pell_mod
from sympy import primerange
from scipy.stats import chi2
P0, P1 = int(sys.argv[1]), int(sys.argv[2])
QS = [3, 5, 7, 11, 13]
M = 1
for q in QS: M *= q
obs = {q: defaultdict(Counter) for q in QS}
n = 0
for p in primerange(P0, P1):
    if p % 8 != 1: continue
    T, U = pell_mod(p, M); n += 1
    for q in QS: obs[q][p % q][(T % q, U % q)] += 1
print(f"primes p = 1 (mod 8) in [{P0}, {P1}]: {n}")
for q in QS:
    for r in sorted(obs[q]):
        if r == 0: continue
        conic = [(t, u) for t in range(q) for u in range(q) if (t * t - r * u * u + 1) % q == 0]
        c = obs[q][r]; N = sum(c.values())
        off = sum(v for k, v in c.items() if k not in conic)
        E = N / len(conic)
        X2 = sum((c.get(k, 0) - E) ** 2 / E for k in conic)
        df = len(conic) - 1
        print(f"q={q:2d} p mod q={r:2d} ((p/q)={'+' if pow(r, (q-1)//2, q) == 1 else '-'}): N={N:6d} conic points={len(conic):3d} "
              f"off-conic={off} chi2={X2:8.1f} df={df} p-value={chi2.sf(X2, df):.3g}")
