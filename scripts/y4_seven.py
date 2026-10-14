"""O212 (BRAINSTORM/y4_seven_control): is the 7-slice set S_7 a fibre of simple Jacobi data?
For words (t,u,v) of odd n <= NMAX, 7 !| n, test whether membership in S_7 (7 | tu-1, tv-1, t, u or v) is a function
of F = (n mod 56, (A/n), (A*/n), (t/n), (u/n), (v/n)) [Jacobi; 0 when not coprime].  Prints #feature-classes that are mixed.
Usage: PYTHONPATH=scripts uv run python scripts/y4_seven.py [NMAX]"""
import sys
from math import gcd
from collections import defaultdict
from sympy import jacobi_symbol as J
from y4_oddslice_cells import words


def jac(a, n):
    return J(a % n, n) if gcd(a, n) == 1 else 0


if __name__ == '__main__':
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 601
    cls = defaultdict(set)
    tot = 0
    for n in range(3, NMAX + 1, 2):
        if n % 7 == 0:
            continue
        for (t, u, v) in words(n):
            A, As = t * u - 1, t * v - 1
            if A < 1 or gcd(A, n) != 1:
                continue
            tot += 1
            mem = any(x % 7 == 0 for x in (A, As, t, u, v))
            F = (n % 56, jac(A, n), jac(As, n), jac(t, n), jac(u, n), jac(v, n))
            cls[F].add(mem)
    mixed = sum(1 for s in cls.values() if len(s) > 1)
    print('words', tot, 'feature classes', len(cls), 'mixed', mixed)
