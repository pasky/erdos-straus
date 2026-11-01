"""Independent bounded recomputations for REVIEW_HCHYP.md.

Run with: ulimit -v 6000000; ulimit -t 120; timeout 120s uv run --no-project scripts/z53_xrev_hchyp_check.py /tmp/xrev_HCHYP
Uses standard-library arithmetic; no imports from the reviewed scripts.
"""
import math
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
DATA = ROOT / "data/z53/hchyp"


def factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            a = 0
            while n % d == 0:
                n //= d
                a += 1
            out.append((d, a))
        d += 1 if d == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def divisors(n):
    ds = [1]
    for p, a in factors(n):
        ds = [d * p**e for d in ds for e in range(a + 1)]
    return ds


def conductor(delta):
    if delta >= 0:
        return None
    d = -math.prod(p for p, a in factors(-delta) if a % 2)
    return abs(d if d % 4 == 1 else 4 * d)


# Compare the C controls with actual integer divisors, not residue BFS.
control_hc = {}
checks = 0
for line in (ROOT / "hc_controls.txt").read_text().splitlines():
    nt, xt, et, lt = line.split()
    n, x = int(nt), int(xt[2:])
    e = any(d % x == x - 1 for d in divisors(n + x))
    l = any(d % x == x - 1 for d in divisors(x * n + 1))
    assert (e, l) == (bool(int(et[2:])), bool(int(lt[2:])))
    if e or l:
        control_hc.setdefault(n, x)
    checks += 2
print("Independent divisor checks:", checks, "HC:", control_hc)

for path in sorted(DATA.glob("*_X2048.txt")):
    rows = [tuple(map(int, s.split())) for s in path.read_text().splitlines()
            if s and not s.startswith("#")]
    records = [tuple(map(int, s.split())) for s in Path(str(path) + ".hc").read_text().splitlines()]
    n = len(records)
    L = math.log(sum(r[0] for r in records) / n)
    hcs = [r[1] or math.inf for r in records]
    mass = 0
    xstar = None
    for x, e, l, either, fail in rows:
        assert 0 <= max(e, l) <= either <= min(n, e + l)
        assert fail == sum(h > x for h in hcs)
        mass += (e + l) / n
        if mass >= L and xstar is None:
            xstar = x
    print(path.name, "N", n, "maxHC", max(hcs), "tails4/8/16",
          [sum(h > x for h in hcs) / n for x in (4, 8, 16)],
          "X*", xstar, "X*/L", None if xstar is None else round(xstar / L, 4))
    if path.name.startswith("stat"):
        ratios = {}
        independent = 1.0
        for x, e, l, either, fail in rows:
            independent *= 1 - either / n
            if x in (7, 8, 12, 15, 16):
                ratios[x] = round((fail / n) / independent, 4)
        print("  coordinate-paired independence ratios", ratios)
    for x, index in ((64, 2), (2048, 5)):
        zs = [r[index] for r in records]
        mean = sum(zs) / n
        assert sum(e + l for t, e, l, _, _ in rows if t <= x) == sum(zs)
        if mean:
            variance = sum((z - mean)**2 for z in zs) / n
            cdf = sum(math.exp(-mean + k * math.log(mean) - math.lgamma(k + 1))
                      for k in range(math.floor(mean / 3) + 1))
            print("  Z", x, "mean", round(mean, 4), "var/mean", round(variance / mean, 4),
                  "min", min(zs), "lower_tail", sum(z <= mean / 3 for z in zs) / n,
                  "Poisson", f"{cdf:.4g}")
    if path.name == "near_k24_1e10_X2048.txt":
        for kind, col in (("E", 1), ("L", 2)):
            aligned, zero = [], []
            for row in rows:
                x = row[0]
                delta = -4 * (24 + x) if kind == "E" else -4 * x * (24 * x + 1)
                cond = conductor(delta)
                if x % cond == 0:
                    aligned.append(x)
                if row[col] == 0:
                    zero.append(x)
            assert set(zero) <= set(aligned)
            print("  near24", kind, "aligned", len(aligned), "zero", len(zero), "zero-set", zero)

# A 65,536-entry totient sieve, rather than the original 10-million-coordinate list.
limit = 65536
phi = list(range(limit + 1))
for p in range(2, limit + 1):
    if phi[p] == p:
        for j in range(p, limit + 1, p):
            phi[j] -= phi[j] // p


def cdf(mu, k):
    term = math.exp(-mu)
    total = term
    for j in range(1, k + 1):
        term *= mu / j
        total += term
    return total


def upper_mass(L, n):
    lam = math.log(L)
    k = (n + 1).bit_length() - 1
    # Split at 2^k - 1 <= n and exponentially tilt Poisson(lambda).
    return (L * cdf(2 * lam, k) - cdf(lam, k)) / n + 1 - cdf(lam, k)


for c in (1, 0.5):
    for L in (18.4, 27.6, 50, 100, 200, 400, 800, 1600):
        mass = 0
        for x in range(4, limit + 1):
            if x % 4 == 0 or x % 8 == 7:
                mass += 2 * c * upper_mass(L, phi[x])
                if mass >= L:
                    print("model", c, L, "X*", x, "X*/L", round(x / L, 5))
                    break
        else:
            raise AssertionError("Increase the explicit sieve bound")
print("All cross-checks passed.")
