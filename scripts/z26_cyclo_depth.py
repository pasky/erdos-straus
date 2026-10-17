#!/usr/bin/env python3
"""O254 / JOINT_BUDGET §4.3, §6: cyclotomic depth of Type II certificates.

For p ≡ 1 (mod 4) enumerate ALL Type II points (window form): windows e ≡ 3 (mod 4), K = (p+e)/4,
pairs (a, b) with ab | K and e | a + b  (c = (a+b)/e, d = K/(ab)); ET class modulus M = 4ab, p ≡ -e (mod M).
Record k(sol) = ord_M(p) (capped at KCAP) and k*(p) = min over solutions.
Checks: (i) exact identity 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp) for every solution (Fractions);
        (ii) Prop 4.3: M never divides p - 1 nor p + 1;
        (iii) T1 control: odd squares n = m^2 ≡ 1 (4) have no Type II point (ET Prop 1.6).
Usage: z26_cyclo_depth.py N [hard|all]
"""
import sys
from fractions import Fraction
from collections import Counter

KCAP = 60
HARD = {1, 121, 169, 289, 361, 529}


def spf_sieve(n):
    s = list(range(n + 1))
    i = 2
    while i * i <= n:
        if s[i] == i:
            for j in range(i * i, n + 1, i):
                if s[j] == j:
                    s[j] = i
        i += 1
    return s


def divisors(n, spf):
    ds = [1]
    while n > 1:
        q = spf[n]; e = 0
        while n % q == 0:
            n //= q; e += 1
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds


def order_capped(p, M):
    if M == 1:
        return 1
    x = p % M; y = x
    for k in range(1, KCAP + 1):
        if y == 1:
            return k
        y = (y * x) % M
    return KCAP + 1


def typeII_points(n, spf):
    out = []
    emax = (n + 4) // 3
    for e in range(3, emax + 1, 4):
        if (n + e) % 4:
            continue
        K = (n + e) // 4
        if e % n == 0:
            continue
        for a in divisors(K, spf):
            for b in divisors(K // a, spf):
                if b < a:
                    continue
                if (a + b) % e == 0:
                    out.append((a, b, (a + b) // e, K // (a * b), e))
    return out


def is_prime(n, spf):
    return n > 1 and spf[n] == n


def main():
    N = int(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'hard'
    spf = spf_sieve(N + N // 3 + 8)
    hist = Counter(); worst = []; nsol_tot = 0; viol43 = 0; badid = 0; nprimes = 0
    for p in range(5, N + 1, 4):
        if not is_prime(p, spf):
            continue
        if mode == 'hard' and p % 840 not in HARD:
            continue
        nprimes += 1
        pts = typeII_points(p, spf)
        assert pts, p
        kmin = KCAP + 1
        for (a, b, c, d, e) in pts:
            M = 4 * a * b
            if (p - 1) % M == 0 or (p + 1) % M == 0:
                viol43 += 1
            if Fraction(1, a*b*d) + Fraction(1, a*c*d*p) + Fraction(1, b*c*d*p) != Fraction(4, p):
                badid += 1
            kmin = min(kmin, order_capped(p, M))
        nsol_tot += len(pts)
        hist[kmin] += 1
        worst.append((kmin, p, len(pts)))
    # T1 control
    t1 = 0
    for m in range(3, int((N) ** 0.5) + 1, 2):
        n = m * m
        if typeII_points(n, spf):
            t1 += 1
    worst.sort(reverse=True)
    print(f"N={N} mode={mode} primes={nprimes} TypeII points={nsol_tot} identity failures={badid} "
          f"Prop4.3 violations={viol43} odd squares with TypeII={t1}")
    print("k*(p) histogram (k* = min ord_{4ab}(p) over Type II points; %d = >%d):" % (KCAP + 1, KCAP),
          dict(sorted(hist.items())))
    print("largest k*:", worst[:12])


if __name__ == '__main__':
    main()
