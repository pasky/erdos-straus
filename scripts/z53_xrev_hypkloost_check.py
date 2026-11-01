"""Independent, bounded numerical audit of the extracted HYPKLOOST snapshot.

Usage: ulimit -v 6000000; timeout 300s env OPENBLAS_NUM_THREADS=1 \
  OMP_NUM_THREADS=8 uv run --with numpy python \
  scripts/z53_xrev_hypkloost_check.py /tmp/xrev_HYPKLOOST
The extraction directory must contain data/, scripts/, and compiled cond/kf.
No full pair-by-prime arrays: data matrices are at most 3000 x 83.
"""
import io
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
from fractions import Fraction

import numpy as np

LIMIT = 6000000 * 1024
soft, hard = resource.getrlimit(resource.RLIMIT_AS)
resource.setrlimit(resource.RLIMIT_AS, (min(LIMIT, hard) if hard != -1 else LIMIT, hard))
root = Path(sys.argv[1])
data = root / "data/z53/hypkloost"


def run(binary, u, v, ns, *extra):
    result = subprocess.run(
        [str(root / binary), str(u), str(v), *map(str, extra)],
        input="".join(f"{int(n)}\n" for n in ns), text=True,
        capture_output=True, check=True, timeout=180,
        env={**os.environ, "OMP_NUM_THREADS": "8"},
    )
    return np.loadtxt(io.StringIO(result.stdout), ndmin=2)


# Recompute the headline moments without the author's covariance/bootstrap code.
for name in ("p12", "rn12", "ns12", "sq12", "p10", "rn10", "sq10"):
    a = np.loadtxt(data / f"c_{name}.tsv.gz")
    n = a[:, 1]
    shares = []
    for start in (43, 3):
        bins = a[:, start:start + 40]
        variance_sum = np.square(bins - bins.mean(axis=0)).mean(axis=0).sum()
        shares.append((n.var() - variance_sum) / variance_sum)
        assert np.max(np.abs(bins.sum(axis=1) - n)) < 1e-8
    assert np.array_equal(a[:, 2], n)
    print(name, "rows", len(a), "var", n.var(), "zero", (n == 0).mean(),
          "shares rel/abs", *shares)
    # Recompute two original rows per set from the C source, not just the data.
    u = 316 if name.endswith("10") else 1000
    actual = run("cond", u, u, a[[0, -1], 0])
    assert np.array_equal(actual, a[[0, -1]])
print("Conductor source rerun: 14 full-scale rows agree byte-value-for-value")


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


# Different exact formula: c_d(m) = sum_{r | gcd(d,m)} r mu(d/r).
ns = [1, 9, 17, 19, 49, 101, 1009, 10007]
actual = run("cond", 2, 3, ns)
max_error = 0.0
for row, n in zip(actual, ns):
    bins = [Fraction(0) for _ in range(80)]
    hits = 0
    for u in range(3, 5):
        for b in range(4, 7):
            q, m = 4 * u * b, n + u + b
            hits += m % q == 0
            for d in divisors(q):
                c = sum(r * mobius(d // r) for r in divisors(math.gcd(d, m)))
                bins[d.bit_length() - 1] += Fraction(c, q)
                bins[40 + (q // d).bit_length() - 1] += Fraction(c, q)
    assert row[1] == hits and sum(bins[:40]) == hits and sum(bins[40:]) == hits
    max_error = max(max_error, np.max(np.abs(row[3:] - list(map(float, bins)))))
assert max_error < 1e-9
print("Independent exact Ramanujan check: 8 small rows, max printed-bin error", max_error)

for name, u, v in (("bal12", 1000, 1000), ("unb12", 100, 10000), ("unb12b", 10000, 100)):
    saved = np.loadtxt(data / f"kf_{name}.tsv")
    # Four complete source reruns per geometry; moments use every saved row.
    indices = [0, 1, len(saved) // 2, len(saved) - 1]
    actual = run("kf", u, v, saved[indices, 0], 16)
    assert np.array_equal(actual, saved[indices])
    normalized = saved[:, 6:] / np.sqrt(saved[:, 5, None])
    residual = saved[:, 2] - saved[:, 4]
    print("KF", name, "rms", np.sqrt(np.mean(normalized**2)), "max", normalized.max(),
          "N1 residual sd", residual.std(), "range", residual.min(), residual.max())
print("KF source rerun: 12 full-scale rows agree byte-value-for-value")

# DFI (1.4), checked visually against the actual source, not LIT_CHECK.md.
# U ~ p^(1/5), V ~ p^(3/5), a=p: true bound/norms ~ p^(3/10)
# whereas trivial/norms ~ p^(2/5), Cbar ~ p^(1/5)/4.
for p in (10**10, 10**20, 10**40):
    u, v = p**0.2, p**0.6
    bound = math.sqrt(u + v) + math.sqrt(1 + p / (u * v)) * min(u, v)
    print("DFI p", p, "true displayed bound / trivial (epsilon omitted)", bound / math.sqrt(u*v))
print("PASS")
