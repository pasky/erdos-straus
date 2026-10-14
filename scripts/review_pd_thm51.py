#!/usr/bin/env python3
"""R209: arithmetic sanity check of PHASE_DIAGRAM Thm 5.1's final bound (in logarithms).

For fixed n, A and huge x: S = first k odd primes not dividing n with P = prod S <= (log x)^A maximal;
B = floor(x^{1/(k+1)} / (3 log^{(A+5)/(k+1)} x));  L = k * x / B^{k-1};  claimed: 2L = x^{(2+o(1)) log3 x/(A log2 x)}.
We print log(2L)/log x next to 2/(k+1) and 2 log3 x/(A log2 x), for log x up to 10^300 (exact-ish via logs).
Also checks the two inequalities used: (3B)^{k+1} log P <= x log P/log^{A+5} x and 2L <= 2k 6^k log^{A+5}x x^{2/(k+1)}.
"""
from math import log, log1p
from sympy import primerange

n = 17
odd_primes = [p for p in primerange(3, 10 ** 5) if n % p]
for A in (1, 3, 10):
    for lx10 in (3, 10, 30, 100, 300):  # log x = 10^lx10
        lx = 10.0 ** lx10              # natural log of x
        llx = log(lx)
        logP, k = 0.0, 0
        while logP + log(odd_primes[k]) <= A * llx:
            logP += log(odd_primes[k]); k += 1
        # log B (floor negligible since B is astronomically large)
        logB = lx / (k + 1) - log(3) - (A + 5) * llx / (k + 1)
        assert logB > 10
        log_count3 = (k + 1) * (log(3) + logB) + log(logP)          # log of (3B)^{k+1} log P
        assert log_count3 <= lx + log(logP) - (A + 5) * llx + 1e-6 * lx
        log2L = log(2 * k) + lx - (k - 1) * logB
        rhs = log(2 * k) + k * log(6) + (A + 5) * llx + 2 * lx / (k + 1)
        assert log2L <= rhs + 1e-9 * lx
        print(f"A={A} log x=1e{lx10}: k={k}  log(2L)/log x={log2L/lx:.3e}  2/(k+1)={2/(k+1):.3e}"
              f"  2log3/(A log2)={2*log(llx)/(A*llx):.3e}")
