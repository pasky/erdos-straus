r"""s4_inertia: TRANSPORT_LAW Thm 3.1's archimedean count #{i : K_i < 0 < K_{i+1}} equals ind_-(path form)/2
(negative inertia index; Sylvester/LDL^T: path form ~ <K_i/K_{i-1}>), for random signed words of length r with
K_r > 0 and all K_i != 0.  usage: s4_inertia.py L r trials"""
import sys, random
import numpy as np
L, r, T = map(int, sys.argv[1:4]); rng = random.Random(3); bad = tot = 0
for _ in range(T):
    w = [rng.choice([x for x in range(-L, L + 1) if x]) for _ in range(r)]
    K = [1]; Km = 0
    for a in w: K, Km = K + [a * K[-1] - (K[-2] if len(K) > 1 else 0)], None
    if K[-1] <= 0 or 0 in K: continue
    G = np.zeros((r, r))
    for i, a in enumerate(w): G[i, i] = a
    for i in range(r - 1): G[i, i + 1] = G[i + 1, i] = -1
    neg = int((np.linalg.eigvalsh(G) < 0).sum())
    mas = sum(1 for i in range(r) if K[i] < 0 < K[i + 1])
    tot += 1; bad += (2 * mas != neg)
print(f"r={r}: {tot} words, Maslov != ind_-/2: {bad}")
