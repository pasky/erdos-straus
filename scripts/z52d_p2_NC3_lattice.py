# Z2798: relation lattice Lambda_q(S) = {x in Z^k : prod_i s_i^{x_i} = 1 (mod q)}, S = first k primes (not dividing q),
# q prime.  Discrete logs ell_i mod (q-1) w.r.t. a primitive root; Lambda = {x : sum x_i ell_i = 0 mod (q-1)}.
# Basis via integer kernel of [ell | q-1]; lambda_1 exact via PARI qfminim on the Gram matrix; GH = sqrt(k/(2 pi e)) det^{1/k}.
import sys, math
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
def primroot(q):
    fac = set(); n = q-1; f = 2
    while f*f <= n:
        while n % f == 0: fac.add(f); n //= f
        f += 1
    if n > 1: fac.add(n)
    for g in range(2, q):
        if all(pow(g, (q-1)//f, q) != 1 for f in fac): return g
def dlog(q, g):
    t = {}; x = 1
    for e in range(q-1): t[x] = e; x = x*g % q
    return t
Q = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
PR = L.primes_upto(400)
from collections import defaultdict
res = defaultdict(list)
for q in L.primes_upto(Q):
    if q < 50: continue
    g = primroot(q); D = dlog(q, g)
    for k in (3, 5, 8):
        S = [pr for pr in PR if pr % q != 0][:k]
        ells = [D[s % q] for s in S]
        A = pari.matrix(1, k+1, ells + [q-1])
        K = pari.matkerint(A)            # (k+1) x r integer kernel basis
        # projection to first k coords gives a basis (generating set) of Lambda; LLL-reduce then Gram
        Bx = pari.matrix(k, K.ncols(), [int(K[i, j]) for i in range(k) for j in range(K.ncols())])
        # Gram of generating set, then reduce via qflll on the basis matrix
        U = pari.qflll(Bx)                  # qflll returns the unimodular transformation; reduced basis = Bx * U
        Bred = Bx * U
        G = Bred.mattranspose() * Bred
        if int(G.matdet()) == 0:
            continue
        det = math.sqrt(float(G.matdet()))  # covolume of the lattice in R^k
        diag = [int(G[i, i]) for i in range(k)]
        Bd = min(diag)
        mins = pari.qfminim(G, Bd)            # [count, vectors (columns), maxnorm]; vectors with norm <= Bd
        V = mins[1]
        Gn = [[int(G[i, j]) for j in range(k)] for i in range(k)]
        def nrm(c): return sum(c[i]*Gn[i][j]*c[j] for i in range(k) for j in range(k))
        cols = [] if str(V.type()) != 't_MAT' else [[int(V[i, j]) for i in range(k)] for j in range(V.ncols())]
        lam2 = min([nrm(c) for c in cols if any(c)] + [Bd])
        lam = math.sqrt(lam2)
        GH = math.sqrt(k/(2*math.pi*math.e)) * det**(1.0/k)
        res[k].append((q, lam, GH, lam/GH))
for k in (3, 5, 8):
    r = [x[3] for x in res[k]]
    if not r: continue
    r.sort()
    print(f"k={k}: q in [50,{Q}], {len(r)} primes; lambda1/GH: min {r[0]:.3f}, median {r[len(r)//2]:.3f}, max {r[-1]:.3f}; fraction with lambda1 < GH: {sum(1 for x in r if x<1)/len(r):.3f}")
