"""Z1174: finite Fourier uncertainty of divisor-residue distributions (G4, NC0).
m = 840 (= 4C with C = 210). Three distributions f on Z/840 (additive group):
  f_all : #primes p <= 2e4, p = 1 mod 4, with p = r (mod 840)            (baseline)
  f_hard: same, restricted to primes NOT covered by any repo chart (s<=60)  (Mordell classes)
  f_div : divisor-residue distribution: over the repo charts (s<=60, dedup by covered set), for each chart the
          numbers N_c = 4a^2 d + 1 (Type I) or a + b (Type II); f_div(r) = #{(c, f): f | N_c, f = r mod 840}.
For each nonzero f: |supp f| * |supp fhat| vs |G| = 840 (Donoho-Stark / finite uncertainty:
  |supp f| |supp fhat| >= |G| for every nonzero f on a finite abelian group).
Also report the minimal product over the (f_div restricted to subsets of charts) family: no -- only the three above."""
import sys, math
sys.path.insert(0, "scripts")
import numpy as np
from z52d_p2_NC0_lib import primes_upto, families, covered_mask, divisors

M = 840
ps = primes_upto(2 * 10**4)
ps = ps[(ps % 4 == 1) & (ps > 5)]
fams = families(60)
seen = {}
for f in fams:
    key = covered_mask(f, ps).tobytes()
    if key not in seen or f["s"] < seen[key]["s"]:
        seen[key] = f
charts = list(seen.values())
cov = np.zeros(len(ps), dtype=bool)
for c in charts:
    cov |= covered_mask(c, ps)
f_all = np.bincount(ps % M, minlength=M).astype(float)
f_hard = np.bincount(ps[~cov] % M, minlength=M).astype(float)
f_div = np.zeros(M)
for c in charts:
    a, d = c["params"]
    N = 4 * a * a * d + 1 if c["type"] == "I" else a + d  # type II: params=(a,b), N=a+b
    for fdiv in divisors(N):
        f_div[fdiv % M] += 1
print(f"|G|={M}; primes 1mod4 <=2e4: {len(ps)}; hard (uncovered) primes: {int((~cov).sum())}; charts: {len(charts)}")

def fourier_support(f):
    F = np.fft.fft(f)  # additive DFT on Z/M
    return int((np.abs(F) > 1e-9 * max(1, np.abs(F).max())).sum())

rows = []
for name, f in [("f_all", f_all), ("f_hard", f_hard), ("f_div", f_div)]:
    S = int((f > 0).sum()); Sh = fourier_support(f)
    rows.append((name, S, Sh, S * Sh))
    print(f"{name:7s} |supp f| = {S:4d}   |supp fhat| = {Sh:4d}   product = {S*Sh:7d}   (>= {M}? {S*Sh >= M})")
# Check the Donoho-Stark inequality on the 2^k-subsets of charts' divisor distributions (small random sample)
rng = np.random.default_rng(0)
mins = None
for trial in range(300):
    k = rng.integers(1, 6)
    idx = rng.choice(len(charts), size=k, replace=False)
    g = np.zeros(M)
    for i in idx:
        c = charts[i]; a, d = c["params"]
        N = 4 * a * a * d + 1 if c["type"] == "I" else a + d
        for fdiv in divisors(N):
            g[fdiv % M] += 1
    S = int((g > 0).sum()); Sh = fourier_support(g)
    if S * Sh < M:
        print("VIOLATION", S, Sh)
    mins = S * Sh if mins is None else min(mins, S * Sh)
print(f"random sub-collections of divisor distributions (300 trials): min |supp||supp^| = {mins} (>= {M} required)")
