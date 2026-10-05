"""R48d: from-scratch check of POINTWISE_OMEGA13 Lemma 3.1: for every atom (M,D), M=3 (4), D | A^2,
A=(M+1)/4: Jacobi (-4D | M) = -1, and (-4D|l) = (-d|l) for every prime l | M (d = squarefree part of D).
Usage: review_o13d_jacobi.py Mmax"""
import sys
from sympy import jacobi_symbol, factorint, divisors

N = int(sys.argv[1])
cnt = bad = 0
for M in range(3, N + 1, 4):
    A = (M + 1) // 4
    ls = list(factorint(M))
    for D in divisors(A * A):
        cnt += 1
        x = (-4 * D) % M
        if jacobi_symbol(x, M) != -1:
            bad += 1
        fd = factorint(D)
        d = 1
        for p, e in fd.items():
            if e % 2:
                d *= p
        for l in ls:
            if jacobi_symbol((-4 * D) % l, l) != jacobi_symbol((-d) % l, l):
                bad += 1
print(f"atoms M<={N}: {cnt}, failures {bad}")
