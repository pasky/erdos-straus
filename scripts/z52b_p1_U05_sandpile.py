"""z52b pass1 U05: Z2784 (Tutte at (-1,-1) of the fan = ±2^{dim bicycle} over GF(2), Rosenstiehl–Read; check vs p),
Z2677 (Hermitian ℤ/4 connection Laplacian of the fan: determinant), Z2652 (least #vertices k with a multigraph of tau=p and
non-square sandpile pairing; k=3 triangles with multiplicities x,y,z: tau=xy+yz+zx, pairing class ((y+z)/p) (cofactor)."""
import numpy as np, itertools, math
from collections import Counter
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
def leg(a, p):
    a %= p; return 0 if a == 0 else (1 if pow(a, (p-1)//2, p) == 1 else -1)
def fan_edges(t, u, v):
    # vertices a=0,b=1,c=2,s=3 ; a-b, b-c single; a-s (v-1), b-s (t-2), c-s (u-1)
    E = [(0,1),(1,2)] + [(0,3)]*(v-1) + [(1,3)]*(t-2) + [(2,3)]*(u-1)
    return E
def gf2_rank(M):
    M = M.copy() % 2; r = 0; rows, cols = M.shape
    for c in range(cols):
        piv = np.nonzero(M[r:, c])[0]
        if len(piv) == 0: continue
        pr = piv[0] + r
        M[[r, pr]] = M[[pr, r]]
        for i in range(rows):
            if i != r and M[i, c]: M[i] ^= M[r]
        r += 1
        if r == rows: break
    return r
def bicycle_dim(V, E):
    m = len(E)
    # incidence over GF(2): B (V x m); cut space = row space of B; cycle space = nullspace of B
    B = np.zeros((V, m), dtype=np.uint8)
    for j, (x, y) in enumerate(E): B[x, j] ^= 1; B[y, j] ^= 1
    rB = gf2_rank(B)
    dim_cut = rB; dim_cyc = m - rB
    # bicycle = cut ∩ cycle ; dim = dim cut + dim cyc - dim(cut+cyc)
    # cut+cyc = span of rows of B and nullspace basis of B. Compute nullspace basis.
    # nullspace via elimination on B
    A = B.copy(); piv_cols = []; r = 0
    for c in range(m):
        p_ = np.nonzero(A[r:, c])[0] if r < V else []
        if len(p_) == 0: continue
        pr = p_[0] + r; A[[r, pr]] = A[[pr, r]]
        for i in range(V):
            if i != r and A[i, c]: A[i] ^= A[r]
        piv_cols.append(c); r += 1
        if r == V: break
    free = [c for c in range(m) if c not in piv_cols]
    N = []
    for f in free:
        vec = np.zeros(m, dtype=np.uint8); vec[f] = 1
        for i, pc in enumerate(piv_cols):
            if A[i, f]: vec[pc] = 1
        N.append(vec)
    N = np.array(N, dtype=np.uint8) if N else np.zeros((0, m), dtype=np.uint8)
    S = np.vstack([B, N]) if len(N) else B
    r_sum = gf2_rank(S)
    return dim_cut + dim_cyc - r_sum
# ---- Z2784: T(-1,-1) = (-1)^{|E|} (-2)^{dim B}; check against fan (t,u,v) with tuv-u-v = p
rows = []
for t in range(3, 12):
    for u in range(3, 12):
        for v in range(3, 12):
            p = t*u*v - u - v
            if p < 5 or p % 4 != 1: continue
            E = fan_edges(t, u, v)
            bd = bicycle_dim(4, E)
            T_m11 = (-1)**len(E) * (-2)**bd
            rows.append((p, t, u, v, bd, T_m11))
log(f"Z2784 fan (t,u,v ∈[3,11], p≡1(4)): {len(rows)} triples; T(-1,-1) values: {Counter(r[5] for r in rows)}; bicycle dims: {Counter(r[4] for r in rows)}")
log("  dependence on p mod 8 / Legendre (2/p):", {(p%8, bd) for p, t, u, v, bd, _ in rows} )
# ---- Z2677: Hermitian ℤ/4 connection Laplacian (gauge i on edge a->b etc.): det of reduced Laplacian with holonomy phases
rng = np.random.default_rng(5)
dets = []
for (p, t, u, v, bd, _) in rows[:200]:
    E = fan_edges(t, u, v)
    # random Z/4 holonomy per edge (unit phase i^k), reduced Laplacian on vertices a,b,c (sink s removed)
    L = np.zeros((3, 3), dtype=complex)
    for (x, y) in E:
        ph = 1j**rng.integers(0, 4)
        for (a_, b_, w) in ((x, y, ph),):
            if a_ < 3: L[a_, a_] += 1
            if b_ < 3: L[b_, b_] += 1
            if a_ < 3 and b_ < 3: L[a_, b_] -= w; L[b_, a_] -= np.conj(w)
    dets.append((p, round(np.linalg.det(L).real, 6), abs(round(np.linalg.det(L).imag, 6))))
bad = [d for d in dets if abs(d[1] - d[0]) > 1e-6]
log(f"Z2677 Hermitian ℤ/4 connection Laplacians (random holonomies, 200 fan words): det equals p in {len(dets)-len(bad)}/{len(dets)} cases")
# ---- Z2652: k*(p) with k=3 (triangles): x,y,z≥1 with xy+yz+zx=p and ((y+z)/p) = -1 (cofactor class)
kstar = {}
for p in range(5, 1500):
    if p % 4 != 1 or any(p % q == 0 for q in range(2, int(p**.5)+1)): continue
    found = False
    for x in range(1, p+1):
        for y in range(1, p+1):
            if x*y >= p: break
            # z from xy + z(x+y) = p
            if (p - x*y) % (x+y) == 0 and (p - x*y)//(x+y) >= 1:
                z = (p - x*y)//(x+y)
                if leg(y+z, p) == -1 or leg(x+z, p) == -1 or leg(x+y, p) == -1:
                    found = True; break
        if found: break
    kstar[p] = 3 if found else None
hit3 = sum(1 for k in kstar.values() if k == 3)
log(f"Z2652 k=3 (triangle multigraphs, tau=xy+yz+zx=p, cofactor pairing non-square): {hit3} of {len(kstar)} primes p≡1(4), 5≤p<1500 have one; "
    f"first failures: {[p for p,k in kstar.items() if k is None][:10]}")
open("data/z52b/pass1/U05/2nd/sandpile_out.txt", "w").write("\n".join(out)+"\n")
