#!/usr/bin/env python3
"""Replay existing forest/certificate helpers on required controls; not a new census.
PYTHONPATH=scripts uv run --with sympy python scripts/z50_ajastra_controls.py
"""
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from sympy import isprime
from z43_astra_check import divisor_edges, certificates

R_ZEROS = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321,
           1134241, 1724209, 1726201, 5212561, 8813281]
HARD = [193, 409, 577, 2521, 3361, 5569, 9601, 66529, 8813281]


def main():
    rows = []
    checked = 0
    for n in sorted(set(R_ZEROS + HARD)):
        assert isprime(n)
        edges = sorted(divisor_edges(n))
        star = [(u, v) for u, v in edges if ((n+u+v)//(u*v)) % 4 == 0]
        if n in R_ZEROS:
            assert not star
        good = [(u, v) for u, v in edges if list(certificates(n, u, v))]
        U = [(u, v) for u, v in edges
             if any(w % 4 == 0 or (w+n) % 8 == 0 for w in (u, v))]
        assert good and U
        for u, v in good:
            for xyz in certificates(n, u, v):
                assert min(xyz) > 0
                assert sum((Fraction(1, x) for x in xyz), Fraction()) == Fraction(4, n)
                checked += 1
        rows.append(dict(n=n, edges=len(edges), star_unordered=len(star),
                         ES5=len(good), U=len(U), U_example=U[0]))
    squares = 0
    for m in range(3, 102, 2):
        n = m*m
        for u, v in divisor_edges(n):
            assert not list(certificates(n, u, v))
            assert not any(w % 4 == 0 or (w+n) % 8 == 0 for w in (u, v))
        squares += 1
    eight = []
    for n in [17, 241]:
        edges = divisor_edges(n)
        assert not any(list(certificates(n, u, v, 8)) for u, v in edges)
        eight.append(dict(n=n, edges=len(edges), numerator8_slot_certificates=0))
    result = dict(primes=rows, rational_certificates_checked=checked,
                  odd_squares_checked=squares, numerator8=eight,
                  scope='Existing helpers replayed; numerator-8 check concerns slots only, not a fresh exhaustive ES8 solver.')
    out = Path('data/z50_ajastra')
    out.mkdir(parents=True, exist_ok=True)
    (out/'controls.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
