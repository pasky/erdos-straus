"""Z2841: forest-edge constraints chi(u) = chi(v) (edges uv | p+u+v, u<v<=V, incl. u = 1 with chi(1) = 1) as an
F2-linear system on x_q = [chi(q) = -1], q prime <= V.  If ES5 failed at p, chi_p would satisfy all of them.
Measure (a) which primes are forced to chi(q) = 1, (b) the resulting upper bound for the pretentious distance
D(chi,1;X)^2 = sum_{q<=X} (1-chi(q))/q <= 2*sum_{q<=X unforced} 1/q, against the Burgess/Vinogradov lower bound
D(chi_p,1;p^{1/4+eps})^2 >= 1 - o(1) (if sum_{q<=x, chi(q)=-1} 1/q < 1/2 - eps then sum_{n<=x} chi(n) >> eps x).
(c) EVIDENCE: correlation between the true D(chi_p,1;X)^2 and the number of bichromatic edges N_-(p)."""
import sys, math, random
import numpy as np
from sympy import primerange, factorint, divisors, isprime, legendre_symbol

def edges(p, V):
    E = []
    for u in range(1, V + 1):
        for v in divisors(p + u):
            if v <= u or v > V: continue
            if (p + u + v) % (u * v) == 0: E.append((u, v))
    return E

def forced(E, primes):
    idx = {q: i for i, q in enumerate(primes)}
    rows = []
    for u, v in E:
        r = np.zeros(len(primes), dtype=np.uint8)
        for w in (u, v):
            for q, e in factorint(w).items():
                r[idx[q]] ^= (e & 1)
        if r.any(): rows.append(r)
    if not rows: return set(), 0
    M = np.array(rows, dtype=np.uint8)
    # row reduce over F2
    M = M.copy(); piv = []; r = 0
    for c in range(M.shape[1]):
        nz = np.nonzero(M[r:, c])[0]
        if len(nz) == 0: continue
        i = r + nz[0]; M[[r, i]] = M[[i, r]]
        for j in np.nonzero(M[:, c])[0]:
            if j != r: M[j] ^= M[r]
        piv.append(c); r += 1
        if r == M.shape[0]: break
    R = M[:r]
    # e_q in rowspace iff the RREF has a row equal to e_q (unit vector) -- true for reduced echelon form
    F = set()
    for row in R:
        nz = np.nonzero(row)[0]
        if len(nz) == 1: F.add(primes[nz[0]])
    return F, r

def D2(p, X):
    return sum((1 - legendre_symbol(q % p, p)) / q for q in primerange(2, int(X) + 1))

if __name__ == "__main__":
    V = int(sys.argv[1]); nsamp = int(sys.argv[2])
    rng = random.Random(2841)
    primesV = list(primerange(2, V + 1))
    print(f"V = {V}: variables = {len(primesV)} primes; sample {nsamp} primes p ≡ 1 (4) per scale")
    for scale in [10**e for e in map(int, sys.argv[3].split(","))]:
        out = []
        while len(out) < nsamp:
            p = rng.randrange(scale, 2 * scale) | 1
            if p % 4 != 1 or not isprime(p): continue
            E = edges(p, V)
            F, rank = forced(E, primesV)
            X = p ** 0.25
            tot = sum(1 / q for q in primesV if q <= X)
            unf = sum(1 / q for q in primesV if q <= X and q not in F)
            totV = sum(1 / q for q in primesV); unfV = sum(1 / q for q in primesV if q not in F)
            out.append((len(E), rank, len(F), 2 * unf, 2 * unfV, D2(p, X), 2 * tot))
        a = np.array(out)
        print(f" scale {scale:.0e}: mean #edges(u<v<={V}) {a[:,0].mean():.1f}, rank {a[:,1].mean():.1f}, #forced primes {a[:,2].mean():.2f} (max {a[:,2].max():.0f});"
              f" D²-upper-bound at X=p^(1/4): mean {a[:,3].mean():.3f} (min {a[:,3].min():.3f}) of max {a[:,6].mean():.3f};"
              f" at X=V: mean {a[:,4].mean():.3f} (min {a[:,4].min():.3f}); true D²(p^(1/4)) mean {a[:,5].mean():.3f}")
