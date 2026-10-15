"""z1: word-level check of FOUR_ADIC_INPUT Lemma 1.1 / Thm 1.3 on all words of all odd n < N (sympy Jacobi)."""
import sys
from sympy import jacobi_symbol
from cf_lib import words_fast
N = int(sys.argv[1]); nw = bad = 0
for n in range(3, N, 2):
    for (t, u, v) in words_fast(n):
        P = (t, u, v, t*u-1, t*v-1); nw += 1
        ev = sum(x % 2 == 0 for x in P); c4 = sum(x % 4 == 0 for x in P)
        chi = jacobi_symbol(-(t*u-1) % n, n) if n > 1 else 1
        if ev != 2 or c4 > 2 or ((c4 > 0) != (chi == -1)): bad += 1; print('BAD', n, (t, u, v), ev, c4, chi)
print('odd n <', N, 'words', nw, 'violations', bad)
