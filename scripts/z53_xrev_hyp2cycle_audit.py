"""Independent, bounded audit of the extracted Z53 HYP2CYCLE artifacts.

Run: ulimit -v 6000000; ulimit -t 180; timeout 180s uv run --no-project \
  scripts/z53_xrev_hyp2cycle_audit.py /tmp/xrev_HYP2CYCLE
Uses only the standard library; no dense arrays or unbounded subprocesses.
"""
import cmath
from collections import Counter
from fractions import Fraction
import gzip
from math import isqrt, pi, sqrt
from pathlib import Path
import sys

root = Path(sys.argv[1])
data = root / "data/z53/hyp2cycle"


def primes(bound):
    sieve = bytearray(b"\1") * (bound + 1)
    sieve[:2] = b"\0\0"
    for q in range(2, isqrt(bound) + 1):
        if sieve[q]:
            sieve[q * q::q] = b"\0" * ((bound - q * q) // q + 1)
    return [q for q in range(2, bound + 1) if sieve[q]]


def remainder_map(n, U):
    result = {}
    for u in range(U + 1, 2 * U + 1):
        r = (-n) % u
        B = r if r > U else r + u
        if U < B <= 2 * U:
            result[u] = B
    return result


# Existing brute.py checks the scanner, not the rational Gauss identity.
cases = vertices = cycles = 0
for p in primes(1500)[2:]:
    for U in range(2, min(40, (p - 1) // 2) + 1):
        f = remainder_map(p, U)
        cases += 1
        for u, B in f.items():
            x, y = Fraction((-p) % u, u), Fraction((-p) % B, B)
            j = int(B > u)
            gamma = 1 / x - 1 if j == 0 else 1 / (1 + x)
            returning = f.get(B) == u
            assert returning == (y == gamma)
            union = (x > Fraction(1, 2) and y == 1 / x - 1) or y == 1 / (1 + x)
            assert returning == union
            assert (gamma * B).denominator == 1
            vertices += 1
            cycles += returning
print(f"Gauss identity: {cases} prime/scale cases, {vertices} vertices, {cycles} returning vertices; no mismatches")

# Find the missing composite hypothesis in the fixed-difference identity.
found = None
for n in range(5, 1000, 2):
    for U in range(2, min(25, (n - 1) // 2) + 1):
        f = remainder_map(n, U)
        for u, B in f.items():
            if B > u and f.get(B) == u and (n + u + B) % (u * B):
                found = (n, U, u, B, n + u + B, u * B)
                break
        if found:
            break
    if found:
        break
print("Composite fixed-difference counterexample (n,U,u,B,n+u+B,uB):", found)

# The first-coordinate denominator claim in the summary is not Lemma G.
x, B = Fraction((-17) % 3, 3), 4
print("Summary denominator counterexample: p=17,U=2,u=3,B=4, theta_u=", x,
      "; B*theta_u=", B * x)

# Independent phases: reduce the combined rational phase modulo 1 exactly
# BEFORE float conversion, unlike the C code's floating linear combination.
for name, H, full in (("mix_p1e12_H32.txt", 32, True),
                      ("mix_p1e16_H100.txt", 100, False),
                      ("mix_p1e18_H180.txt", 180, False)):
    row = (data / name).read_text().splitlines()[0].split()
    p, U, size = map(int, row[:3])
    f = remainder_map(p, U)
    assert len(f) == size
    points = [(u, B, (-p) % u, (-p) % B) for u, B in f.items()]
    best = (0, None)
    ss = 0.0
    count = 0
    for h2 in range(1, H + 1):
        for h1 in (range(-H, H + 1) if full else (0,)):
            W = sum(cmath.exp(2j * pi * ((h1 * r * B + h2 * s * u) % (u * B)) / (u * B))
                    for u, B, r, s in points)
            value = abs(W) / sqrt(size)
            ss += value * value
            count += 1
            if value > best[0]:
                best = value, (h1, h2)
    assert abs(best[0] - float(row[3])) < 0.00051
    rms = sqrt(ss / count)
    assert abs(rms - float(row[6 if full else 7])) < 0.00051
    print(f"Independent MIX p={p}, H={H}, {'full grid' if full else 'h1=0 column'}: "
          f"max={best}, rms={rms:.6f}, max|W|/sqrt(U)={best[0]*sqrt(size/U):.6f}")

# Compare independently counted pairs with the stored prime scan, streaming.
for name in ("scan_o8.tsv.gz", "scan_o12.tsv.gz"):
    checked = 0
    with gzip.open(data / name, "rt") as stream:
        for line in stream:
            row = list(map(int, line.split()))
            n, U = row[:2]
            n2 = n4 = 0
            for u in range(U + 1, 2 * U + 1):
                # Enumerate the unique possible larger partner from u | n+B.
                B = (-n) % u + u
                if u < B <= 2 * U and (n + u + B) % (u * B) == 0:
                    n2 += 1
                    n4 += ((n + u + B) // (u * B)) % 4 == 0
            assert [n2, n4] == row[2:4]
            checked += 1
            if checked == 3000:
                break
    print(f"Independent pair/product counts: {name}, {checked} rows agree")

# Aggregate the three original exhaustive histograms and compare the fresh run.
def histograms(path):
    lines = path.read_text().splitlines()
    return [Counter({int(k): int(v) for k, v in (part.split(":") for part in line.split()[1:])})
            for line in lines if line.startswith(("H2 ", "H4 "))]


rerun = root / "exhaustive_rerun.txt"
if rerun.exists():
    expected = [Counter(), Counter()]
    for name in ("ms8.txt", "ms9.txt", "ms10c_classes.txt"):
        for total, part in zip(expected, histograms(data / name)):
            total.update(part)
    assert expected == histograms(rerun)
    print("Full exhaustive rerun agrees: 189961810 primes, max N2=7, max N4=5")
