"""O94: brute-force checks for EXCEPTIONAL_MN.md.
(1) Lemma 1.1 identity m/n = 1/(suw)+1/(nsvw)+1/(nuvw) on random atoms (exact Fractions).
(2) Lemma 1.3 distinct projections mod l at fixed l (toy parameters without the H floor
    replaced by the needed inequality muv > K and z^2 < l)."""
import random, math
from fractions import Fraction
from sympy import isprime, divisors
random.seed(94)
bad = 0; cnt = 0
for _ in range(3000):
    m = random.randint(4, 60)
    k = random.randint(1, 50)
    if math.gcd(k, m) != 1: continue
    for l in range(random.randint(10, 10**5), 10**6):
        if (k * l + 1) % m == 0 and isprime(l): break
    A = (k * l + 1) // m
    ds = divisors(A)
    u = random.choice(ds); v = random.choice(divisors(A // u)); w = A // (u * v)
    if math.gcd(u, v) != 1 or math.gcd(u*v, k) != 1: continue
    inv = pow(v, -1, k * l)
    r = (-u * inv) % (k * l)
    for n in (r, r + k*l, r + 7*k*l):
        if n == 0: continue
        s = Fraction(n * v + u, k * l)
        assert s.denominator == 1 and s > 0
        s = int(s)
        lhs = Fraction(m, n); rhs = Fraction(1, s*u*w) + Fraction(1, n*s*v*w) + Fraction(1, n*u*v*w)
        cnt += 1
        if lhs != rhs: bad += 1
print("identity checks", cnt, "failures", bad)
# (2) dedup: for fixed l, atoms (k,u,v) with m*u*v | k*l+1, (u,v)=1, u,v<=z, z^2<l, k<=K<m*u*v
bad2 = 0; tot = 0
for m in (4, 5, 6, 7, 11, 12):
    K = 6
    for l in [p for p in range(1000, 3000) if isprime(p)]:
        z = int(math.isqrt(l - 1))
        seen = {}
        for k in range(1, K + 1):
            if math.gcd(k, m) != 1 or (k*l + 1) % m: continue
            A = (k*l + 1) // m
            for u in divisors(A):
                if u > z: break
                for v in divisors(A // u):
                    if v > z or math.gcd(u, v) != 1 or math.gcd(u*v, k) != 1 or m*u*v <= K: continue
                    cls = (-u * pow(v, -1, l)) % l
                    tot += 1
                    if cls in seen: bad2 += 1
                    seen[cls] = (k, u, v)
print("dedup atoms", tot, "collisions", bad2)
