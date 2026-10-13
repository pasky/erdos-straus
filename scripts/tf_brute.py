"""O194 TES_FINITE method B (independent certification, no factorisation, no shared code with tf_exact/tf_core
except nothing: own arithmetic in numpy).  Complete enumeration of TES(n) by Prop 1.1 (a)+(b):
  some i with N(x_i) <= N(c_i) N(n)/9;  then r = 9/n - c_i/x_i = A/B (A = 9x_i - c_i n, B = n x_i), and for one of the
  other two indices j: N(x_j) <= 4 N(c_j) N(B)/N(A);  x_k = c_k B x_j / (A x_j - B c_j) must lie in O.
All lattice points of both disks are enumerated (numpy int64; magnitudes checked).
usage: tf_brute.py a b [a b ...]   (each pair = a 2-primary pi; n = pi)
"""
import sys
import math
import numpy as np

CS = [(0, 1), (-1, -1), (2, 0)]  # w, w^2, 2


def m(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def nrm(x): return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]


def lattice(R, chunk=4_000_000):
    """yield arrays (a, b) of all nonzero a + b w with a^2 - ab + b^2 <= R, in row chunks (memory-bounded)."""
    bm = int(math.sqrt(4 * R / 3)) + 2
    rows = max(1, chunk // (2 * bm + 1))
    a = np.arange(-bm, bm + 1, dtype=np.int64)
    for b0 in range(-bm, bm + 1, rows):
        bb = np.arange(b0, min(b0 + rows, bm + 1), dtype=np.int64)
        A, B = np.meshgrid(a, bb, indexing='ij')
        A, B = A.ravel(), B.ravel()
        N = A * A - A * B + B * B
        keep = (N <= R) & (N > 0)
        yield A[keep], B[keep]


def vmul(a, b, c, d):
    return a * c - b * d, a * d + b * c - b * d


def solve(n):
    Nn = nrm(n)
    sols = set()
    for i in range(3):
        others = [k for k in range(3) if k != i]
        XA, XB = [np.concatenate(t) for t in zip(*lattice(nrm(CS[i]) * Nn / 9))]
        for xa, xb in zip(XA.tolist(), XB.tolist()):
            if xa % 2 != 1 or xb % 2 != 0:
                continue
            xi = (xa, xb)
            Ael = (9 * xa - m(CS[i], n)[0], 9 * xb - m(CS[i], n)[1])
            Bel = m(n, xi)
            NA, NB = nrm(Ael), nrm(Bel)
            assert NA > 0
            for j in others:
                k = [q for q in others if q != j][0]
                R = 4 * nrm(CS[j]) * NB / NA
                for ja, jb in lattice(R + 1e-9):
                    sel = (ja % 2 == 1) & (jb % 2 == 0)
                    ja, jb = ja[sel], jb[sel]
                    # den = A x_j - B c_j ; num = c_k B x_j
                    da, db = vmul(Ael[0], Ael[1], ja, jb)
                    Bc = m(Bel, CS[j])
                    da, db = da - Bc[0], db - Bc[1]
                    cB = m(CS[k], Bel)
                    na, nb = vmul(cB[0], cB[1], ja, jb)
                    # x_k = num/den: num * conj(den) / N(den)
                    Nd = da * da - da * db + db * db
                    ok = Nd != 0
                    ca, cb = da - db, -db  # conj
                    pa, pb = vmul(na, nb, ca, cb)
                    Ndn = np.where(ok, Nd, 1)
                    ok &= (pa % Ndn == 0) & (pb % Ndn == 0)
                    assert np.abs(pa).max(initial=0) < 2**62 and np.abs(pb).max(initial=0) < 2**62
                    for t in np.nonzero(ok)[0].tolist():
                        xk = (int(pa[t] // Nd[t]), int(pb[t] // Nd[t]))
                        if xk == (0, 0) or xk[0] % 2 != 1 or xk[1] % 2 != 0:
                            continue
                        xs = [None] * 3
                        xs[i], xs[j], xs[k] = xi, (int(ja[t]), int(jb[t])), xk
                        # exact verification in python ints
                        x1, x2, x3 = xs
                        lhs = m((9, 0), m(x1, m(x2, x3)))
                        t1, t2, t3 = m(CS[0], m(x2, x3)), m(CS[1], m(x1, x3)), m(CS[2], m(x1, x2))
                        rhs = m(n, (t1[0] + t2[0] + t3[0], t1[1] + t2[1] + t3[1]))
                        assert lhs == rhs, xs
                        sols.add(tuple(xs))
    return sols


if __name__ == '__main__':
    args = list(map(int, sys.argv[1:]))
    for a, b in zip(args[::2], args[1::2]):
        s = solve((a, b))
        print(f"pi = {a}+{b}w, N = {nrm((a, b))}: {len(s)} solutions", sorted(s)[:3])
