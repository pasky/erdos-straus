"""R286 from-scratch check of LOWER_TAIL_FABLE Thm 1.1 (canonical two-target form) and Lemma 2.7.

For every prime p = 1 (mod 4), p < P:
 (a) enumerate ALL solutions 4/p = 1/x+1/y+1/z (x <= y <= z) via (a y - b)(a z - b) = b^2,
     a/b = 4/p - 1/x (reduced: gcd(4x-p, px) = 1 since p does not divide x <= 3p/4);
 (b) classify by number of denominators divisible by p (must be 1 or 2);
 (c) map EVERY solution to a certificate (m,u,d) of the claimed type and verify
     d | mp+u, d = -1 resp. -p (mod 4mu), and that the stated reconstruction returns that solution;
 (d) soundness: every certificate in the window m,u <= W reconstructs (exact Fractions) to an ES
     solution, of the claimed type when p does not divide mu;
 (e) Lemma 2.7 on all certificates from (c) and (d): Type II (p/d) = -1;
     Type I (p/w) = -1 (Kronecker), and record how often (p/d) = +1.
"""
import sys
from fractions import Fraction
from math import gcd


def factor(n):
    f = {}
    q = 2
    while q * q <= n:
        while n % q == 0:
            f[q] = f.get(q, 0) + 1
            n //= q
        q += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divs_from(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds


def divisors(n):
    return divs_from(factor(n))


def isprime(n):
    return n > 1 and all(n % q for q in range(2, int(n ** 0.5) + 1))


def jacobi(a, n):  # n odd positive
    a %= n
    s = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                s = -s
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            s = -s
        a %= n
    return s if n == 1 else 0


def kron(p, w):  # Kronecker (p/w), p odd prime, w >= 1
    s = 1
    while w % 2 == 0:
        w //= 2
        s *= 1 if p % 8 in (1, 7) else -1
    return s * jacobi(p, w)


def solutions(p):
    out = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        a, b = 4 * x - p, p * x
        assert gcd(a, b) == 1
        fx = factor(x)
        f2 = {q: 2 * e for q, e in fx.items()}
        f2[p] = f2.get(p, 0) + 2
        for dl in divs_from(f2):
            if dl <= b and (dl + b) % a == 0 and (b * b // dl + b) % a == 0:
                y, z = (dl + b) // a, (b * b // dl + b) // a
                if y >= x:
                    assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
                    out.append((x, y, z))
    return out


def cert_of(p, sol):
    """map a solution to all certificates (type, m, u, w, d) reproducing it"""
    pm = [s for s in sol if s % p == 0]
    pf = [s for s in sol if s % p]
    res = []
    if len(pm) == 2:
        X = pf[0]
        Y, Z = pm[0] // p, pm[1] // p
        e = 4 * X - p
        for w in divisors(X):
            for u in divisors(X // w):
                v = X // (u * w)
                if (u + v) % e == 0:
                    m = (u + v) // e
                    if sorted((m * v * w, m * u * w)) == sorted((Y, Z)):
                        res.append(("II", m, u, w, 4 * m * u * w - 1))
    elif len(pm) == 1:
        Z = pm[0] // p
        for X, Y in ((pf[0], pf[1]), (pf[1], pf[0])):
            for w in divisors(X):
                for m in divisors(X // w):
                    u = X // (m * w)
                    if Y % (u * w) == 0 and (Y // (u * w)) * m * w == Z:
                        res.append(("I", m, u, w, 4 * m * u * w - p))
    else:
        raise AssertionError(("bad type", p, sol))
    return res


def check_cert(p, c):
    t, m, u, w, d = c
    N = m * p + u
    assert d > 0 and N % d == 0, c
    if t == "II":
        assert (d + 1) % (4 * m * u) == 0
        v = N // d
        assert (u + v) % m == 0
        sol = sorted((u * v * w, m * p * v * w, m * p * u * w))
    else:
        assert (d + p) % (4 * m * u) == 0
        h = N // d
        sol = sorted((m * u * w, h * p * m * w, h * u * w))
    assert sum(Fraction(1, s) for s in sol) == Fraction(4, p), (p, c)
    return tuple(sol)


def lemma27(p, c, stats):
    t, m, u, w, d = c
    if t == "II":
        if jacobi(p, d) != -1:
            stats["L27 II violations"] += 1
    else:
        if kron(p, w) != -1:
            stats["L27 I violations"] += 1
        if jacobi(p, d) == 1:
            stats["L27 I: (p/d)=+1 cases"] += 1
            if (p, m, u, d) == (13, 2, 1, 3):
                stats["p=13 (2,1,3) seen"] += 1


if __name__ == "__main__":
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    W = int(sys.argv[2]) if len(sys.argv) > 2 else 25
    from collections import Counter
    st = Counter()
    for p in range(5, P, 4):
        if not isprime(p):
            continue
        st["primes"] += 1
        sols = solutions(p)
        types = set()
        for s in sols:
            cs = cert_of(p, s)
            k = sum(1 for z in s if z % p == 0)
            if not cs:
                st["solution with NO certificate"] += 1
                print("no cert", p, s)
            for c in cs:
                assert check_cert(p, c) == tuple(sorted(s))
                assert c[0] == ("II" if k == 2 else "I")
                lemma27(p, c, st)
                st["certs from solutions"] += 1
            types.add(k)
            st["solutions"] += 1
        st["has I"] += 1 in types
        st["has II"] += 2 in types
        if 1 not in types or 2 not in types:
            print("missing type at", p, types)
        # (d) soundness in a window, independent direct search
        solset = {tuple(sorted(s)) for s in sols}
        for m in range(1, W):
            for u in range(1, W):
                N = m * p + u
                for d in divisors(N):
                    for t, tgt in (("II", -1), ("I", -p)):
                        if (d - tgt) % (4 * m * u) == 0:
                            w = (d - tgt) // (4 * m * u)
                            if w < 1:
                                continue
                            sol = check_cert(p, (t, m, u, w, d))
                            st["window certs " + t] += 1
                            if sol not in solset:
                                st["window cert -> unknown solution"] += 1
                            kk = sum(1 for z in sol if z % p == 0)
                            if p % m and p % u and kk != (2 if t == "II" else 1):
                                st["window type mismatch"] += 1
                            if p % m and p % u:
                                lemma27(p, (t, m, u, w, d), st)
    for k, v in sorted(st.items()):
        print(k, v)
