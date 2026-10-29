#!/usr/bin/env python3
"""Exact small checks for untruncated growing-rank cap classes and sieve."""
import json
from fractions import Fraction
from itertools import product
from math import isqrt, log, prod
from z51_lcaps_toy import primes, factor


def main():
    ps = primes(200000)
    prime_set = set(ps)
    checks = 0
    rows = []
    for S, E in [([3], 4), ([3, 5], 3), ([3, 5, 7], 2)]:
        P = prod(S)
        qs = [prod(s**a for s, a in zip(S, aa))
              for aa in product(range(E+1), repeat=len(S))]
        B = len(qs)
        assert B == (E+1)**len(S) and len(set(qs)) == B
        ell_list = [ell for ell in ps if ell % (4*P) == 4*P-1]
        good = bad = overflow = local_checks = 0
        for ell in ell_list:
            residues = {(-4*q*q) % ell for q in qs}
            assert all(pow(t, (ell-1)//2, ell) == ell-1 for t in residues)
            good += len(residues) == B
            bad += len(residues) != B
            if local_checks >= 200:
                continue
            for Q in qs:
                p = (-4*Q*Q) % ell
                p += ell * (((1-p)*pow(ell, -1, 8)) % 8)
                while p not in prime_set and p <= 200000:
                    p += 8*ell
                if p > 200000 or p in S:
                    continue
                D = Q*Q
                A = (ell+1)//4
                V = (p+4*D)//ell
                assert (p+4*D) % ell == 0 and (p+V) % 4 == 0
                x, y = (p+V)//4, p*A
                z = Fraction(p*x*A, D)
                assert Fraction(4, p) == Fraction(1, x)+Fraction(1, y)+1/z
                root = isqrt(z.denominator)
                assert root*root == z.denominator
                assert root % 2 and root % p
                ff = factor(root)
                assert all(s in S and b <= E and y % s == 0 for s, b in ff.items())
                checks += 1
                local_checks += 1
                overflow += z.denominator > 1
                if local_checks >= 200:
                    break
        # Pairwise integer differences give a valid union bound on bad primes.
        pair_counts = sum(sum((u*u-v*v) % ell == 0 for ell in ell_list)
                          for i, u in enumerate(qs) for v in qs[:i])
        assert bad <= pair_counts
        rows.append(dict(S=S, E=E, B=B, primes=len(ell_list), good=good,
                         bad=bad, pair_collision_count=pair_counts, overflow=overflow))
    # Actual Montgomery bound with an exactly summed denominator, toy scale.
    X, Qlevel, E = 2000, 44, 2
    ell_list = [ell for ell in ps if ell <= Qlevel and ell % 12 == 11]
    forbidden = {ell: {(-4*3**(2*a)) % ell for a in range(E+1)} for ell in ell_list}
    terms = {1: Fraction(1)}
    for ell in ell_list:
        w = len(forbidden[ell])
        terms.update({q*ell: v*Fraction(w, ell-w) for q, v in list(terms.items())
                      if q*ell <= Qlevel})
    Ls = sum(terms.values())
    actual = sum(all(n % ell not in forbidden[ell] for ell in ell_list)
                 for n in range(1, X+1))
    assert actual*Ls <= X+Qlevel**2
    print(json.dumps(dict(status='PASS', rational_checks=checks, rows=rows,
                          sieve=dict(X=X, Q=Qlevel, actual=actual,
                                     L=str(Ls), bound=float((X+Qlevel**2)/Ls))), indent=2))


if __name__ == '__main__':
    main()
