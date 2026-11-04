"""Independent CENTRAL cross-review checks; uv run --with sympy python FILE ROOT.

ROOT is a git-archive extraction of side-agent/z56-central, with the memo's C
program compiled as ROOT/z56sl and sample_*_out.txt from one input per family.
Run under `ulimit -v 6000000; timeout 180s ...`. No dense arrays are allocated.
"""
from pathlib import Path
import math
import subprocess
import sys

from mpmath import mp
from sympy import divisors, integer_nthroot

mp.dps = 60
root = Path(sys.argv[1])
data = root / "data/z56/central"


def parse(line):
    main, tail = line.split("||")
    parts = main.split("|")
    head = parts[0].split()
    key = (head[0], *map(int, head[1:4]))
    return key, list(map(float, head[4:])), [
        list(map(float, p.split())) for p in parts[1:]
    ], list(map(float, tail.split()))


stored = {}
for path in sorted(data.glob("slices_*.txt")):
    for line in path.read_text().splitlines():
        key, head, bands, tail = parse(line)
        assert key not in stored
        stored[key] = (head, bands, tail)

# Compare every shared field, including all four F_L values and dyadic slices.
checked = 0
for name in ("sample_direct_out.txt", "sample_proxy_out.txt"):
    for line in (root / name).read_text().splitlines():
        key, head, bands, tail = parse(line)
        old_head, old_bands, old_tail = stored[key]
        assert head == old_head and tail == old_tail, key
        for band, old in zip(bands, old_bands):
            shared = len(old) if len(old) == 5 else 3
            for a, b in zip(band[:shared], old[:shared]):
                assert a == b or (math.isnan(a) and math.isnan(b)), key
        checked += 1
assert checked == 13
print(f"C rerun: {checked} family/scale samples agree in every shared printed field")

# Independently recover the Theorem L residual without using the large-band
# counts or the C floating-point cutoffs. Rational powers use exact integer roots.
maximum = (mp.mpf(0), None)
checked = 0
for line in (data / "slices_e10.txt").read_text().splitlines():
    key, _, bands, _ = parse(line)
    _, x, y, _ = key
    for j, band in enumerate(bands, 1):
        delta = mp.mpf(j) / 20
        lo = int(integer_nthroot(x ** (10 - j), 20)[0])
        hi = int(integer_nthroot(x ** (10 + j), 20)[0])
        # Integer pairs with k > L and m > L', not included in reflected P1.
        kmax = (x + y) // (hi + 1)
        assert kmax - lo <= 1
        extra = sum(max(0, (x + y) // k - max(hi, x // k))
                    for k in range(lo + 1, kmax + 1))
        assert extra in (0, 1)
        remainder = (x + y) * mp.log1p(mp.mpf(y) / x) - y
        residual = (extra + 2 * y * (mp.harmonic(lo)
                    - (mp.mpf("0.5") - delta) * mp.log(x) - mp.euler)
                    - remainder)
        assert abs(residual - mp.mpf(str(band[3]))) < mp.mpf("0.000051"), (key, j)
        if abs(residual) > maximum[0]:
            maximum = (abs(residual), (x, str(delta)))
        checked += 1
print(f"Independent 60-digit residuals: {checked} agree to printed precision")
print(f"Max |residual| = {mp.nstr(maximum[0], 24)} at {maximum[1]}")

# A genuinely different algorithm: factor each n in the short interval, rather
# than looping over m and using the hyperbola identity.
x, y, u = 100000007, 200, 100
counts = [0] * 4
small = [0] * 4
lo = [int(integer_nthroot(x ** (10 - j), 20)[0]) for j in range(1, 5)]
hi = [int(integer_nthroot(x ** (10 + j), 20)[0]) for j in range(1, 5)]
divisor_count = central_count = 0
for n in range(x + 1, x + y + 1):
    ds = divisors(n)
    divisor_count += len(ds)
    central_count += sum(u * u < d <= 4 * u * u for d in ds)
    for j in range(4):
        small[j] += sum(d <= lo[j] for d in ds)
        counts[j] += sum(lo[j] < d <= hi[j] for d in ds)
main = y * mp.log(x) + (x + y) * mp.log1p(mp.mpf(y) / x) + (2 * mp.euler - 1) * y
central_error = central_count - y * (mp.harmonic(4 * u * u) - mp.harmonic(u * u))
run = subprocess.run(["timeout", "60s", "env", "Z56_DIRECT=1", str(root / "z56sl")],
                     input=f"{x} {y} {u} independent\n", text=True,
                     capture_output=True, check=True, timeout=65)
_, head, bands, _ = parse(run.stdout)
assert abs(mp.mpf(head[0]) - (divisor_count - main)) < mp.mpf("0.000051")
assert abs(mp.mpf(head[1]) - central_error) < mp.mpf("0.000051")
for j, band in enumerate(bands):
    expected = (counts[j] - mp.mpf(j + 1) / 10 * y * mp.log(x),
                counts[j] - y * (mp.harmonic(hi[j]) - mp.harmonic(lo[j])),
                small[j] - y * mp.harmonic(lo[j]))
    for actual, value in zip(band[:3], expected):
        assert abs(mp.mpf(actual) - value) < mp.mpf("0.000051")
print(f"Independent divisor enumeration: D={divisor_count}, central count={central_count}")
print(f"D-Main={float(divisor_count-main):.4f}, Ec={float(central_error):.4f}; all four bands agree")
