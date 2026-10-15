# z2_classify.py (O225): sign-clean t-levels and u-levels on the family n = m^2 + k.
# Predicted (odd-prime group criterion, NEAR_SQUARE_EXIST Thm 2.1/2.3): level M (side t or u) is "dirty-capable"
# iff some odd class c (mod L) has c = -1 (mod M), psi1(c) = +1 (splitting in the family) and psi2(c) = -1 (chi).
#   t-side: N = t n + 1 = t m^2 + c0, c0 = t k + 1; psi1 = (-t c0 / c), psi2 = (-t / c)
#   u-side: N = n + u = m^2 + K,     K = k + u;      psi1 = (-K / c),    psi2 = (-u / c)
# Empirical: for every m <= MMAX with n = m^2 + k = 1 (mod 4) (all n, Jacobi sign via DK Thm 4.5), list the divisors
# A = -1 (mod M) of N and record whether some word has chi = -1. Reports disagreements and gcd-exceptional m.
import sys
from math import gcd
from sympy import jacobi_symbol, factorint, divisors

def kron_odd(a, c):            # Kronecker (a/c) for odd c > 0  (= Jacobi)
    return jacobi_symbol(a % c, c) if c > 1 else 1

def predicted_dirty(side, k, M):
    if side == 't':
        c0 = M * k + 1; a1, a2 = -M * c0, -M
    else:
        K = k + M; a1, a2 = -K, -M
    if a1 == 0: return None
    L = 8 * M * abs(a1)
    for c in range(1, L, 2):
        if (c + 1) % M or gcd(c, L) != 1: continue
        if kron_odd(a1, c) == 1 and kron_odd(a2, c) == -1: return c
    return 0

def chi_table(t, u, v):
    A, As = t * u - 1, t * v - 1
    return -1 if (t % 4 == 0 or u % 4 == 0 or v % 4 == 0 or A % 4 == 0 or As % 4 == 0) else 1

def empirical(side, k, M, MMAX):
    neg = []; nm = 0
    for m in range(1, MMAX + 1):
        n = m * m + k
        if n % 4 != 1: continue
        g = gcd(m, M * k + 1) if side == 't' else gcd(m, k + M)
        if EXCL and g > 1: continue
        nm += 1
        if side == 't':
            t = M; N = t * n + 1
            for A in divisors(N):
                if (A + 1) % t: continue
                u = (A + 1) // t; As = N // A; v = (As + 1) // t
                if chi_table(t, u, v) == -1: neg.append(m); break
        else:
            u = M; N = n + u
            for A in divisors(N):
                if (A + 1) % u: continue
                t = (A + 1) // u; v = N // A
                if chi_table(t, u, v) == -1: neg.append(m); break
    return nm, neg

EXCL = False
if __name__ == '__main__':
    EXCL = len(sys.argv) > 5
    side, ks, MAXL, MMAX = sys.argv[1], [int(x) for x in sys.argv[2].split(',')], int(sys.argv[3]), int(sys.argv[4])
    for k in ks:
        clean_pred, clean_emp, bad = [], [], []
        for M in range(1, MAXL + 1):
            pd = predicted_dirty(side, k, M)
            nm, neg = empirical(side, k, M, MMAX)
            if nm == 0: continue
            if pd == 0: clean_pred.append(M)
            if not neg: clean_emp.append(M)
            if pd == 0 and neg: bad.append((M, 'pred clean, chi=-1 at m=', neg[:6], len(neg)))
            if pd and not neg: bad.append((M, 'pred dirty (class %d) but none seen' % pd))
        print(f'side {side} k={k}: predicted clean {clean_pred}')
        print(f'   empirically clean (m<={MMAX}) {clean_emp}')
        for b in bad: print('   DISAGREE', b)
