"""z52b pass1 U05 Z1729 (percolation of the level graph) and Z2385 (spectral gap of the shared-prime graph):
vertices C=1..T (T=400), edge C~C' iff some prime q ≤ H (H=200) divides both 4Cp+1 and 4C'p+1. Components, giant
fraction, normalized-Laplacian spectral gap; for hard primes (409, 577, 5569, 9601) and controls (401, 433, 1009, 2521)."""
import numpy as np
from collections import Counter
def factor(n):
    f = Counter(); d = 2
    while d*d <= n:
        while n % d == 0: f[d] += 1; n //= d
        d += 1
    if n > 1: f[n] += 1
    return f
T, H = 400, 200
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
for p in (409, 577, 5569, 9601, 401, 433, 1009, 2521):
    primes = [set(q for q in factor(4*C*p+1) if q <= H) for C in range(1, T+1)]
    A = np.zeros((T, T))
    for i in range(T):
        for j in range(i+1, T):
            if primes[i] & primes[j]: A[i, j] = A[j, i] = 1
    deg = A.sum(1)
    # components
    seen = [False]*T; comps = []
    for s in range(T):
        if seen[s]: continue
        st = [s]; seen[s] = True; c = 0
        while st:
            x = st.pop(); c += 1
            for y in np.nonzero(A[x])[0]:
                if not seen[y]: seen[y] = True; st.append(y)
        comps.append(c)
    giant = max(comps)/T
    Dm = np.diag([d**-0.5 if d > 0 else 0 for d in deg])
    L = np.eye(T) - Dm @ A @ Dm
    ev = np.sort(np.linalg.eigvalsh(L))
    isolated = int((deg == 0).sum())
    log(f"p={p}: edges={int(A.sum()/2)}, isolated C={isolated}, components={len(comps)}, giant fraction={giant:.3f}, "
        f"normalized-Laplacian λ2={ev[1]:.4f}")
open("data/z52b/pass1/U05/2nd/graph2_out.txt","w").write("\n".join(out)+"\n")
