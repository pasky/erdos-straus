#!/usr/bin/env python3
"""z56 K4BILIN: level threshold of the Friedlander-Iwaniec route for P(4,15) (model numerics, Assessment).
One shift (A) exact through the divisor expansion r(A) = 4 sum_{k|A} chi(k), k <= sqrt x (costs level 1/2);
the other shift (B) by the semi-linear lower sieve (level x^thD, sifting to z = x^thz, 1/4 < thz < thD)
plus Iwaniec switching of the two-Q-prime configurations (mass B(thz), times a loss constant L >= 1).
Positivity:  f(thD/thz) - L * B(thz) > 0.  Total main-term level needed: 1/2 + thD.
Model L:  'fixed' (given constant), or 'gehsw' L = pen*2/a with a = thD (switched sum with GEH-type input at level
1/2 + a, prime p detected by an upper linear sieve of level x^a, r(A) exact).
Uses F, f, B from scripts/z55_p415_sieve.py (semi-linear beta sieve, Nath-Xie/FI normalisation).
"""
import sys, importlib.util, math
spec = importlib.util.spec_from_file_location("p415", "scripts/z55_p415_sieve.py")
P = importlib.util.module_from_spec(spec); spec.loader.exec_module(P)

def ok(thD, Lfun):
    best = None
    for i in range(1, 2000):
        thz = 0.25 + i * (min(thD, 0.5) - 0.25) / 2000
        if thz >= thD: break
        v = P.fv(thD / thz) - Lfun(thD) * P.B(thz)
        if v > 0 and (best is None or v > best[0]): best = (v, thz)
    return best

def thresh(Lfun):
    lo, hi = 0.25, 0.5
    if ok(hi - 1e-9, Lfun) is None: return None
    for _ in range(40):
        mid = (lo + hi) / 2
        if ok(mid, Lfun): hi = mid
        else: lo = mid
    return hi, ok(hi, Lfun)

if __name__ == "__main__":
    print("# FI route: minimal thD (sieve level on shift B) with f(thD/thz) > L*B(thz); total level = 1/2 + thD")
    for L in [1, 2, 4, 8, 16, 32, 64, 128, 1000, 1e4]:
        r = thresh(lambda t, L=L: L)
        print(f"fixed L={L:>7}: thD* = {r[0]:.4f}  total = {0.5 + r[0]:.4f}  (thz={r[1][1]:.4f})" if r else f"L={L}: none <1/2")
    for pen in [1.0, 2.35, 5.0]:
        r = thresh(lambda t, pen=pen: pen * 2 / t)
        print(f"gehsw pen={pen}: thD* = {r[0]:.4f} total = {0.5 + r[0]:.4f} (thz={r[1][1]:.4f})" if r else f"pen={pen}: none")
