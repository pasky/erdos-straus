"""R73 from-scratch numeric checks of LS7 Prop 4.1 and Prop 5.1 (exact H* by brute force).

Prop 4.1: P set of primes, k prime not in P, r prime > max P, j with j ≡ −(P̄ r)^{−1} (mod 4k);
M = P̄ r j.  Check: M ≡ 3 (4); −1/k mod M ∈ ℛ(M) (= −4D, D = A/k | A²); residue −1/k at every p∈P;
H*(class) = k whenever k < sqrt(M/2).
Prop 5.1: ℓ < p < q primes; class x ≡ −(4ℓ+pq) (mod 4pqℓ); rough part mod pqℓ.
Check: x ≡ −4ℓ (mod pq), x ≡ −pq (mod ℓ); H*(x mod pqℓ) ≥ pq/(4ℓ+1); residue mod p = −4ℓ.
"""
import random
from math import gcd, isqrt
import numpy as np
from sympy import primerange, isprime, nextprime


def hstar(b, G):
    s = np.arange(1, G + 1, dtype=np.int64)
    r = (-b * s) % G
    h = np.maximum(r, s)[np.gcd(s, G) == 1]
    return int(h.min())


random.seed(73)
bad = 0
# ---- Prop 4.1
n41 = 0
for trial in range(300):
    m = random.randint(1, 3)
    P = sorted(random.sample(list(primerange(7, 60)), m))
    Pbar = int(np.prod(P))
    y = max(P)
    k = random.choice([q for q in primerange(3, 40) if q not in P])
    r = nextprime(y + random.randint(0, 40))
    if r == k:
        continue
    c = (-pow(Pbar * r % (4 * k), -1, 4 * k)) % (4 * k)
    j = c + 4 * k * random.randint(0, 3)
    if j == 0:
        j = 4 * k
    if gcd(j, 2) == 0:
        continue
    M = Pbar * r * j
    if M > 3_000_000:
        continue
    A = (M + 1) // 4
    ok = (M % 4 == 3) and A % k == 0
    b = (-pow(k, -1, M)) % M
    D = A // k
    ok = ok and ((A * A) % D == 0) and ((-4 * D) % M == b)
    ok = ok and all(b % p == (-pow(k, -1, p)) % p for p in P)
    if k * k * 2 < M:
        hs = hstar(b, M)
        ok = ok and hs == k
    n41 += 1
    if not ok:
        bad += 1
        print("Prop4.1 FAIL", P, k, r, j, M)
print("Prop 4.1 instances:", n41)

# ---- Prop 5.1
n51 = 0
minratio = 1e9
for l in primerange(3, 30):
    for p in primerange(l + 1, 60):
        for q in primerange(p + 1, 90):
            G = 4 * p * q * l
            x = (-(4 * l + p * q)) % G
            Gr = p * q * l
            b = x % Gr
            ok = b % (p * q) == (-4 * l) % (p * q) and b % l == (-p * q) % l and b % p == (-4 * l) % p
            hs = hstar(b, Gr)
            ok = ok and hs * (4 * l + 1) >= p * q
            minratio = min(minratio, hs * (4 * l + 1) / (p * q))
            n51 += 1
            if not ok:
                bad += 1
                print("Prop5.1 FAIL", l, p, q, hs)
print("Prop 5.1 instances:", n51, "min H*(4l+1)/(pq) =", round(minratio, 4))
print("failures:", bad)
