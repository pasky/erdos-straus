"""R284 from-scratch check of the ABH transfer (BOARD2_SLATE (1), ZAREMBA_TRANSFER attribution note).

For primes p and all quadratic non-residues A mod p:
 * HJ (ceiling) length r(p/A) vs 1 + sum of even-index regular CF digits of A/p (ABH convention a_r > 1);
 * Barkan-Hickerson: S_alt(A/p) + 12 D(A/p) bounded (D = classical Dedekind sum s(A, p));
 * lambda(p) = min_QNR r(p/A) and median vs (6/pi^2) L log L.
No code shared with the author's z42_abh_check.py.
"""
import math, sys
import numpy as np

def cf(a, n):  # regular CF of a/n, a<n, canonical (last digit > 1)
    out = []
    while a:
        out.append(n // a)
        n, a = a, n % a
    return out  # a/n = [0; out...]; Euclid automatically gives last digit >= 2 unless a/n=1/1

def hj_len(n, a):  # n/a = b1 - 1/(b2 - ...), b_i >= 2
    r = 0
    while a:
        b = -(-n // a)
        r += 1
        n, a = a, b * a - n
    return r

def dedekind_x4n2(a, n):  # 4 n^2 * s(a,n), exact integer
    b = np.arange(1, n, dtype=np.int64)
    return int(np.sum((2 * b - n) * (2 * ((a * b) % n) - n)))

def isprime(n):
    return n > 1 and all(n % d for d in range(2, int(n**.5) + 1))

def run(p, dedekind=True):
    qnr = [A for A in range(1, p) if pow(A, (p - 1) // 2, p) == p - 1]
    deltas, alts, rs = set(), [], []
    for A in qnr:
        c = cf(A, p)
        assert c[-1] > 1
        even = sum(c[j] for j in range(1, len(c), 2))  # c_2, c_4, ... (1-based even)
        r = hj_len(p, A)
        rs.append(r)
        deltas.add(1 + even - r)
        if dedekind:
            salt = sum((-1) ** (i + 1) * c[i] for i in range(len(c)))  # sum (-1)^i a_i, i 1-based
            s4 = dedekind_x4n2(A, p)
            alts.append(abs(salt + 12 * s4 / (4 * p * p)))
    L = math.log(p)
    print(f"p={p}: #QNR={len(qnr)} delta(1+even-r) in {sorted(deltas)}; lambda={min(rs)} median r={np.median(rs)} "
          f"(6/pi^2)LlogL={6/math.pi**2*L*math.log(L):.2f}" + (f"; max|S_alt+12D|={max(alts):.3f}" if dedekind else ""))
    return min(rs)

if __name__ == "__main__":
    for p in [1009, 1013, 10007, 10009]:
        run(p)
    for p in [100003, 100049, 1000003]:
        run(p, dedekind=False)
