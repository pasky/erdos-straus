"""Finite stress tests, NOT a proof of the countable scheduling theorem.

uv run --no-sync python scripts/z73_prime_sign_audit.py
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import gcd


def check_twist_projection(q):
    # Dirichlet output 1+(P-1)Y; then the row YU+(P-1)V=1 on Y != 0.
    # The five primes tested include a geometrically reducible divisor P²-2
    # and a genuine row coordinate U. Enumerate the whole open chart mod q.
    squares = {i * i % q for i in range(1, q)}
    chi = [0 if x == 0 else (1 if x in squares else -1) for x in range(q)]
    assert chi[-1] == -1
    roots = [sum(z*z % q == x for z in range(q)) for x in range(q)]
    projections = defaultdict(set)
    counts = defaultdict(int)
    twist_count = 0
    target = (-1, 1, -1, -1, 1)
    for p in range(1, q):
        for y in range(1, q):
            out = (1+(p-1)*y) % q
            vals = (p, (p*p-2) % q, y, out)
            if not all(vals):
                continue
            signs = tuple(chi[x] for x in vals)
            assert chi[2*y % q] == chi[2]*signs[2]  # rational associates cannot be independent
            first_roots = 1
            for e, x in zip(target[:4], vals):
                first_roots *= roots[e*x % q]
            yinv = pow(y, -1, q)
            for v in range(q):
                u = (1-(p-1)*v)*yinv % q
                if not u:
                    continue
                assert (y*u + (p-1)*v) % q == 1
                word = signs + (chi[u],)
                projections[word].add(p)
                counts[word] += 1
                twist_count += first_roots * roots[target[-1]*u % q]
    assert len(counts) == 32
    assert twist_count == 32*counts[target]
    # Lower bound needed by the proof: projection, NOT every fixed P fibre.
    for word, n in counts.items():
        assert len(projections[word])*q**2 >= n
        assert len(projections[word]) < q-1
    print(f'q={q}: all 32 words, min #tuples={min(counts.values())}, '
          f'min #P residues={min(map(len, projections.values()))}, '
          f'P²−2 splits={chi[2] == 1}')
    return projections[target]


def check_compression(B):
    # One deep place 2 (K=3), one sign test 43 with B the actual projection,
    # others exactly 1. Full enumeration of cylinder probabilities at m.
    # Include powers above both depths, including noncoprime N and m/N.
    q = 43
    for a, b, c in product(range(6), range(3), (0, 1)):
        m = 2**a*q**b*3**c
        local2 = [r for r in range(2**a) if (r-1) % 2**min(a, 3) == 0]
        localq = [r for r in range(q**b) if b == 0 or r % q in B]
        denom = len(local2)*len(localq)
        N = 2**max(a-3, 0)*q**b
        D = Fraction(q, len(B))
        hits = 0
        for r in range(m):
            if ((r-1) % 3**c == 0 and (r-1) % 2**min(a, 3) == 0
                    and (not b or r % q in B)):
                hits += 1
                assert (r-1) % (m//N) == 0
                assert gcd(r, m) == 1
        assert hits == denom and Fraction(1, denom) <= D/N
    print('36 mixed-depth moduli: exact support, normalization and D/N bound checked')


if __name__ == '__main__':
    B43 = check_twist_projection(43)
    for prime in (47, 59, 71):
        check_twist_projection(prime)
    check_compression(B43)
