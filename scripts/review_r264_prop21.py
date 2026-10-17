"""R264 from-scratch check of FORCED_WINDOW Prop 2.1 and Lemma 1.1 (no author code used).

(A) Type II ES solutions found by brute force (4/p = 1/x + 1/y + 1/z, p | y, p | z, p ∤ x):
    windows m = 4x - p with m/x = 1/a + 1/b.
(B) cap-0 certificates: delta in prod [-b_s, b_s] with prod s^delta == -1 (mod m).
(C) Prop 2.1 converse: coprime (u, v), r = (-p mod 4uv), r | u+v, p ∤ r.
Checks A == B == C as window sets, and forward claims of Prop 2.1 for every certificate.
Lemma 1.1: parity-split box certificates at forced prime windows q ≡ 3 (8), p ≡ 1 (8); exact ES rebuild.
Usage: python review_r264_prop21.py PMAX QMAX
"""
import sys
from fractions import Fraction
from itertools import product
from math import gcd, isqrt


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i :: i] = bytearray(len(s[i * i :: i]))
    return [i for i in range(n + 1) if s[i]]


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def legendre(a, q):
    r = pow(a % q, (q - 1) // 2, q)
    return -1 if r == q - 1 else r


def typeII_windows(p):
    out = set()
    for m in range(3, p, 4):
        if m % p == 0:
            continue
        K = (p + m) // 4
        lo = -(-K // m)
        for a in range(lo, 2 * K // m + 1):
            num = m * a - K
            if num > 0 and (K * a) % num == 0:
                out.add(m)
                break
    return out


def certs(p, m):
    K = (p + m) // 4
    f = factor(K)
    S = sorted(f)
    res = []
    for d in product(*[range(-f[s], f[s] + 1) for s in S]):
        val = 1
        for s, e in zip(S, d):
            val = val * pow(s, e, m) % m if e >= 0 else val * pow(pow(s, -e, m), -1, m) % m
        if val == m - 1 or (m == 1):
            res.append(dict(zip(S, d)))
    return K, f, res


def check_p(p):
    A = typeII_windows(p)
    B = set()
    nfwd = 0
    for m in range(3, p, 4):
        if m % p == 0:
            continue
        K, f, cs = certs(p, m)
        if cs:
            B.add(m)
        for c in cs:
            u = 1
            v = 1
            for s, e in c.items():
                if e > 0:
                    u *= s**e
                elif e < 0:
                    v *= s ** (-e)
            assert gcd(u, v) == 1 and K % (u * v) == 0 and (u + v) % m == 0
            assert (-p) % (4 * u * v) == m and 4 * u * v >= 2 * m, (p, m, u, v)
            nfwd += 1
    C = set()
    for u in range(1, p):
        for v in range(1, (p // 2) // u + 2):
            if gcd(u, v) != 1:
                continue
            r = (-p) % (4 * u * v)
            if r and (u + v) % r == 0 and r % p != 0:
                C.add(r)
    assert A == B == C, (p, sorted(A ^ B), sorted(B ^ C))
    return len(B), nfwd


def lemma11(p, qmax):
    """parity-split certificates at forced q ≡ 3 (8); returns list of (q, cap_parity, cap0_exists)."""
    out = []
    for q in primes_upto(qmax):
        if q % 8 != 3 or legendre(p, q) != -1:
            continue
        K = (p + q) // 4
        assert K % 2 == 1
        f = factor(K)
        assert legendre(K, q) == -1
        O = [s for s in f if f[s] % 2 == 1]
        c = 1
        for s in O:
            c *= s
        assert legendre(c, q) == -1
        t = (-c) % q
        assert legendre(t, q) == 1
        S = sorted(f)
        found = None
        for e in range(0, q):
            rng = [range(0, (f[s] + (s in O)) // 2 + e + 1) for s in S]
            for j in product(*rng):
                val = 1
                for s, jj in zip(S, j):
                    val = val * pow(s, 2 * jj, q) % q
                if val == t:
                    found = (e, j)
                    break
            if found:
                break
        e, j = found
        delta = {s: -(1 if s in O else 0) + 2 * jj for s, jj in zip(S, j)}
        # admissibility in D_s(e)
        for s in S:
            b = f[s]
            ds = delta[s]
            assert -b <= ds <= b or (ds > b and (ds - b) % 2 == 0 and (ds - b) // 2 <= e)
        # rebuild ES via d = K * prod s^delta (CAP_DOWN Lemma 1.1 recipe, recomputed)
        d = Fraction(K)
        for s in S:
            d *= Fraction(s) ** delta[s]
        assert d.denominator == 1
        d = d.numerator
        assert (K + d) % q == 0
        Aq = (K + d) // q
        x, y, z = K, p * Aq, Fraction(p * K * Aq, d)
        assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + 1 / z
        den = z.denominator
        r = isqrt(den)
        assert r * r == den and r % 2 == 1 and gcd(r, p) == 1
        for l, v in factor(r).items() if r > 1 else []:
            assert v <= e and y % l == 0
        cap0 = bool(certs(p, q)[2])
        out.append((q, e, cap0))
    return out


if __name__ == "__main__":
    PMAX, QMAX = int(sys.argv[1]), int(sys.argv[2])
    tot = 0
    for p in primes_upto(PMAX):
        if p % 4 != 1:
            continue
        nw, nf = check_p(p)
        tot += nf
    print(f"Prop 2.1: A==B==C for all p≡1(4) ≤ {PMAX}; {tot} certificates checked forward")
    strict = 0
    n = 0
    for p in primes_upto(PMAX):
        if p % 8 != 1:
            continue
        for q, e, cap0 in lemma11(p, QMAX):
            n += 1
            if e > 0 and cap0:
                strict += 1
                if strict <= 5:
                    print("parity-cap > 0 but cap 0:", p, q, e)
    print(f"Lemma 1.1: {n} (p,q) parity certificates rebuilt exactly; {strict} with parity-cap>0 but cap(q)=0")
