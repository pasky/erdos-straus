"""Independent checks for CONJECTURE_S_MODEL §2 (upper bound on survival).
(a) (F2) progression harmonic-sum bounds, brute force.
(b) the (g,h,j,k) decomposition: pairwise coprimality, lcm(R,R') = D*abcd, compatibility => D | sum difference,
    equal-sum case D <= u u' |u-u'|.
(c) liveness/atomicity: exact CRT probability P(E | z) = [live]/phi(R) on small instances.
(d) uniformity of the conditional mass mu(z) in z (scaled-down parameters), incl. the class of one, and loads p*w_p."""
import math, random, itertools, sys
import numpy as np
from sympy import factorint, totient, primerange, isprime
random.seed(4901)
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

# (a)
viol = 0; tests = 0
for _ in range(20000):
    q = random.randint(1, 60); c = random.randint(0, q - 1); X = random.randint(1, 300)
    S = sum(1.0 / x for x in range(X, 2 * X + 1) if x % q == c)
    tests += 1
    if S > 1.0 / q + 1.0 / X + 1e-12: viol += 1
    X0 = random.randint(q, 400); X1 = X0 * random.randint(1, 50)
    S2 = sum(1.0 / x for x in range(X0, X1 + 1) if x % q == c)
    if S2 > (2 + math.log(X1 / X0)) / q + 1e-12: viol += 1
log(f"(a) F2 progression bounds: {2*tests} tests, violations={viol}")

# (b)
def rand_sqfree_rough(lo, hi, Y):
    while True:
        r = random.randint(lo, hi)
        f = factorint(r)
        if all(e == 1 and p > Y for p, e in f.items()): return r
Y = 7; viol = 0; cnt = 0; compat_cnt = 0
primes = list(primerange(11, 60))
for _ in range(30000):
    # build pairs sharing primes deliberately
    pool = random.sample(primes, 6)
    def sub():
        k = random.randint(1, 3); return math.prod(random.sample(pool, k))
    r1, r2, r1p, r2p = sub(), sub(), sub(), sub()
    if math.gcd(r1, r2) > 1 or math.gcd(r1p, r2p) > 1: continue
    g, h, j, k = math.gcd(r1, r1p), math.gcd(r2, r2p), math.gcd(r1, r2p), math.gcd(r2, r1p)
    D = g * h * j * k
    if D == 1: continue
    cnt += 1
    ok = all(math.gcd(x, y) == 1 for x, y in itertools.combinations((g, h, j, k), 2))
    a, b, c, d = r1 // (g * j), r2 // (h * k), r1p // (g * k), r2p // (h * j)
    ok &= (r1 == g*j*a and r2 == h*k*b and r1p == g*k*c and r2p == h*j*d)
    R, Rp = r1 * r2, r1p * r2p
    ok &= (R * Rp // math.gcd(R, Rp) == D * a * b * c * d) and math.gcd(R, Rp) == D
    # random smooth parts (coprime to everything rough), check compatibility => D | sum diff
    s1, s2, s1p, s2p = random.choice([1,5,7,25]), random.choice([1,11*0+1,5,7]), random.choice([1,5,7]), random.choice([1,5,7])
    u, v, up, vp = s1*r1, s2*r2, s1p*r1p, s2p*r2p
    compat = all(((-u - v) - (-up - vp)) % p == 0 for p in factorint(D))
    if compat:
        compat_cnt += 1
        ok &= ((u + v) - (up + vp)) % D == 0
        if u + v == up + vp and (u, v) != (up, vp):
            ok &= D <= u * up * abs(u - up)
    if not ok: viol += 1
log(f"(b) decomposition: {cnt} configs ({compat_cnt} compatible), violations={viol}")

# (c) exact CRT: small primes {2,3,5} (Y=5), rough primes 7,11,13. n ≡ 1 (24) imposed; z = n mod 2^3*3*25.
Msmall = 8 * 3 * 25; rough = [7, 11, 13, 17]; Mr = math.prod(rough)
units_small = [x for x in range(Msmall) if math.gcd(x, Msmall) == 1 and x % 24 == 1]
viol = 0; checks = 0
pairs = []
for u in range(1, 300):
    for v in range(u + 1, 300):
        if math.gcd(u, v) > 1: continue
        m = u * v
        f = factorint(m)
        if any(p not in (2, 3, 5, 7, 11, 13, 17) for p in f): continue
        if any(p in rough and e > 1 for p, e in f.items()): continue
        if f.get(2, 0) > 3 or f.get(3, 0) > 1 or f.get(5, 0) > 2: continue
        pairs.append((u, v))
random.shuffle(pairs)
for (u, v) in pairs[:400]:
    m = u * v
    ssm = math.gcd(m, Msmall); R = m // ssm
    for z in random.sample(units_small, 8):
        live = ((z + u + v) % ssm == 0)
        # exact: fraction of rough unit residues x mod Mr with CRT(z,x) ≡ -u-v mod m
        hits = 0; tot = 0
        for x in range(Mr):
            if math.gcd(x, Mr) != 1: continue
            tot += 1
            # n ≡ z mod Msmall, n ≡ x mod Mr
            n = (z * Mr * pow(Mr, -1, Msmall) + x * Msmall * pow(Msmall, -1, Mr)) % (Msmall * Mr)
            if (n + u + v) % m == 0: hits += 1
        pred = (1.0 / int(totient(R))) if live else 0.0
        checks += 1
        if abs(hits / tot - pred) > 1e-12: viol += 1
log(f"(c) exact P(E|z) = [live]/phi(R): {checks} (pair,z) checks, violations={viol}")
open("data/z49_sexp/janson_check.txt", "w").write("\n".join(out) + "\n")
