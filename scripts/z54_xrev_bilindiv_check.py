"""Bounded independent checks for extracted z54 BILINDIV review runs.

Usage: uv run python scripts/z54_xrev_bilindiv_check.py /tmp/xrev_BILINDIV
The extraction must contain data/z54/bilindiv and the rerun/ outputs.
Run under timeout and ulimit. Only the U=1000 case is independently scanned;
all arrays are O(U), and the m scan has 3*U**2 iterations (no Cartesian arrays).
"""
import cmath
import gzip
import math
from pathlib import Path
import sys

root = Path(sys.argv[1])
stored = root / "data/z54/bilindiv"
rerun = root / "rerun"


def rows(text):
    return [line.strip() for line in text.splitlines() if line[:1].isdigit()]


for name in ("td_falsifier.txt", "td_extended.txt", "untied.txt"):
    a = rows((stored / name).read_text())
    b = rows((rerun / name).read_text())
    assert sorted(a) == sorted(b), name
    print(f"{name}: {len(a)} rows agree exactly")

with gzip.open(stored / "cyclines.txt.gz", "rt") as f:
    a = rows(f.read())
b = rows((rerun / "cyclines.txt").read_text())
assert sorted(a) == sorted(b)
print(f"cyclines: all {len(a)} nonempty rows agree exactly")
for U in (316, 1000):
    rr = [s.split() for s in b if int(s.split()[1]) == U]
    cycles = [int(x[2:]) for r in rr for x in r[4:] if x.startswith("r=")]
    controls = [int(r[-1].split("=")[1]) for r in rr]
    print(f"U={U}: cycles={len(cycles)}, controls={len(controls)}")
    for cutoff in (3, 4):
        nc = sum(x >= cutoff for x in cycles)
        nq = sum(x >= cutoff for x in controls)
        print(f"  r>={cutoff}: {nc}/{len(cycles)}={nc/len(cycles):.6%}; "
              f"controls {nq}/{len(controls)}={nq/len(controls):.6%}")

brute = [list(map(int, s.split())) for s in rows((rerun / "brute.txt").read_text())]
strip = [s.split() for s in rows((rerun / "td_p8.txt").read_text())]
assert len(brute) == len(strip) == 300
for r, s in zip(brute, strip):
    assert r == [int(s[i]) for i in (0, 1, 4, 5)]
assert sum(r[2] for r in brute) == 113
print("300-prime brute/strip: zero mismatches; sum N2=113")

geom = rows((rerun / "geom_one.txt").read_text())
assert len(geom) == 1 and geom[0] in rows((stored / "geom.txt").read_text())
print("geometry/anatomy first p12 row agrees:", geom[0])

# Independent orientation: scan products m, not levels k, then evaluate each
# frequency directly rather than using the C program's complex recurrence.
p, U, H = 1000000000177, 1000, 20
points, ds, cycles = [], [], []
for m in range(U * U + 1, 4 * U * U + 1):
    k = (p + 2 * U) // m + 1
    s = k * m - p
    if s > 4 * U:
        continue
    points.append((k, m))
    D = s * s - 4 * m
    if D < 1:
        continue
    ds.append(D)
    w = math.isqrt(D)
    if w * w == D and (s - w) % 2 == 0:
        u, v = (s - w) // 2, (s + w) // 2
        if U < u < v <= 2 * U:
            cycles.append((u, v, k))
assert len(points) == 2835 and len(ds) == 1639 and not cycles
magnitudes = []
for h in range(1, H + 1):
    terms = [cmath.exp(2j * math.pi * h * (math.sqrt(D) % 1)) for D in ds]
    T = complex(math.fsum(z.real for z in terms), math.fsum(z.imag for z in terms))
    magnitudes.append(abs(T) / math.sqrt(len(ds)))
stats = [max(magnitudes), math.sqrt(math.fsum(x*x for x in magnitudes)/H), magnitudes[0]]
row = next(s.split() for s in rows((stored / "td_falsifier.txt").read_text())
           if s.startswith(str(p) + " "))
assert [f"{x:.3f}" for x in stats] == [row[i] for i in (6, 8, 9)]
assert magnitudes.index(max(magnitudes)) + 1 == int(row[7])
print("Independent m-scan/direct Fourier: E1=2835, E1+=1639, N2=0;", stats)

# Concrete split-order and translated-height counterexamples in the memo's range.
p, U, u, v, k = 100000037, 100, 115, 168, 5176
assert 16 * U**3 <= p and k*u*v-u-v == p
s, m = u+v, u*v
assert (-p) % k == s and (p+s)//k == m
assert s*s - 4*m == 53**2
# Evaluation sends a+b*t to (a+115b,a+168b); the image has index 53,
# so it is not Z x Z (its discriminant is 53**2, not 1).
M = max(k*v-1, k*u-1, u*v, k, u, v, 1)
assert M == 869567 and M < p
print("Counterexamples: split order index=53; translated coefficient norm=869567<p")
print("All review checks passed.")
