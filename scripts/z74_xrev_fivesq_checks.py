"""Cross-lab (Opus) review checks for LOGIC_FIVE_SQUARE_BCM.md.

Finite sanity checks of the elementary arithmetic the note rests on:
 1. Q4 = sum of 4 squares has no primitive zero mod 8 (=> anisotropic over Q_2),
    while Q5 has primitive zeros mod 2^k that lift (explicit vector (sqrt(-7),2,1,1,1)).
 2. Q4 is onto Z/2^k (k<=12), so four squares cover Z_2 (compactness step).
 3. -1 = four squares mod 2^k, and appending 1 gives a primitive isotropic 5-vector.
 4. Hyperbolic-pair formula of §1 over F_l for random isotropic u.
 5. ES bounds x<=3n/4, y<=2nx, z<=nxy (sorted) on all solutions for small n.
 6. b + h(b^2+1) > 0 for all integers b, h>=1 (positivity used to renew the S-hypothesis).
Run: ulimit -v 6000000; timeout 1800 uv run --offline --no-project python scripts/z74_xrev_fivesq_checks.py
"""
import itertools, random
from fractions import Fraction

def check1():
    bad = [v for v in itertools.product(range(8), repeat=4)
           if any(x % 2 for x in v) and sum(x * x for x in v) % 8 == 0]
    assert not bad, bad[:5]
    # Q5 primitive zero: lift sqrt(-7) in Z_2 to precision 2^K
    K = 60
    M = 1 << K
    r = 1  # r^2 = -7 mod 2^k, Hensel for squares at 2 (adjust by 2^(k-1))
    for k in range(3, K):
        if (r * r + 7) % (1 << (k + 1)):
            r += 1 << (k - 1)
    assert (r * r + 7) % M == 0
    assert (r * r + 4 + 1 + 1 + 1) % M == 0
    return "Q4 no primitive zero mod 8; Q5 zero (sqrt(-7),2,1,1,1) lifts to 2^60"

def check2():
    for k in range(1, 13):
        m = 1 << k
        sq = {(x * x) % m for x in range(m)}
        two = {(a + b) % m for a in sq for b in sq}
        four = {(a + b) % m for a in two for b in two}
        assert len(four) == m, k
    return "Q4 onto Z/2^k, k<=12"

def check3():
    for k in range(3, 13):
        m = 1 << k
        root = {}
        for x in range(m):
            root.setdefault(x * x % m, x)
        found = None
        for v in itertools.product(range(m), repeat=3):
            t = (-1 - sum(x * x for x in v)) % m
            if t in root:
                found = v + (root[t],); break
        assert (sum(x * x for x in found) + 1) % m == 0
        assert found is not None, k
        # primitive isotropic 5-vector (v,1): last coordinate odd
    return "-1 = four squares mod 2^k (k<=12); (v,1) primitive isotropic"

def check4(trials=2000):
    primes = [3, 5, 7, 11, 13, 101, 1009]
    for _ in range(trials):
        l = random.choice(primes)
        # random isotropic nonzero u in F_l^5
        while True:
            u = [random.randrange(l) for _ in range(5)]
            if any(u) and sum(x * x for x in u) % l == 0:
                break
        i = next(j for j in range(5) if u[j])
        v = [0] * 5; v[i] = pow(u[i], -1, l)          # u.v = 1
        c = sum(x * x for x in v) * pow(2, -1, l) % l
        v = [(v[j] - c * u[j]) % l for j in range(5)]  # now Q(v)=0, u.v=1
        assert sum(x * x for x in v) % l == 0
        assert sum(a * b for a, b in zip(u, v)) % l == 1
        b = random.randrange(l)
        w = [(u[j] + b * pow(2, -1, l) * v[j]) % l for j in range(5)]
        assert sum(x * x for x in w) % l == b and any(w)
    return f"hyperbolic-pair formula ok ({trials} random trials)"

def check5(N=120):
    cnt = 0
    for n in range(2, N + 1):
        for x in range(1, n + 1):
            num = 4 * x - n
            if num <= 0:
                continue
            # 1/y+1/z = num/(n x), y<=z
            D = n * x
            for y in range(x, 2 * D // num + 1):
                zn = D * y
                zd = num * y - D
                if zd <= 0 or zn % zd:
                    continue
                z = zn // zd
                if z < y:
                    continue
                assert 4 * x * y * z == n * (x * y + y * z + z * x)
                assert 4 * x <= 3 * n and y <= 2 * n * x and z <= n * x * y <= 2 * n ** 4
                cnt += 1
    return f"ES sorted bounds hold on all {cnt} solutions, n<= {N}"

def check6():
    for h in range(1, 40):
        for b in range(-2000, 2001):
            assert b + h * (b * b + 1) > 0
    return "b+h(b^2+1)>0 on test grid (algebraically: (h-1)(b^2+1)+(b^2+b+1))"

if __name__ == "__main__":
    random.seed(74)
    for f in (check1, check2, check3, check4, check5, check6):
        print(f.__name__, "PASS:", f())
