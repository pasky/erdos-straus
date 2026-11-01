"""Hard primes and mod-840-matched controls for the FOURIER lane (deterministic).
Hard = the 14 (★)-zeros ≤ 1e10 (FRONTIER §2.1) ∪ the 16 primes p ≡ 1 (4) ≤ 1e7 with largest m_II (least window
hitting −1; data/z45_siegel_dichotomy/windows.csv.gz, ties broken by p).  Controls: for each hard p, the 2 nearest primes
below and 2 above in the same class mod 840 (not in the hard set, not with m_II ≥ 31 when ≤ 1e7)."""
import gzip, csv, json
from z52d_fourier_lib import isprime
STAR = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]
rows = list(csv.reader(gzip.open('../data/z45_siegel_dichotomy/windows.csv.gz', 'rt')))[1:]
mII = {int(r[0]): int(r[2]) for r in rows}
top = sorted(mII, key=lambda p: (-mII[p], p))[:16]
hard = sorted(set(STAR) | set(top))
ctrl = {}
for p in hard:
    out = []
    for step in (-840, 840):
        q = p + step
        k = 0
        while k < 2 and q > 0:
            if isprime(q) and q not in hard and mII.get(q, 0) < 31:
                out.append(q); k += 1
            q += step
    ctrl[p] = sorted(out)
json.dump({'hard': hard, 'star': STAR, 'mII_top': top, 'ctrl': ctrl, 'mII': {p: mII.get(p) for p in hard}},
          open('../data/z52d/fourier/primes.json', 'w'), indent=0)
print(len(hard), hard)
print(sum(len(v) for v in ctrl.values()))
