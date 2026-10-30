"""AP-avoidance density for ES certificate families (lane dividing, wave z52b).
Random 'prime-like' residues N (coprime to small primes, in Mordell's hard classes mod 840) are tested against
Type I families  N ≡ -f (mod 4ad), f | 4a^2 d + 1   and Type II families  N ≡ -e (mod 4ab), e | a+b.
We report the surviving fraction delta(X) after all families with parameter product ≤ X.
This is a CRT/equidistribution model (ES restricted to families of size ≤ X), not a statement about primes."""
import numpy as np, sys
from sympy import divisors, primerange

X_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
NS = int(sys.argv[2]) if len(sys.argv) > 2 else 2_000_000
rng = np.random.default_rng(1)
N = 840 * rng.integers(2**50, 2**51, size=NS * 3, dtype=np.int64) + rng.choice([1, 121, 169, 289, 361, 529], size=NS * 3)
for q in primerange(11, 200):          # make N 'prime-like' w.r.t. small moduli
    N = N[N % q != 0]
N = N[:NS]
n0 = len(N)
fams = []
for a in range(1, X_MAX + 1):
    for d in range(1, X_MAX // a + 1):
        m = 4 * a * d
        res = {(-f) % m for f in divisors(4 * a * a * d + 1)}
        fams.append((a * d, m, res, "I"))
for a in range(1, X_MAX + 1):
    for b in range(a, X_MAX // a + 1):
        m = 4 * a * b
        res = {(-e) % m for e in divisors(a + b)}
        fams.append((a * b, m, res, "II"))
fams.sort(key=lambda t: (t[0], t[1]))
checkpoints = sorted({int(round(10 ** (k / 4))) for k in range(4, 4 * len(str(X_MAX)) + 1)} | {X_MAX})
checkpoints = [c for c in checkpoints if c <= X_MAX]
ci = 0
print(f"samples {n0}; families {len(fams)}")
for size, m, res, typ in fams:
    while ci < len(checkpoints) and size > checkpoints[ci]:
        print(f"X={checkpoints[ci]:6d} survivors={len(N):8d} delta={len(N)/n0:.3e}", flush=True)
        ci += 1
    if len(N) == 0:
        break
    tab = np.zeros(m, dtype=bool)
    tab[list(res)] = True
    N = N[~tab[N % m]]
while ci < len(checkpoints):
    print(f"X={checkpoints[ci]:6d} survivors={len(N):8d} delta={len(N)/n0:.3e}")
    ci += 1
