# Z2764 (Smith/Z2 complex) and Z2765 (Euler characteristic of the poset of partial certificates).
# Definitions chosen here (the item leaves them open):
#  Z2764: X_p = flag complex of the 'share a letter' graph on words W_p (two words adjacent iff they share a coordinate value
#         t, u or v). Involution sigma(t,u,v)=(t,v,u) (A -> A*). Compute F2 Betti numbers of X_p and of the fixed subcomplex
#         (order complex of sigma-invariant faces), check the Smith inequality, and count sigma-fixed words.
#  Z2765: poset of words under componentwise order; Euler characteristic of its order complex (chains) and mu(0,1).
import sys, itertools
import numpy as np
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L

def rank_f2(M):
    M = M.copy() % 2; r = 0; rows, cols = M.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c]: piv = i; break
        if piv is None: continue
        M[[r, piv]] = M[[piv, r]]
        for i in range(rows):
            if i != r and M[i, c]: M[i] ^= M[r]
        r += 1
        if r == rows: break
    return r

def faces_of_flag(adj, n):
    faces = [[]]  # all cliques (incl. empty)
    def ext(cl, cand):
        for idx, v in enumerate(cand):
            nc = cl + [v]
            faces.append(nc)
            ext(nc, [w for w in cand[idx+1:] if w in adj[v]])
    ext([], list(range(n)))
    return faces

def betti_f2(faces):
    # reduced Betti numbers over F2 of complex given by all faces (including empty face)
    bydim = {}
    for f in faces:
        bydim.setdefault(len(f)-1, []).append(tuple(sorted(f)))
    maxd = max(bydim)
    idx = {d: {f: i for i, f in enumerate(bydim[d])} for d in bydim}
    ranks = {}
    for d in range(0, maxd+1):
        if d not in bydim or (d-1) not in bydim: ranks[d] = 0; continue
        M = np.zeros((len(bydim[d-1]), len(bydim[d])), dtype=np.uint8)
        for j, f in enumerate(bydim[d]):
            for k in range(len(f)):
                g = f[:k] + f[k+1:]
                M[idx[d-1][g], j] = 1
        ranks[d] = rank_f2(M.T)  # rank of boundary d -> d-1
    betti = {}
    for d in range(-1, maxd+1):
        nd = len(bydim.get(d, []))
        betti[d] = nd - ranks.get(d, 0) - ranks.get(d+1, 0)
    return betti

out = []
for p in L.primes_upto(int(sys.argv[1]) if len(sys.argv) > 1 else 300):
    if p < 17 or p % 8 != 1: continue
    W = L.words(p)
    n = len(W)
    if n == 0: continue
    adj = {i: set() for i in range(n)}
    for i, j in itertools.combinations(range(n), 2):
        if set(W[i]) & set(W[j]): adj[i].add(j); adj[j].add(i)
    faces = faces_of_flag(adj, n)
    b = betti_f2(faces)
    tot = sum(v for k, v in b.items() if k >= 0)
    # sigma: (t,u,v)->(t,v,u); invariant faces
    sig = [W.index((t, v, u)) if (t, v, u) in W else None for (t, u, v) in W]
    fixed_words = sum(1 for i, (t, u, v) in enumerate(W) if u == v)
    inv = [f for f in faces if len(f) > 0 and all(sig[x] is not None and sig[x] in f for x in f)]
    # fixed subcomplex = realization of sigma-invariant faces; use order complex of invariant faces (barycentric)
    invset = set(tuple(sorted(f)) for f in inv)
    # order complex of poset of invariant nonempty faces under inclusion
    pf = sorted(invset, key=len)
    chains = [[()]]  # empty chain placeholder for empty complex handling
    cnt = {}
    def ch(prefix, start):
        pass
    # Euler-char / Betti of the order complex of invariant faces (inclusion poset)
    poset = pf
    # build chains of poset
    chain_list = [[(f,)] for f in poset]
    allchains = [[(f,)] for f in poset]
    frontier = [[(f,)] for f in poset]
    while frontier:
        nxt = []
        for c in frontier:
            last = c[-1]
            for g in poset:
                if len(g) > len(last) and set(last) < set(g):
                    nxt.append(c + [g])
        allchains += nxt; frontier = nxt
    # dimension-wise counts of the order complex
    dimcount = {}
    for c in allchains:
        dimcount[len(c)-1] = dimcount.get(len(c)-1, 0) + 1
    chi_fixed = sum((-1)**d * c for d, c in dimcount.items())
    out.append((p, n, tot, b, fixed_words, len(invset), chi_fixed))
    print(f"p={p} |W|={n} sum_betti(F2,X)={tot} betti={ {k:v for k,v in b.items() if v} } fixed_words={fixed_words} inv_faces={len(invset)} chi(Fix)={chi_fixed}")
