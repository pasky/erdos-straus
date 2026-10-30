"""Least certificate-family size for primes in Mordell's hard classes (lane dividing, z52b).
For each prime p ≤ P in classes {1,121,169,289,361,529} mod 840, find the smallest s = ad (Type I: p ≡ -f mod 4ad,
f | 4a^2 d+1) or s = ab (Type II: p ≡ -e mod 4ab, e | a+b) that solves it. Compare max s with the CRT-avoidance
model delta(X) ≈ exp(-c (ln X)^3) from z52b_dividing_avoid.py."""
import numpy as np, sys
from sympy import divisors, primerange

P = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
X_MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
ps = np.array([p for p in primerange(2, P) if p % 840 in (1, 121, 169, 289, 361, 529)], dtype=np.int64)
print("hard primes:", len(ps))
fams = []
for a in range(1, X_MAX + 1):
    for d in range(1, X_MAX // a + 1):
        fams.append((a * d, 4 * a * d, {(-f) % (4 * a * d) for f in divisors(4 * a * a * d + 1)}))
for a in range(1, X_MAX + 1):
    for b in range(a, X_MAX // a + 1):
        fams.append((a * b, 4 * a * b, {(-e) % (4 * a * b) for e in divisors(a + b)}))
fams.sort(key=lambda t: (t[0], t[1]))
alive = ps.copy()
least = {}
for s, m, res in fams:
    if len(alive) == 0:
        break
    tab = np.zeros(m, dtype=bool); tab[list(res)] = True
    hit = tab[alive % m]
    for p in alive[hit][:]:
        least[int(p)] = s
    alive = alive[~hit]
print("unsolved within X_MAX:", alive[:20], len(alive))
vals = np.array([least[int(p)] for p in ps])
for q in (0.5, 0.9, 0.99, 0.999, 1.0):
    print(f"quantile {q}: {np.quantile(vals, q):.0f}")
order = np.argsort(-vals)[:10]
print("hardest primes (p, least s):", [(int(ps[i]), int(vals[i])) for i in order])
# record-setters
rec = 0
for p, v in zip(ps, vals):
    if v > rec:
        rec = v; print(f"record p={p} s={v}")
