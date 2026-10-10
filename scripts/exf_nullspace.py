"""O131 step 2: exact linear-relation search (mod P = 2^31-1, then exact verification) between ES-variant columns
and classical columns over various row sets.  dim(span E ∩ span C) = rk C + rk E - rk(C ∪ E)."""
import numpy as np, sys
from sympy import isprime
P = 2147483647
Z = np.load('data/exf/columns_2e4.npz'); keys = list(Z.keys())
E = [k for k in keys if k.startswith('ES:')]; C = [k for k in keys if k.startswith('C:')]
N = len(Z[keys[0]]) - 1
def rank_mod(A):
    A = np.array(A, dtype=object) % P; A = np.array(A, dtype=np.int64)
    r = 0; rows, cols = A.shape; piv = []
    for j in range(cols):
        nz = np.nonzero(A[r:, j])[0]
        if len(nz) == 0: continue
        i = r + nz[0]; A[[r, i]] = A[[i, r]]
        inv = pow(int(A[r, j]), P - 2, P); A[r] = (A[r] * inv) % P
        f = A[:, j].copy(); f[r] = 0
        A = (A - (f[:, None] * A[r][None, :]) % P) % P
        piv.append(j); r += 1
        if r == rows: break
    return r, piv
def analyse(name, rows, rng=np.random.default_rng(1)):
    rows = np.array(rows)
    if len(rows) > 500: rows = np.sort(rng.choice(rows, 500, replace=False))
    MC = np.stack([Z[k][rows] for k in C], 1); ME = np.stack([Z[k][rows] for k in E], 1)
    rC, pC = rank_mod(MC); rE, _ = rank_mod(ME); rCE, _ = rank_mod(np.concatenate([MC, ME], 1))
    print(f'[{name}] rows={len(rows)} rkC={rC}/{len(C)} rkE={rE}/{len(E)} rk(C∪E)={rCE}  dim(E∩C)={rC + rE - rCE}')
    base = np.concatenate([MC[:, pC]], 1)
    hits = [k for k in E if rank_mod(np.concatenate([base, Z[k][rows][:, None]], 1))[0] == rC]
    if hits: print('   ES columns inside span(C):', hits)
    return rC, rE, rCE
allrows = np.arange(2, N + 1)
primes = np.array([p for p in range(5, N + 1) if isprime(p)])
analyse('all n>=2', allrows)
analyse('odd n', allrows[allrows % 2 == 1])
analyse('primes>=5', primes)
analyse('primes 1 mod 4', primes[primes % 4 == 1])
analyse('primes 3 mod 4', primes[primes % 4 == 3])
analyse('primes 1 mod 24', primes[primes % 24 == 1])
# pure-ES relations on primes: identify zero columns and duplicate columns, then the residual rank deficiency
rows = primes
ME = np.stack([Z[k][rows] for k in E], 1)
zero = [E[j] for j in range(len(E)) if not ME[:, j].any()]
print('ES columns identically 0 on primes:', zero)
dup = [(E[i], E[j]) for i in range(len(E)) for j in range(i) if ME[:, i].any() and np.array_equal(ME[:, i], ME[:, j])]
print('ES duplicate pairs on primes:', dup)
keep = [j for j in range(len(E)) if ME[:, j].any() and not any(E[j] == a for a, _ in dup)]
r, _ = rank_mod(ME[np.sort(np.random.default_rng(2).choice(len(rows), 500, replace=False))][:, keep])
print('rank after removing zero/duplicate columns:', r, '/', len(keep))
