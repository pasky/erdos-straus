#!/usr/bin/env python3
"""POINTWISE_OMEGA2 §8 (EVIDENCE): single-prime atoms at a prime l (PO Lemma 9.1, all m coprime to l).

Parametrisation used (§8): an atom with rough part l is (r', x, t) with
  x = 4P, P = s r' <= l/2 (s squarefree), d := t x - l >= 1, d | r' x + 1,
  m := (r' x + 1)/d, k := m t - r' >= r', m l = 3 (mod 4);
then A = P k = (m l + 1)/4, D = P r', class -4D = -r'/k (mod l), partner -(4D)^{-1}.
Prints per l: #triples, #classes (with partners), max over r' of #triples, and the
largest r' and t occurring.

usage: omega2_ffull.py l1 l2 ...   or   omega2_ffull.py range A B step
"""
import sys
from sympy import divisors, isprime


def sqfree(n):
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def triples(l):
    out = []
    for P in range(1, l // 2 + 1):
        x = 4 * P
        for rp in divisors(P):
            if not sqfree(P // rp):
                continue
            N0 = rp * x + 1
            for d in divisors(N0):
                if (l + d) % x:
                    continue
                t = (l + d) // x
                m = N0 // d
                k = m * t - rp
                if k < rp or (m * l) % 4 != 3:
                    continue
                out.append((rp, x, t, d, m, k))
    return out


def report(l):
    T = triples(l)
    cls = set()
    byr = {}
    for rp, x, t, d, m, k in T:
        D = (x // 4) * rp
        cls.add((-4 * D) % l)
        cls.add((-pow(4 * D, -1, l)) % l)
        byr[rp] = byr.get(rp, 0) + 1
    mr = max(byr.items(), key=lambda kv: kv[1]) if byr else (0, 0)
    print(f"l={l} triples={len(T)} classes={len(cls)} triples/sqrt(l)={len(T)/l**0.5:.3f} "
          f"max_r'={max((t[0] for t in T), default=0)} max_t={max((t[2] for t in T), default=0)} "
          f"busiest r'={mr[0]} ({mr[1]}) #r'>1: {sum(v for r, v in byr.items() if r > 1)}")
    return T


def typeI_points(n, sqfree_d=True):
    """N-points (a,b,c,d,e,f) of Elsholtz-Tao's Sigma_I^n with a <= b (ET (2.1)-(2.9)),
    enumerated via (a,c,d): f = 4acd - n >= 1, f | 4a^2 d + 1, e = (4a^2 d+1)/f, b = ce - a."""
    pts = []
    a = 1
    while 4 * a <= 3 * n + n:
        c = 1
        while 4 * a * c <= 4 * n:
            d = 1
            while 4 * a * c * d <= 4 * n:   # Lemma 2.8: acd <= 3n/4 < n
                f = 4 * a * c * d - n
                if f >= 1 and (4 * a * a * d + 1) % f == 0 and (not sqfree_d or sqfree(d)):
                    e = (4 * a * a * d + 1) // f
                    b = c * e - a
                    if b >= a:
                        assert 4 * a * b * d == n * e + 1 and b * f == n * a + c
                        pts.append((a, b, c, d, e, f))
                d += 1
            c += 1
        a += 1
    return pts


def dictionary_check(nmax):
    """atoms with rough part r (all m, D <= A) == Type I points of Sigma_I^r (a<=b, d squarefree)."""
    bad = 0
    tot = 0
    for r in range(3, nmax + 1, 2):
        A1 = sorted((rp, x // 4 // rp, (rp + k) // m, m, d) for rp, x, t, d, m, k in triples_r(r))
        A2 = sorted((a, d, c, e, f) for a, b, c, d, e, f in typeI_points(r))
        tot += len(A1)
        if A1 != A2:
            bad += 1
    print(f"dictionary check r<= {nmax} odd: {tot} atoms, mismatching r: {bad}")


def triples_r(r):
    """triples() for an arbitrary odd r (rough part), without the mr = 3 (4) filter replaced by
    the general one: M = m r = 3 (mod 4)."""
    out = []
    for P in range(1, r // 2 + 1):
        x = 4 * P
        for rp in divisors(P):
            if not sqfree(P // rp):
                continue
            N0 = rp * x + 1
            for d in divisors(N0):
                if (r + d) % x:
                    continue
                t = (r + d) // x
                m = N0 // d
                k = m * t - rp
                if k < rp or (m * r) % 4 != 3:
                    continue
                out.append((rp, x, t, d, m, k))
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "dict":
        dictionary_check(int(a[1])); sys.exit()
    if a[0] == "cmp":   # classes from triples() vs PO's F_full (pointwise_omega_haar.py)
        from pointwise_omega_haar import F_full
        for l in map(int, a[1:]):
            c = set()
            for rp, x, t, d, m, k in triples(l):
                D = (x // 4) * rp
                c.add((-4 * D) % l); c.add((-pow(4 * D, -1, l)) % l)
            print(l, "match" if c == F_full(l) else "MISMATCH", len(c))
        sys.exit()
    if a[0] == "range":
        A, B, st = map(int, a[1:])
        ls = []
        x = A
        while x < B:
            y = x
            while not isprime(y):
                y += 1
            ls.append(y)
            x += st
    else:
        ls = list(map(int, a))
    for l in ls:
        report(l)

