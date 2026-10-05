#!/usr/bin/env python3
"""O24 (EXCEPTIONAL_TUPLES2.md §5): single-form effects summed over ALL forms (r,s).

For each form phi=(r,s) (gcd 1, 4rs-1<=y) the phi-primes are l<=y, l = -1 mod 4rs,
with class -r/s mod l (Lemma 1.1). Per form:
  Zphi_j  = CRT mass of j-tuples whose phi-group has product > N s + r (forced zero,
            Cor 1.2), via DP over phi-primes (state: size, binned log; logs rounded
            down => lower bound) convolved with e(p') of the other hits;
  Fmix_j  = sum_k Flphi_k * e_{j-k}(non-phi primes): floor deficit of the phi-progression
            carried by independent other hits (approximation, EVIDENCE only);
  Flphi_j = (1/N) sum over pure phi-tuples G (|G|=j, q<=Ns+r) of (N/q - #{n<=N: q|ns+r}).
Sum over forms. Residue collisions between forms are ignored (each counted per form),
so the totals are estimates (EVIDENCE), not bounds.
usage: tuples2_allforms.py N y [Jmax] [step]
"""
import sys
from math import log, gcd
import numpy as np
from tuples_moments import primes_upto, R_set, esym

N = int(float(sys.argv[1])); y = int(float(sys.argv[2]))
J = int(sys.argv[3]) if len(sys.argv) > 3 else 12
step = float(sys.argv[4]) if len(sys.argv) > 4 else 0.005
P = [int(l) for l in primes_upto(y) if l % 4 == 3]
pmap = {l: len(R_set(l)) / l for l in P}
e = esym(list(pmap.values()), J)
Ztot = np.zeros(J + 1); Ftot = np.zeros(J + 1); Fmix = np.zeros(J + 1); Z11 = None
nforms = 0
for r in range(1, (y + 1) // 4 + 1):
    for s in range(1, (y + 1) // (4 * r) + 1):
        if gcd(r, s) != 1 or 4 * r * s - 1 > y:
            continue
        nforms += 1
        Q = [l for l in P if (l + 1) % (4 * r * s) == 0]
        if not Q:
            continue
        thr = log(N * s + r)
        B = int(thr / step) + 1
        dp = np.zeros((J + 1, B + 1)); dp[0, 0] = 1.0
        for l in Q:                       # phi-prime: class -r/s (shift) or another class
            w = int(log(l) / step)
            sh = np.zeros_like(dp)
            if w <= B:
                sh[:, w:] = dp[:, :B + 1 - w]
                sh[:, B] += dp[:, B + 1 - w:].sum(axis=1)
            else:
                sh[:, B] = dp.sum(axis=1)
            new = dp.copy()
            new[1:] += sh[:-1] / l + (pmap[l] - 1 / l) * dp[:-1]
            dp = new
        G = dp[:, B]                      # tuples on phi-primes whose phi-group is certainly > thr
        Qs = set(Q)
        rest = esym([pmap[l] for l in P if l not in Qs], J)
        Zphi = np.convolve(G, rest)[:J + 1]
        Ztot += Zphi
        if (r, s) == (1, 1):
            Z11 = Zphi.copy()
        # floor deficit of pure phi-tuples
        Fl = np.zeros(J + 1)
        X = N * s + r
        def dfs(i, q, j):
            if j >= 1:
                b = (-r * pow(s, -1, q)) % q
                if b == 0:
                    b = q
                cnt = (N - b) // q + 1 if b <= N else 0
                Fl[j] += N / q - cnt
            if j == J:
                return
            for k in range(i, len(Q)):
                if q * Q[k] > X:
                    break
                dfs(k + 1, q * Q[k], j + 1)
        dfs(0, 1, 0)
        Ftot += Fl / N
        Fmix += np.convolve(Fl / N, rest)[:J + 1]   # pure phi-group + independent other hits (approx.)
print(f"# N={N:.3g} y={y} forms={nforms} step={step}")
print("# j  e_j  Z11_j  Zall_j  Flall_j(pure)  Flmix_j(approx)  (Zall+Flall)/e_j  (Zall+Flmix)/e_j")
for j in range(1, J + 1):
    print(f"{j:3d} {e[j]:.4e} {Z11[j]:.4e} {Ztot[j]:.4e} {Ftot[j]:.4e} {Fmix[j]:.4e} "
          f"{(Ztot[j]+Ftot[j])/e[j]:.4e} {(Ztot[j]+Fmix[j])/e[j]:.4e}")
