"""O266: HJ-length ladder at fixed p.  For n (prime or odd square) compute r(n/A) for all A in [1,n), gcd(A,n)=1,
via r(n/A) = 1 + sum_{i odd} a_i of the regular CF n/A = [a0; a1, ...].  Reports
  |S_L(n)| for L = 2..8 and at L = c*log n, QNR fraction inside S_L, lambda(n), median r, and the pigeonhole level
  L_half(n) = least L with |S_L| > (n-1)/2  (Theorem A rung).
Usage: z36_ladder.py N1 N2 ...  (each n analysed fully; vectorised numpy, O(n log n)).
"""
import sys, math
import numpy as np


def hj_lengths(n):
    A = np.arange(1, n, dtype=np.int64)
    x = np.full_like(A, n)
    y = A.copy()
    r = np.ones_like(A)            # 1 + sum of odd-index digits
    tot = np.zeros_like(A)         # sum of all digits a1, a2, ...
    i = 0
    alive = y > 0
    while alive.any():
        q = np.where(alive, x // np.where(y > 0, y, 1), 0)
        if i % 2 == 1:
            r += q
        if i >= 1:
            tot += q
        x, y = np.where(alive, y, x), np.where(alive, x - q * np.where(alive, y, 0), 0)
        alive = y > 0
        i += 1
    return A, r, tot


def jacobi_vec(A, n):
    a = A.copy() % n
    m = np.full_like(a, n)
    res = np.ones_like(a)
    while True:
        nz = a != 0
        if not nz.any():
            break
        # remove factors 2
        while True:
            ev = nz & (a % 2 == 0)
            if not ev.any():
                break
            a = np.where(ev, a // 2, a)
            mm = m % 8
            res = np.where(ev & ((mm == 3) | (mm == 5)), -res, res)
        sw = nz
        a2, m2 = np.where(sw, m, a), np.where(sw, a, m)
        res = np.where(sw & (a2 % 4 == 3) & (m2 % 4 == 3), -res, res)
        a = np.where(sw, a2 % np.where(m2 > 0, m2, 1), a)
        m = np.where(sw, m2, m)
    return np.where(m == 1, res, 0)


def analyse(n):
    A, r, tot = hj_lengths(n)
    g = np.gcd(A, n)
    keep = g == 1
    A, r, tot = A[keep], r[keep], tot[keep]
    chi = jacobi_vec(A, n)
    ln = math.log(n)
    out = {"n": n, "phi": len(A)}
    for L in range(2, 9):
        s = r <= L
        out[f"S{L}"] = int(s.sum())
        out[f"nr{L}"] = int((s & (chi == -1)).sum())
    lam = int(r[chi == -1].min()) if (chi == -1).any() else None
    out["lambda"] = lam
    rs = np.sort(r)
    out["median_r"] = int(rs[len(rs) // 2])
    out["L_half"] = int(rs[(n - 1) // 2]) if len(rs) > (n - 1) // 2 else None  # |S_L|>(n-1)/2 needs L>=this
    out["median_tot"] = int(np.sort(tot)[len(tot) // 2])
    for c in (0.5, 1.0, 1.5, 2.0):
        L = int(c * ln)
        s = r <= L
        k = int(s.sum())
        out[f"c{c}"] = (L, k, round(math.log(max(k, 1)) / ln, 3), round(float((chi[s] == -1).mean()) if k else 0, 3))
    return out


if __name__ == "__main__":
    for a in sys.argv[1:]:
        print(analyse(int(a)), flush=True)
