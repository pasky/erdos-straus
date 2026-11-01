"""(a) Inverse-lemma census on small cyclic groups Z/m (m even, target τ = m/2, the image of −1 in (Z/q)^*, m = q − 1)
with exponent boxes {Σ δ_i g_i : δ_i ∈ [−1,1]} (k generators, multisets, budget 1).
For every multiset with gcd(g_1..g_k, m) = 1 (full generated subgroup) whose box misses τ (r(τ) = 0, exact Fourier
count rounded to an integer and cross-checked), compute c(r) = −(−1)^r Π(1+2cos(2π r g_i/m))/3^k for r ≠ 0, and
  L(B,η) holds  ⟺  ∃ r ≠ 0, ord(r) = m/gcd(r,m) ≤ B, c(r) ≥ η     (all characters), resp. r odd only (odd characters).
Output: per (m,k) the number of obstructed full configs and the fraction satisfying L(B,η)."""
import sys, json
import numpy as np
from itertools import combinations_with_replacement
from math import gcd
from functools import reduce

def run(m, k):
    r = np.arange(m)
    order = m // np.gcd(r, m)
    sgn = np.where(r % 2 == 0, 1.0, -1.0)  # χ_r(τ) = (−1)^r
    configs = np.array([c for c in combinations_with_replacement(range(1, m), k)
                        if reduce(gcd, c, m) == 1], dtype=np.int64)
    if len(configs) == 0:
        return None
    ang = 2 * np.pi * (configs[:, :, None] * r[None, None, :] % m) / m  # n × k × m
    F = np.prod(1 + 2 * np.cos(ang), axis=1)  # n × m
    rcount = (F * sgn[None, :]).sum(axis=1) / m
    rint = np.rint(rcount)
    assert np.abs(rcount - rint).max() < 1e-6
    obs = rint == 0
    c = -sgn[None, :] * F[obs] / 3 ** k
    out = {'m': m, 'k': k, 'n_full': int(len(configs)), 'n_obs': int(obs.sum())}
    if obs.sum() == 0:
        return out
    for B in (2, 4, 6, 12):
        mask = (order <= B) & (r != 0)
        for eta in (0.05, 0.1, 0.2):
            cm = c[:, mask]
            out[f'L{B}_{eta}'] = round(float((cm >= eta).any(axis=1).mean()) if mask.any() else 0.0, 4)
            mo = mask & (r % 2 == 1)
            cmo = c[:, mo]
            out[f'Lodd{B}_{eta}'] = round(float((cmo >= eta).any(axis=1).mean()) if mo.any() else 0.0, 4)
    out['anyorder_max_c_median'] = round(float(np.median(c[:, 1:].max(axis=1))), 4)
    return out

if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 46
    for k in (1, 2, 3, 4):
        for m in range(6, M + 1, 2):
            o = run(m, k)
            if o:
                print(json.dumps(o))
                sys.stdout.flush()
