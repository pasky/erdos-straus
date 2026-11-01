#!/usr/bin/env python3
"""Small exact checks for audit A; no random heuristics or large arrays."""
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path


def factors(n):
    out = {}
    q = 2
    while q * q <= n:
        while n % q == 0:
            out[q] = out.get(q, 0) + 1
            n //= q
        q += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n, square=False):
    ds = [1]
    for q, a in factors(n).items():
        ds = [d * q**e for d in ds for e in range((2 if square else 1)*a + 1)]
    return ds


def solutions(n):
    out = set()
    for x in range(n//4 + 1, 3*n//4 + 1):
        g = gcd(4*x - n, n*x)
        a, b = (4*x - n)//g, n*x//g
        for d in divisors(b, square=True):
            if d > b or (d + b) % a or (b*b//d + b) % a:
                continue
            y, z = (d+b)//a, (b*b//d+b)//a
            if x <= y <= z:
                assert Fraction(4,n) == sum(Fraction(1,v) for v in (x,y,z))
                out.add((x,y,z))
    return sorted(out)


def star(p):
    out = []
    for c in range(1, (p+2)//4 + 1):
        n = 4*c*p+1
        for d in divisors(n):
            if d % (4*c) == 4*c-1:
                out.append((c,d))
    return out


def main():
    result = {}
    assert not star(409)
    result['Z1352_Z1473'] = {'p': 409, 'all_star_hits': star(409),
                            'exhaustive_C_bound': (409+2)//4,
                            'reason_bound': 'p=4CuB-u-B >=4C-2 for positive u,B'}
    # The proposed Fermat congruence loses the divisor class already at C=1.
    p,c = 409,1
    x,y = 2*p+1,2*p
    assert x*x-y*y == 4*c*p+1 and (x+1) % (2*c) == 0
    assert (x-y) % (4*c) != 4*c-1
    result['Z1956'] = {'p': p, 'C': c, 'X': x, 'Y': y,
                       'factors': [x-y,x+y], 'weak_congruence_true_but_no_star_hit': True}
    # Mordell-hard residue classes mod 840 can be covered by larger moduli.
    n = 5881
    xyz = ((3*n+1)//11, 3*n, 3*n*((3*n+1)//11))
    assert n % 840 == 1 and (3*n+1) % 11 == 0
    assert sum(Fraction(1,v) for v in xyz) == Fraction(4,n)
    result['Z1296_Z1798'] = {'progression': 'n = 5881 + 9240k, k >= 0',
                             'identity': 'x=(3n+1)/11, y=3n, z=3nx',
                             'base_check': [n,xyz], 'all_n_are_1_mod_840': True}
    # Sharing two denominators does not require the target n to be a multiple.
    for n,xyz in [(4,(2,4,4)),(5,(2,4,20))]:
        assert sum(Fraction(1,v) for v in xyz) == Fraction(4,n)
    result['Z1964'] = {'non_scaling_move': [[4,[2,4,4]],[5,[2,4,20]]]}
    # Nonvanishing at every finite beta does not imply a positive limit.
    result['Z1325'] = 'Z(beta)=exp(-beta) is entire and zero-free but tends to zero.'
    ss = solutions(241)
    assert len(ss) == 8 and all(any(v % 3 == 0 for v in xyz) for xyz in ss)
    result['Z0863'] = {'p':241, 'solutions':ss, 'all_meet_3':True,
                       'is_global_not_local': 'For n=241, (x,y,z)=(n,n,n/2) is a positive rational solution and a 3-adic unit solution.'}
    # Demonstrate failure of the M=1 restriction, not the unproved all-M claim.
    missing = []
    for p in [73,97,193,241,409,577]:
        ss = solutions(p)
        if not any(any(v & (v-1) == 0 for v in xyz) for xyz in ss):
            missing.append(p)
    result['Z1942'] = {'M1_failures_among_test_primes': missing,
                       'scope': 'Does not prove failure for every fixed M or any density claim.'}
    path = Path('data/z52d/avenue/rank_A/checks.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
