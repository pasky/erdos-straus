"""z53_hyp2cycle_cells3mod4.py — the n = 3 (mod 4) companion of DEDEKIND_ES Thm 4.5, by the same 512-cell argument.
For a length-3 word (v,t,u) (n = tuv - u - v, A = tu - 1, A* = tv - 1), DEDEKIND_ES Cor 4.1 gives
2(A/n) = n + 1 - n*((v-3)+(t-3)+(u-3)) - A - A*  (mod 8), a function of (t,u,v) mod 8.
Claim checked: for n = 3 (4), (A/n) = +1  <=>  4 | tu-1 or 4 | tv-1 or 4 | t or 4 | u or 4 | v.
Also brute-force check of the Jacobi symbols on all words with n <= N (argv[1]) and n = 3 (4)."""
import sys
from sympy import jacobi_symbol
def five(t, u, v): return (t*u-1) % 4 == 0 or (t*v-1) % 4 == 0 or t % 4 == 0 or u % 4 == 0 or v % 4 == 0
bad = cells = 0
for t in range(8):
    for u in range(8):
        for v in range(8):
            n = (t*u*v - u - v) % 8
            if n % 4 != 3: continue
            A, As = (t*u-1) % 8, (t*v-1) % 8
            s2 = (n + 1 - n*((v-3)+(t-3)+(u-3)) - A - As) % 8
            sign = 1 if s2 == 2 else (-1 if s2 == 6 else None)
            cells += 1
            if sign is None or (sign == 1) != five(t, u, v): bad += 1
print("cells n=3(4):", cells, "mismatches:", bad)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
words = mism = 0
for t in range(2, N):
    for u in range(2, N):
        if t*u*2 - u - 2 > N: break
        for v in range(2, N):
            n = t*u*v - u - v
            if n > N: break
            if n % 4 != 3 or n < 3: continue
            j = jacobi_symbol((t*u-1) % n, n)
            if j == 0: continue
            words += 1
            if (j == 1) != five(t, u, v): mism += 1
print("words n=3(4), n<=%d, unit A:" % N, words, "mismatches:", mism)
