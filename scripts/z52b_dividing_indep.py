"""Independence test for the residue model (lane dividing, z52b): compare observed survivor fraction delta(X)
with the product over families of (1 - marginal hit rate), marginals measured on the same sample."""
import numpy as np, sys
from sympy import divisors, primerange
X_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
NS = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
rng = np.random.default_rng(2)
N = 840 * rng.integers(2**50, 2**51, size=NS * 3, dtype=np.int64) + rng.choice([1, 121, 169, 289, 361, 529], size=NS * 3)
for q in primerange(11, 200):
    N = N[N % q != 0]
N = N[:NS]
fams = []
for a in range(1, X_MAX + 1):
    for d in range(1, X_MAX // a + 1):
        fams.append((a * d, 4 * a * d, {(-f) % (4 * a * d) for f in divisors(4 * a * a * d + 1)}))
for a in range(1, X_MAX + 1):
    for b in range(a, X_MAX // a + 1):
        fams.append((a * b, 4 * a * b, {(-e) % (4 * a * b) for e in divisors(a + b)}))
fams.sort(key=lambda t: (t[0], t[1]))
alive = np.ones(len(N), dtype=bool)
logprod = 0.0
cps = [32, 56, 100, 178, 316, 562, 1000, 1778, 3000]
ci = 0
for s, m, res in fams:
    while ci < len(cps) and s > cps[ci]:
        print(f"X={cps[ci]:5d} observed={alive.mean():.3e} independent={np.exp(logprod):.3e} ratio={alive.mean()/np.exp(logprod):.2f}", flush=True)
        ci += 1
    tab = np.zeros(m, dtype=bool); tab[list(res)] = True
    hit = tab[N % m]
    r = hit.mean()
    if r >= 1:
        logprod = -np.inf
    else:
        logprod += np.log1p(-r)
    alive &= ~hit
while ci < len(cps) and cps[ci] <= X_MAX:
    print(f"X={cps[ci]:5d} observed={alive.mean():.3e} independent={np.exp(logprod):.3e} ratio={alive.mean()/np.exp(logprod):.2f}")
    ci += 1
