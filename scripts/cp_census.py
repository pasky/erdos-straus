"""O203 census (COMPOSITION_ES §4): for each n (primes in [lo, hi], or odd squares as T1 control), list all ES
points (B = 1 V_n points) via Thm 1.3: mu = nj + t, D = 4tj - 1 | n + 4t^2.  For each, run one period of the CF of
sqrt(N), N = 4(mu^2 - n), and record every proper divisor d' of D (1 < d' < D) such that the divisor of norm d' of
the ES ideal e_mu = (eps_mu) is principal in O' = Z[2 sqrt f] (Lagrange: all primitive reps of |norm| < sqrt N are
convergents; orientation test p*j = +-(1 - 2 mu j) q mod d'), with the sign (-1)^k of the generator's norm.
Outputs per n: #ES points, #with D prime, #with a principal proper divisor ("decomposable"), #V-decomposable
(chain of >= 3 negative-norm principal pieces, R202 sense), #skipped (period > cap).
Usage: cp_census.py lo hi cap [squares]"""
import sys
from math import isqrt, gcd
from sympy import isprime, divisors, primerange


def es_points(n):
    out = []
    for t in range(1, n + 1):
        M = n + 4 * t * t
        for D in divisors(M):
            if D % (4 * t) == 4 * t - 1:
                j = (D + 1) // (4 * t)
                out.append((n * j + t, D, j))
    return out


def principal_divisors(n, mu, D, j, cap):
    N = 4 * (mu * mu - n)
    a0 = isqrt(N)
    m, d, a = 0, 1, a0
    p_prev, p, q_prev, q = 1, a0, 0, 1
    xE = 1 - 2 * mu * j
    found = {}
    k = 0
    seen_es = False
    while True:
        k += 1
        m = d * a - m
        d = (N - m * m) // d
        a = (a0 + m) // d
        if D % d == 0 and d > 1:
            s = (-1) ** k
            if (p * j - xE * q) % d == 0 or (p * j + xE * q) % d == 0:
                if d == D:
                    if s == -1 and k == (3 if mu > 2 * n else 1):
                        seen_es = True
                else:
                    found.setdefault(d, set()).add(s)
        if d == 1 and k % 2 == 0:
            break
        if k > cap:
            return None
        p_prev, p = p, a * p + p_prev
        q_prev, q = q, a * q + q_prev
    assert seen_es, (n, mu, D)
    return found


def vdecomp(D, found):
    """chain 1 | d1 | d2 | D, d1 negative principal, d2 positive principal (then the 3 quotients are negative)."""
    neg = [d for d, s in found.items() if -1 in s]
    pos = [d for d, s in found.items() if 1 in s]
    return any(d2 % d1 == 0 and d2 > d1 for d1 in neg for d2 in pos)


def main():
    lo, hi, cap = map(int, sys.argv[1:4])
    squares = len(sys.argv) > 4
    ns = [m * m for m in range(3, isqrt(hi) + 1, 2) if m * m >= lo] if squares else list(primerange(max(lo, 5), hi + 1))
    tot = [0] * 5
    nany = 0
    for n in ns:
        c = [0] * 5
        for mu, D, j in es_points(n):
            c[0] += 1
            if isprime(D):
                c[1] += 1
                continue
            fd = principal_divisors(n, mu, D, j, cap)
            if fd is None:
                c[4] += 1
                continue
            if fd:
                c[2] += 1
            if vdecomp(D, fd):
                c[3] += 1
        if c[2]:
            nany += 1
        tot = [x + y for x, y in zip(tot, c)]
        if len(ns) <= 40:
            print(n, "ES", c[0], "Dprime", c[1], "decomp", c[2], "Vdecomp", c[3], "skipped", c[4])
    print("TOTAL n", len(ns), "ES points", tot[0], "D prime", tot[1], "decomposable", tot[2], "V-decomposable", tot[3],
          "skipped", tot[4], "| n with >=1 decomposable ES point", nany)


if __name__ == "__main__":
    main()
