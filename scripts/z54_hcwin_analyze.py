#!/usr/bin/env python3
"""z54 HCWIN: calibrate the conditioned class-lottery hypothesis Lot against data from z54_hcwin_lines.c.

Input file rows: n HC  then for X in TH (8,16,...,1024): Lam Gam Z LamOut Zout GE GL.
For each window X: P(HC > X | mass bin) for mass = Lam (anatomy) and Gam (genus), fit of -log P(fail) ~ c*mass,
max mass among failures (the Lot falsifier), outer-certificate share, mass/log n quantiles.
Usage: python3 z54_hcwin_analyze.py file [file ...]
"""
import sys, math
import numpy as np

TH = [8, 16, 32, 64, 128, 256, 512, 1024]
W = 7

def load(fn):
    rows = []
    with open(fn) as f:
        for line in f:
            if line.startswith('#'):
                continue
            a = line.split()
            if len(a) < 2:
                continue
            rows.append([float(v) for v in a])
    nt = (len(rows[0]) - 2) // W
    A = np.array([r[:2 + W * nt] for r in rows if len(r) >= 2 + W * nt])
    return A, nt

def fail_curve(mass, fail, nbins=12):
    """bins by mass quantile; returns list of (mass_mean, n, nfail)"""
    order = np.argsort(mass)
    out = []
    for chunk in np.array_split(order, nbins):
        if len(chunk) == 0:
            continue
        out.append((mass[chunk].mean(), len(chunk), int(fail[chunk].sum())))
    return out

def fit_c(mass, fail):
    """ML fit of P(fail | m) = exp(-c m) (one-parameter)."""
    best = None
    for c in np.linspace(0.01, 3.0, 300):
        pf = np.exp(-c * mass)
        pf = np.clip(pf, 1e-300, 1 - 1e-12)
        ll = np.sum(np.where(fail, np.log(pf), np.log1p(-pf)))
        if best is None or ll > best[1]:
            best = (c, ll)
    return best[0]

def main():
    for fn in sys.argv[1:]:
        A, nt = load(fn)
        n = A[:, 0]; hc = A[:, 1]
        L = np.log(n)
        print(f"=== {fn}: N={len(n)}  log n in [{L.min():.2f},{L.max():.2f}]  HC==0(no line<=Xmax): {(hc==0).sum()}")
        for t in range(nt):
            X = TH[t]
            lam = A[:, 2 + W * t]; gam = A[:, 3 + W * t]; Z = A[:, 4 + W * t]; lo = A[:, 5 + W * t]; zo = A[:, 6 + W * t]
            fail = (hc == 0) | (hc > X)
            nf = int(fail.sum())
            line = f"X={X:5d} fail={nf:6d} ({nf/len(n):.2e})  mean Lam/logn={np.mean(lam/L):.3f} Gam/logn={np.mean(gam/L):.3f} LamOut/logn={np.mean(lo/L):.3f}"
            if nf:
                line += f" | failures: max Lam/logn={np.max(lam[fail]/L[fail]):.3f} max Gam/logn={np.max(gam[fail]/L[fail]):.3f}"
            succ = Z > 0
            if succ.sum():
                line += f" | outer-cert share among succ: {np.mean(zo[succ] > 0):.3f}"
            print(line)
            if 0 < nf < len(n):
                cL = fit_c(lam, fail); cG = fit_c(gam, fail)
                print(f"      fit P(fail)=exp(-c*mass): c_Lam={cL:.3f} c_Gam={cG:.3f}")
                for nm, m in (("Gam", gam),):
                    cur = fail_curve(m, fail, 8)
                    print("      " + nm + " bins (mean, n, fail, -log(Pfail)/mean):  " + "  ".join(
                        f"({mm:.1f},{k},{ff},{(-math.log(ff/k)/mm if ff else float('nan')):.2f})" for mm, k, ff in cur))

if __name__ == '__main__':
    main()
