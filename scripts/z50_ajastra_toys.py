#!/usr/bin/env python3
"""Bounded, exact finite tests for EXSET_ARITH_JANSON_ASTRA.md.
Run: ulimit -v 8000000; timeout 180 uv run python scripts/z50_ajastra_toys.py
No dense Cartesian-product arrays; bytearrays are at most N+1 bytes.
"""
import json
import math
from fractions import Fraction
from pathlib import Path


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p::p] = b'\x00' * ((n-p*p)//p + 1)
    return [p for p in range(2, n+1) if sieve[p]]


def translated_squares(N, Q, k):
    alive = bytearray(b'\x01') * (N+1)
    alive[0] = 0
    mu, max_load, atoms = 0.0, 0.0, 0
    for p in primes_upto(Q):
        if p <= Q//2:
            continue
        square = bytearray(p)
        for x in range(p):
            square[x*x % p] = 1
        bad = [a for a in range(p) if all(not square[(a-j) % p] for j in range(k))]
        mu += len(bad)/p
        atoms += len(bad)
        max_load = max(max_load, (len(bad)-1)/p)
        for a in bad:
            start = a if a else p
            if start <= N:
                alive[start::p] = b'\x00' * ((N-start)//p+1)
    planted = set()
    for x in range(1, math.isqrt(N)+1):
        for j in range(k):
            n = x*x+j
            if n <= N:
                assert alive[n], (N, Q, k, n)
                planted.add(n)
    return dict(N=N, Q=Q, k=k, mu=mu, delta=0, max_conflict_load=max_load,
                atoms=atoms, avoiders=sum(alive), planted=len(planted),
                AJ_C1_no_error=(N+Q*Q)*math.exp(-mu), square_floor=math.sqrt(N))


def atomic_counts():
    # Independent exhaustive CRT / interval intersection verification.
    cases = 0
    N = 137
    for p in [3, 5, 7]:
        for q in [3, 5, 7]:
            for a in range(p):
                for b in range(q):
                    period = math.lcm(p, q)
                    residues = [r for r in range(period) if r % p == a and r % q == b]
                    actual = sum(n % p == a and n % q == b for n in range(1, N+1))
                    assert len(residues) <= 1
                    expected = N * len(residues) / period
                    assert abs(actual-expected) < 1 + 1e-12
                    cases += 1
    return dict(checked_intersections=cases)


def fibre_tests():
    ps = [5, 7, 11, 13]
    N, s = 10000, 6
    rows = []
    for c in range(s):
        omega = {p: {(c+j) % p for j in range(1+c % 3)} for p in ps}
        beta = {p: Fraction(len(omega[p]), p) for p in ps}
        Z = math.prod(1/(1-beta[p]) for p in ps)
        mu = sum(beta.values())
        nu = math.log(float(Z))
        actual = sum(all(n % p not in omega[p] for p in ps)
                     for n in range(1, N+1) if n % s == c)
        Nc = sum(n % s == c for n in range(1, N+1))
        for R in [1, 5, 10, 30, 100]:
            denom, prob = Fraction(0), Fraction(0)
            for mask in range(1 << len(ps)):
                chosen = [p for i, p in enumerate(ps) if mask >> i & 1]
                d = math.prod(chosen)
                if d <= R:
                    denom += math.prod(beta[p]/(1-beta[p]) for p in chosen)
                    prob += math.prod(beta[p] if p in chosen else 1-beta[p] for p in ps)
            assert denom == Z*prob
            bound = Fraction(Nc+R*R)/denom
            assert actual <= bound
            k = int(math.log(R)/math.log(min(ps)))
            if 0 < k < mu:
                chernoff = nu-float(mu)+k+k*math.log(float(mu)/k)
                assert math.log(float(denom)) <= chernoff+1e-12
            rows.append(dict(c=c, R=R, Nc=Nc, actual=actual,
                             denominator=str(denom), tail_probability=str(prob), bound=float(bound)))
    return rows


def main():
    result = dict(atomic_counts=atomic_counts(), translated_squares=[
        translated_squares(1_000_000, Q, 4) for Q in [1000, 2000, 4000]
    ])
    out = Path('data/z50_ajastra')
    out.mkdir(parents=True, exist_ok=True)
    (out/'round1.json').write_text(json.dumps(result, indent=2)+'\n')
    second = fibre_tests()
    (out/'round2.json').write_text(json.dumps(second, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    print(f'Round 2: {len(second)} exact denominator/fibre checks passed.')


if __name__ == '__main__':
    main()
