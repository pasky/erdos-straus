"""O273 item (4): far lower-tail law P(R*_m = 0 | M) on the c = 1 line of m/n (EVIDENCE; across-n, barrier B6).

Inputs (produced by scripts/z42_zero_law.c; large intermediate files live in a tempdir, not in the repo):
  --zprox   lines "n proxy" for zeros (R* = 0) in the window
  --zexact  lines "n M M0" exact BM main term for a subset of zeros (all zeros with large proxy)
  --pprox   lines "n proxy" for a uniform sample of admissible n in the window (population)
  --pexact  lines "n M M0" exact for a sub-sample of the population (calibration)
  --lo --hi window, --nadm number of admissible n in the window, --zset optional "n" list of ALL zeros in window
M-hat := exact M where available, else proxy + median(exact - proxy) (calibrated on the population sub-sample).
Bins of width 2; P(0 | bin) = Z_bin / (nadm * f_bin); Poisson reference: R*/2 ~ Poi(M/2) => P = exp(-M/2).
Fit: log(-log P) = log A + beta log M over bins with M in [Mlo, Mhi] (weights = zero counts).
"""
import argparse
import math

import numpy as np


def load(path, cols):
    a = np.loadtxt(path, ndmin=2)
    return a[:, :cols]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zprox")
    ap.add_argument("--zexact")
    ap.add_argument("--pprox")
    ap.add_argument("--pexact")
    ap.add_argument("--lo", type=float)
    ap.add_argument("--hi", type=float)
    ap.add_argument("--nadm", type=float)
    ap.add_argument("--zeroset", help="file of all zero n (to flag population members)")
    ap.add_argument("--Mlo", type=float, default=10)
    ap.add_argument("--Mhi", type=float, default=30)
    ap.add_argument("--width", type=float, default=2)
    a = ap.parse_args()

    zp = load(a.zprox, 2)
    zp = zp[(zp[:, 0] >= a.lo) & (zp[:, 0] <= a.hi)]
    ze = load(a.zexact, 3) if a.zexact else np.zeros((0, 3))
    pp = load(a.pprox, 2)
    pe = load(a.pexact, 3) if a.pexact else np.zeros((0, 3))

    # calibration
    pmap = dict(zip(pp[:, 0].astype(np.int64), pp[:, 1]))
    d_pop = np.array([m - pmap[int(n)] for n, m, _ in pe if int(n) in pmap])
    zmap = dict(zip(zp[:, 0].astype(np.int64), zp[:, 1]))
    d_zero = np.array([m - zmap[int(n)] for n, m, _ in ze if int(n) in zmap])
    off = float(np.median(d_pop)) if len(d_pop) else 0.0
    print(f"calibration exact-proxy: population n={len(d_pop)} median {off:.3f} rms-dev "
          f"{np.sqrt(np.mean((d_pop - off) ** 2)) if len(d_pop) else float('nan'):.3f} max|dev| "
          f"{np.max(np.abs(d_pop - off)) if len(d_pop) else float('nan'):.3f};  zeros n={len(d_zero)} median "
          f"{np.median(d_zero) if len(d_zero) else float('nan'):.3f} rms-dev "
          f"{np.sqrt(np.mean((d_zero - off) ** 2)) if len(d_zero) else float('nan'):.3f}")

    zex = dict(zip(ze[:, 0].astype(np.int64), ze[:, 1]))
    Mz = np.array([zex.get(int(n), p + off) for n, p in zp])
    pex = dict(zip(pe[:, 0].astype(np.int64), pe[:, 1]))
    Mp = np.array([pex.get(int(n), p + off) for n, p in pp])
    nz_exact = sum(1 for n, _ in zp if int(n) in zex)
    print(f"window [{a.lo:.3g},{a.hi:.3g}]: zeros {len(zp)} (exact M for {nz_exact}), population sample {len(pp)}, "
          f"admissible {a.nadm:.6g}")
    for t in (20, 22, 24, 26, 28, 30):
        sel = Mz >= t
        print(f"  zeros with M >= {t}: {int(sel.sum())}  (of which exact: "
              f"{sum(1 for n, m in zip(zp[:, 0], Mz) if m >= t and int(n) in zex)})")

    edges = np.arange(0, 40 + a.width, a.width)
    rows = []
    print(" bin        Z      f_pop    P(0|M)      P/E[exp(-M/2)|bin]   -logP")
    for lo_, hi_ in zip(edges[:-1], edges[1:]):
        Z = int(((Mz >= lo_) & (Mz < hi_)).sum())
        f = float(((Mp >= lo_) & (Mp < hi_)).mean())
        if f == 0 or Z == 0:
            if Z or f:
                print(f" [{lo_:4.0f},{hi_:4.0f})  {Z:6d}  {f:8.5f}       -")
            continue
        npop = f * a.nadm
        P = Z / npop
        Mmid = float(np.mean(Mz[(Mz >= lo_) & (Mz < hi_)]))
        inb = (Mp >= lo_) & (Mp < hi_)
        pois = float(np.mean(np.exp(-Mp[inb] / 2)))  # E[exp(-M/2) | M in bin] over the population (review repair)
        # relative error: Poisson on Z plus binomial on f
        rel = math.sqrt(1 / Z + (1 - f) / (f * len(pp)))
        rows.append((Mmid, P, Z, rel))
        print(f" [{lo_:4.0f},{hi_:4.0f})  {Z:6d}  {f:8.5f}  {P:10.3e} (±{100*rel:4.0f}%)  {P/pois:8.2f}  {-math.log(P):6.2f}")
    sel = [(m, p, z, r) for m, p, z, r in rows if a.Mlo <= m <= a.Mhi]
    if len(sel) >= 3:
        x = np.log([m for m, *_ in sel])
        y = np.log([-math.log(p) for _, p, _, _ in sel])
        # y = log(-log P): sigma_y = rel/|log P|  (review repair: weights were 1/rel^2)
        w = np.array([math.log(p) ** 2 / (r * r) for _, p, _, r in sel])
        W = np.diag(w)
        X = np.vstack([np.ones_like(x), x]).T
        cov = np.linalg.inv(X.T @ W @ X)
        coef = cov @ X.T @ W @ y
        res = y - X @ coef
        chi2 = float(res @ W @ res)
        dof = len(sel) - 2
        print(f"chi2 = {chi2:.1f} on {dof} dof (formal SE below is scaled by sqrt(chi2/dof) when > 1)")
        cov = cov * max(1.0, chi2 / dof)
        print(f"fit -log P = A M^beta on M in [{a.Mlo},{a.Mhi}] ({len(sel)} bins): beta = {coef[1]:.3f} ± "
              f"{math.sqrt(cov[1,1]):.3f} (stat., ignores bin correlation), A = {math.exp(coef[0]):.3f}")
        # also linear slope of log P per unit M
        xs = np.array([m for m, *_ in sel])
        ys = np.log([p for _, p, _, _ in sel])
        sl = np.polyfit(xs, ys, 1, w=np.array([1 / r for *_, r in sel]))
        print(f"linear: d log P / dM = {sl[0]:.3f} (Poisson reference -0.5)")
        top = sel[-3:]
        if len(top) == 3:
            loc = [(math.log(-math.log(top[i + 1][1])) - math.log(-math.log(top[i][1]))) /
                   (math.log(top[i + 1][0]) - math.log(top[i][0])) for i in range(2)]
            print("local beta over the top three bins:", [round(v, 3) for v in loc])


if __name__ == "__main__":
    main()
