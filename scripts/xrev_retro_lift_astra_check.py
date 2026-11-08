"""Independent bounded audit of Z65_LIFT's arithmetic and falsifier metadata.
Run: ulimit -v 4000000; timeout 300 uv run --no-project scripts/xrev_retro_lift_astra_check.py
Uses direct y enumeration (not the memo's divisor enumerator), streams triples,
and tests raw G2 identities/inequalities, not the G3 cluster-shape implementation.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def triples(p, k):
    for x in range(p // k + 1, 3 * p // k + 1):
        a, b = k * x - p, p * x
        for y in range(max(x, b // a + 1), 2 * b // a + 1):
            z, rem = divmod(b * y, a * y - b)
            if not rem:
                yield x, y, z


def cluster(es, p):
    if len(es) == 1:
        return es[0] % p != 0
    pp = []
    for e in es:
        q = 1
        while e % (q * p) == 0:
            q *= p
        pp.append(q)
    tame_sum = sum((1 - F(q, e) for q, e in zip(pp, es)), F(0))
    if tame_sum >= 1:
        return False
    m = 1 / (1 - tame_sum)
    if m.denominator != 1 or m.numerator % p == 0:
        return False
    # The G2(b) lower bound increases with |P|; use its smallest possible value.
    P = max(p, *pp)
    return sum((F(m, e) * (q - 1) for q, e in zip(pp, es)), F(0)) >= 2 * (1 - F(1, P))


def passes(t, p):
    partitions = (((0, 1), (2,)), ((0, 2), (1,)), ((1, 2), (0,)), ((0, 1, 2),))
    return any(all(cluster([t[i] for i in c], p) for c in part) for part in partitions)


for k in (4, 8):
    total = accepted = identities = p2 = 0
    other = []
    for p in range(5, 1501):
        if not prime(p):
            continue
        for t in triples(p, k):
            total += 1
            p2 += any(e % (p * p) == 0 for e in t)
            if not passes(t, p):
                continue
            accepted += 1
            m, rem = divmod(p + 1, k - 1)
            if not rem and t == tuple(sorted((m, p, p * m))):
                identities += 1
            else:
                other.append((p, t))
    print(f"k={k}: total={total}, raw-G2 survivors={accepted}, identities={identities}, p²={p2}, other={other}")
    assert (total, accepted, identities, p2, other) == (
        (11800, 122, 122, 0, []) if k == 4 else (4965, 39, 38, 0, [(7, (2, 2, 7))])
    )

root = Path(__file__).resolve().parents[1] / "data/z58/screens"
for name in ("star_prime_zeros.txt", "gstar_zeros.txt", "r8_zeros_1e10.txt", "composite_zeros_le8e6.txt"):
    rows = [list(map(int, s.split())) for s in (root / name).read_text().splitlines() if s and not s.startswith("#")]
    ns = [r[0] for r in rows]
    print(name, "count=", len(ns), "residues mod 12=", sorted({n % 12 for n in ns}))
    if name.startswith(("star_", "gstar_")):
        assert all(prime(n) and n % 12 == 1 for n in ns)
    if name.startswith("r8_"):
        assert all(prime(n) and n % 7 != 6 and r[2] == 0 for n, r in zip(ns, rows))
        print("  none is 6 mod 7: no numerator-8 Mordell survivor at these zeros")
    if name.startswith("composite_"):
        assert all(not prime(n) and isqrt(n) ** 2 != n for n in ns)
print("PASS; screen zero counts themselves are inherited, not re-certified here")
