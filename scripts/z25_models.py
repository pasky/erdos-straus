"""Numerator-k models k/n = 1/x+1/y+1/z (k != 4) have genuine prime exceptions E_k.
Test the k-analogues of candidate laws (CERTIFIED finite computations):
 (D)  Q(p) = prime factors of (p^2-1)/4 all in S_k  but p in E_k   -> recombination law false for k
 (Duv) u=(p-1)/2, v=(p+1)/2 both in S_k but p in E_k
 (SQ) p in E_k but p^2 in S_k                                       -> square law false for k
"""
import sys
from sympy import primerange, primefactors
from z25_common import has_sol
K = range(int(sys.argv[1]), int(sys.argv[2])); P = int(sys.argv[3])
memo = {}
def S(n, k):
    if (n, k) not in memo: memo[(n, k)] = has_sol(n, k)
    return memo[(n, k)]
for k in K:
    ex = [p for p in primerange(3, P) if not S(p, k)]
    D = [p for p in ex if p > 3 * k and all(S(q, k) for q in primefactors((p * p - 1) // 4) if q > k)]
    Duv = [p for p in ex if p > 3 * k and S((p - 1) // 2, k) and S((p + 1) // 2, k)]
    print(f"k={k} E_k primes<{P}: {len(ex)} max={max(ex) if ex else None}; D-law fails at {D[:8]}; uv-law fails at {Duv[:8]}", flush=True)
