"""R227: which side carries the K0 = 8 depletion?  For primes p = m^2 + K0 (m = floor sqrt p) in (1e5, 5e6), p = 1 (4):
share of ordered words lying on the u = 1 (or v = 1) side and their chi = -1 rate; plus, for K0 = 20, the u = 16 side
(u(K0+u) = 16*36, gcd(m, 36) >= 3 forced).  Words with u = U0: A = t*U0 - 1 | p + U0, A = -1 (mod U0).
usage: uv run --with sympy python scripts/review_r227_k0.py
"""
from math import isqrt
from sympy import isprime, divisors, jacobi_symbol as J, factorint


def side_words(p, u0):
    out = []
    for A in divisors(p + u0):
        if (A + 1) % u0 == 0 and A >= 1:
            out.append(J(A, p))
    return out


for K0, u0 in ((8, 1), (20, 16), (24, 1), (48, 1)):
    tot = neg = 0
    n_p = 0
    allw = 0
    for m in range(isqrt(10 ** 5), isqrt(5 * 10 ** 6) + 1):
        p = m * m + K0
        if p % 4 != 1 or not isprime(p) or p >= 5 * 10 ** 6:
            continue
        n_p += 1
        w = side_words(p, u0)
        tot += 2 * len(w)  # (t,u0,v) and (t,v,u0); overlap u=v=u0 negligible
        neg += 2 * sum(1 for c in w if c == -1)
        if K0 == 48 and n_p <= 0:
            pass
    print(f"K0={K0} side u={u0}: primes {n_p}, words on side (x2 ordered) {tot}, per prime {tot / max(n_p, 1):.1f}, "
          f"chi=-1 rate {neg / max(tot, 1):.3f}")

# K0 = 48: u = 1 side p+1 = m^2 + 49; 7 | m makes it 49 * clean (psi(7) = -1), else clean.  Split primes by 7 | m.
for cond in (True, False):
    tot = neg = n_p = 0
    for m in range(isqrt(10 ** 5), isqrt(5 * 10 ** 6) + 1):
        p = m * m + 48
        if p % 4 != 1 or not isprime(p) or (m % 7 == 0) != cond:
            continue
        n_p += 1
        w = side_words(p, 1)
        tot += len(w)
        neg += sum(1 for c in w if c == -1)
    print(f"K0=48, 7|m={cond}: primes {n_p}, u=1 side chi=-1 rate {neg / max(tot, 1):.3f}")
