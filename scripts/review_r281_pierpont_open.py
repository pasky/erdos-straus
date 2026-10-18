"""R281 from-scratch spot-check of EXP_15 §1.3 EVIDENCE: open cells (a mod L, b mod L) of 2^a3^b + 1.
For each open cell: (i) Lemma 1.2 descent does not apply (no odd prime p | gcd(a0, b0, L)); (ii) Lemma 1.1 window does not
apply (a0 ≡ 0, b0 ≡ 1 (4) and X ≢ ±1 (11)); (iii) no admissible prime q < QMAX divides n on the cell; (iv) list admissible
primes q (ord_q 2, ord_q 3 | L) with n mod q a quadratic non-residue (author: "every open cell is a QNR mod some q").
Also verifies every divisor-class ('D') cell in the json: q | n on the whole cell."""
import json, sys
from sympy import primerange, n_order, legendre_symbol, factorint

fn = sys.argv[1]
QMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
dat = json.load(open(fn))
L = dat['L']
adm = [q for q in primerange(5, QMAX) if pow(2, L, q) == 1 and pow(3, L, q) == 1]
print("L =", L, "admissible primes <", QMAX, ":", adm[:30], "... total", len(adm))
oddL = [p for p in factorint(L) if p > 2]
bad = 0
nq_hist = []
for a0, b0 in dat['left']:
    # use representatives a, b >= 10 in the class (A0 = 10)
    a, b = a0 + L, b0 + L
    desc = [p for p in oddL if a0 % p == 0 and b0 % p == 0]
    win = False
    if a0 % 4 == 0 and b0 % 4 == 1:
        X = pow(2, (a - 4) // 4, 11) * pow(3, (b - 1) // 4, 11) % 11
        win = X not in (0, 1, 10)
    divs = [q for q in adm if (pow(2, a, q) * pow(3, b, q) + 1) % q == 0]
    qnr = [q for q in adm if legendre_symbol((pow(2, a, q) * pow(3, b, q) + 1) % q, q) == -1]
    if desc or win or divs or not qnr:
        bad += 1
        print("CELL", (a0, b0), "descent", desc, "window", win, "divisors", divs, "qnr", qnr[:5])
    nq_hist.append(qnr[0] if qnr else None)
print("open cells:", len(dat['left']), "anomalies:", bad, "smallest QNR primes:", sorted(set(nq_hist), key=lambda v: (v is None, v or 0)))
for cl in dat.get('classes', []):
    if cl['fam'] == 'D':
        q = cl['params'][0]
        assert L % n_order(2, q) == 0 and L % n_order(3, q) == 0
        for a0, b0 in cl['cells']:
            assert (pow(2, a0 + L, q) * pow(3, b0 + L, q) + 1) % q == 0
        print("divisor class", q, ":", len(cl['cells']), "cells verified")
