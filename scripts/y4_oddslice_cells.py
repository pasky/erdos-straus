"""O212 (BRAINSTORM/y4_oneodd_slices): parity of the five-slice ES certificates.

A word (t,u,v) >= 1 of odd n: t*u*v - u - v = n, A = tu-1, A* = tv-1, gcd(A, n) = 1, chi = (-A/n).
Slices (m = 4): slot X in {A, A*, t, u, v} with 4 | X.  Claim (PROVED in the memo): the slice solution from slot X has
exactly one odd denominator iff v2(X) = 2, and is all-even iff v2(X) >= 3.  Checked here on every word with exact
rationals.  Then: tabulate the chi = -1 words by class (one-odd only / all-even only / both) against candidate
invariants (n mod 16, (2/n), (-1/n), (2/A), ...).
Usage: PYTHONPATH=scripts uv run python scripts/y4_oddslice_cells.py [NMAX]
"""
import sys
from fractions import Fraction
from math import gcd
from collections import Counter, defaultdict
from sympy import jacobi_symbol as J


def v2(x):
    return (x & -x).bit_length() - 1


def words(n):
    for t in range(1, n + 3):
        u = 1
        while t * u * u <= n + 2 * u:
            if t * u > 1 and (n + u) % (t * u - 1) == 0:
                v = (n + u) // (t * u - 1)
                if v >= u:
                    yield (t, u, v)
                    if v != u:
                        yield (t, v, u)
            u += 1


def slice_sols(n, t, u, v):
    """yield (slot name, v2(slot), (x,y,z)) for every slot divisible by 4"""
    A, As = t * u - 1, t * v - 1
    if A % 4 == 0:
        d = A // 4
        yield 'I', v2(A), (As * d * n, v * d, As * v * d)
    if As % 4 == 0:
        d = As // 4
        yield "I'", v2(As), (A * d * n, u * d, A * u * d)
    if t % 4 == 0:
        c = t // 4
        yield 'T', v2(t), (u * v * c, u * c * n, v * c * n)
    if u % 4 == 0:
        w = u // 4
        yield 'U', v2(u), (w * As, t * n * w, t * n * w * As)
    if v % 4 == 0:
        w = v // 4
        yield 'V', v2(v), (w * A, t * n * w, t * n * w * A)


if __name__ == '__main__':
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 801
    bad = 0
    nwords = 0
    cls_by = defaultdict(Counter)
    cellcls = defaultdict(set)
    for n in range(3, NMAX + 1, 2):
        for (t, u, v) in words(n):
            A = t * u - 1
            if A < 1 or gcd(A, n) != 1:
                continue
            nwords += 1
            chi = J((-A) % n, n) if n > 1 else 1
            odd = even = False
            for name, e, (x, y, z) in slice_sols(n, t, u, v):
                assert x and y and z
                assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
                nodd = (x & 1) + (y & 1) + (z & 1)
                if (nodd == 1) != (e == 2) or (nodd == 0) != (e >= 3):
                    bad += 1
                if e == 2:
                    odd = True
                else:
                    even = True
            if chi == 1:
                assert not (odd or even)
                continue
            assert odd or even
            c = 'both' if odd and even else ('odd' if odd else 'even')
            cellcls[(t % 8, u % 8, v % 8)].add(c)
            cls_by['n mod 16'][(n % 16, c)] += 1
            cls_by['(2/n)'][(J(2, n), c)] += 1
            cls_by['(t/n)'][(J(t % n, n) if gcd(t, n) == 1 else 0, c)] += 1
            cls_by['(2A/n),n%8'][(J(2 * A % n, n), n % 8, c)] += 1
    print('words', nwords, 'parity-rule violations', bad)
    for k, ctr in cls_by.items():
        print(k, sorted(ctr.items()))
    amb = [k for k, s in cellcls.items() if len(s) > 1]
    print('chi=-1 cells mod 8:', len(cellcls), ' cells with >1 class:', len(amb))
    print('class counts over cells:', Counter(next(iter(s)) for s in cellcls.values() if len(s) == 1))
