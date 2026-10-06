"""R53 from-scratch check of SPW2 Lemma 2.3: f supported on an interval of
ell integer points with zero class sums mod every d <= D  =>  f = 0 iff
ell <= Phi(D).  Computes exact rank over Q (fraction-free elimination mod a
large prime AND over Fractions for small cases)."""
import math, sys
from fractions import Fraction as Fr

def phi_sum(D):
    return sum(sum(1 for a in range(1, d+1) if math.gcd(a, d) == 1) for d in range(1, D+1))

def rank_Q(rows, ncols):
    M = [[Fr(v) for v in r] for r in rows]
    rk = 0
    for c in range(ncols):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c] / M[rk][c]
                M[i] = [a - f*b for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk

def constraint_rows(D, ell, start=0):
    rows = []
    for d in range(1, D+1):
        for b in range(d):
            rows.append([1 if (start + x) % d == b else 0 for x in range(ell)])
    return rows

if __name__ == "__main__":
    for D in range(1, 9):
        P = phi_sum(D)
        for ell in range(1, P + 4):
            for start in (0, 5):
                rk = rank_Q(constraint_rows(D, ell, start), ell)
                kernel = ell - rk
                assert kernel == max(0, ell - P), (D, ell, start, rk, P)
        print(f"D={D}: Phi(D)={P}; kernel dim = max(0, ell-Phi(D)) for ell<=Phi+3  OK")
    # when does Phi(D) >= (2C-1)N+2 (= #points of [N-CN, CN+1]) at C=2, N in {2D, 2D+1}?
    for N in range(2, 80):
        D = N//2
        if phi_sum(D) >= 3*N + 2:
            print("first N with Phi(D) >= 3N+2 (C=2):", N, "Phi(D)=", phi_sum(D)); break
    for N in range(2, 80):
        if all(phi_sum(M//2) >= 3*M + 2 for M in range(N, 200)):
            print("Phi(D) >= 3N+2 for all N in [", N, ",200)"); break
    for D in range(2, 30):
        if phi_sum(D) > 3*(2*D+1): print("Phi(D) > 3N (both parities) from D =", D); break
