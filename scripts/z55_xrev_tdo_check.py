"""Independent, bounded checks of the extracted z55 TDO memo data.

Run: ulimit -v 6000000; timeout 180s uv run python \
    scripts/z55_xrev_tdo_check.py /tmp/xrev_TDO
Uses only the standard library; no dense Cartesian-product arrays.
Existing z54 checks cover their own m-scans, not these k-scans/boundaries.
"""
import cmath
from collections import Counter
import math
from pathlib import Path
import random
import sys

root = Path(sys.argv[1])
data = root / "data/z55/tdo"


def strip_k(n, U):
    """Enumerate integer levels and their m intervals, not residues modulo m."""
    points = set()
    for k in range((n + 2 * U) // (4 * U * U) + 1,
                   (n + 4 * U) // (U * U + 1) + 1):
        lo = max(U * U + 1, (n + 2 * U) // k + 1)
        hi = min(4 * U * U, (n + 4 * U) // k)
        for m in range(lo, hi + 1):
            s = k * m - n
            if s * s - 4 * m >= 1:
                points.add((s, m))
    return points


def strip_m(n, U):
    points = set()
    for m in range(U * U + 1, 4 * U * U + 1):
        s = (-n) % m
        if 2 * U < s <= 4 * U and s * s - 4 * m >= 1:
            points.add((s, m))
    return points


for name in ("e8", "e10", "e12", "e14", "all_e12", "squares_e12"):
    rows = [line.split() for line in (data / f"scan_{name}.txt").read_text().splitlines()]
    stats = [sum(int(r[2]) / int(r[1]) for r in rows) / len(rows),
             sum(float(r[3]) / math.sqrt(int(r[1])) for r in rows) / len(rows),
             max(float(r[3]) / math.sqrt(int(r[1])) for r in rows),
             sum(float(r[5]) / int(r[1]) for r in rows) / len(rows)]
    print(name, len(rows), "table statistics:", *(f"{x:.6f}" for x in stats))
    # Independent direct complex evaluation on each scale, including squares.
    r = rows[0]
    n, U, count = map(int, r[:3])
    points = strip_k(n, U)
    assert len(points) == count
    phases = [math.sqrt(s * s - 4 * m) % 1 for s, m in points]
    magnitudes = []
    for h in range(1, 9):
        terms = [cmath.exp(2j * math.pi * h * w) for w in phases]
        magnitudes.append(abs(complex(math.fsum(z.real for z in terms),
                                      math.fsum(z.imag for z in terms))))
    assert abs(max(magnitudes) - float(r[3])) <= 0.00051
    assert magnitudes.index(max(magnitudes)) + 1 == int(r[4])
    assert abs(sum(x * x for x in magnitudes) / 8 - float(r[5])) <= 0.00051
    print("  independent k-scan and h=1..8 agree:", n)
    if name == "squares_e12":
        print("  square ranges:",
              min(float(r[3]) / math.sqrt(int(r[1])) for r in rows), stats[2],
              min(float(r[5]) / int(r[1]) for r in rows),
              max(float(r[5]) / int(r[1]) for r in rows))

rng = random.Random(55)
for i in range(150):
    U = rng.randrange(5, 25)
    n = 0 if i == 0 else rng.randrange(200000)
    points = strip_k(n, U)
    assert points == strip_m(n, U), (n, U)
    ds = Counter(s * s - 4 * m for s, m in points)
    for h in (1, 3):
        lhs = sum(cmath.exp(2j * math.pi * h * math.sqrt(D)) * count
                  for D, count in ds.items())
        rhs = sum(cmath.exp(-2j * math.pi * h * (s - math.sqrt(s * s - 4 * m)))
                  for s, m in points)
        assert abs(lhs - rhs) < 1e-8
print("150 small-input k/m identities and discriminant/root-phase checks passed")

for i in range(180):
    U0 = rng.randrange(9, 22)
    G = rng.choice((1, U0, rng.randrange(1, U0 + 1)))
    n = rng.randrange(200000)
    U = rng.randrange(U0, U0 + G + 1)
    lo, hi = U0 * U0 + 1, 4 * (U0 + G) ** 2
    boundary = set()
    for m in range(lo, hi + 1):
        s = (-n) % m
        if not 2 * U0 < s <= 4 * U0 + 4 * G:
            continue
        sb = s <= 2 * U0 + 2 * G or s > 4 * U0
        mb = m <= (U0 + G) ** 2 or m > 4 * U0 * U0
        if sb or mb:
            boundary.add((s, m))
    assert strip_k(n, U) ^ strip_k(n, U0) <= boundary, (n, U0, G, U)
print("180 boundary symmetric-difference inclusions passed, including G=1 and G=U0")

# The collision estimate is the nontrivial combinatorial input of Lemma 4.2.
for U0, G in ((9, 1), (9, 9), (20, 3), (20, 20)):
    S0 = list(range(2 * U0 + 1, 4 * U0 + 4 * G + 1))
    Sb = list(range(2 * U0 + 1, 2 * U0 + 2 * G + 1))
    Sb += list(range(4 * U0 + 1, 4 * U0 + 4 * G + 1))
    Q = 4 * (U0 + G) ** 2
    for S in (S0, Sb):
        for q in range(1, Q + 1):
            collisions = sum(v * v for v in Counter(s % q for s in S).values())
            assert q * collisions <= len(S) ** 2 + 2 * q * len(S)
print("Lemma 4.2 residue-collision bounds passed for four endpoint/interior boxes")
print("All independent checks passed.")
