#!/usr/bin/env python3
"""z54 HCWIN: joint-failure calibration of the conditioned lottery (scan files of z54_hcwin_lines.c, mode scan).

Row: p HC  GE(X) GL(X) D(X) for X in SX = 8,12,16,20,24,28,32,40,48,64  (untruncated genus masses m = g/|G_x^2| summed
over E- resp. L- *lottery* lines (x not dividing 24) with x <= X; D = number of deterministic lines x | 24 (G_x of
exponent 2, genus = class) with g > 0 -- each of them succeeds).
Lottery-with-independence prediction, for primes with D = 0: P(HC > X | data) = exp(-(GE + cL*GL)), cL = level-line
constant (pairing d <-> N/d).
Prints per X: observed failures, expected sum, ratio, split of observed failures into genus-dead (GE+GL == 0) and
class failures (GE+GL > 0), and calibration by bins of S = GE + cL*GL.
Usage: python3 z54_hcwin_joint.py scanfile [cL ...]
"""
import sys, math
import numpy as np

SX = [8, 12, 16, 20, 24, 28, 32, 40, 48, 64]

def main():
    fn = sys.argv[1]
    cLs = [float(v) for v in sys.argv[2:]] or [0.5]
    import pandas as pd
    A = pd.read_csv(fn, sep=" ", header=None).to_numpy(dtype=float)
    hc = A[:, 1]
    print(f"=== {fn}: N={len(A)} p in [{A[0,0]:.4g}, {A[-1,0]:.4g}]")
    for t, X in enumerate(SX):
        GE = A[:, 2 + 3 * t]; GL = A[:, 3 + 3 * t]; D = A[:, 4 + 3 * t]
        fail = (hc == 0) | (hc > X)
        nf = int(fail.sum())
        if (fail & (D > 0)).any():
            print('  WARNING: failure with a deterministic line g>0', int((fail & (D > 0)).sum()))
        live = D == 0
        dead = fail & (GE + GL == 0)
        out = f"X={X:3d} #(D=0)={int(live.sum())} obs fail={nf:6d} (genus-dead {int(dead.sum())}, class {nf-int(dead.sum())})"
        for cL in cLs:
            S = GE + cL * GL
            exp_all = np.exp(-S[live]).sum()
            pos = live & (S > 0)
            exp_cls = np.exp(-S[pos]).sum()
            obs_cls = int((fail & pos).sum())
            out += f" | cL={cL}: expected(all)={exp_all:.1f} class obs/exp={obs_cls}/{exp_cls:.1f}={obs_cls/exp_cls if exp_cls>0 else float('nan'):.2f}"
            if fail[pos].any():
                out += f" maxS(class fail)={S[fail & pos].max():.2f}"
        print(out)
        cL = cLs[0]
        S = GE + cL * GL
        pos = live & (S > 0)
        # calibration by bins of S among S>0
        edges = [0, 1, 2, 3, 4, 5, 6, 8, 10, 15, 1e9]
        parts = []
        for a, b in zip(edges[:-1], edges[1:]):
            sel = pos & (S > a) & (S <= b)
            k = int(sel.sum())
            if k == 0:
                continue
            o = int((fail & sel).sum()); e = np.exp(-S[sel]).sum()
            parts.append(f"({a:g},{b:g}]: n={k} obs={o} exp={e:.1f}")
        print("     S-bins (cL=%g): " % cL + "; ".join(parts))

if __name__ == '__main__':
    main()
