"""s9_ladder_thinning.py (O271): the k/p two-line union = "some word of p has a coordinate == 0 (mod k)" (SPARKS9 Cor 1.2),
a k-dependent thinning of the numerator-free word set W(p).  For each k, runs /tmp/s9_words (compiled scripts/s9_words.c) on all
primes in [5, PMAX] and compares observed union failures with the mirror-binomial thinning prediction
sum_p (1 - pi_k)^{W(p)/2}, pi_k = U/W pooled in (decade x p mod 24) cells.  usage: python s9_ladder_thinning.py PMAX k1 k2 ..."""
import sys, subprocess
import numpy as np
PMAX = int(sys.argv[1])
print(f"all primes 5 <= p <= {PMAX}; columns: k | mean pi_k | observed union failures | predicted (W/2 trials) | ratio obs/pred | failures in (PMAX/10, PMAX]")
for k in map(int, sys.argv[2:]):
    out = subprocess.run(["/tmp/s9_words", "5", str(PMAX), "0", str(k)], capture_output=True, text=True, check=True).stdout
    d = np.array([list(map(int, l.split())) for l in out.splitlines()])
    p, W, U = d[:, 0], d[:, 1], d[:, 4]
    cell = np.floor(np.log10(p)).astype(int) * 100 + p % 24
    pi = np.zeros(len(p))
    for c in np.unique(cell):
        m = cell == c; pi[m] = U[m].sum() / W[m].sum()
    pred = np.sum((1 - pi) ** (W / 2.0))
    obs = int((U == 0).sum()); big = int(((U == 0) & (p > PMAX // 10)).sum())
    print(f"k={k:3d} | {np.mean(U / W):.3f} | {obs:6d} | {pred:9.1f} | {obs / pred if pred > 0 else float('nan'):6.2f} | {big}")
