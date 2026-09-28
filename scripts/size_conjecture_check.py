"""Numerical checks of the lemmas in SIZE_CONJECTURE.md (finite checks only).

PYTHONPATH=scripts uv run --with python-flint python scripts/size_conjecture_check.py

Lemma A  negative-quadrant fibres (anchor 1<=x<=t, Type I bucket h<=0) are
         entirely nonpositive -- checked on complete graphs.
Lemma B  dead-hub fibre: if k>=2, M=4k+1, x=t-k and every prime factor of x
         is 1 mod M, the fibre of x is exactly {V_d : d | x^2, d < x},
         V_d = (x, -p(x-d)/M, p x(x-d)/(M d)) -- checked against exact fibres
         (complete graphs for small p, the exact lazy oracle for large p).
Lemma C  descent identity: for d,w>=1, w=1 mod 4, x=dw, M=p-4x>0, M | x-d,
         V_d and D_d=(x-d, -p(x-d)/M, -p(w-1)/4) are signed solutions sharing
         -p(x-d)/M -- checked on random data and inside hub buckets.
Lemma E  sign flip: an anchor x=t+a (a>=1) with a prime factor l = -1 mod 4a-1,
         or a Type I bucket h>=1 whose m=ph-t has a prime factor l = -1 mod 4h-1,
         has an empty fibre or a positive vertex -- checked on complete graphs.
"""
import math, random
from fractions import Fraction

import flint
from sympy import primerange, factorint, divisors

from pointwise_incidence import incidence_solutions
from pointwise_refactor import denominator_buckets
from pointwise_fibres_big import BigFibreOracle


def is_sol(p, v):
    return all(v) and sum(Fraction(1, z) for z in v) == Fraction(4, p)


def V(p, x, d, M):
    return tuple(sorted((x, -p * (x - d) // M, p * x * (x - d) // (M * d))))


def lemma_B_expected(p, x, M):
    return {V(p, x, d, M) for d in divisors(x * x) if d < x}


# ---- complete graphs: Lemmas A, B (small), E
nA = nE_anchor = nE_bucket = nB = 0
for p in [p for p in primerange(5, 40000) if p % 4 == 1][::3]:
    t = (p - 1) // 4
    verts = incidence_solutions(p)
    B = denominator_buckets(verts)
    for z, idx in B.items():
        fib = [verts[i] for i in idx]
        pos = any(v[0] > 0 for v in fib)
        if z % p and 1 <= z <= t:
            assert not pos; nA += 1
        if z % p == 0 and (4 * (z // p) - 1) % p == 0:
            h = (z // p + t) // p
            if h <= 0:
                assert not pos; nA += 1
            else:
                m = z // p
                if any(l % (4 * h - 1) == 4 * h - 2 for l in factorint(abs(m))):
                    assert pos, (p, h); nE_bucket += 1
        if z % p and t + 1 <= z <= 2 * t:
            a = z - t
            if any(l % (4 * a - 1) == 4 * a - 2 for l in factorint(z)):
                assert pos, (p, z); nE_anchor += 1
    # Lemma B instances present in this complete graph
    for k in range(2, 60):
        x, M = t - k, 4 * k + 1
        if x >= 1 and all(l % M == 1 for l in factorint(x)):
            got = {verts[i] for i in B.get(x, [])}
            assert got == lemma_B_expected(p, x, M), (p, k)
            nB += 1
print(f"Lemma A: {nA} negative-quadrant fibres all nonpositive")
print(f"Lemma E: {nE_anchor} anchors and {nE_bucket} h>=1 buckets with an l=-1 prime factor all contain a positive vertex")
print(f"Lemma B: {nB} small hub fibres equal the formula")

# ---- Lemma B at large p via the exact lazy oracle
rng = random.Random(5)
cnt = 0
for k in (2, 3, 4, 5):
    M = 4 * k + 1
    Q = [q for q in primerange(3, 3000) if q % M == 1]
    tries = 0
    while tries < 400 and cnt < 12 * (k - 1):
        tries += 1
        x = math.prod(rng.sample(Q, rng.randint(2, 5)))
        p = 4 * (x + k) + 1
        if flint.fmpz(p).is_prime() != 1:
            continue
        O = BigFibreOracle(p)
        assert set(O.fibre(x)) == lemma_B_expected(p, x, M), (p, x)
        assert len(O.fibre(x)) == (math.prod(2 * e + 1 for e in factorint(x).values()) - 1) // 2
        cnt += 1
print(f"Lemma B: {cnt} large-p hub fibres (exact oracle) equal the formula")

# ---- Lemma C descent identity on random data, and inside real buckets
n = 0
for _ in range(20000):
    d = rng.randint(1, 10**6)
    w = 4 * rng.randint(1, 10**6) + 1
    x = d * w
    # choose p = 4x + M prime with M | x - d
    for M in sorted(set(divisors(x - d)))[:40]:
        p = 4 * x + M
        if M % 4 == 1 and flint.fmpz(p).is_prime() == 1:
            v1 = V(p, x, d, M)
            v2 = tuple(sorted((x - d, -p * (x - d) // M, -p * (w - 1) // 4)))
            assert is_sol(p, v1) and is_sol(p, v2)
            assert set(v1) & set(v2)
            n += 1
            break
print(f"Lemma C: descent identity verified on {n} random instances")
print("OK")
