"""R227: does R225's u-side mechanism (K0 + u = s^2, gcd(m, s) = 1, so p + u = m^2 + s^2) explain the N-/U residuals
that three-side psi-cleanliness leaves at K0 = 4, 12, 20, 28?  For primes p = m^2 + K0 in (1e5, 5e6), p = 1 (4):
enumerate words with u = s^2 - K0 (u >= 1, s <= SMAX) [and mirrored v], keep the UNFORCED ones (no psi-clean side),
report their count and chi = -1 rate, and N-/U before/after removing them (needs census file for N-, U).
usage: uv run --with sympy python scripts/review_r227_r225side.py /tmp/r227_def.txt
"""
import sys
from math import isqrt, gcd
from sympy import isprime, divisors, jacobi_symbol as J, factorint

cen = {}
for line in open(sys.argv[1]):
    f = line.split()
    cen[int(f[0])] = (int(f[2]), int(f[3]))  # Nm, U


def clean(x, p):
    return all(J(r, p) != -1 for r in factorint(x))


SMAX = 60
for K0 in (4, 12, 20, 28, 8, 16, 24, 300 + 1):
    tot = neg = 0
    Nm = U = 0
    nprim = 0
    for m in range(isqrt(10 ** 5), isqrt(5 * 10 ** 6) + 1):
        p = m * m + K0
        if p % 4 != 1 or p >= 5 * 10 ** 6 or not isprime(p) or p not in cen:
            continue
        nprim += 1
        Nm += cen[p][0]
        U += cen[p][1]
        seen = set()
        for s in range(isqrt(K0) + 1, SMAX):
            u = s * s - K0
            if u < 1 or gcd(m, s) != 1:
                continue
            for A in divisors(p + u):
                if (A + 1) % u:
                    continue
                t, v = (A + 1) // u, (p + u) // A
                B = t * v - 1
                for w in ((t, u, v), (t, v, u)):
                    if w in seen:
                        continue
                    seen.add(w)
                    if clean(A * B, p) or clean(A * v, p) or clean(B * u, p):
                        continue
                    tot += 1
                    neg += J(A, p) == -1
    print(f"K0={K0}: primes {nprim}, unforced R225-side words {tot} ({tot / max(nprim, 1):.2f}/prime), chi=-1 among them "
          f"{neg}; N-/U {Nm / max(U, 1):.4f} -> after removing {(Nm - neg) / max(U - tot, 1):.4f}")
