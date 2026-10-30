"""Local point counts of the ES surface 4xyz = n(xy+yz+zx) over F_q (affine, and with xyz != 0 i.e. the torus part
relevant to unit fractions), as a function of n mod q; compare the QR/QNR dependence with the fitted per-prime weights."""
import json
from sympy import primerange, legendre_symbol
out = {}
for q in primerange(3, 48):
    rows = {}
    for n in range(1, q):
        aff = 0; tor = 0
        for x in range(q):
            for y in range(q):
                for z in range(q):
                    if (4*x*y*z - n*(x*y + y*z + z*x)) % q == 0:
                        aff += 1
                        if x and y and z: tor += 1
        rows[n] = (aff, tor)
    qr = [rows[n][1] for n in rows if legendre_symbol(n, q) == 1]
    qn = [rows[n][1] for n in rows if legendre_symbol(n, q) == -1]
    out[q] = dict(torus_QR=sorted(set(qr)), torus_QNR=sorted(set(qn)), affine=sorted(set(r[0] for r in rows.values())))
    print(q, out[q], flush=True)
json.dump(out, open('data/z52b/localpts.json', 'w'), indent=1)
