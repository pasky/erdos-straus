"""Independent finite-identity and data audit of the pinned SYNTH archive.

Run from the repository root:
  ulimit -v 6000000; timeout 90s uv run --with sympy python \
    scripts/z57_xrev_synth_audit.py /tmp/xrev_SYNTH
Uses O(N log² N) stored triples for N=1000; no large Cartesian arrays.
The large-range triple counts are separately rerun with z57_synth_check8.py.
"""
from collections import Counter
from fractions import Fraction
from math import gcd, log, pi
from pathlib import Path
import sys

from sympy import isprime, primerange

archive = Path(sys.argv[1])
data = archive / "data/z57/synth"
mordell = {1, 121, 169, 289, 361, 529}

# Direct triple enumeration versus A.1's modulus enumeration, including even n.
# Existing FAMTRY checks concern odd n; this also checks the asserted extension.
N = 1000
triples = [set() for _ in range(N + 1)]
for u in range(1, (N + 1) // 3 + 1):
    for b in range(1, (N + u) // (4 * u - 1) + 1):
        for c in range(1, (N + u + b) // (4 * u * b) + 1):
            n = 4 * u * b * c - u - b
            triples[n].add((u, b, c))
for n in range(1, N + 1):
    hits = set()
    for d in range(3, (4 * n + 1) // 3 + 1, 4):
        r = (-n) % d
        if r and ((d + 1) // 4) % r == 0:
            hits.add((r, (n + r) // d, (d + 1) // (4 * r)))
    assert hits == triples[n], n
    for u, b, c in hits:
        assert sum((Fraction(1, u*b*c), Fraction(1, n*b*c),
                    Fraction(1, n*u*c))) == Fraction(4, n)
        if c % 2 == 0:
            h = c // 2
            assert sum((Fraction(1, u*b*h), Fraction(1, n*b*h),
                        Fraction(1, n*u*h))) == Fraction(8, n)
print(f"A.1 and 4/n, C-even 8/n identities: all n=1..{N} agree")

survivors = {r for r in range(840) if gcd(r, 840) == 1 and r % 8 == 1
             and r % 3 == 1 and r % 5 in {1, 4} and r % 7 in {1, 2, 4}}
assert survivors == mordell
print("Mordell CRT survivors:", sorted(survivors))

rows = [tuple(map(int, line.split())) for line in (data / "tri_1e8.txt").read_text().splitlines()]
star = [p for p, r, r8 in rows if r == 0]
z8 = [p for p, r, r8 in rows if r8 == 0]
zodd = [p for p, r, r8 in rows if r == r8]
print("R/R8/Rodd zeros:", len(star), len(z8), len(zodd),
      "last:", max(star), max(z8), max(zodd))
print("R8 zeros by decade:", sorted(Counter(len(str(p))-1 for p in z8).items()))
assert (len(star), len(z8), len(zodd)) == (14, 1270, 423)
assert sum(p > 10**7 for p in zodd) == 156

hi = [tuple(map(int, line.split())) for line in (data / "dec8_1e10.txt").read_text().splitlines()]
assert len(hi) == len({p for p, _, _ in hi}) == 12
assert all(isprime(p) and p > 10**10 and r > 0 and r8 == 0 for p, r, r8 in hi)
hi_mordell = sorted(p for p, _, _ in hi if p % 840 in mordell)
assert len(hi_mordell) == 4
print("High-range Mordell R8 zeros (all with R>0):", hi_mordell)

low_r = {p: r for p, r, _ in rows if p > 10**7 and r <= 8}
mass = {int(t[0]): float(t[4]) for line in (data / "mgen_lowR.txt").read_text().splitlines()
        if len(t := line.split()) == 9}
assert len(low_r) == 334 and low_r.keys() <= mass.keys()
cv = 5 / (4 * pi*pi)
violations = [p for p, r in low_r.items() if r-mass[p] < -cv*log(p)**2]
subset = [p for p in low_r if p % 840 in mordell]
assert len(violations) == 7 and len(subset) == 249
assert all(p % 840 not in mordell for p in violations)
margins = [(low_r[p]/log(p)**2-mass[p]/log(p)**2+cv, p) for p in subset]
print("Uniform violations:", [(p, p % 840) for p in violations])
print("Mordell sample: size, minimum scaled margin:", len(subset), min(margins))
print("Mordell Mgen/L² mean:", sum(mass[p]/log(p)**2 for p in subset)/len(subset))
# Verify the decisive eight fresh C-program sums, if present.
rerun = archive / "mgen_rerun.txt"
if rerun.exists():
    fresh = {int(t[0]): float(t[4]) for line in rerun.read_text().splitlines()
             if len(t := line.split()) == 9}
    assert set(violations) | {min(margins)[1]} <= fresh.keys()
    assert all(abs(mass[p]-m) < 1e-5 for p, m in fresh.items())
    print("Eight decisive genus sums agree with fresh enumerations")

f4 = []
for line in Path("data/z56/famdesign/zeros_le1e8.txt").read_text().splitlines():
    if not line.startswith("#"):
        t = line.split()
        if t[8] == "0":
            f4.append(int(t[0]))
f4.append(564661441)
assert len(f4) == 38
small_primes = list(primerange(2, 100))
for name, zero_set in (("star", star), ("G*", f4)):
    assert all(isprime(p) for p in zero_set)
    least = [next(q for q in small_primes if pow(q, (p-1)//2, p) == p-1) for p in zero_set]
    print(name, "least prime nonresidues:", sorted(set(least)))
    assert all(q < 2*log(p)**2 for p, q in zip(zero_set, least))
print("PASS (large-range exhaustiveness and asymptotic claims are not inferred here)")
