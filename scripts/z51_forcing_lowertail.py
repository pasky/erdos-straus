#!/usr/bin/env python3
"""z51 forcing: lower tail of the number of successful forced windows (Type II) with q <= R, observed vs the
Poisson-binomial model with the empirical per-q rates (EXSET_CHAR_FORCING §4.3). Usage: z51_forcing_lowertail.py K R"""
import sys
K, R = sys.argv[1], int(sys.argv[2])
qs = [q for q in range(3, 401, 4) if all(q % d for d in range(2, int(q**.5)+1))]
rows = [l.split()[4] for l in open(f"data/z51_forcing/win_1e{K}_perp.txt") if not l.startswith('#')]
idx = [i for i, q in enumerate(qs) if q <= R]
nfor = [0]*len(qs); nsucc = [0]*len(qs)
for pat in rows:
    for i in idx:
        if pat[i] in 'SfF':
            nfor[i] += 1; nsucc[i] += (pat[i] == 'S')
s = [nsucc[i]/nfor[i] for i in range(len(qs)) if nfor[i]]
obs = {}; model = {}
for pat in rows:
    forced = [i for i in idx if pat[i] in 'SfF']
    k = sum(pat[i] == 'S' for i in forced); obs[k] = obs.get(k, 0) + 1
    dist = [1.0]
    for i in forced:
        si = nsucc[i]/nfor[i]; new = [0.0]*(len(dist)+1)
        for j, v in enumerate(dist): new[j] += v*(1-si); new[j+1] += v*si
        dist = new
    for j, v in enumerate(dist): model[j] = model.get(j, 0) + v
n = len(rows)
mean_obs = sum(k*v for k, v in obs.items())/n; mean_mod = sum(k*v for k, v in model.items())/n
var_obs = sum(k*k*v for k, v in obs.items())/n - mean_obs**2; var_mod = sum(k*k*v for k, v in model.items())/n - mean_mod**2
print(f"p~1e{K}, q<=R={R}, {n} primes: mean #successful forced windows obs {mean_obs:.3f} model {mean_mod:.3f}; var obs {var_obs:.3f} model {var_mod:.3f}")
cum_o = cum_m = 0
for j in range(0, 8):
    cum_o += obs.get(j, 0); cum_m += model.get(j, 0)
    print(f"  P(#succ <= {j}): obs {cum_o/n:.4e}  model {cum_m/n:.4e}")
