"""z52d LANE=FOURIER — arithmetic window scan (Type II e-slices) with full Fourier profiles.

For each prime p ≡ 1 (mod 4) in the list and every window 3 ≤ e ≤ E, e ≡ 3 (mod 4), gcd(e,p)=1, N=(p+e)/4:
  r = #box vectors hitting −1 (direct, exact) and the Fourier identity r = φ⁻¹Σχ(−1)F (checked, |diff| < 1e-6);
  forced := Jacobi (e/p) = −1;  type ∈ ok / sub (−1 ∉ H=⟨s⟩) / pov (−1 ∈ H, missed by the box);  Hfull := (H = G);
  for obstructed windows: c(χ_{−e}) (Jacobi (·/e), the BM/(I)7 character), kill flags (odd χ with c = 1: real χ_{−e},
  other real, only non-real), max c over χ≠1 of order ≤ B (B in BLIST) for all χ and for odd χ, global max c with order,
  and all characters with c ≥ ETA_REC (primitive id, order, parity, c) for the cross-window test.
Output: one JSON line per window to stdout (gzip it).  Usage: python z52d_fourier_scan.py E p1 p2 ...
"""
import sys, json
import numpy as np
from z52d_fourier_lib import Group, window_data, fourier_profile, direct_r, gen_subgroup, jacobi, phi

BLIST = (2, 3, 4, 6, 8, 12, 24)
ETA_REC = 0.15
_G = {}


def group(e):
    if e not in _G:
        G = Group(e)
        # index of Jacobi character (·/e): component j_t = φ_t/2 if k odd else 0
        target = np.array([(ph // 2) * (k % 2) for (l, k), ph in zip(G.comps, G.phis)])
        G.jac_idx = int(np.nonzero((G.J == target[None, :]).all(axis=1))[0][0])
        G.real = (2 * G.J % G.phi_arr[None, :] == 0).all(axis=1)
        G.oddmask = G.chim1 == -1
        _G[e] = G
    return _G[e]


def scan_prime(p, E):
    for e in range(3, E + 1, 4):
        if p % 4 != 1 or e % 4 != 3 or p % e == 0:
            continue
        N = (p + e) // 4
        G = group(e)
        sb = window_data(G, N)
        rd, vals = direct_r(e, sb)
        F, M, c, rf = fourier_profile(G, sb)
        assert abs(rf - rd) < 1e-6 * max(1, M), (p, e, rf, rd)
        forced = jacobi(e, p) == -1
        H = gen_subgroup(e, [s % e for s, b in sb])
        rec = dict(p=p, e=e, prime_e=len(G.comps) == 1 and G.comps[0][1] == 1, forced=forced, omega=len(sb),
                   M=M, phi=G.n, r=rd, Hfull=len(H) == G.n, nvals=len(vals))
        if rd > 0:
            rec['type'] = 'ok'
            yield rec
            continue
        rec['type'] = 'sub' if (e - 1) not in H else 'pov'
        nt = np.arange(G.n) != 0
        kill = (np.abs(c - 1) < 1e-9) & G.oddmask
        rec['kill_jac'] = bool(kill[G.jac_idx])
        rec['kill_real'] = bool((kill & G.real).any())
        rec['kill_min_order'] = int(G.order[kill].min()) if kill.any() else 0
        rec['c_jac'] = round(float(c[G.jac_idx]), 6)
        for B in BLIST:
            m = nt & (G.order <= B)
            rec[f'mx{B}'] = round(float(c[m].max()), 6) if m.any() else None
            mo = m & G.oddmask
            rec[f'mxo{B}'] = round(float(c[mo].max()), 6) if mo.any() else None
        i = int(np.argmax(np.where(nt, c, -9)))
        rec['cmax'] = round(float(c[i]), 6)
        rec['cmax_order'] = int(G.order[i])
        rec['cmax_odd'] = bool(G.oddmask[i])
        io = int(np.argmax(np.where(G.oddmask, c, -9)))
        rec['cmax_odd_val'] = round(float(c[io]), 6)
        rec['cmax_odd_order'] = int(G.order[io])
        rec['even_mass'] = round(float(c[nt & ~G.oddmask].sum()), 6)
        top = []
        for j in np.nonzero(nt & (c >= ETA_REC))[0]:
            pid = G.prim_id(int(j))
            top.append([[[l, str(fr)] for l, fr in pid], int(G.order[j]), bool(G.oddmask[j]), round(float(c[j]), 4),
                        bool(j == G.jac_idx)])
        rec['top'] = top
        yield rec


if __name__ == '__main__':
    E = int(sys.argv[1])
    for p in map(int, sys.argv[2:]):
        for rec in scan_prime(p, E):
            print(json.dumps(rec, separators=(',', ':')))
