"""Independent z56 FAMATTACK arithmetic/statistics audit.
Run under timeout/ulimit via uv run --with numpy --with sympy python FILE /tmp/xrev_FAMATTACK.
The directory must contain the archived memo's data, compiled wcount/mgen, and census.txt.
Memory stays below 1 GB: load one N x 27 dataset at a time, never form pairwise-prime arrays.
"""
import gzip
import math
from pathlib import Path
import subprocess
import sys
from fractions import Fraction

import numpy as np
from sympy import factorint, isprime

root = Path(sys.argv[1])
data = root / "data/z56/famattack"

def load(name):
    with gzip.open(data / name, "rt") as f:
        a = np.loadtxt(f, dtype=np.int64)
    assert a.shape[1] == 27
    assert np.all(a[:, 1] == 2 * a[:, 2:].sum(axis=1))
    return a

def prime_list(lo, hi):
    # Independent segmented Eratosthenes sieve; at most 4 MB per interval.
    small = bytearray(b"\x01") * (math.isqrt(hi) + 1)
    small[:2] = b"\x00\x00"
    for q in range(2, math.isqrt(len(small) - 1) + 1):
        if small[q]:
            small[q*q::q] = bytes((len(small)-1-q*q)//q + 1)
    segment = bytearray(b"\x01") * (hi-lo+1)
    for q in range(2, len(small)):
        if small[q]:
            start = max(q*q, ((lo+q-1)//q)*q)
            if start <= hi:
                segment[start-lo::q] = bytes((hi-start)//q+1)
    return np.array([n for n in range(lo + (1-lo) % 4, hi+1, 4) if segment[n-lo]])

zeros = np.loadtxt(root / "census.txt", dtype=np.int64)[:, 0]
primes = [int(n) for n in zeros if isprime(int(n))]
squares = [int(n) for n in zeros if math.isqrt(int(n))**2 == n]
composites = [int(n) for n in zeros if n not in primes and n not in squares]
assert (len(primes), len(squares), len(composites)) == (13, 1413, 285)
assert squares == [m*m for m in range(3, math.isqrt(7999801)+1, 2)]
print("independent census:", len(zeros), "zeros; prime/square/other", len(primes), len(squares), len(composites))
print("composite decades:", [sum(10**d <= n < 10**(d+1) for n in composites) for d in range(1, 7)])

# Exact rational area calculation, not the memo's tiling script.
a, b = Fraction(1, 15), Fraction(3, 5)
F = lambda x: 3*x/4 - 5*x*x/8
G = lambda x: 3*x/4 - 3*x*x/2
area = F(b)-F(a)
area_x = G(Fraction(1, 5))-G(a)
assert (area, area_x) == (Fraction(8, 45), Fraction(7, 150))
print("tile areas/coefficients:", area, area_x, 8*float(area)/math.pi**4, 8*float(area_x)/math.pi**4)

rng = np.random.default_rng(56)
ns = load("wcount_ns_w.txt.gz")
assert len(ns) == 965
near_ks = dict(np.loadtxt(data / "nearsq_primes_1e9.txt", dtype=np.int64))
for n in ns[:, 0]:
    n = int(n)
    assert isprime(n) and math.isqrt(n-int(near_ks[n]))**2 == n-int(near_ks[n])

for filename, lo, hi in [
    ("wcount_1e8.txt.gz", 100000000, 104000000),
    ("wcount_1e9.txt.gz", 1000000000, 1002000000),
    ("wcount_1p2e9.txt.gz", 1199000000, 1200000000),
]:
    a = load(filename)
    p = a[:, 0]
    assert np.array_equal(p, prime_list(lo, hi))
    assert np.all(a[:, 1] > 0)
    # Rerun the source C engine at 11 spread-out points per interval.
    ix = np.linspace(0, len(a)-1, 11, dtype=int)
    output = subprocess.run([str(root / "wcount"), "list", "50000"],
                            input="\n".join(map(str, p[ix]))+"\n", text=True,
                            capture_output=True, check=True, timeout=60).stdout
    got = np.array([list(map(int, line.split())) for line in output.splitlines()])
    assert np.array_equal(got, a[ix])
    g = a[:, 2:].reshape(-1, 5, 5)
    groups = [np.flatnonzero(p % 840 == s) for s in np.unique(p % 840)]
    print(filename, "N", len(a), "prime census and 11 exact grid reruns MATCH")
    for label, X in [("u", g.sum(2)), ("C", g.sum(1))]:
        residual = X.astype(float)
        for ix in groups:
            residual[ix] -= X[ix].mean(0)
        corr = np.corrcoef(residual.T)
        print(label, "means", np.round(X.mean(0), 3), "within-840 negative leads",
              [(i, j, round(corr[i,j], 5), round(corr[i,j]*math.sqrt(len(a)), 2))
               for i in range(5) for j in range(i+1, 5) if corr[i,j]*math.sqrt(len(a)) < -4])
        covariance = residual.T @ residual / len(a)
        print(label, "off-diagonal covariance sum", covariance.sum()-np.trace(covariance))
    Z = a[:, 2:] == 0
    rates = Z.mean(0)
    eligible = np.flatnonzero((rates >= .05) & (rates <= .95))
    class_rates = np.array([Z[ix].mean(0) for ix in groups])
    sizes = np.array([len(ix) for ix in groups])
    ratios = []
    for k in range(2, 9):
        observed = expected = 0.0
        for _ in range(300):
            cells = rng.choice(eligible, size=k, replace=False)
            observed += np.count_nonzero(np.logical_and.reduce(Z[:, cells], axis=1))
            expected += np.dot(sizes, np.prod(class_rates[:, cells], axis=1))
        ratios.append(round(observed/expected, 3))
    print("pooled joint-empty ratios k=2..8", ratios)
    if lo >= 1000000000:
        class_mean = {int(p[ix[0]] % 840): a[ix, 2:].mean(0) for ix in groups}
        expected = np.array([class_mean[int(n % 840)] for n in ns[:, 0]])
        actual = ns[:, 2:].reshape(-1, 5, 5).sum(0)
        expected = expected.reshape(-1, 5, 5).sum(0)
        print("near-square total/u/C ratios", actual.sum()/expected.sum(),
              actual.sum(1)/expected.sum(1), actual.sum(0)/expected.sum(0))

# Rerun the decisive genus masses, and every non-square census zero's exact count.
non_square = sorted(primes + composites + [8813281])
output = subprocess.run([str(root / "wcount"), "list", "40000"],
                        input="\n".join(map(str, non_square))+"\n", text=True,
                        capture_output=True, check=True, timeout=60).stdout
assert all(int(line.split()[1]) == 0 for line in output.splitlines())
print("all 299 non-square zeros reproduced with source engine")
values = [25, 9801, 1002001, 409, 810001, 8813281, 1000009]
output = subprocess.run([str(root / "mgen")], input="\n".join(map(str, values))+"\n",
                        text=True, capture_output=True, check=True, timeout=180).stdout
print("genus engine rerun:\n"+output, end="")
for line in output.splitlines():
    n, mass, rs, _ = line.split()
    if int(n) in (25, 9801, 1002001):
        assert float(mass) == 0 and int(rs) == 0
    if int(n) in non_square:
        assert int(rs) == 0
print("810001 factorization", factorint(810001))
print("PASS")
