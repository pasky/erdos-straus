"""O94 toy check v2 (EVIDENCE only; R94A repair D5): deduplicated fibre mass with an
m-independent floor u,v in (F, z] and K >= m^2.  Counts DISTINCT classes mod l
(mu_c = sum_l f_c(l)/l with f_c(l) = #distinct (-u/v mod l) over active atoms), checks that
no two active atoms at the same l collide (Lemma 1.3; m*u*v > m*F^2 > K, z^2 < l), and prints
m*mu and phi(m)*mu averaged over reduced c."""
import sys, math, random
import numpy as np
from sympy import primerange, totient
x = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**6
K = int(sys.argv[2]) if len(sys.argv) > 2 else 170
F = int(sys.argv[3]) if len(sys.argv) > 3 else 6
z = int(sys.argv[4]) if len(sys.argv) > 4 else 60
nc = int(sys.argv[5]) if len(sys.argv) > 5 else 2
assert z * z < x and F * F * 4 > K
P = np.array(list(primerange(x + 1, 2 * x + 1)), dtype=np.int64)
random.seed(2)
cs = []
while len(cs) < nc:
    c = random.randrange(1, 10**12)
    if all(c % p for p in primerange(2, K + 1)): cs.append(c)
print(f"x={x} K={K} F={F} z={z} #primes={len(P)} c={cs}")
coll = 0
for m in range(4, 14):
    assert K >= m * m
    tot = 0.0
    for c in cs:
        seen = {}
        for k in range(1, K + 1):
            if math.gcd(k, m) != 1: continue
            for v in range(F + 1, z + 1):
                if math.gcd(v, k) != 1: continue
                u0 = (-c * v) % k
                u = u0 if u0 > F else u0 + k * ((F - u0) // k + 1)
                for u in range(u, z + 1, k):
                    if math.gcd(u, v) != 1: continue
                    q = m * u * v
                    r = (-pow(k, -1, q)) % q
                    for idx in np.nonzero(P % q == r)[0]:
                        key = (int(idx), u, v)   # class -u/v mod l determined by (u,v) as z^2<l
                        if key in seen: coll += 1
                        else: seen[key] = k
        tot += sum(1.0 / P[i] for (i, _, _) in seen)
    tot /= len(cs)
    ph = int(totient(m))
    print(f"m={m:3d} mu={tot:.5f} m*mu={m*tot:.3f} phi(m)*mu={ph*tot:.3f}", flush=True)
print("collisions", coll); sys.exit(1 if coll else 0)
