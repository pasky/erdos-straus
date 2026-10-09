"""R102A from-scratch checks for EXCEPTIONAL_MN2 §1 (small cases).

(1) Bonferroni: Q_r(h) = sum_{j<=r} (-1)^j C(h,j) satisfies 1[h=0] <= Q_r <= 1[h=0] + C(h,r+1), r even.
(2) e_{j}(p_1..p_n) <= (sum p)^j / j!.
(3) MN Lemma 1.1 identity m/n = 1/(suw)+1/(nsvw)+1/(nuvw) when kl+1 = m u v w, n v = -u (mod kl).
(4) Toy atom family: at fixed prime l, distinct atoms (k,u,v) with (k,m)=1, k<=K, H<u,v<=z,
    (u,v)=(uv,k)=1, m u v | k l + 1 have distinct classes -u/v mod l whenever K < H^2 and z^2 < l.
Exit status 1 on any failure.
"""
import random
import sys
from fractions import Fraction
from itertools import combinations
from math import comb, gcd, prod

fail = 0

for r in range(0, 12, 2):
    for h in range(0, 40):
        q = sum((-1) ** j * comb(h, j) for j in range(r + 1))
        lo = 1 if h == 0 else 0
        if not (lo <= q <= lo + comb(h, r + 1)):
            print("Bonferroni fail", r, h, q)
            fail += 1

rng = random.Random(1)
for _ in range(300):
    n = rng.randint(1, 9)
    p = [rng.random() for _ in range(n)]
    for j in range(1, n + 1):
        e = sum(prod(c) for c in combinations(p, j))
        bound = sum(p) ** j / prod(range(1, j + 1))
        if e > bound * (1 + 1e-12):
            print("e_j fail", p, j)
            fail += 1


def isprime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def divisors(x):
    return [d for d in range(1, x + 1) if x % d == 0]


cnt = 0
for _ in range(3000):
    m = rng.randint(4, 40)
    k = rng.randint(1, 30)
    l = rng.choice([q for q in range(2, 400) if isprime(q)])
    M = k * l + 1
    if M % m:
        continue
    R = M // m
    ds = divisors(R)
    u = rng.choice(ds)
    v = rng.choice(divisors(R // u))
    w = R // (u * v)
    if gcd(u * v, k * l) != 1:
        print("unit fail")
        fail += 1
        continue
    a = (-u * pow(v, -1, k * l)) % (k * l)
    for n in [a + k * l * j for j in range(0, 4)]:
        if n == 0:
            continue
        s, rem = divmod(n * v + u, k * l)
        assert rem == 0
        if Fraction(m, n) != Fraction(1, s * u * w) + Fraction(1, n * s * v * w) + Fraction(1, n * u * v * w):
            print("identity fail", m, k, l, u, v, w, n)
            fail += 1
        cnt += 1
print("identity instances", cnt)

# (4) toy distinctness (parameters scaled down, keeping K < H^2, z^2 < l)
coll = 0
tested = 0
for m in [4, 5, 6, 7, 12, 30]:
    K, H, z = 6, 3, 30
    for l in [q for q in range(z * z + 1, z * z + 4000) if isprime(q)]:
        seen = {}
        for k in range(1, K + 1):
            if gcd(k, m) != 1 or (k * l + 1) % m:
                continue
            N = (k * l + 1) // m
            for u in range(H + 1, z + 1):
                if N % u:
                    continue
                for v in range(H + 1, z + 1):
                    if (N // u) % v or gcd(u, v) != 1 or gcd(u * v, k) != 1:
                        continue
                    cls = (-u * pow(v, -1, l)) % l
                    tested += 1
                    if cls == 0 or cls in seen:
                        coll += 1
                        print("collision", m, l, (k, u, v), seen.get(cls))
                    seen[cls] = (k, u, v)
print("toy atoms tested", tested, "collisions", coll)
fail += coll
print("FAILURES", fail)
sys.exit(1 if fail else 0)
