#!/usr/bin/env python3
"""Exact finite audits for EXSET_I3; no asymptotic constants are fitted.
Memory: O(Y+N), Y=100000, N=1000000. No pair-product arrays.
Run under ulimit -v 8000000 and timeout 180 with uv run python.
"""
from fractions import Fraction
from math import gcd, isqrt, lcm, log, prod
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/z50_i3ex"
OUT.mkdir(parents=True, exist_ok=True)
Y = 100000
spf = list(range(Y + 2))
for p in range(2, isqrt(Y + 1) + 1):
    if spf[p] == p:
        for m in range(p * p, Y + 2, p):
            if spf[m] == m:
                spf[m] = p


def divisors(m):
    ds = [1]
    while m > 1:
        p = spf[m]
        old = ds[:]
        power = 1
        while m % p == 0:
            m //= p
            power *= p
            ds.extend(d * power for d in old)
    return ds


def native(m):
    return sorted(u for u in divisors(m + 1) if 3 <= u <= (m + 1) // 3)


def primes_of(m):
    ps = []
    while m > 1:
        p = spf[m]
        ps.append(p)
        while m % p == 0:
            m //= p
    return ps


# New tests: class multiplicity, quadratic supply, zero-base elimination,
# smooth-mass profile and conditional-fibre averaging.
profile = []
mass = 0.0
smooth = {y: 0.0 for y in (5, 11, 31, 101)}
base_checks = 0
for m in range(8, Y + 1):
    us = native(m)
    assert len({(-u) % m for u in us}) == len(us)
    mass += len(us) / m
    ps = primes_of(m)
    for u in us:
        assert gcd(u, m) == 1
        n = ((3 * m + u + m - 1) // m) * m - u
        t, v = (m + 1) // u, (n + u) // m
        assert min(t, u, v) >= 3 and t * u * v - u - v == n
        for p in ps:
            if p <= 11:
                assert (-u) % p != 0
                base_checks += 1
    for y in smooth:
        if max(ps) <= y:
            smooth[y] += len(us) / m
    if m in (100, 1000, 10000, Y):
        profile.append({"Y": m, "mass": mass, "mass_over_log2": mass / log(m) ** 2})

fibres = []
K = 4
LK = lcm(*range(1, K + 1))
atoms = []
for q in range(13, 102):
    if spf[q] != q:
        continue
    for k in range(1, K + 1):
        # A toy distinct-residue cutoff, not the asymptotic BV parameters.
        for u in native(k * q):
            if K < u < q:
                atoms.append((k, q, u))
assert len({(k * q, (-u) % (k * q)) for k, q, u in atoms}) == len(atoms)
fibre_means = []
for c in range(LK):
    by_q = {}
    for k, q, u in atoms:
        if (c + u) % k == 0:
            by_q.setdefault(q, []).append((-u) % q)
    for q, residues in by_q.items():
        assert len(set(residues)) == len(residues)
    mu = sum((Fraction(len(rs), q) for q, rs in by_q.items()), Fraction())
    fibre_means.append(mu)
    fibres.append({"c": c, "mean": str(mu), "mean_float": float(mu)})
assert sum(fibre_means) / LK == sum((Fraction(1, k * q) for k, q, _ in atoms), Fraction())

# Full-period native avoiders for tiny families; the zero base is checked
# for ALL residues, not merely at one sample point.
period_rows = []
for B in (8, 12, 16):
    classes = [(m, (-u) % m) for m in range(8, B + 1) for u in native(m)]
    Q = lcm(*(m for m, _ in classes))
    assert Q <= 1000000
    hit = bytearray(Q)
    for m, a in classes:
        hit[a::m] = b"\1" * len(hit[a::m])
    period_rows.append({"B": B, "Q": Q, "avoiders": Q - sum(hit)})

# Independent direct triple enumeration, rather than factoring n+u.
B = 5000
counts = [0] * (B + 1)
for t in range(3, (B + 6) // 9 + 1):
    u = 3
    while t * u * u - 2 * u <= B:
        for v in range(u, (B + u) // (t * u - 1) + 1):
            n = t * u * v - u - v
            counts[n] += 1 if u == v else 2
        u += 1
zeros = [n for n in range(3, B + 1) if counts[n] == 0]
old_zeros = [int(line.split()[1]) for line in (ROOT / "data/z48_ltfable/big_1e9.txt").read_text().splitlines() if line.startswith("I30 ")]
assert zeros == [n for n in old_zeros if n <= B]

# Larger controls: trial divisors, no dependency on either prior census engine.
def words(n):
    result = []
    u = 3
    while 3 * u * u - 2 * u <= n:
        x = n + u
        for d in range(1, isqrt(x) + 1):
            if x % d:
                continue
            for a in ((d,) if d * d == x else (d, x // d)):
                if a >= 3 * u - 1 and (a + 1) % u == 0 and x // a >= u:
                    t, v = (a + 1) // u, x // a
                    assert t * u * v - u - v == n
                    result.append((t, u, v))
        u += 1
    return result

rzeros = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321,
          1134241, 1724209, 1726201, 5212561, 8813281]
controls = sorted(set(rzeros + [193, 2521, 3361, 66529, 17, 241, 49, 121, 1225, 1600, 19600, 2433600]))
control_rows = []
for n in controls:
    ws = words(n)
    count = sum(1 if u == v else 2 for t, u, v in ws)
    assert (count == 0) == (n in old_zeros)
    if n in rzeros:
        assert ws
    if isqrt(n) ** 2 == n:
        assert all(t % 4 != 0 for t, _, _ in ws)
    if n in (17, 241):
        assert all(t % 8 != 0 for t, _, _ in ws)
    control_rows.append({"n": n, "ordered_count": count, "first_word": ws[0] if ws else None})
assert (3, 5, 9) in words(121)

# Interval avoiders vs TRUE interior exceptions. Only n>=3B is compared:
# below that point a congruence hit may have v<3.
N = 1000000
interval_rows = []
for B in (32, 128, 512, 2048):
    hit = bytearray(N + 1)
    for m in range(8, B + 1):
        for u in native(m):
            a = (-u) % m
            hit[a::m] = b"\1" * len(hit[a::m])
    lo = 3 * B
    avoid = N - lo + 1 - sum(hit[lo:])
    actual = sum(lo <= n <= N for n in old_zeros)
    assert all(not hit[n] for n in old_zeros if lo <= n <= N)
    interval_rows.append({"B": B, "lo": lo, "N": N, "native_avoiders": avoid, "certified_I3_zeros": actual})

result = {"mass_profile": profile, "smooth_partial_sums_to_Y": smooth,
          "base_elimination_checks": base_checks, "fibre_L": LK, "atoms": len(atoms),
          "fibres": fibres, "exact_periods": period_rows,
          "independent_census": {"N": 5000, "zeros": len(zeros), "last": zeros[-1]},
          "controls": control_rows, "truncated_avoiders": interval_rows,
          "empirical_E3": {str(n): sum(z <= n for z in old_zeros) for n in (1000, 10000, 100000, 1000000, 10000000, 1000000000)},
          "status": "PASS; finite exact checks only, asymptotic constants not tested"}
(OUT / "checks.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
