"""review_fms_cube.py P [P1] — R191 from-scratch check of FIXED_MODULUS_SHOTS Lemma 1.1, Lemma 4.1, Prop 6.1.

Independent ES solvers (no cube theory):
  Type II (p | y, p | z, p ∤ x): e = 4x - p, e/x = 1/y' + 1/z'  <=>  (e y' - x)(e z' - x) = x^2;
          x <= p/2 because 1/y' + 1/z' <= 2.  All ORDERED (x, y, z).
  Type I  (p | x only): for every y in (p/4, 2p/3] (1/y >= (4/p - 1/x)/2 >= 3/(2p) for the smaller of y, z),
          (A z - B)(A x - B) = B^2 with A = 4y - p, B = p y; keep p | x, p ∤ y z; ORDERED (y, z).
Cube enumerations:
  Type II (c, d) with 3cd <= p + 1, divisors h of p + 4c^2 d with h ≡ -1 mod 4cd (j = (h+1)/4cd).
          For p <= P1 also a WIDE scan cd <= 2p (to test that 3cd <= p+1 loses nothing).
  Type I  (w, f) with wf <= 2p/3, divisors g of p^2 + 4wf^2 with g ≡ -p mod 4wf, v = (g+p)/(4wf).
Prop 6.1: track max h / ((p+1)(p+5)/4) and max g / p^2.
Type I is checked for p <= P1 only (cost).
"""
import sys
from fractions import Fraction as F

P = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
P1 = int(sys.argv[2]) if len(sys.argv) > 2 else 1500

LIM = max(4 * (P + 1) ** 2 // 9 + P + 10, 25 * P1 * P1 // 9 + 10, 4 * 600 * 600 + 310, 2 * P * P // 3 + 10)
spf = list(range(LIM + 1))
i = 2
while i * i <= LIM:
    if spf[i] == i:
        for k in range(i * i, LIM + 1, i):
            if spf[k] == k:
                spf[k] = i
    i += 1


def fac(n):
    out = {}
    while n > 1:
        q = spf[n]
        out[q] = out.get(q, 0) + 1
        n //= q
    return out


def divs_from(f):
    ds = [1]
    for q, a in f.items():
        ds = [d * q ** k for d in ds for k in range(a + 1)]
    return ds


def divs(n):
    return divs_from(fac(n))


def is_sol(p, x, y, z):
    return F(1, x) + F(1, y) + F(1, z) == F(4, p)


def brute_II(p):
    S = set()
    for x in range(p // 4 + 1, p // 2 + 1):
        e = 4 * x - p
        f = fac(x)
        for D in divs_from({q: 2 * a for q, a in f.items()}):
            D2 = x * x // D
            if (x + D) % e or (x + D2) % e:
                continue
            S.add((x, p * ((x + D) // e), p * ((x + D2) // e)))
    return S


def cube_II(p, wide=False):
    S = set()
    pts = 0
    maxh = 0
    lim = 2 * p if wide else (p + 1) // 3
    for c in range(1, lim + 1):
        for d in range(1, lim // c + 1):
            if not wide and 3 * c * d > p + 1:
                break
            N = p + 4 * c * c * d
            m = 4 * c * d
            for h in divs(N) if N <= LIM else []:
                if (h + 1) % m:
                    continue
                j = (h + 1) // m
                a1 = (p * j + c) % h == 0
                a3 = (4 * d * j * j * p + 1) % h == 0
                assert a1 and a3, (p, c, d, j)
                assert 3 * c * d <= p + 1, ("3cd bound", p, c, d, j)
                e = N // h
                assert (p + e) % 4 == 0
                x = (p + e) // 4
                assert (p * x * j) % c == 0 and x % p
                y, z = p * c * d * j, p * x * j // c
                assert is_sol(p, x, y, z)
                S.add((x, y, z))
                pts += 1
                maxh = max(maxh, h)
            if wide and N > LIM:
                raise SystemExit("LIM too small for wide scan")
    return S, pts, maxh


def brute_I(p):
    S = set()
    for y in range(p // 4 + 1, 2 * p // 3 + 1):
        A, B = 4 * y - p, p * y
        fB = fac(B)
        for D in divs_from({q: 2 * a for q, a in fB.items()}):
            D2 = B * B // D
            if (B + D) % A or (B + D2) % A:
                continue
            z, x = (B + D) // A, (B + D2) // A
            if x % p or z % p == 0 or y % p == 0:
                continue
            S.add((x, y, z))
            S.add((x, z, y))
    return S


def cube_I(p):
    S = set()
    allsol = 0
    maxg = 0
    for w in range(1, p + 1):
        for f in range(1, p // w + 1):
            if 3 * w * f > 2 * p:
                break
            N = p * p + 4 * w * f * f
            m = 4 * w * f
            for g in divs(N):
                if (g + p) % m:
                    continue
                v = (g + p) // m
                b1 = (p * v + f) % g == 0
                b3 = (4 * v * v * w + 1) % g == 0
                if p * p % g == 0 and g > 1:  # g = p or p^2 — coprimality fails
                    continue
                assert b1 == b3, (p, v, w, f, g)
                if not b1:
                    continue
                u = (p * v + f) // g
                x, y, z = p * u * v * w, w * f * u, w * f * v
                assert is_sol(p, x, y, z)
                allsol += 1
                if (u * v * w * f) % p:
                    S.add((x, y, z))
                    maxg = max(maxg, g)
    return S, maxg


def primes(n):
    return [q for q in range(5, n + 1) if spf[q] == q]


bad = 0
r61 = 0
r61g = 0
att = 0
for p in primes(P):
    B = brute_II(p)
    C, pts, mh = cube_II(p)
    if B != C:
        bad += 1
        print("TYPE II MISMATCH", p, len(B), len(C))
    if p <= 300:
        Cw, _, _ = cube_II(p, wide=True)
        assert Cw == C, ("wide", p)
    bnd = (p + 1) * (p + 5) // 4 - 1 if (p + 1) * (p + 5) % 4 == 0 else (p + 1) * (p + 5) / 4 - 1
    assert mh <= bnd, ("Prop 6.1 II", p, mh)
    if mh == bnd:
        att += 1
    r61 = max(r61, mh / ((p + 1) * (p + 5) / 4))
    if p <= P1:
        BI = brute_I(p)
        CI, mg = cube_I(p)
        if BI != CI:
            bad += 1
            print("TYPE I MISMATCH", p, len(BI), len(CI), sorted(BI ^ CI)[:3])
        assert mg < 3 * p * p
        r61g = max(r61g, mg / p ** 2)
print(f"primes 5..{P}: {len(primes(P))}; Type I checked to {P1}; mismatches {bad}")
print(f"Prop 6.1 II: max h/((p+1)(p+5)/4) = {r61:.6f}; bound (p+1)(p+5)/4-1 attained at {att} primes")
print(f"Prop 6.1 I : max g/p^2 = {r61g:.6f}")

# fully naive sanity check of the two brute-force solvers (all ordered triples, small p)
for p in primes(min(P, 70)):
    naive2, naive1 = set(), set()
    for x in range(1, 3 * p + 1):
        r = F(4, p) - F(1, x)
        if r <= 0:
            continue
        for y in range(1, int(2 / r) + 2):
            s = r - F(1, y)
            if s > 0 and s.numerator == 1:
                z = s.denominator
                k = (x % p == 0) + (y % p == 0) + (z % p == 0)
                if k == 2:
                    t = sorted((x, y, z), key=lambda a: a % p == 0)  # non-multiple first
                    naive2.add((t[0], t[1], t[2]))
                    naive2.add((t[0], t[2], t[1]))
                if k == 1:
                    t = sorted((x, y, z), key=lambda a: a % p != 0)  # multiple first
                    naive1.add((t[0], t[1], t[2]))
                    naive1.add((t[0], t[2], t[1]))
    assert naive2 == brute_II(p), p
    assert naive1 == brute_I(p), p
print("naive solver agrees with brute_II/brute_I for p <= 70")
