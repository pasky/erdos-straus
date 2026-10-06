"""Produce a covering certificate for Sigma_r mod L (task O80).

usage: mordell_cert.py r variant Mmax L out.json
Enumerates the residues of Sigma_r (variant main/np) mod L (L must be a multiple of the base
modulus), finds for each one a class (all seven ET families, modulus M | L, M <= Mmax),
reduces to a small set of classes by greedy set cover, and writes
{r, variant, L, classes: [[fam, params], ...], exceptions: [residues mod L left uncovered]}.
The certificate is checked independently by mordell_check.py.
"""
import sys, json
import numpy as np
from mordell_cover import base
from mordell_lib import residue_table, divisors

def main():
    r = int(sys.argv[1]); variant = sys.argv[2]; Mmax = int(sys.argv[3])
    L = int(sys.argv[4]); out = sys.argv[5]
    L0, X0 = base(r, variant)
    assert L % L0 == 0
    X = (X0[:, None] + L0 * np.arange(L // L0, dtype=np.int64)[None, :]).ravel()
    X = X[np.gcd(X, L) == 1]
    X = np.sort(X)
    n = len(X)
    # candidate classes: for each modulus M | L, M <= Mmax, each class -> set of indices
    cover = {}
    for M in divisors(L):
        if M < 3 or M > Mmax:
            continue
        w = residue_table(M)
        if not w:
            continue
        # group residues by witness class
        bycls = {}
        for res, cl in w.items():
            bycls.setdefault(cl, []).append(res)
        y = X % M
        for cl, rs in bycls.items():
            idx = np.nonzero(np.isin(y, rs))[0]
            if len(idx):
                key = (cl[0], tuple(cl[1]))
                cover[key] = set(idx.tolist())
    uncovered = set(range(n))
    chosen = []
    while True:
        best, bs = None, 0
        for key, s in cover.items():
            k = len(s & uncovered)
            if k > bs:
                best, bs = key, k
        if best is None:
            break
        chosen.append(best)
        uncovered -= cover.pop(best)
    exc = sorted(int(X[i]) for i in uncovered)
    print(f"L={L} |Sigma mod L|={n} classes={len(chosen)} exceptions={len(exc)}")
    json.dump({'r': r, 'variant': variant, 'L': L,
               'classes': [[f, list(P)] for f, P in chosen], 'exceptions': exc},
              open(out, 'w'))

if __name__ == '__main__':
    main()
