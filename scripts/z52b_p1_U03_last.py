"""z52b Pass-1 U03 last quick checks: Z1447 (exists C<=100 with prime factor = -1 mod 4C), Z2970 (Legendre
relations among exact (star)-failures), Z2038 (union over k of y=kx solvability), Z2459 (multiplicative energy of
A_p={4Cp+1: C<=100} vs random set of same size)."""
import numpy as np, json, random
from math import gcd
d = np.load("data/z52b/pass1/U03/feat_P100000_K100.npz")
pr = d["primes"]; hm1 = d["hm1"]; R = d["R"].astype(np.int64)
any_hm1 = hm1.any(1)
print("Z1447: fraction of p<=1e5 (1 mod 4) with some C<=100 having a prime factor = -1 mod 4C:", round(float(any_hm1.mean()), 4))
print("       first C with such prime: median", int(np.median([np.argmax(hm1[i]) + 1 for i in np.nonzero(any_hm1)[0]])))
fails = [409, 577, 5569, 9601, 23929, 83449]
def leg(a, p): return pow(a % p, (p - 1) // 2, p) if a % p else 0
for p in fails:
    print("Z2970 p=%d: (q/p) for other fails q:" % p, [(q, (1 if leg(q, p) == 1 else -1)) for q in fails if q != p and leg(q, p) != 0])
# Z2038 union over k
ex = json.load(open("data/z52b/pass1/U03/exact_results.json"))["Z2038"]
print("Z2038: per-k solvable counts (p<=2e4 primes in exact_100k.log run used p<=1e5 list):", {k: v[0] for k, v in ex.items()}, "of", list(ex.values())[0][1])
# Z2459 energy
def energy(A):
    from collections import Counter
    c = Counter(); A = list(A)
    for i in range(len(A)):
        for j in range(len(A)):
            c[A[i] * A[j]] += 1
    return sum(v * v for v in c.values())
rng = random.Random(1); rel = []
for p in pr[::40]:
    p = int(p); A = [4 * C * p + 1 for C in range(1, 101)]
    lo, hi = min(A), max(A); B = sorted(rng.sample(range(lo, hi), 100))
    rel.append(energy(A) / energy(B))
print("Z2459: E(A_p)/E(random same-size, same range) over p sample: median %.3f, mean %.3f, n=%d" % (np.median(rel), np.mean(rel), len(rel)))
