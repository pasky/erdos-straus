"""O202: fibrewise integral Hasse principle in the lambda-direction.
For n and its three smallest admissible primes D, and windows lam in [L0, L0+W): count locally-ok lam
(mk_genus.local_ok) and globally solvable lam (mk_fixedD.solve); assert global => local.
Usage: mk_fibreHP.py W L0[,L0,...] n [n ...]"""
import sys
from mk_fixedD import solve
from mk_genus import local_ok


def adm_primes(n, cnt=3):
    out, l = [], 3
    while len(out) < cnt:
        if all(l % q for q in range(2, int(l ** .5) + 1)) and l % 4 == 3 and n % l and \
                pow((-n) % l, (l - 1) // 2, l) == 1:
            out.append(l)
        l += 1
    return out


W = int(sys.argv[1])
L0s = [int(x) for x in sys.argv[2].split(',')]
for n in map(int, sys.argv[3:]):
    row = []
    for D in adm_primes(n):
        cells = []
        for L0 in L0s:
            loc = hit = 0
            for lam in range(L0, L0 + W):
                r = solve(n, D, lam)
                if r == "skip":
                    continue
                lo = local_ok(n, D, lam)
                assert lo or r is None
                loc += lo
                hit += r is not None
            cells.append(f"{hit}/{loc}")
        row.append(f"D={D}: " + " ".join(cells))
    print(f"n={n}: " + " | ".join(row), flush=True)
