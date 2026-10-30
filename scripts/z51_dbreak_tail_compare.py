# z51 dbreak round 4 (R4 repair): empirical P(R < x) from an exact census histogram versus the Monte Carlo model law,
# evaluated at the SAME histogram edges x (nearest edges to -mu/2, -3mu/4, -mu, -1.25mu). Model SE = sqrt(p(1-p)/D).
import sys, glob, math, re
def hist(paths):
    h = {}; mu = None
    for p in paths:
        for l in open(p):
            if l.startswith('HIST '):
                _, v, c = l.split(); h[round(float(v), 3)] = h.get(round(float(v), 3), 0) + int(c)
            m = re.search(r'mu=([0-9.]+)', l)
            if m and mu is None: mu = float(m.group(1))
    return h, mu
for ex, mc in [(f"data/z51_dbreak/resid_exact_b{b}_N{N}.txt", f"data/z51_dbreak/mmc_b{b}_N{N}.txt") for b, N in
               [("0.6", "10000000000"), ("0.75", "1000000000"), ("0.9", "10000000"), ("0.9", "100000000")]]:
    he, mu = hist([ex]); hm, _ = hist([mc]); te = sum(he.values()); tm = sum(hm.values())
    print(f"{ex.split('/')[-1]}  mu={mu:.4f}  census={te}  model draws={tm}")
    for f in (0.5, 0.75, 1.0, 1.25):
        x = -10 + round((-f * mu + 10) / 0.02) * 0.02
        pe = sum(c for v, c in he.items() if v + 0.02 <= x + 1e-9) / te
        pm = sum(c for v, c in hm.items() if v + 0.02 <= x + 1e-9) / tm
        se = math.sqrt(max(pm * (1 - pm), 1e-30) / tm)
        print(f"   x={x:+.2f} (~-{f}mu): emp {pe:.5f}  model {pm:.5f} +- {se:.5f}  ratio {pe / pm if pm > 0 else float('nan'):.3f}")
