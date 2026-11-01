"""Z2844: per p-mod-8 class, the 2-bridge knots K(p,A) attached to length-3 HJ words p/A = [[v,t,u]]:
Arf (= 0 iff p = +-1 mod 8, Levine; checked via Conway c2 in Z2800 script for n < 400) and signature
sigma(K(p,A)) = mubar(L(p,A)) = -3 + sum_{j in Wu set} b_j (identity checked in Z2800 for all 32 364 pairs n < 400).
For p = 1 (8): share of words with sigma = 0 (8) at 'hard' primes vs controls.
hard_M = Mordell-hard (p mod 840 in {1,121,169,289,361,529}); hard_L = lambda(p) = 3 (no boundary certificate:
(p+1)/2 has no prime factor = 3 mod 4); hard_low = bottom decile of #certificate words / log^2 p.
Usage: python z52d_p2_ZF1_Z2844_knotclass.py N out.json
"""
import sys, json, math
import numpy as np
from sympy import factorint


def sieve(N):
    s = np.ones(N + 1, bool); s[:2] = False
    for i in range(2, int(N ** .5) + 1):
        if s[i]: s[i * i::i] = False
    return s


def wu_sum(v, t, u):
    b = (v, t, u)
    for s0 in (0, 1):
        S = [s0]
        for j in range(2):
            prev = S[j - 1] if j > 0 else 0
            S.append((b[j] - prev - b[j] * S[j]) % 2)
        if (S[1] + b[2] * S[2] - b[2]) % 2 == 0:
            return sum(bb for bb, s in zip(b, S) if s)
    raise ValueError


def main():
    N = int(sys.argv[1]); P = sieve(N)
    tot = {}; s0 = {}
    for t in range(2, N):
        if 2 * t * 2 - 4 >= N: break
        for u in range(2, N):
            if 2 * t * u - u - 2 >= N: break
            for v in range(2, N):
                n = t * u * v - u - v
                if n >= N: break
                if n % 8 != 1 or not P[n]: continue
                sig = -3 + wu_sum(v, t, u)
                tot[n] = tot.get(n, 0) + 1
                if sig % 8 == 0: s0[n] = s0.get(n, 0) + 1
    ps = sorted(tot)
    allp = [p for p in range(9, N, 8) if P[p]]
    missing = [p for p in allp if p not in tot]
    hardM = {1, 121, 169, 289, 361, 529}
    rows = []
    for p in ps:
        T = tot[p]; Z = s0.get(p, 0); C = T - Z
        f = factorint((p + 1) // 2)
        lam3 = all(q % 4 == 1 for q in f)
        rows.append((p, T, Z, C, p % 840 in hardM, lam3))
    arr = np.array([(r[2] / r[1], r[3] / math.log(r[0]) ** 2, r[4], r[5]) for r in rows])
    share0 = arr[:, 0]; cn = arr[:, 1]
    lowdec = cn <= np.quantile(cn, 0.1)
    out = dict(N=N, primes_1mod8=len(allp), primes_without_words=missing,
               mean_share_sigma0=float(share0.mean()),
               mordell_hard=dict(n=int(arr[:, 2].sum()), share0=float(share0[arr[:, 2] == 1].mean()),
                                 ctrl=float(share0[arr[:, 2] == 0].mean())),
               lambda3=dict(n=int(arr[:, 3].sum()), share0=float(share0[arr[:, 3] == 1].mean()),
                            ctrl=float(share0[arr[:, 3] == 0].mean())),
               low_cert_decile=dict(n=int(lowdec.sum()), share0=float(share0[lowdec].mean()),
                                    ctrl=float(share0[~lowdec].mean())),
               mordell_hard_vs_1mod24_ctrl=dict(
                   share0_hard=float(share0[(arr[:, 2] == 1)].mean()),
                   share0_ctrl_1mod24=float(share0[(arr[:, 2] == 0) & (np.array([r[0] % 24 for r in rows]) == 1)].mean()),
                   share0_ctrl_1mod24_lam3=float(share0[(arr[:, 2] == 0) & (arr[:, 3] == 1) & (np.array([r[0] % 24 for r in rows]) == 1)].mean()),
                   share0_hard_lam3=float(share0[(arr[:, 2] == 1) & (arr[:, 3] == 1)].mean())),
               min_cert_words=min((r[3], r[0]) for r in rows),
               primes_with_all_words_sigma0=[r[0] for r in rows if r[3] == 0],
               smallest_rows=[r[:4] for r in rows[:15]])
    # by window
    win = []
    for lo in [10 ** k for k in range(2, 7)]:
        sel = [(r[2] / r[1]) for r in rows if lo <= r[0] < 10 * lo]
        if sel: win.append((lo, len(sel), float(np.mean(sel))))
    out['share0_by_decade'] = win
    print(json.dumps(out, indent=1))
    json.dump(out, open(sys.argv[2], 'w'), indent=1)


if __name__ == '__main__':
    main()
