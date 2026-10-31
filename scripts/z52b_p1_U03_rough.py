"""z52b Pass-1 U03 Z2587 (fixed model): (p,C) pairs, C<=10, N_C=4Cp+1 with no prime factor <= y.
Model: for prime q, P(q | N_C) = 1/(q-1) if q ∤ 4C (p unit mod q) (p equidistributed mod q over units), 0 if q | 4C (N_C ≡ 1 mod q).
Independence over q <= y, averaged over C<=10."""
import numpy as np
pr = np.load("data/z52b/pass1/U03/feat_P100000_K100.npz")["primes"]
for y in [7, 13, 23]:
    small = [q for q in range(2, y + 1) if all(q % r for r in range(2, q))]
    obs = [all((4 * C * int(p) + 1) % q for q in small) for p in pr for C in range(1, 11)]
    model = []
    for C in range(1, 11):
        pr_ = 1.0
        for q in small:
            pr_ *= 1.0 if (4 * C) % q == 0 else (1 - 1 / (q - 1))
        model.append(pr_)
    print(f"Z2587 y={y}: obs {np.mean(obs):.4f} vs model (q|4C aware) {np.mean(model):.4f}")
