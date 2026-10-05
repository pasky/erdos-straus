"""O40: test the BDW dual inequality  (1/N) sum_{n<=N} g(n) <= A * E[g^+]  (E over Z/L0)
for g = sum_{d<=D} w_d * E_d(x mod d),  E_d(b) = c(b,d) - N/d  (window profile deviation).
Exact enumeration of Z/L0 when L0 <= 2e6, else Monte Carlo over uniform x in [0,L0) (EVIDENCE).
usage: spw_bdw_dualtest.py wmode N [N ...]      wmode in {one, d, sqrtd}
"""
import sys, random
from math import gcd
import numpy as np

def cnt(b, d, N):
    b %= d
    first = b if b >= 1 else d
    return 0 if first > N else (N - first) // d + 1

def run(N, wmode, samples=400000, seed=1):
    D = N // 2
    L0 = 1
    for d in range(1, D + 1):
        L0 = L0 * d // gcd(L0, d)
    w = {d: {"one": 1.0, "d": float(d), "sqrtd": d ** 0.5}[wmode] for d in range(2, D + 1)}
    E = {d: np.array([cnt(b, d, N) - N / d for b in range(d)]) for d in range(2, D + 1)}
    def g_of(xs):
        tot = np.zeros(len(xs))
        for d in range(2, D + 1):
            tot += w[d] * E[d][xs % d]
        return tot
    win = g_of(np.arange(1, N + 1)).mean()
    if L0 <= 2_000_000:
        gp = np.maximum(g_of(np.arange(L0)), 0).mean(); how = "exact"
    else:
        rng = random.Random(seed)
        xs = np.array([rng.randrange(L0) % (2**62) for _ in range(1)], dtype=np.int64)  # placeholder
        # sample residues exactly: x uniform mod L0 <=> residues mod d consistent; use python ints
        vals = []
        acc = np.zeros(samples)
        xs_big = [rng.randrange(L0) for _ in range(samples)]
        for d in range(2, D + 1):
            r = np.fromiter((x % d for x in xs_big), dtype=np.int64, count=samples)
            acc += w[d] * E[d][r]
        gp = np.maximum(acc, 0).mean(); how = f"MC n={samples}"
    print(f"N={N} w={wmode}: window avg={win:.4f}  E[g+]={gp:.4f}  ratio={win/gp:.4f}  "
          f"(A*={max(cnt(b,d,N)*d/N for d in range(1,D+1) for b in range(d)):.4f}) [{how}]", flush=True)

if __name__ == "__main__":
    wmode = sys.argv[1]
    for N in map(int, sys.argv[2:]):
        run(N, wmode)
