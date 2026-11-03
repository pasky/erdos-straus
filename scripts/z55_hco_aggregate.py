"""Aggregate z55_hco_census outputs: total histogram, coverage, max HC per range, tail fractions."""
import sys, re, glob, math
files = sorted(glob.glob('data/z55/hco/census_*.txt'), key=lambda f: int(re.search(r'RANGE \[(\d+)', open(f).read())[1]))
tot = {}; n5 = n1 = 0; ranges = []; high = []
for f in files:
    s = open(f).read()
    m = re.search(r'RANGE \[(\d+),(\d+)\) p=5\(8\): (\d+)  p=1\(8\): (\d+)  fail: (\d+)', s)
    a, b, c5, c1, fl = map(int, m.groups()); assert fl == 0
    h = {int(k): int(v) for k, v in re.findall(r' (\d+):(\d+)', s.split('hist:')[1])}
    assert sum(h.values()) == c1
    ranges.append((a, b, c1, max(h), h)); n5 += c5; n1 += c1
    for k, v in h.items(): tot[k] = tot.get(k, 0) + v
    high += [(int(p), int(hc)) for p, hc in re.findall(r'HIGH p=(\d+) HC=(\d+)', s)]
ranges.sort()
cov = 0
for a, b, c1, mx, h in ranges:
    assert a == cov, (a, cov); cov = b
print(f"covered [0,{cov}); primes p=5(8): {n5}, p=1(8): {n1}; max HC = {max(tot)}")
print("hist:", ' '.join(f"{k}:{tot[k]}" for k in sorted(tot)))
for a, b, c1, mx, h in ranges:
    t4 = sum(v for k, v in h.items() if k > 4) / c1; t8 = sum(v for k, v in h.items() if k > 8) / c1
    t16 = sum(v for k, v in h.items() if k > 16) / c1
    L = math.log(b)
    print(f"[{a:.2e},{b:.2e}) n1={c1} maxHC={mx} P(HC>4)={t4:.4f} P(HC>8)={t8:.5f} P(HC>16)={t16:.2e} (log b)^(2log2)={L**(2*math.log(2)):.1f}")
print("HIGH (HC>=52):", sorted((p, hc) for p, hc in high if hc >= 52))
