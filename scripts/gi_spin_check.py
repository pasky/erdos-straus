"""O170 Lemma 1.3 check: for n = 1 mod 4 and every W-certificate tn+1 = m m'' (4|m, m''=-1 mod t),
the Jacobi symbol (m''/n) = -1."""
from sympy import jacobi_symbol, divisors
bad = tot = 0
for n in range(5, 3001, 4):
    for t in range(1, n + 3):
        N = t * n + 1
        for m in divisors(N):
            if m % 4 == 0 and (m + 1) % t == 0:
                mpp = N // m
                if (mpp + 1) % t:
                    continue
                tot += 1
                if jacobi_symbol(mpp, n) != -1:
                    bad += 1
print("certificates", tot, "violations", bad)
