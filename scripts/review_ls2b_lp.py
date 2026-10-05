"""R27b from-scratch check of LARGESIEVE2 Prop 8.2(a): best level-lambda majorant
of a K=2 band family has mean >= 1 (no saving), when no allowed modulus is
divisible by a full D_i = l_i l'_i.

LP: minimise E_U nu over nu = sum_d f_d(n mod d) (d over allowed maximal moduli),
subject to nu(x) >= 1_A(x) for all x mod Q.  Contrast: add D_1 to the allowed
moduli (level > lambda) and the full modulus Q (exact density).
"""
import math, itertools, random
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix


def in_band_family(n, D, a, eta):
    r = (n * a) % D
    x = r / D
    return min(x, 1 - x) <= 0.5 - eta + 1e-12


def best_majorant(Q, moduli, Aset):
    cols = []
    for d in moduli:
        for b in range(d):
            cols.append((d, b))
    nv = len(cols)
    M = lil_matrix((Q, nv))
    idx = {c: j for j, c in enumerate(cols)}
    for x in range(Q):
        for d in moduli:
            M[x, idx[(d, x % d)]] = 1.0
    # objective: E_U nu = sum_d sum_b f_d(b)/d
    c = np.array([1.0 / d for (d, b) in cols])
    rhs = np.array([1.0 if x in Aset else 0.0 for x in range(Q)])
    res = linprog(c, A_ub=-M.tocsr(), b_ub=-rhs, bounds=[(None, None)] * nv, method="highs")
    assert res.status == 0, res.message
    return res.fun


def main():
    random.seed(2)
    eta = 1 / 8
    for (l1, m1, l2, m2) in [(5, 7, 11, 13), (5, 11, 7, 13), (7, 11, 5, 13)]:
        D1, D2 = l1 * m1, l2 * m2
        Q = D1 * D2
        for trial in range(3):
            a1 = random.choice([a for a in range(1, D1) if math.gcd(a, D1) == 1])
            a2 = random.choice([a for a in range(1, D2) if math.gcd(a, D2) == 1])
            Aset = {x for x in range(Q) if in_band_family(x, D1, a1, eta) and in_band_family(x, D2, a2, eta)}
            dens = len(Aset) / Q
            low = [p * q for p in (l1, m1) for q in (l2, m2)]
            v_low = best_majorant(Q, low, Aset)
            v_hi1 = best_majorant(Q, [D1, l2, m2], Aset)
            print(f"D=({D1},{D2}) a=({a1},{a2}) density={dens:.4f}  "
                  f"LP(level<L_i)={v_low:.6f}  LP(with D1)={v_hi1:.6f}")


if __name__ == "__main__":
    main()
