"""R243 from-scratch checks of CAP_DOWN Lemma 1.1, Thm 1.2, Prop 1.3, Lemma 3.1, T1, Prop 4.1.

Independent of scripts/z13_*. Uses only exact integer/Fraction arithmetic.
Usage: PYTHONPATH=scripts uv run python scripts/review_r243_lemmas.py [NMAX]
"""
import sys
import random
from fractions import Fraction
from math import gcd, isqrt


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def is_prime(n):
    return n > 1 and factor(n) == {n: 1}


def jacobi(a, m):
    assert m > 0 and m % 2 == 1
    a %= m
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5):
                r = -r
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            r = -r
        a %= m
    return r if m == 1 else 0


def def11_cap(n, x, y, z):
    """Return the least e with (x,y,z) in ES^{(y,e)}(n) per EXPONENT_CAP Def 1.1, or None if in no cap."""
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / Fraction(z), "identity fails"
    assert isinstance(x, int) and isinstance(y, int) and x > 0 and y > 0 and z > 0
    den = Fraction(z).denominator
    e = 0
    for l, v in factor(den).items():
        if l == 2 or n % l == 0 or y % l != 0 or v % 2:
            return None
        e = max(e, v // 2)
    return e


def ordmod(s, q):
    s %= q
    o, t = 1, s
    while t != 1:
        t = t * s % q
        o += 1
    return o


def lemma11_triple(n, m, d):
    K = (n + m) // 4
    assert (K + d) % m == 0
    A = (K + d) // m
    return K, n * A, Fraction(n * K * A, d)


def lemma11_predicted_cap(K, d):
    """Lemma 1.1 predicted cap or None if hypotheses (ii)/(iii) fail."""
    fK = factor(K)
    fd = factor(d)
    e = 0
    for s, c in fd.items():
        b = fK.get(s, 0)
        assert b > 0, "d must be K-smooth"
        if s == 2:
            if c > 2 * b:
                return None
        elif c > 2 * b:
            if c % 2:
                return None
            e = max(e, c // 2 - b)
    return e


def check_lemma11_random(trials=20000, seed=1):
    rng = random.Random(seed)
    nchk = 0
    for _ in range(trials):
        n = rng.randrange(1, 3000) * 2 + 1
        m = rng.randrange(1, 400)
        if (n + m) % 4 or gcd(m, n) != 1:
            continue
        K = (n + m) // 4
        if gcd(K, n) != 1:
            continue
        fK = list(factor(K).items())
        if not fK:
            continue
        # random K-smooth d with exponents up to 2b+5
        d = 1
        for s, b in fK:
            d *= s ** rng.randrange(0, 2 * b + 6)
        if (K + d) % m:
            # adjust: try a few random exponents until congruence
            continue
        x, y, z = lemma11_triple(n, m, d)
        pred = lemma11_predicted_cap(K, d)
        actual = def11_cap(n, x, y, z)
        assert pred == actual, (n, m, d, pred, actual)
        nchk += 1
    return nchk


def check_lemma11_exhaustive(nmax=600, mmax=60):
    """All n odd <= nmax, windows m <= mmax, all K-smooth d with c_s <= 2b_s+6."""
    nchk = 0
    for n in range(1, nmax + 1, 2):
        for m in range(1, mmax + 1):
            if (n + m) % 4 or gcd(m, n) != 1:
                continue
            K = (n + m) // 4
            if gcd(K, n) != 1:
                continue
            fK = list(factor(K).items())
            ds = [1]
            for s, b in fK:
                ds = [dd * s ** c for dd in ds for c in range(2 * b + 7)]
            for d in ds:
                if (K + d) % m:
                    continue
                x, y, z = lemma11_triple(n, m, d)
                pred = lemma11_predicted_cap(K, d)
                actual = def11_cap(n, x, y, z)
                assert pred == actual, (n, m, d, pred, actual)
                nchk += 1
    return nchk


def thm12_witness(n, q):
    """Thm 1.2 construction (my own: brute-force discrete log over <odd primes of K'>)."""
    K = (n + q) // 4
    t = 0
    Kp = K
    while Kp % 2 == 0:
        Kp //= 2
        t += 1
    S = sorted(factor(Kp))
    target = (-Kp) % q
    # h with h^2 = -K' and h in <S>; search exponent vectors via BFS over residues
    reach = {1 % q: ()}
    frontier = [1 % q]
    while frontier:
        nf = []
        for r in frontier:
            for i, s in enumerate(S):
                r2 = r * s % q
                if r2 not in reach:
                    vec = list(reach[r] or [0] * len(S))
                    vec[i] += 1
                    reach[r2] = tuple(vec)
                    nf.append(r2)
        frontier = nf
    hs = [h for h in reach if h * h % q == target]
    assert hs, ("no square root of -K' in <S>", n, q)
    best = None
    for h in hs:
        vec = reach[h] or (0,) * len(S)
        d = 2 ** t
        for s, a in zip(S, vec):
            d *= s ** (2 * a)
        assert (d + K) % q == 0
        x, y, z = lemma11_triple(n, q, d)
        e = def11_cap(n, x, y, z)
        assert e is not None and e <= q - 3, (n, q, d, e)
        best = e if best is None else min(best, e)
    return best


def prop13_witness(n, q):
    K = (n + q) // 4
    fK = factor(K)
    caps = []
    for s, b in fK.items():
        if s == 2 or b % 2 == 0 or jacobi(s, q) != -1:
            continue
        o = ordmod(s, q)
        assert o % 4 == 2
        assert pow(s, o // 2, q) == q - 1
        d = K * s ** (o // 2)
        x, y, z = lemma11_triple(n, q, d)
        e = def11_cap(n, x, y, z)
        assert e == max(0, (o // 2 - b) // 2), (n, q, s, e)
        assert 4 * e <= q - 3
        caps.append(e)
    assert caps, ("no Prop 1.3 prime", n, q)
    return min(caps)


def check_thm12(nmax):
    """All non-square n ≡ 1 (4) <= nmax (any prime factors), all primes q ≡ 3 (4) < 300 with (q/n) = -1."""
    cnt = {"fire": 0, "excluded": 0}
    for n in range(5, nmax + 1, 4):
        if isqrt(n) ** 2 == n:
            continue
        for q in range(3, 300, 4):
            if not is_prime(q) or n % q == 0 or jacobi(q, n) != -1:
                continue
            K = (n + q) // 4
            t = (K & -K).bit_length() - 1
            if not (q % 8 == 7 or t % 2 == 0):
                cnt["excluded"] += 1
                assert n % 8 == 5 and q % 8 == 3 and ((n + q) & -(n + q)).bit_length() % 2 == 0
                continue
            # (K'/q) = -1 check
            Kp = K >> t
            assert jacobi(Kp, q) == -1
            e1 = thm12_witness(n, q)
            e2 = prop13_witness(n, q)
            assert e1 is not None and e2 is not None
            cnt["fire"] += 1
    return cnt


def check_lemma31(nmax=61, xmax=None):
    """Brute force: all solutions with given x enumerated by D1 vs. direct (y up to bound)."""
    nchk = 0
    for n in range(1, nmax + 1, 2):
        for x in range((n + 4) // 4, n + 1):
            m = 4 * x - n
            if m <= 0 or gcd(m, n) != 1 or gcd(x, n) != 1:
                continue
            N = n * x
            # y ranges over integers with 1/y < m/N, i.e. y > N/m; z>0 rational; finitely many y with z in ES^{(y,e)}?
            # Enumerate D1 | (2nx)^big smooth with c_s up to 2b_s+4 and compare with direct Def 1.1 test of all y <= N + N^2 bound.
            for y in range(N // m + 1, (N + min(N * N, 30000)) // m + 2):
                r = Fraction(4, n) - Fraction(1, x) - Fraction(1, y)
                if r <= 0:
                    continue
                z = 1 / r
                D1 = m * y - N
                e = def11_cap(n, x, y, z)
                # Lemma 3.1 prediction
                fD = factor(D1)
                fN = factor(N)
                ok = True
                pe = 0
                for s, c in fD.items():
                    if (2 * n * x) % s:
                        ok = False
                        break
                    b = fN.get(s, 0)
                    if s == 2 or n % s == 0:
                        if c > 2 * b:
                            ok = False
                            break
                    else:
                        if c > 2 * b:
                            if c % 2:
                                ok = False
                                break
                            pe = max(pe, c // 2 - b)
                pred = pe if ok else None
                assert pred == e, (n, x, y, z, pred, e)
                nchk += 1
    return nchk


def check_T1(amax=60, mmax=200, emax=4):
    hits = 0
    for a in range(1, amax + 1, 2):
        n = a * a
        for m in range(3, mmax + 1, 4):
            if gcd(m, n) != 1:
                continue
            K = (n + m) // 4
            if gcd(K, n) != 1:
                continue
            ds = [1]
            for s, b in factor(K).items():
                ds = [dd * s ** c for dd in ds for c in range(2 * b + 2 * emax + 1)]
            for d in ds:
                if (K + d) % m == 0 and lemma11_predicted_cap(K, d) is not None:
                    hits += 1
    return hits


def check_prop41a(nmax=200000):
    """Least Lemma-1.1 cap at q when K = s prime, ord_q(s) = q-1: exhaustive c in [0, 3q]."""
    nchk = 0
    for q in [7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83]:
        for n in range(1, nmax, 4 if q % 4 == 3 else 2):
            if (n + q) % 4:
                continue
            K = (n + q) // 4
            if not is_prime(K) or K == 2 or n % q == 0 or ordmod(K, q) != q - 1:
                continue
            if nchk > 3000:
                return nchk
            best = None
            for c in range(0, 3 * q):
                d = K ** c
                if (K + d) % q:
                    continue
                e = lemma11_predicted_cap(K, d)
                if e is not None:
                    best = e if best is None else min(best, e)
            assert best == (q - 3) // 4, (n, q, best)
            nchk += 1
    return nchk


def check_prop41b_example():
    n, m = 5, 567
    K = (n + m) // 4
    out = {}
    for s in factor(K):
        out[s] = (ordmod(s, 81), ordmod(s, 7))
    return K, out


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    print("Lemma 1.1 exhaustive checks:", check_lemma11_exhaustive())
    print("Lemma 1.1 random checks:", check_lemma11_random())
    print("Thm 1.2 / Prop 1.3:", check_thm12(nmax))
    print("Lemma 3.1 brute force:", check_lemma31())
    print("T1 hits (should be 0):", check_T1())
    print("Prop 4.1(a):", check_prop41a())
    print("Prop 4.1(b) example:", check_prop41b_example())
