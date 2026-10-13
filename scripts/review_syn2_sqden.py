"""R193 from-scratch checks for SYNTHESIS_SPARKS2 §2 (ES^□).

(A) Prop 2.2 recipe at every prime 5 <= p < PMAX: exact verification of the ES^□ solution,
    Type II shape, Q < 2r for p > 2r, distribution of r(p).
(B) n = 825 claim (least admissible Q = 17 for r = 7).
(C) Brute force of ES^□(n) at small odd squares n = m² (Lemma 2.1): no solution with Type I/II shape at every
    prime of m; also full Hilbert-symbol census (inv at every place, mute places 0, product formula).
(D) Least-non-residue statistic: fraction of primes p ≡ 1 (4) with r(p) > (log p)/2  (Reading 2 claim).
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_syn2_sqden.py [PMAX]
"""
import sys, math
from fractions import Fraction as F
from sympy import primerange, factorint, legendre_symbol, isprime

def v(p, x):
    x = abs(x); k = 0
    while x % p == 0: x //= p; k += 1
    return k

def vq(p, fr):
    return v(p, fr.numerator) - v(p, fr.denominator)

def is_sq(n):
    r = math.isqrt(n); return r * r == n

def ok_den(z, n):  # ES^□: z>0, denominator odd square coprime to n
    d = z.denominator
    return z > 0 and d % 2 == 1 and math.gcd(d, n) == 1 and is_sq(d)

def shot(n, Q, g):
    """UNIT_ORBIT_ES Prop 2.1 with divisor g ≡ 3 (4) of n+4Q²."""
    a = n + 4 * Q * Q
    assert a % g == 0 and g % 4 == 3
    e = a // g
    x = F(n + e, 4); y = F(n * (g + 1), 4); z = F(n) * x * (g + 1) / (4 * Q * Q)
    return x, y, z

def check_sol(n, x, y, z):
    assert x.denominator == 1 and y.denominator == 1 and x > 0 and y > 0
    assert F(4, n) == 1 / x + 1 / y + 1 / z
    assert ok_den(z, n)
    # Type II shape at every prime of n
    for l, k in factorint(n).items():
        vals = sorted([vq(l, x), vq(l, y), vq(l, z)])
        assert vals[0] == 0 and vals[1] >= k, (n, l, vals)

def r_of(n):
    r = 3
    while True:
        if r % 4 == 3 and isprime(r) and n % r and legendre_symbol(n % r, r) == -1:
            return r
        r += 4

def recipe(n):
    if n % 4 == 3:
        return 1, n + 4, None
    r = r_of(n)
    s = next(t for t in range(1, r) if (4 * t * t + n) % r == 0)
    cand = [t for t in (s, r - s) if t % 2 == 1][0]
    Q = cand
    while math.gcd(Q, n) != 1:
        Q += 2 * r
    return Q, r, r

def partA(PMAX):
    from collections import Counter
    cnt = 0; dist = Counter(); maxr = (0, 0); maxQ = 0; bad_bound = 0
    for p in primerange(5, PMAX):
        Q, g, r = recipe(p)
        check_sol(p, *shot(p, Q, g)); cnt += 1
        if r:
            dist[r] += 1; maxr = max(maxr, (r, p)); maxQ = max(maxQ, Q)
            if p > 2 * r and not Q < 2 * r: bad_bound += 1
    print(f"(A) primes 5..{PMAX}: {cnt} solved & verified; max r(p) = {maxr}; max Q = {maxQ}; "
          f"Q<2r violations (p>2r): {bad_bound}")
    print("    r(p) distribution:", sorted(dist.items())[:8])

def partB():
    n, r = 825, 7
    roots = [t for t in range(1, 2 * r) if (4 * t * t + n) % r == 0 and t % 2]
    Qs = [Q for Q in range(1, 100, 2) if (4 * Q * Q + n) % r == 0 and math.gcd(Q, n) == 1]
    print(f"(B) n=825: r(825) = {r_of(825)}, odd roots < 2r: {roots}, least admissible Q: {Qs[0]}")
    Q, g, _ = recipe(825); check_sol(825, *shot(825, Q, g))

# ---- Hilbert symbols over Q ----
def hilb(a, b, p):
    """(a,b)_p in {1,-1}, a,b nonzero Fractions; p prime or 0 (=infinity)."""
    if p == 0:
        return -1 if (a < 0 and b < 0) else 1
    al, be = vq(p, a), vq(p, b)
    u = a / F(p) ** al; w = b / F(p) ** be
    if p != 2:
        uu = u.numerator * pow(u.denominator, -1, p) % p
        ww = w.numerator * pow(w.denominator, -1, p) % p
        e = al * be * ((p - 1) // 2)
        e += be * (int(legendre_symbol(uu, p)) == -1) + al * (int(legendre_symbol(ww, p)) == -1)
        s = -1 if e % 2 else 1
        return s
    uu = u.numerator * pow(u.denominator, -1, 8) % 8
    ww = w.numerator * pow(w.denominator, -1, 8) % 8
    eps = lambda t: ((t - 1) // 2) % 2
    om = lambda t: ((t * t - 1) // 8) % 2
    e = eps(uu) * eps(ww) + al * om(ww) + be * om(uu)
    return -1 if e % 2 else 1

def partC(ms, XM=3, YM=40, control=False):
    for m in ms:
        n = m * m
        fac = factorint(m)
        tot = I2 = 0; invfail = 0; anyshape_at_some = 0
        for x in range(n // 4 + 1, XM * n + 1):
            r1 = F(4, n) - F(1, x)
            if r1 <= 0: continue
            y0 = int(1 / r1) + 1
            for y in range(max(y0, 1), YM * n + 1):
                rem = r1 - F(1, y)
                if rem <= 0: continue
                z = 1 / rem
                if control:
                    d = z.denominator
                    if not (d % 2 and math.gcd(d, n) == 1) or is_sq(d): continue
                elif not ok_den(z, n): continue
                tot += 1
                shapes = []
                for l in fac:
                    k = v(l, n); vals = sorted([v(l, x), v(l, y), vq(l, z)])
                    t1 = vals[0] == 0 and vals[1] == 0 and vals[2] >= k
                    t2 = vals[0] == 0 and vals[1] >= k
                    shapes.append(t1 or t2)
                if all(shapes): I2 += 1
                if any(shapes): anyshape_at_some += 1
                # Hilbert census: alpha = (-x/z, -y/z)
                A, B = -F(x) / z, -F(y) / z
                places = set(factorint(abs(A.numerator) * A.denominator * abs(B.numerator) * B.denominator * 2 * n)) | {0}
                s = {pl: hilb(A, B, pl) for pl in places}
                prod = 1
                for val in s.values(): prod *= val
                mute = [pl for pl in places if pl not in (0, 2) and n % pl and s[pl] == -1]
                sum_n = 1
                for l in fac: sum_n *= s[l]
                if prod != 1 or mute or s[0] != -1 or s[2] != 1 or sum_n != -1: invfail += 1
        print(f"(C{'-control: odd NON-square denominators' if control else ''}) n={n}: {tot} ES^□ solutions (x<= {XM}n, y<= {YM}n); Type I/II at every prime of m: {I2}; "
              f"I/II at some prime: {anyshape_at_some}; Hilbert-census failures: {invfail}")

def partD(PMAX):
    tot = big = 0
    for p in primerange(5, PMAX):
        if p % 4 == 1:
            tot += 1
            if r_of(p) > math.log(p) / 2: big += 1
    print(f"(D) p≡1(4) < {PMAX}: fraction with r(p) > (log p)/2 = {big}/{tot} = {big/tot:.4f}")

if __name__ == "__main__":
    PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    partA(PMAX); partB()
    partC([3, 5, 7, 9, 15], XM=2, YM=30)
    partC([3, 5], XM=2, YM=30, control=True)
    partD(PMAX)
