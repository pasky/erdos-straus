"""z52c_bmL_stats.py — statistics for BM_LVALUE.md §1, §3 from data/z52c/bmL/*.tsv.gz.

Usage: uv run python scripts/z52c_bmL_stats.py > data/z52c/bmL/stats.txt
"""
import gzip, math, sys
import numpy as np

D = "data/z52c/bmL/"
FAIL1 = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281]
FAIL3 = [7, 31, 79, 127, 199, 2719, 8191, 861199]


def load(name):
    with gzip.open(D + name + ".tsv.gz", "rt") as f:
        hdr = f.readline().split()
        a = np.loadtxt(f)
    return {h: a[:, i] for i, h in enumerate(hdr)}


def sub(d, m):
    return {k: v[m] for k, v in d.items()}


def cat(*ds):
    return {k: np.concatenate([d[k] for d in ds]) for k in ds[0]}


cen, win, strat = load("census"), load("window"), load("strat")
alld = cat(cen, win, strat)
_, ix = np.unique(alld["p"], return_index=True)
alld = sub(alld, ix)
print(f"# primes: census {len(cen['p'])}, window {len(win['p'])}, strat {len(strat['p'])}; distinct {len(alld['p'])}")


def errtab(d, title):
    print(f"\n## {title}")
    print("range | class | N | mean err | sd err | max|err| (at p) | sd(err·√p/L^1.5) | max|bulk err| | max|Tbdry| | range of T")
    for lo, hi in [(10**3, 10**4), (10**4, 10**5), (10**5, 10**6 + 1), (10**6 + 1, 9_800_000), (9_800_000, 10**7)]:
        for cls in (1, 5, 3, 7):
            m = (d["p"] >= lo) & (d["p"] < hi) & (d["p8"] == cls)
            if m.sum() < 5:
                continue
            p, e = d["p"][m], d["err"][m]
            L = np.log(p)
            be = d["Tbulk"][m] - d["pred"][m]
            k = np.argmax(np.abs(e))
            print(f"[{lo:.0e},{hi:.0e}) | {cls} (8) | {m.sum()} | {e.mean():+.4f} | {e.std():.4f} | {abs(e[k]):.4f} ({int(p[k])}) | "
                  f"{(e*np.sqrt(p)/L**1.5).std():.3f} | {np.abs(be).max():.4f} | {np.abs(d['Tbdry'][m]).max():.4f} | "
                  f"[{d['T'][m].min():.2f}, {d['T'][m].max():.2f}]")


errtab(alld, "Error err = T − ¼·sgn·E·L(1,χ)² by range and p mod 8")

# decay fit of rms error, p = 1 (4)
print("\n## RMS error vs p (p ≡ 1 (4)), dyadic bins; fit log rms = a + α log p")
m1 = alld["p"] % 4 == 1
p, e = alld["p"][m1], alld["err"][m1]
xs, ys = [], []
for k in range(10, 24):
    m = (p >= 2**k) & (p < 2**(k + 1))
    if m.sum() >= 20:
        rms = math.sqrt((e[m]**2).mean())
        xs.append(math.log(np.median(p[m]))); ys.append(math.log(rms))
        print(f"[2^{k},2^{k+1}) N={m.sum()} rms={rms:.4f} mean={e[m].mean():+.4f} rms·√p/L^1.5={rms*math.sqrt(np.median(p[m]))/math.log(np.median(p[m]))**1.5:.3f}")
al = np.polyfit(xs, ys, 1)
print(f"fit: rms ≈ {math.exp(al[1]):.3g}·p^{al[0]:.3f}")

print("\n## (★)-failure primes (p ≡ 1 (4)) and p ≡ 7 (8) failures ≤ 10⁶")
print("p | p mod 8 | R | M0 | T | ¼E L² | err | L(1,χ) | E | M_BM = M0−T | M_BM/L² | Mgen")
for q in FAIL1 + FAIL3:
    m = alld["p"] == q
    if not m.any():
        print(q, "missing"); continue
    r = sub(alld, m)
    L = math.log(q)
    print(f"{q} | {int(r['p8'][0])} | {int(r['R'][0])} | {r['M0'][0]:.3f} | {r['T'][0]:.4f} | {r['pred'][0]:.4f} | {r['err'][0]:+.4f} | "
          f"{r['L1'][0]:.4f} | {r['E'][0]:.4f} | {r['M0'][0]-r['T'][0]:.3f} | {(r['M0'][0]-r['T'][0])/L**2:.4f} | {r['Mgen'][0]:.3f}")


def corr_block(d, title):
    print(f"\n## {title}  (N = {len(d['p'])})")
    R, M0, T, pred, Mg = d["R"], d["M0"], d["T"], d["pred"], d["Mgen"]
    y = R - M0
    for nm, x in [("T", T), ("¼E L²", pred), ("M0 − Mgen", M0 - Mg)]:
        A = np.vstack([x, np.ones_like(x)]).T
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        r = np.corrcoef(x, y)[0, 1]
        print(f"regress R − M0 on −({nm}): slope {-coef[0]:+.3f}, corr {-r:+.3f}, R² {r*r:.3f}")
    for nm, M in [("M0", M0), ("M_BM = M0 − T", M0 - T), ("M0 − ¼E L²", M0 - pred), ("Mgen", Mg)]:
        res = R - M
        print(f"main term {nm}: mean(R − M) {res.mean():+.3f}, var(R − M)/(2·mean M) {res.var()/(2*M.mean()):.3f}, "
              f"corr(R, M) {np.corrcoef(R, M)[0,1]:+.3f}")


for lo, hi, cls in [(10**5, 10**6 + 1, 1), (9_800_000, 10**7, 1), (10**5, 10**6 + 1, 3), (9_800_000, 10**7, 3)]:
    m = (alld["p"] >= lo) & (alld["p"] < hi) & (alld["p"] % 4 == cls)
    corr_block(sub(alld, m), f"[{lo:.0e},{hi:.0e}), p ≡ {cls} (4)")

# hardest primes by R/M_BM, p = 1 (4), p >= 1e4
print("\n## 25 smallest R/M_BM among p ≡ 1 (4), p ≥ 10⁴ (census + window + strat)")
m = (alld["p"] % 4 == 1) & (alld["p"] >= 10**4)
d = sub(alld, m)
MBM = d["M0"] - d["T"]
o = np.argsort(d["R"] / MBM)[:25]
z = (d["L1"] - d["L1"].mean()) / d["L1"].std()
for i in o:
    print(f"p={int(d['p'][i])} p8={int(d['p8'][i])} R={int(d['R'][i])} M0={d['M0'][i]:.2f} T={d['T'][i]:+.3f} "
          f"pred={d['pred'][i]:+.3f} L1={d['L1'][i]:.3f} (z {z[i]:+.2f}) M_BM={MBM[i]:.2f} Mgen={d['Mgen'][i]:.2f}")

# share of hard primes with p = 1 (8) and large L
print("\n## Among p ≡ 1 (4), p ∈ [10⁴, 10⁷]: fraction with p ≡ 1 (8) and mean L(1,χ), all vs. lowest 1% of R/M0")
q = d["R"] / d["M0"]
lo1 = q <= np.quantile(q, 0.01)
for nm, mm in [("all", np.ones_like(lo1)), ("lowest 1% R/M0", lo1)]:
    print(f"{nm}: N={mm.sum()} frac p≡1(8)={np.mean(d['p8'][mm]==1):.3f} mean L1={d['L1'][mm].mean():.3f} "
          f"mean T/M0={np.mean(d['T'][mm]/d['M0'][mm]):+.4f}")

print("\n## M_BM/L² extremes (p ≡ 1 (4), p ≥ 10⁵)")
m = (alld["p"] % 4 == 1) & (alld["p"] >= 10**5)
d = sub(alld, m); L = np.log(d["p"])
r = (d["M0"] - d["T"]) / L**2
i = np.argmin(r)
print(f"min M_BM/L² = {r[i]:.4f} at p={int(d['p'][i])} (T={d['T'][i]:.3f}, L1={d['L1'][i]:.3f}); max T/L² = {(d['T']/L**2).max():.4f}; "
      f"max L1/log p = {(d['L1']/L).max():.4f}; max E (p≡1(8)) = {d['E'][d['p8']==1].max():.4f}")

# §3.3 controls: does L(1,χ) predict the lower tail beyond the main terms?
print("\n## Residual correlations with L(1,χ) (p ≡ 1 (4), p ≥ 10⁵; z := (R − M)/√M)")
m = (alld["p"] % 4 == 1) & (alld["p"] >= 10**5)
d = sub(alld, m)
for nm, M in [("M0", d["M0"]), ("M_BM", d["M0"] - d["T"]), ("Mgen", d["Mgen"])]:
    z = (d["R"] - M) / np.sqrt(M)
    lo = z <= np.quantile(z, 0.01)
    print(f"{nm}: corr(z, L1) = {np.corrcoef(z, d['L1'])[0,1]:+.3f}; within p≡1(8): {np.corrcoef(z[d['p8']==1], d['L1'][d['p8']==1])[0,1]:+.3f}; "
          f"lowest 1% of z: frac p≡1(8) {np.mean(d['p8'][lo]==1):.2f}, mean L1 {d['L1'][lo].mean():.2f} (all: {d['L1'].mean():.2f})")
print("\n## Failure primes vs. the subpopulation with the same small-prime pattern χ(2)=χ(3)=χ(5)=+1 (p ≡ 1 (8), p ≡ 1 (3), p ≡ ±1 (5))")
P = alld["p"].astype(np.int64)
pat = (P % 8 == 1) & (P % 3 == 1) & ((P % 5 == 1) | (P % 5 == 4))
dd = sub(alld, pat & (P >= 10**4))
print(f"subpopulation (p ≥ 10⁴): N={len(dd['p'])}, mean L1={dd['L1'].mean():.3f}, sd={dd['L1'].std():.3f}")
for q in FAIL1:
    mm = alld["p"] == q
    in_pat = bool(pat[mm][0])
    r = (alld["L1"][mm][0] - dd["L1"].mean()) / dd["L1"].std()
    print(f"  {q}: pattern {'yes' if in_pat else 'no '} χ(7)={'+' if pow(q % 7, 3, 7) == 1 else '-'} L1={alld['L1'][mm][0]:.3f} z_within={r:+.2f}")
