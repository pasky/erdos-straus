"""s9_level_poisson.py (O271): is the (★) zero rate "level-Poisson", P(R = 0) ~ exp(-E[#hit levels])?
Inputs: pairs of files (s9_janson output: p R D NL ; z38_mbm output: p isprime R M0 MBM MBM8), p == 1 (mod 4).
Bins primes by M_BM8 (O268's arithmetic main term); per bin: n, observed zeros, and predicted zeros under
  Poisson n e^{-mu}, swap-Poisson n e^{-mu/2}, level-Poisson n e^{-E NL}  (mu = E R, NL = #distinct hit levels t),
and the same with per-prime exponents from a within-bin linear fit NL ~ a + b*M_BM8 (sum_p exp(-fit(p))).
usage: python s9_level_poisson.py JAN1 MBM1 [JAN2 MBM2 ...]"""
import sys
import numpy as np
P, R, NL, M8 = [], [], [], []
for jf, mf in zip(sys.argv[1::2], sys.argv[2::2]):
    J = np.loadtxt(jf, dtype=np.int64)
    mb = {}
    for line in open(mf):
        a = line.split()
        if int(a[0]) % 4 == 1: mb[int(a[0])] = (int(a[2]), float(a[5]))
    for p, r, d, nl in J:
        if int(p) in mb:
            assert mb[int(p)][0] == r
            P.append(p); R.append(r); NL.append(nl); M8.append(mb[int(p)][1])
P, R, NL, M8 = map(np.array, (P, R, NL, M8))
print(f"{len(P)} primes p == 1 (4), {P.min()}..{P.max()} (R cross-checked against z38_mbm)")
b, a = np.polyfit(M8, NL, 1)
print(f"global fit E[NL | M_BM8] ~ {a:.3f} + {b:.4f} M_BM8")
print(" M_BM8 bin |      n  zeros |  mu   E NL | Poisson  swap-P  level-P  level-P(fit)")
edges = [0, 4, 6, 8, 10, 12, 14, 16, 20, 25, 30, 40, 80]
tot = np.zeros(5)
for lo, hi in zip(edges[:-1], edges[1:]):
    s = (M8 >= lo) & (M8 < hi); n = s.sum()
    if n == 0: continue
    mu, el = R[s].mean(), NL[s].mean()
    row = np.array([(R[s] == 0).sum(), n*np.exp(-mu), n*np.exp(-mu/2), n*np.exp(-el), np.exp(-(a + b*M8[s])).sum()])
    tot += row   # R279-style self-review fix: totals include every bin (small bins were silently dropped before)
    print(f"[{lo:2d},{hi:2d})  | {n:6d} {int(row[0]):5d} | {mu:5.1f} {el:5.2f} | {row[1]:7.2g} {row[2]:7.2g} {row[3]:7.2g} {row[4]:9.2g}")
print(f"TOTAL observed {int(tot[0])} | Poisson {tot[1]:.2f}  swap-Poisson {tot[2]:.2f}  level-Poisson {tot[3]:.2f}  level-Poisson(fit) {tot[4]:.2f}")
