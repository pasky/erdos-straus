"""R68b from-scratch re-implementation of POINTWISE_OMEGA17 §5 toy LP (EVIDENCE check).

Sieve primes 17..71; at each l pick round(frac*l) random nonzero residues ("events").
bit_l(n) = [n mod l in events_l]. Atoms = 2^14 bit configurations (Lemma 5.1).
True measure: primes 71<p<=x.  Information: exact prime counts on every cell of every <=k-set
of bits.  Fake: M_G in [0, cap_G], sum = N.  Minimise M on the all-zero (avoider) atom.
cap_G = #{n<=x in S with config G}, S = n coprime to all primes <= 71 except possibly some
small primes (slack variants), or cap = inf (diffuse).
Usage: review_o17_toylp.py seed x frac k
"""
import itertools, sys, math
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, csr_matrix

seed, x, frac, k = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
rng = np.random.default_rng(seed)
small = [2, 3, 5, 7, 11, 13]
sieve = [p for p in range(17, 72) if all(p % q for q in range(2, p))]
ev = {l: set(rng.choice(np.arange(1, l), size=int(round(frac * l)), replace=False).tolist()) for l in sieve}
R = sum(len(ev[l]) / (l - 1 - len(ev[l])) for l in sieve)

n = np.arange(1, x + 1, dtype=np.int64)
isp = np.ones(x + 1, bool); isp[:2] = False
for p in range(2, int(x ** 0.5) + 1):
    if isp[p]:
        isp[p * p::p] = False
cop_sieve = np.ones(x, bool)
for l in sieve:
    cop_sieve &= (n % l != 0)
cfg = np.zeros(x, np.int64)
for b, l in enumerate(sieve):
    m = np.isin(n % l, list(ev[l]))
    cfg |= (m.astype(np.int64) << b)
primes = isp[1:] & (n > 71)
N = int(primes.sum())
pc = np.bincount(cfg[primes], minlength=1 << 14).astype(float)

def solve(cap):
    nb = len(sieve); nv = 1 << nb
    rows = []; rhs = []
    for a in range(1, k + 1):
        for K in itertools.combinations(range(nb), a):
            mask = sum(1 << b for b in K)
            key = np.arange(nv) & mask
            for pat in range(1 << a):
                pm = sum(((pat >> i) & 1) << b for i, b in enumerate(K))
                rows.append(key == pm); rhs.append(pc[key == pm].sum())
    rows.append(np.ones(nv, bool)); rhs.append(N)
    A = csr_matrix(np.array(rows, dtype=float))
    c = np.zeros(nv); c[0] = 1
    bounds = [(0, None if cap is None else float(cap[g])) for g in range(nv)]
    r = linprog(c, A_eq=A, b_eq=rhs, bounds=bounds, method="highs")
    assert r.status == 0, r.message
    return r.fun

print(f"seed={seed} x={x} frac={frac} k={k} R={R:.3f} N={N} true avoiders={int(pc[0])}")
print(f"  diffuse: {solve(None):.1f}", flush=True)
for j in range(len(small), -1, -1):
    S = cop_sieve.copy()
    for q in small[:j]:
        S &= (n % q != 0)
    S &= ~((n <= 71) & ~primes)  # irrelevant small n
    cap = np.bincount(cfg[S], minlength=1 << 14)
    print(f"  S coprime to first {j} small primes: slack={S.sum()/N:.2f} min avoider mass={solve(cap):.1f}", flush=True)
