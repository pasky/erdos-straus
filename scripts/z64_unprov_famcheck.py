"""z64 UNPROV falsifier for Thm A vs Thm B (Z64_UNPROV.md §3).

Thm B: every class solvable by polynomials is IOpen-provable.  Thm A: no unit-square class is NOI-provable.
They would contradict each other if some polynomially solvable primitive class n = rho (mod Q) contained a unit square.
This script enumerates the four explicit ET identity families used in scripts/z64_unprov_mordell840.py (T2a, T1a, T1d, T2c)
with modulus Q <= QMAX, and checks that no primitive family class rho mod Q is a unit square mod Q.
(ET Prop 1.6 / Mordell-Schinzel predict exactly this; a hit would refute one of the two theorems.)
Output: data/z64/unprov/famcheck.txt
"""
import sys
from math import gcd

QMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4000


def divisors(m):
    out = []
    d = 1
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            if d * d != m:
                out.append(m // d)
        d += 1
    return out


def unit_squares(Q, cache={}):
    if Q not in cache:
        cache[Q] = {(s * s) % Q for s in range(Q) if gcd(s, Q) == 1}
    return cache[Q]


def members():
    # T2a: -e mod 4ab, e | a+b, gcd(e,4ab)=1
    for a in range(1, QMAX // 4 + 1):
        for b in range(a, QMAX // (4 * a) + 1):
            Q = 4 * a * b
            for e in divisors(a + b):
                if gcd(e, Q) == 1:
                    yield ('T2a', Q, (-e) % Q)
    # T1a: -f mod 4ad, f | 4a^2 d + 1
    for a in range(1, QMAX // 4 + 1):
        for d in range(1, QMAX // (4 * a) + 1):
            Q = 4 * a * d
            for f in divisors(4 * a * a * d + 1):
                yield ('T1a', Q, (-f) % Q)
    # T1d: n e = -1 mod 4ab, e | a+b, gcd(e,4ab)=1
    for a in range(1, QMAX // 4 + 1):
        for b in range(a, QMAX // (4 * a) + 1):
            Q = 4 * a * b
            for e in divisors(a + b):
                if gcd(e, Q) == 1:
                    yield ('T1d', Q, (-pow(e, -1, Q)) % Q)
    # T2c: -4a^2 d - e mod 4ade, gcd(4ad, e)=1
    for a in range(1, QMAX // 4 + 1):
        for d in range(1, QMAX // (4 * a) + 1):
            for e in range(1, QMAX // (4 * a * d) + 1):
                if gcd(4 * a * d, e) == 1:
                    Q = 4 * a * d * e
                    yield ('T2c', Q, (-4 * a * a * d - e) % Q)


def main():
    n = 0
    prim = 0
    bad = []
    for name, Q, rho in members():
        n += 1
        if gcd(rho, Q) != 1:
            continue
        prim += 1
        if rho in unit_squares(Q):
            bad.append((name, Q, rho))
    lines = [f"# z64 UNPROV famcheck: QMAX={QMAX}",
             f"# family members enumerated: {n}; primitive: {prim}",
             f"# primitive family classes containing a unit square: {len(bad)}"]
    lines += [str(b) for b in bad[:50]]
    open('data/z64/unprov/famcheck.txt', 'w').write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == '__main__':
    main()
