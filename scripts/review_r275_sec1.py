"""R275 from-scratch checks for MODP_RECIPROCITY §1 (Prop 1.1, Prop 1.2, Burde, q≡3 sign bookkeeping).
Independent of scripts/z35_*.  Usage: review_r275_sec1.py [PMAX_DICT] [PMAX_QUARTIC]"""
import sys
from math import isqrt, gcd


def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\0\0"
    for i in range(2, isqrt(n) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]


def jacobi(a, n):
    assert n > 0 and n % 2
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0


def two_squares(p):
    """p = a^2 + b^2, a odd, b even, both > 0 (brute force)."""
    for b in range(2, isqrt(p) + 1, 2):
        a2 = p - b * b; a = isqrt(a2)
        if a * a == a2: return a, b
    raise ValueError(p)


def divisors(n):
    ds = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            ds.append(i)
            if i != n // i: ds.append(n // i)
    return ds


def qpow4_index(q, p, a, b):
    """k in {0,1,2,3} with q^((p-1)/4) == (a/b)^k mod p."""
    T = pow(q, (p - 1) // 4, p); ip = a * pow(b, -1, p) % p
    for k in range(4):
        if pow(ip, k, p) == T: return k
    raise ValueError


def gmul(x, y, q):
    return ((x[0]*y[0] - x[1]*y[1]) % q, (x[0]*y[1] + x[1]*y[0]) % q)


def gpow(x, e, q):
    r = (1, 0)
    while e:
        if e & 1: r = gmul(r, x, q)
        x = gmul(x, x, q); e >>= 1
    return r


def ginv(x, q):  # in F_q[i], q = 3 mod 4
    n = (x[0]*x[0] + x[1]*x[1]) % q; ni = pow(n, -1, q)
    return (x[0]*ni % q, (-x[1])*ni % q)


UNITS = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}


def predicted_q3(q, p, a, b):
    """Reviewer's derivation: reduction i -> a/b is reduction mod lam = a - b i (a odd, b even => lam primary up to +-1).
    [q/lam]_4 = [-1/lam]_4 [lam/q]_4 (biquadratic reciprocity with primary -q, (q^2-1)/4 even; [-1/q]_4 = 1),
    [-1/lam]_4 = (-1)^((p-1)/4), [lam/q]_4 = lam^((q^2-1)/4) = (lambar/lam)^((q+1)/4) mod q."""
    lam = (a % q, (-b) % q); lamb = (a % q, b % q)
    v = gpow(gmul(lamb, ginv(lam, q), q), (q + 1) // 4, q)
    k = None
    for (u0, u1), kk in UNITS.items():
        if (u0 % q, u1 % q) == v: k = kk
    assert k is not None, (q, p, v)
    if (p - 1) // 4 % 2: k = (k + 2) % 4
    return k


def main():
    PD = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    PQ = int(sys.argv[2]) if len(sys.argv) > 2 else 300000
    P = [p for p in primes_upto(max(PD, PQ)) if p % 4 == 1]
    # ---- Prop 1.1 bijection + Prop 1.2 (a),(b)
    nprime = ncert = bad = 0
    for p in P:
        if p > PD: break
        nprime += 1
        S1 = set()
        for d in range(1, (p + 3) // 8 + 2):
            for w in divisors(p + 4 * d):
                if w % (4 * d) == 4 * d - 1 and w < p + 4 * d:
                    g = (p + 4 * d) // w; c = (w + 1) // (4 * d); S1.add((c * g - 1, g, d))
        S2 = set()
        for m in range(1, (p + 1) // 3 + 2):
            g = (-p) % (4 * m)
            if g and (m + 1) % g == 0: S2.add((m, g, (p + g) // (4 * m)))
        if S1 != S2: bad += 1; print("Prop1.1 mismatch", p)
        # (iii): g = 3 mod 4 and m | (p+g)/4 with m = -1 mod g
        S3 = set()
        for g in range(3, (p + 1) // 3 + 3, 4):
            for m in divisors((p + g) // 4):
                if m % g == g - 1: S3.add((m, g, (p + g) // (4 * m)))
        if S3 != S2: bad += 1; print("Prop1.1(iii) mismatch", p)
        for (m, g, d) in S2:
            ncert += 1
            c = (m + 1) // g; w = 4 * c * d - 1
            assert w * g == p + 4 * d and 4 * m * d - g == p
            dd = d
            while dd % 2 == 0: dd //= 2
            mm = m
            while mm % 2 == 0: mm //= 2
            ok = (jacobi(w, p) == -1 and jacobi(g, p) == jacobi(-d, g) and jacobi(dd, p) == jacobi(-g, dd)
                  and jacobi(mm, p) == jacobi(-g, mm))
            lhs = pow(w, (p - 1) // 4, p) * pow(g, (p - 1) // 4, p) % p
            rhs = jacobi(2, p) * pow(d, (p - 1) // 4, p) % p
            if not ok or lhs != rhs: bad += 1; print("Prop1.2 fail", p, m, g, d)
    print(f"Prop 1.1 (i)=(ii)=(iii) and Prop 1.2(a),(b): {nprime} primes p<={PD}, {ncert} certificates, {bad} failures")
    # ---- quartic symbols as functions of (a,b)
    AB = {p: two_squares(p) for p in P if p <= PQ}
    # q = 3 mod 4: explicit formula
    for q in [3, 7, 11, 19, 23, 31, 43]:
        n = f = 0
        for p, (a, b) in AB.items():
            if p == q: continue
            n += 1
            if qpow4_index(q, p, a, b) != predicted_q3(q, p, a, b): f += 1
        print(f"q={q}: explicit law (q/p)_4 = (-1)^((p-1)/4)*((a+bi)/(a-bi))^((q+1)/4) [i->a/b]: {n} primes, {f} failures")
    # q = 3 mod 4: depends on (a:b) mod q and p mod 8 only (b mod 4); conflicts without p mod 8
    for q in [3, 7, 11]:
        D1, D2 = {}, {}; c1 = c2 = 0
        for p, (a, b) in AB.items():
            if p == q: continue
            k = qpow4_index(q, p, a, b)
            # projective point (a:b) mod q
            if b % q: key = (a * pow(b, -1, q) % q, 'aff')
            else: key = (0, 'inf')
            if D1.setdefault((key, p % 8), k) != k: c1 += 1
            if D2.setdefault(key, k) != k: c2 += 1
        print(f"q={q}: function of ((a:b) mod q, p mod 8): {c1} conflicts; of (a:b) mod q alone: {c2} conflicts")
    # q = 1 mod 4: function of (a mod q, b mod q) alone (reviewer's derivation), no 2-adic data
    for q in [5, 13, 17, 29, 37]:
        D = {}; c = 0
        for p, (a, b) in AB.items():
            if p == q: continue
            k = qpow4_index(q, p, a, b)
            if D.setdefault((a % q, b % q), k) != k: c += 1
        print(f"q={q}: function of (a mod q, b mod q) alone: {c} conflicts")
    # q = 2
    for mod in [8, 16]:
        D = {}; c = 0
        for p, (a, b) in AB.items():
            k = qpow4_index(2, p, a, b)
            if D.setdefault((a % mod, b % mod), k) != k: c += 1
        print(f"q=2: function of (a, b) mod {mod}: {c} conflicts")
    # Burde: (p/q)_4 (q/p)_4 = ((ac - bd)/q) for (p/q)=1
    Q = [q for q in P if q < 200]
    n = f1 = f2 = 0
    for q in Q:
        c_, d_ = two_squares(q)
        for p, (a, b) in AB.items():
            if p > 20000: break
            if p == q or jacobi(p, q) != 1: continue
            s1 = 1 if pow(p, (q - 1) // 4, q) == 1 else -1
            s2 = 1 if pow(q, (p - 1) // 4, p) == 1 else -1
            n += 1
            if s1 * s2 != jacobi(a * c_ - b * d_, q): f1 += 1
            if s1 * s2 != jacobi(a * c_ - b * d_, p): f2 += 1
    print(f"Burde ((ac-bd)/q): {n} pairs (q<200, p<2e4, (p/q)=1), {f1} failures; variant ((ac-bd)/p): {f2} failures")


if __name__ == "__main__":
    main()
