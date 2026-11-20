"""z74 Opus cross-review (NRMODELS lane): independent finite checks. Stdlib only.

A. Compressed-modulus encoding (LOGIC_NONSQUARE_PROFILE §1 / Z73_NONSQUARE_ADELIC_REVIEW §1 /
   LOGIC_UNIVERSAL_NR_AUDIT §2 / LOGIC_STANDARD_PRIME_SIGNS §1).  Literal enumeration of all ET Prop 1.9
   parameterized classes with modulus m <= MMAX; for every admissible compression N (N | m, peeled part of a
   principal 4-block from the factors after the 4, r = 1 mod m/N) apply the *forward* encoding of the note's
   table, check the weighted identity 4xyzt = Lx+My+Hz, the slot-product bound <= N^2, the variable bound
   <= 2N^2 and m <= 512 N^11.  Also check that N = 1 is never admissible (no class contains 1).
   This is a different engine from scripts/z73_compression_audit.py (which compares literal vs inverse sets).
B. Character / projection facts used by the sign lemmas.
C. ES_RIGIDITY_NR §4: the menu-C (unary T^2+1) identity and the Jacobi contradiction, tested on actual
   integral specializations.
D. Z73_NONSQUARE_ADELIC_REVIEW §4 / LOGIC_NONSQUARE_PROFILE §4: the II-2 square-class-change example.
Usage: uv run --offline --no-project python scripts/z74_xrev_nrmodels_checks.py [MMAX]
"""
import sys
from fractions import Fraction as Fr
from math import gcd, isqrt
from collections import Counter
from functools import lru_cache

MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000


@lru_cache(maxsize=None)
def divs(n):
    s = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return s + [n // d for d in reversed(s) if d * d != n]


def factor(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def vp(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def split(N, parts):
    """Allocate N greedily (prime power by prime power, partial powers allowed) to divisors of parts."""
    out = [1] * len(parts)
    for p, k in factor(N).items():
        for i, a in enumerate(parts):
            take = min(k, vp(a // out[i], p))
            out[i] *= p ** take
            k -= take
        assert k == 0, (N, parts)
    return out


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    res = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


# ---------------------------------------------------------------- A
def check_eq(x, y, z, t, L, M, H, N):
    assert min(x, y, z, t) >= 1
    assert 4 * x * y * z * t == L * x + M * y + H * z, (x, y, z, t, L, M, H)
    assert max(L * M, L * H, M * H) <= N * N
    assert max(x, y, z, t) <= 2 * N * N


def encode(tag, prm, m, r, N):
    """Forward encoding from the note's table. Returns nothing; asserts."""
    if tag in ('I4', 'II1'):
        a, b, e = prm
        A, B = split(N, [a, b])
        x, y = a // A, b // B
        assert (e + 1) % (4 * x * y) == 0
        t = (e + 1) // (4 * x * y)
        z = (a + b) // e
        check_eq(x, y, z, t, A, B, 1, N)
    elif tag == 'II2':
        a, d, f = prm
        assert f % N == 0
        fp = f // N
        c = (f + 1) // (4 * a * d)
        assert (4 * a * a * d + 1) % fp == 0 and (a + c) % fp == 0
        w = (a + c) // fp
        check_eq(a, c, w, d, N, N, 1, N)
    elif tag == 'I2':
        a, c, f = prm
        F = gcd(N, f)
        A, B = split(N // F, [a, c])
        x, y, fp = a // A, c // B, f // F
        assert (f + 1) % (4 * x * y) == 0 and (a + c) % fp == 0
        t = (f + 1) // (4 * x * y)
        w = (a + c) // fp
        check_eq(x, y, w, t, F * A, F * B, 1, N)
    elif tag in ('I1', 'I3', 'II3'):
        c, d, f = prm[:3]
        F = gcd(N, f) if tag != 'I1' else 1
        C, D = split(N // F, [c, d])
        x, tt, fp = c // C, d // D, f // F
        assert (f + 1) % (4 * x * tt) == 0 and (1 + 4 * c * c * d) % fp == 0
        h = (f + 1) // (4 * x * tt)
        J = C * C * D
        assert (h + J * x) % fp == 0
        w = (h + J * x) // fp
        check_eq(x, h, w, tt, F * J, F, 1, N)
    else:
        raise ValueError(tag)
    assert m <= 512 * N ** 11


def classes(M):
    for a in range(1, M // 4 + 1):
        for b in range(1, M // (4 * a) + 1):
            t = 4 * a * b
            for f in divs(4 * a * a * b + 1):                      # I-1 (a,d)=(a,b)
                yield 'I1', (a, b, f), t, -f
            for e in divs(a + b):
                if gcd(e, t) == 1:
                    yield 'I4', (a, b, e), t, -pow(e, -1, t)
                    yield 'II1', (a, b, e), t, -e
            for f in range(1, M // t + 1):
                if gcd(t, f) != 1:
                    continue
                mm = t * f
                yield 'II3', (a, b, f), mm, -4 * a * a * b - f       # (a,d,e)=(a,b,f)
                # I-2 (a,c,f)=(a,b,f): n=-f mod 4ab, n=-b/a mod f
                r2 = None
                for r in range(-f % t, mm, t):
                    if (a * r + b) % f == 0:
                        yield 'I2', (a, b, f), mm, r
                    if (r * r + 4 * a * a * b) % f == 0:              # I-3 (c,d,f)=(a,b,f), one root class
                        yield 'I3', (a, b, f, r % f), mm, r
    for f in range(3, M + 1, 4):
        for a in divs((f + 1) // 4):
            for d in divs((f + 1) // (4 * a)):
                yield 'II2', (a, d, f), f, -4 * a * a * d


def part_A():
    rows = Counter()
    perN = Counter()
    noncop = 0
    nclass = 0
    for tag, prm, m, r in classes(MMAX):
        r %= m
        assert gcd(r, m) == 1
        nclass += 1
        assert (r - 1) % m != 0, ('N=1 admissible', tag, prm)   # no class contains 1
        base = m if tag == 'II2' else m // 4
        for N in divs(base):
            if N >= 2 and (r - 1) % (m // N) == 0:
                encode(tag, prm, m, r, N)
                rows[tag] += 1
                perN[N] += 1
                if gcd(N, m // N) > 1:
                    noncop += 1
    print(f"A. classes with m<={MMAX}: {nclass}; admissible (class,N) rows encoded+verified: {sum(rows.values())}")
    print("   by family:", dict(sorted(rows.items())), f"; rows with gcd(N,m/N)>1: {noncop}")
    # regression example quoted in the review: II-3 a=11,d=2,e=247
    m, r = 4 * 11 * 2 * 247, (-4 * 121 * 2 - 247) % 21736
    assert m == 21736 and (r - 1) % 152 == 0
    encode('II3', (11, 2, 247), m, r, 143)
    print("   II-3 regression (a,d,e)=(11,2,247), N=143: encoded OK")


# ---------------------------------------------------------------- B
def primes(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b'\0\0'
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def leg(a, q):
    a %= q
    return 0 if a == 0 else (1 if pow(a, (q - 1) // 2, q) == 1 else -1)


def part_B():
    ps = [q for q in primes(400) if q > 2]
    for q in ps:
        assert sum(leg(P * P + 1, q) for P in range(q)) == -1
        sq = {}
        for X in range(q):
            for Y in range(q):
                b = (X * X + Y * Y) % q
                sq[b] = sq.get(b, 0) + 1
        assert all(sq[b] == q - leg(-1, q) for b in range(1, q))
    # norm-base projection: s = Y + X^3 + 2 (an irreducible over Q), project negative-sign pairs by X^2+Y^2
    worst = 9
    for q in [p for p in ps if p >= 31]:
        B = {(X * X + Y * Y) % q for X in range(q) for Y in range(q)
             if (X * X + Y * Y) % q and leg(Y + X ** 3 + 2, q) == -1}
        worst = min(worst, len(B) / q)
    print(f"B. sum_P chi(P^2+1) = -1 and #(X^2+Y^2=b) = q - chi(-1) for all odd q<400; "
          f"min |B_q|/q (norm-base example, 31<=q<400) = {worst:.3f} (claim >= 1/3 for large q)")
    # multi-slot words on a 2-dim chart (P,t): five pairwise non-associate primes
    slots = [lambda P, t: P, lambda P, t: t, lambda P, t: P + t + 1,
             lambda P, t: P * t - 3, lambda P, t: t * t - P]
    for q in [p for p in ps if p % 4 == 3 and 60 < p < 200]:
        words = {}
        for P in range(1, q):
            for t in range(q):
                vals = [s(P, t) % q for s in slots]
                if 0 in vals:
                    continue
                w = tuple(leg(v, q) for v in vals)
                words.setdefault(w, set()).add(P)
        assert len(words) == 32, q
        mn = min(len(v) for v in words.values())
        assert mn >= q / 2 ** 6, (q, mn)
    print("   5-slot sign words: all 32 words realised for every q=3 mod 4 in (60,200), projection >= q/2^(k+1)")


# ---------------------------------------------------------------- C
def part_C():
    # menu C: P=T^2+1, D=h(T^2+kT+u), 4y-P=(T^2-kT+u)/h, u=1+k^2/2, 4lam=u^2-1, x=(P+D)/4, z=Pxy/lam
    hits = 0
    tested = 0
    for kn in range(1, 13):
        for kd in range(1, 7):
            k = Fr(kn, kd)
            for hn in range(1, 9):
                for hd in range(1, 9):
                    h = Fr(hn, hd)
                    u = 1 + k * k / 2
                    lam = (u * u - 1) / 4
                    assert lam == (k / 4) ** 2 * (k * k + 4)
                    for T in range(-200, 201):
                        P = T * T + 1
                        D = h * (T * T + k * T + u)
                        x = (P + D) / 4
                        y = (P + (T * T - k * T + u) / h) / 4
                        z = P * x * y / lam
                        assert Fr(4, P) == 1 / x + 1 / y + 1 / z
                        tested += 1
                        if not (x.denominator == y.denominator == z.denominator == 1):
                            continue
                        n, X, Y = P, int(x), int(y)
                        L = 4 * X * Y - n * (X + Y)
                        assert L == lam and L > 0
                        if gcd(n, L) != 1 or n % 8 != 1:
                            continue
                        hits += 1
                        g = gcd(X, Y)
                        a, b = X // g, Y // g
                        w = 4 * g * a * b - n * (a + b)
                        assert g % w == 0
                        e = g // w
                        e0 = e
                        j = 0
                        while e0 % 2 == 0:
                            e0 //= 2
                            j += 1
                        f = 4 * X - n
                        assert f > 0 and f % 4 == 3 and (n * n + 4 * L) % f == 0 and gcd(f, n * L) == 1
                        assert jacobi(-e, f) == 1
                        assert jacobi(-e, f) == -jacobi(n, e0)      # reciprocity step
                        assert jacobi(n, e0) == -1                # hence never (n/e0)=1
    print(f"C. menu-C identity checked at {tested} rational points; {hits} integral specialisations with "
          f"gcd(n,lam)=1, n=1 mod 8: all have (-e/f)=1=-(n/e0), so (n/e0)=-1 as the proof requires")


# ---------------------------------------------------------------- D
def part_D():
    cnt = 0
    for ell in [7, 11, 19, 23, 31, 43]:
        for g in range(1, ell):
            if leg(g, ell) != -1:
                continue
            d = next(d for d in range(1, 10 * ell) if (-4 * d - g) % ell == 0)
            target = (-pow(ell, -1, 4 * d)) % (4 * d)
            q = next(q for q in primes(10 ** 6) if q % (4 * d) == target and q > 4 * d and q != ell)
            f = ell * q
            assert (f + 1) % (4 * d) == 0                         # II-2 with a=1
            assert leg(-4 * d, q) == 1                            # changed component is a square unit
            assert (-4 * d - g) % ell == 0                        # l-component unchanged
            cnt += 1
    print(f"D. II-2 square-class-change example verified for {cnt} (ell,g) pairs")


if __name__ == '__main__':
    part_A()
    part_B()
    part_C()
    part_D()
    print("ALL CHECKS PASSED")
