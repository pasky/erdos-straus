"""Exact small diagnostics, not an ES census or an asymptotic experiment.

Run: timeout 180 uv run python scripts/z52_thin_astra_checks.py
Memory: O(e + sqrt(max n)) per window; no Cartesian-product arrays.
Existing z43/z45 suites already test full ES identities and numerator-8 failures;
this script tests NEW orbit-index, spare-factor and homogenization statements.
"""
from collections import defaultdict
from itertools import product
from math import gcd, isqrt
import json
from pathlib import Path

R_ZEROS = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617,
           712321, 1134241, 1724209, 1726201, 5212561, 8813281]
HARD = sorted(set(R_ZEROS + [193, 2521, 3361, 66529]))


def primes_upto(bound):
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[:2] = b"\x00\x00"
    for q in range(2, isqrt(bound) + 1):
        if sieve[q]:
            sieve[q*q:bound+1:q] = b"\x00" * ((bound-q*q)//q+1)
    return [q for q in range(2, bound + 1) if sieve[q]]


PRIMES = primes_upto(20000)


def factor(n):
    out = []
    for q in PRIMES:
        if q*q > n:
            break
        k = 0
        while n % q == 0:
            k += 1
            n //= q
        if k:
            out.append((q, k))
    if n > 1:
        out.append((n, 1))
    return out


def ratio_count(factors, e):
    """Counts exponent vectors, NOT labelled prime-copy assignments."""
    counts = {1: 1}
    for ell, k in factors:
        nxt = defaultdict(int)
        for r, count in counts.items():
            for j in range(-k, k+1):
                nxt[r * pow(ell, j, e) % e] += count
        counts = dict(nxt)
    return counts.get(e-1, 0)


def divisor_projection(factors, q, power=2):
    out = {1}
    for ell, k in factors:
        out = {r * pow(ell, power*j, q) % q for r in out for j in range(k+1)}
    return out


def spare_factor(factors, q):
    """A nonresidue factor whose deletion still covers the odd quotient."""
    for i, (ell, k) in enumerate(factors):
        if pow(ell, (q-1)//2, q) != q-1:
            continue
        smaller = factors.copy()
        smaller[i] = (ell, k-1)
        if len(divisor_projection(smaller, q)) == (q-1)//2:
            return ell
    return None


def window(n, e, numerator=4):
    assert (n+e) % numerator == 0
    N = (n+e)//numerator
    assert gcd(N, e) == 1
    fs = factor(N)
    count = ratio_count(fs, e)
    assert count % 2 == 0  # gamma -> -gamma is free at target -1
    return N, fs, count//2


def scan(n, bound, numerator=4):
    first_hit = first_odd = first_spare = first_pigeonhole = None
    hits = odds = spares = pigeonholes = 0
    for e in range((-n) % numerator or numerator, bound+1, numerator):
        if e < 3 or gcd(e, n) != 1:
            continue
        N, fs, index = window(n, e, numerator)
        if index:
            hits += 1
            first_hit = first_hit or [e, N, index]
        if index % 2:
            odds += 1
            first_odd = first_odd or [e, N, index]
        if numerator == 4 and e in PRIME_SET and e % 4 == 3:
            # Comparator already proved/tested in s6_divisor_pigeonhole;
            # this run measures subsumption of our proposed refinement.
            divisor_classes = len(divisor_projection(fs, e, power=1))
            pigeonhole = divisor_classes > (e-1)//2
            if pigeonhole:
                pigeonholes += 1
                first_pigeonhole = first_pigeonhole or [e, N, divisor_classes]
            ell = spare_factor(fs, e)
            if ell is not None:
                assert index > 0 and pigeonhole
                spares += 1
                first_spare = first_spare or [e, N, ell]
    return dict(n=n, bound=bound, hit_windows=hits, odd_index_windows=odds,
                spare_windows=spares, pigeonhole_windows=pigeonholes,
                first_hit=first_hit, first_odd=first_odd,
                first_spare=first_spare, first_pigeonhole=first_pigeonhole)


PRIME_SET = set(PRIMES)


def homogeneous_counts(n, k, ell):
    # Projective representatives: first nonzero coordinate = 1.
    interior = boundary = 0
    for first in range(4):
        for tail in product(range(ell), repeat=3-first):
            x, y, z, w = (0,)*first + (1,) + tail
            if (k*x*y*z - n*w*(x*y+x*z+y*z)) % ell == 0:
                if x*y*z*w % ell:
                    interior += 1
                else:
                    boundary += 1
    return dict(n=n, k=k, ell=ell, interior=interior, boundary=boundary)


def main():
    # Independent exponent-vector enumeration of the new DP statistic.
    independent = 0
    for q in [3, 7, 11, 19]:
        for N in range(2, 100):
            if gcd(N, q) != 1:
                continue
            fs = factor(N)
            explicit = 0
            for exps in product(*(range(-k, k+1) for _, k in fs)):
                residue = 1
                for (ell, _), j in zip(fs, exps):
                    residue = residue * pow(ell, j, q) % q
                explicit += residue == q-1
            assert explicit == ratio_count(fs, q)
            if spare_factor(fs, q) is not None:
                assert explicit > 0
            independent += 1

    homogeneous = []
    for n, k in [(193, 4), (9, 4), (17, 8), (131, 8), (241, 8)]:
        for ell in [3, 5, 7, 11]:
            if (n*k) % ell:
                row = homogeneous_counts(n, k, ell)
                assert row['interior'] == ell*ell-3*ell+3
                assert row['boundary'] == 6*ell-2
                homogeneous.append(row)

    census = [scan(p, min(255, p-1)) for p in PRIMES if p % 4 == 1]
    controls = [scan(p, min(2047, p-1)) for p in HARD]
    # Every target ratio has e <= (n+4)/3, since a+b <= ab+1 <= N+1.
    complete_diagnostics = [scan(p, (p+4)//3) for p in [37, 2521, 9601, 19333, 66529]]
    squares = [scan(a*a, 255) for a in [3, 5, 7, 9, 11, 13, 15]]
    for row in squares:
        assert row['hit_windows'] == 0
    numerator8 = [scan(n, 1023, 8) for n in [17, 131, 241]]
    for row in numerator8:
        assert row['hit_windows'] == 0
    result = dict(
        scope='Exact bounded windows only; no universal ES claim.',
        independent_exponent_checks=independent,
        prime_count=len(census),
        census_no_hit=[r['n'] for r in census if r['first_hit'] is None],
        census_no_odd=[r['n'] for r in census if r['first_odd'] is None],
        census_no_spare=[r['n'] for r in census if r['first_spare'] is None],
        census_no_pigeonhole=[r['n'] for r in census if r['first_pigeonhole'] is None],
        census_spare_windows=sum(r['spare_windows'] for r in census),
        census_pigeonhole_windows=sum(r['pigeonhole_windows'] for r in census),
        controls=controls, complete_diagnostics=complete_diagnostics,
        squares=squares, numerator8=numerator8,
        homogeneous=homogeneous)
    path = Path('data/z52_thin_astra/checks.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ['homogeneous', 'squares', 'numerator8']}, indent=2))


if __name__ == '__main__':
    main()
