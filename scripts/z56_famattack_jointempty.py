# Multivariate joint-emptiness test (addresses: pairwise association does not determine P(all empty)).
# Windows = the 25 (u,C) grid cells of wcount. For random subsets S of cells (size k) with per-cell zero rates in [0.05, 0.95],
# (all sampled subsets kept, including those with no observed joint emptiness) compare P(all cells in S empty) with the conditional-independence prediction within strata p mod 840:
#   E_ind = sum_s (n_s/N) * prod_{i in S} P_s(cell i empty).
import sys, numpy as np
sys.path.insert(0, 'scripts')
from z56_famattack_assoc import load
rng = np.random.default_rng(56)
for fn in sys.argv[1:]:
    p, R, g = load(fn); N = len(p); Z = (g.reshape(N, 25) == 0)
    rates = Z.mean(0); ok = np.where((rates >= 0.05) & (rates <= 0.95))[0]
    strata = p % 840; us = np.unique(strata)
    Ps = np.array([Z[strata == s].mean(0) for s in us]); ws = np.array([(strata == s).mean() for s in us])
    sidx = np.searchsorted(us, strata)
    print(f"{fn}: N={N}; eligible cells {len(ok)}: " + " ".join(f"{i//5}{i%5}:{rates[i]:.2f}" for i in ok))
    for k in range(2, min(len(ok), 8) + 1):
        O = []; E = []
        for _ in range(300):
            S = rng.choice(ok, size=k, replace=False)
            O.append(Z[:, S].all(1).sum()); E.append(N * (ws * Ps[:, S].prod(1)).sum())
        O = np.array(O, float); E = np.array(E)
        # no selection on obs > 0: pooled ratio over all sampled subsets, and per-subset comparison
        print(f"  k={k}: 300 subsets; pooled joint-empty count observed {O.sum():.0f} vs within-840 independence {E.sum():.1f} (ratio {O.sum()/E.sum():.3f}); "
              f"median per-subset obs/exp {np.median(O/np.maximum(E,1e-12)):.3f}; frac obs>exp {np.mean(O>E):.2f}; frac obs=0 {np.mean(O==0):.2f}")
    S = ok; obs = Z[:, S].all(1).mean(); exp_ind = (ws * Ps[:, S].prod(1)).sum()
    print(f"  all eligible cells jointly empty: observed {obs:.5f} ({int(obs*N)} primes), within-840 independence {exp_ind:.6f}, ratio {obs/exp_ind if exp_ind>0 else float('nan'):.2f}")
