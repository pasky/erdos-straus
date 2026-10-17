"""Numerator-k models k/n = 1/x+1/y+1/z (k != 4) have genuine prime exceptions E_k.
Test the k-analogues of candidate laws (CERTIFIED finite computations):
 (Dtr) TRUNCATED recombination: every prime factor q > k of (p^2-1)/4 is in S_k, but p in E_k
       (refutes only the truncated law; the untruncated law's hypothesis can fail at small q, e.g. 2 in E_k)
 (Duv) u=(p-1)/2, v=(p+1)/2 both in S_k but p in E_k
 (SQ)  p in E_k but p^2 in S_k  (tested for p < SQMAX)
 (ISO) largest exceptional prime below P
"""
import sys
from sympy import primerange, primefactors
from z25_common import has_sol
K = range(int(sys.argv[1]), int(sys.argv[2])); P = int(sys.argv[3])
SQMAX = int(sys.argv[4]) if len(sys.argv) > 4 else 0
memo = {}
def S(n, k):
    if (n, k) not in memo: memo[(n, k)] = has_sol(n, k)
    return memo[(n, k)]
for k in K:
    ex = [p for p in primerange(2, P) if not S(p, k)]
    D = [p for p in ex if p > 3 * k and all(S(q, k) for q in primefactors((p * p - 1) // 4) if q > k)]
    Duv = [p for p in ex if p > 3 * k and S((p - 1) // 2, k) and S((p + 1) // 2, k)]
    sq = [(p, S(p * p, k)) for p in ex if p < SQMAX]
    sqfail = [p for p, s in sq if not s]
    print(f"k={k} E_k primes<{P}: {len(ex)} {ex[:6]}... max={max(ex) if ex else None}; "
          f"truncated-D fails at {D[:6]}; uv fails at {Duv[:6]}; "
          f"SQ tested {len(sq)}, p^2 also exceptional at {sqfail}", flush=True)
