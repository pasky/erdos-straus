#!/usr/bin/env python3
"""Finite check of the new 029 fixed-progression/index-two specialization.
Not a test of the analytic manuscripts. Only small modular objects are built.
"""
import json
from pathlib import Path
from sympy import isprime, legendre_symbol, n_order
from sympy.ntheory.modular import crt

ROOT = Path(__file__).resolve().parents[1]

def main():
    rows = []
    for n in [5, 13, 17, 29, 193, 409, 577, 2521, 3361]:
        assert isprime(n) and n % 4 == 1
        a = next(a for a in range(2, n) if legendre_symbol(a, n) == -1)
        for s in [3, 5, 7, 11]:
            if s == n:
                continue
            u, modulus = map(int, crt([8, s, n], [3, s-1, a]))
            assert u % 4 == 3 and (u-1)//2 % 2 == 1
            assert (u-1) % s and (u-1) % n
            witness = None
            for j in range(200):
                r = u + j*modulus
                if not isprime(r):
                    continue
                assert legendre_symbol(n, r) == -1
                assert legendre_symbol(s, r) == 1
                order = int(n_order(s, r))
                if order == (r-1)//2:
                    target = (-n * pow(4, -1, r)) % r
                    assert order % 2 == 1 and pow(target, order, r) == 1
                    witness = dict(n=n, s=s, u=u, modulus=modulus, r=r,
                                   order=order, square_target=target)
                    break
            assert witness is not None, (n, s)
            rows.append(witness)
    out = ROOT/'data/z47_oai_impact/specialization-check.json'
    out.write_text(json.dumps({'scope': 'Finite compatibility and index-two examples; no analytic verification',
                               'examples': rows}, indent=2)+'\n')
    print(len(rows), 'fixed-progression examples; max prime', max(r['r'] for r in rows))
    for row in rows:
        if row['s'] == 3:
            print(row)

if __name__ == '__main__':
    main()
