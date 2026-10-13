"""R168 from-scratch check of Thm 7.3 / Cor 7.4 (block witnesses miss p ≡ 1 mod M_E)."""
import sys
from math import gcd, log, lcm
from sympy import primerange, isprime, factorint, divisors


def M(E):
    B = (E + 1) / 4
    m = 1
    for k in range(1, E + 1): m = lcm(m, k)
    K2 = 0
    while 2 ** (K2 + 1) <= B: K2 += 1
    m *= 2 ** (K2 + 3)
    for l in primerange(3, int(B) + 1):
        K = 0
        while l ** (K + 1) <= B: K += 1
        m *= l ** (K + 1)
    return m


def smooth_part(n, B):
    s = 1
    for l in primerange(2, int(B) + 1):
        while n % l == 0: n //= l; s *= l
    return s


def block_witness(p, e, E):
    N = (p + e) // 4
    s = smooth_part(N, (E + 1) / 4); P = N // s; c = P % e
    for a in divisors(s):
        for b in divisors(s // a):
            for (x, y) in ((a, b), (a * c, b), (a, b * c)):
                if (x + y) % e == 0: return True
    return False


def full_witness(p, e):
    N = (p + e) // 4
    return any((a + b) % e == 0 for a in divisors(N) for b in divisors(N // a))


# Cor 7.4 constant: log M_E / E
for E in (50, 200, 1000, 4000):
    print(f"E={E}: log M_E / E = {log(M(E)) / E:.3f}")

full = len(sys.argv) > 1
for E in (7, 11, 15, 19, 23):
    m = M(E); found = 0; viol = 0; s_ok = True; solved_private = 0; checked_full = 0
    k = 1
    while found < 12:
        p = 1 + k * m; k += 1
        if not isprime(p): continue
        found += 1
        for e in range(3, E + 1, 4):
            N = (p + e) // 4
            s_ok &= smooth_part(N, (E + 1) / 4) == (1 + e) // 4
            viol += block_witness(p, e, E)
        if full and found <= 4:
            checked_full += 1
            solved_private += any(full_witness(p, e) for e in range(3, E + 1, 4))
    print(f"E={E} M_E={m} (log10 {log(m,10):.1f}): primes {found}, s_e=(1+e)/4 always: {s_ok}, block-witness violations {viol}"
          + (f"; of first {checked_full}, solved by a private witness at some e<=E: {solved_private}" if full else ""))
