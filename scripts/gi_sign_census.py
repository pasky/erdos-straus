"""O170 §4 census: for n = 1 mod 4, count nontrivial sign-blind pairs (m'' != 1, t <= n+2) by class."""
import sys
from sympy import divisors, isprime
def census(n):
    plus = minus = 0
    for t in range(3, n + 3, 4):
        N = t * n + 1
        for m in divisors(N):
            if m % 4: continue
            mpp = N // m
            if mpp == 1: continue
            if (mpp - 1) % t == 0: plus += 1
            elif (mpp + 1) % t == 0: minus += 1
    return plus, minus
if __name__ == "__main__":
  ps = [p for p in range(10001, 12000, 24) if isprime(p)][:8]
  for p in ps: print("prime", p, census(p))
  for k in (99, 101, 105, 107): print("square", k*k, census(k*k))
