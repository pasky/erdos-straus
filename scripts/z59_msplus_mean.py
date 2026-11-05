# z59 MSPLUS: two-term (plus constant) local mean model for R(n) on residue classes a mod Q, and comparison with the
# exact census table from scripts/z59_msplus_strat.c ("A" lines).
#   E[R | n = a mod Q] = sum_{u,B} w(u mod Q, B mod Q; a) / (uB)  over 4uB - u - B <= n,
#   w(al, be; a) = 1{a = -(al+be) mod g} g/4,  g = gcd(4 al be, Q)   (exact probability that n = -(u+B) mod 4uB).
# Hyperbola/Mellin: sum_{u = al, B = be, uB <= Y} 1/(uB) = log^2 Y/(2Q^2) + (c_al + c_be) log Y / Q + c_al c_be + o(1),
#   c_al = -(log Q + digamma(al/Q))/Q  (al in 1..Q).  Boundary correction (4uB - u - B <= n instead of uB <= n/4):
#   + 2 sum_u (1/u) log(4u/(4u-1)) Wbar(u mod Q),  Wbar(al) = sum_be w(al,be)/Q   [B >> u side; u <-> B symmetric].
# Model: M(a, n) = S(a)/8 log^2 Y + c1(a) log Y + c0(a), Y = n/4.
# Usage: uv run --with numpy --with scipy python z59_msplus_mean.py STRAT_OUTPUT
import sys, math
import numpy as np
from scipy.special import digamma

def model(Q, avals):
    al = np.arange(1, Q + 1)
    c = -(math.log(Q) + digamma(al / Q)) / Q
    out = {}
    A = al[:, None]; Bm = al[None, :]
    G = np.gcd((4 * A * Bm) % Q, Q); G[G == 0] = Q
    S = (A + Bm) % Q
    us = np.arange(1, 200001)
    corr_u = (1.0 / us) * np.log(4 * us / (4 * us - 1.0))
    corr_al = np.bincount((us - 1) % Q, weights=corr_u, minlength=Q)  # index al-1 for al = 1..Q
    for a in avals:
        cons = ((a + S) % G == 0)
        w = np.where(cons, G / 4.0, 0.0)
        lead = w.sum() / (2 * Q * Q)
        Wbar = w.sum(axis=1) / Q
        c1 = 2 * (Wbar * c).sum()
        c0 = (w * c[:, None] * c[None, :]).sum() + 2 * (corr_al * Wbar).sum()
        out[a] = (lead, c1, c0)
    return out

def main(fn):
    tab = {}
    for line in open(fn):
        if line[0] != 'A': continue
        _, cat, a, b, cnt, s, s2, z, l2 = line.split()
        tab[(cat, int(a), int(b))] = (float(cnt), float(s), float(s2), float(z), float(l2))
    avals = sorted(set(k[1] for k in tab))
    mod = model(840, avals)
    M = {1, 121, 169, 289, 361, 529}
    # per bin, compare observed mean with model mean for groups
    for b in range(24, 37):
        lo = 10 ** (b / 4); hi = 10 ** ((b + 1) / 4); nmid = math.sqrt(lo * hi); L = math.log(nmid / 4)
        groups = {}
        for (cat, a, bb), (cnt, s, s2, z, l2) in tab.items():
            if bb != b or cat == 'S': continue
            g3 = math.gcd(a, 105)
            key = (cat, 'M' if a in M else ('unit' if g3 == 1 else f'g{g3}'))
            lead, c1, c0 = mod[a]
            m = lead * L * L + c1 * L + c0
            G = groups.setdefault(key, [0, 0, 0, 0, 0])
            G[0] += cnt; G[1] += s; G[2] += cnt * m; G[3] += z; G[4] += cnt * lead * 8
        print(f"bin {b} n~{nmid:.3g} L={L:.2f}")
        for key in sorted(groups):
            cnt, s, ms, z, S8 = groups[key]
            print(f"   {key[0]} {key[1]:6s} cnt={cnt:10.0f} obs={s/cnt:8.3f} model={ms/cnt:8.3f} ratio={s/ms:6.3f} "
                  f"S={S8/cnt:6.3f} zeros={z:.0f}")

if __name__ == '__main__':
    main(sys.argv[1])
