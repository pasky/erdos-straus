#!/usr/bin/env python3
"""Hostile review (round 2) of POINTWISE_OMEGA.md §8: Lemma 8.1 (ck_min >= n_p),
the notes (48.12) records, the p=193 (c,k)=(26,2) example, and Prop 8.3's construction
on small instances.  Independent code (nothing imported from pointwise_omega_*/verify.py).

ck_min(p) = min{ ck : (c,k) in B_p, sf(c) not in {1,2,3,6}, exists D | p^2+4ck^2, D = -p mod 4ck }
B_p = {1<=k<=floor(2p/3), 1<=c<=floor((2p+k)/(4k)), gcd(p,ck)=1}   (notes (36.1), (44.2), (48.9))
Usage: PYTHONPATH=scripts uv run python scripts/review_omega_typeI.py [PMAX=30000]
"""
import sys
from sympy import primerange, factorint, divisors, legendre_symbol, isprime


def sqfree_part(c):
    s = 1
    for q, e in factorint(c).items():
        if e % 2:
            s *= q
    return s


def slice_positive(p, c, k):
    h = 4 * c * k
    N = p * p + 4 * c * k * k
    t = (-p) % h
    return any(d % h == t for d in divisors(N))


def ck_min(p, cap=400):
    for P in range(1, cap + 1):
        for k in divisors(P):
            c = P // k
            if not (1 <= k <= (2 * p) // 3 and 1 <= c <= (2 * p + k) // (4 * k)):
                continue
            if (c * k) % p == 0:
                continue
            if sqfree_part(c) in (1, 2, 3, 6):
                continue
            if slice_positive(p, c, k):
                return P
    return None


def least_qnr(p):
    n = 2
    while legendre_symbol(n, p) == 1:
        n += 1
    return n


def main():
    PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
    ok = True
    viol = eq = cnt = 0
    recs = []
    best = 0
    for p in primerange(5, PMAX):
        if p % 24 != 1:
            continue
        cnt += 1
        cm = ck_min(p)
        npp = least_qnr(p)
        if cm is None or cm < npp:
            viol += 1
        eq += (cm == npp)
        if cm is not None and cm > best:
            best = cm
            recs.append((p, cm))
    print(f"p=1 (24), p<{PMAX}: {cnt} primes; ck_min<n_p violations: {viol}; equality: {eq}")
    print("strict ck_min records (p, ck_min):", recs)
    exp = [(73, 7), (193, 10), (241, 11), (769, 13), (1321, 21), (2281, 26), (2521, 38), (9601, 67), (12289, 77)]
    if PMAX > 12289:
        ok &= (recs == exp) or print("records differ from notes (48.12):", exp)
    ok &= viol == 0 and cnt == 385 if PMAX == 30000 else viol == 0
    # p=193, (26,2) example
    p, c, k = 193, 26, 2
    N = p * p + 4 * c * k * k
    h = 4 * c * k
    hit = [d for d in divisors(N) if d % h == (-p) % h]
    pp = [q ** e for q, E in factorint(N).items() for e in range(1, E + 1)]
    print(f"p=193,(c,k)=(26,2): N={N}={factorint(N)}, h={h}, -p mod h={(-p) % h}, "
          f"hitting divisors {hit}, hitting prime powers {[d for d in pp if d % h == (-p) % h]}")
    # Prop 8.3 construction, small instance: l=5, L=24*7, a = 1 (a/5)=1 but 5 not | L
    for (l, L, a) in ((5, 168, 1), (7, 120, 1), (13, 24 * 13, 73), (11, 24 * 11 * 5, 241)):
        # choose c0 mod 4l: c0 = a mod gcd(L,4l), c0 = 1 (4), (c0/l) = -1 (possible only if l !| L or (a/l)=-1)
        from math import gcd
        g = gcd(L, 4 * l)
        c0s = [c0 for c0 in range(1, 4 * l) if c0 % 4 == 1 and c0 % l and c0 % g == a % g
               and legendre_symbol(c0 % l, l) == -1]
        if not c0s:
            print(f"  Prop 8.3 l={l}, L={L}, a={a}: no c0 (hypothesis of the contrapositive not met)")
            continue
        c0 = c0s[0]
        q = next(q for q in primerange(3, 10 ** 6) if q % (4 * l) == (-c0) % (4 * l) and L % q)
        rho = next(r for r in range(1, q) if (r * r + 4 * l) % q == 0)
        # find primes p = a (L), = c0 (4l), = rho (q)
        from sympy.ntheory.modular import crt
        mod = L * 4 * l // g * q
        base = int(crt([L, 4 * l, q], [a, c0, rho])[0]) if g == 4 else None
        if base is None:
            base = int(crt([L, q], [a, rho])[0])
            mod = L * q
        found = 0
        bad = 0
        n = base
        while found < 20:
            n += mod
            if isprime(n) and n > 4 * l:
                found += 1
                if not slice_positive(n, l, 1):
                    bad += 1
        print(f"  Prop 8.3 l={l}, L={L}, a={a}: c0={c0}, q={q}, rho={rho}: 20 primes, slice (l,1) zero at {bad}")
        ok &= bad == 0
    print("ALL OK" if ok else "FAILURE")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
