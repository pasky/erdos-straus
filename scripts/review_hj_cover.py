"""R174: from-scratch check of HJ_DEEP Lemma 3.2 numerics. For modulus M, mark every residue class mod M that is
forced (on the residue level, ignoring the size condition on the third letter) by a fixed-pair family whose modulus
divides M:  (t,u): n == -u (mod tu-1);  (t,v): same by symmetry;  (u,v): n == -(u+v) (mod uv).  Report uncovered fraction,
first uncovered residues, and whether M-1 is uncovered."""
import sys, numpy as np
M = int(sys.argv[1])
divs = [d for d in range(1, M + 1) if M % d == 0]
cov = np.zeros(M, dtype=bool)
for m in divs:
    if m < 3: continue
    reds = set()
    for u in range(2, m + 2):           # (t,u): tu-1 = m
        if (m + 1) % u == 0 and (m + 1) // u >= 2: reds.add((-u) % m)
    for u in range(2, m + 1):           # (u,v): uv = m
        if m % u == 0 and m // u >= 2: reds.add((-(u + m // u)) % m)
    for r in reds: cov[r::m] = True
unc = np.flatnonzero(~cov)
print(f"M={M} uncovered fraction={len(unc)/M:.4%} first={unc[:8].tolist()} M-1 uncovered={not cov[M-1]}")
