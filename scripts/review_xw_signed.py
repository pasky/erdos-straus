"""R32: from-scratch check of POINTWISE_XWIN Lemma 2.1 (random signed products).
rho_k = P(-1 not in {prod c_i^{e_i}: e in {-1,0,1}^k}) for c uniform in ((Z/a)^x)^k.
Exact via multisets (multinomial weights) for small cases; Monte Carlo otherwise.
Compares with 3n 3^-k + (9/4) t (5/9)^k and with the lower bound 2^-k (prime a)."""
import random, sys
from math import gcd, factorial
from itertools import combinations_with_replacement
from collections import Counter

def group(a):
    return [g for g in range(1, a) if gcd(g, a) == 1]

def bad(cs, a):
    reach = {1}
    for c in cs:
        ci = pow(c, -1, a)
        reach = reach | {r * c % a for r in reach} | {r * ci % a for r in reach}
    return (a - 1) not in reach

def omega(n):
    return len({p for p in range(2, n + 1) if n % p == 0 and all(p % q for q in range(2, p))})

def exact(a, k):
    G = group(a); n = len(G)
    tot = 0
    for ms in combinations_with_replacement(G, k):
        if bad(ms, a):
            w = factorial(k)
            for m in Counter(ms).values():
                w //= factorial(m)
            tot += w
    return tot / n ** k

def mc(a, k, trials, rng):
    G = group(a)
    return sum(bad([rng.choice(G) for _ in range(k)], a) for _ in range(trials)) / trials

if __name__ == "__main__":
    rng = random.Random(7)
    worst = 0
    for a in (3, 7, 11, 15, 19, 23, 35, 39, 55, 63, 91, 105):
        n = len(group(a)); t = 2 ** omega(a)
        for k in range(0, 13):
            if k <= 8 and (n <= 12 or k <= 5):
                r, how = exact(a, k), "exact"
            else:
                r, how = mc(a, k, 20000, rng), "mc"
            bound = 3 * n * 3.0 ** -k + 2.25 * t * (5 / 9) ** k
            prime = all(a % q for q in range(2, a))
            lb = 2.0 ** -k if prime else 0
            flag = "" if r <= bound + (0.01 if how == "mc" else 1e-12) and (how == "mc" or r >= lb - 1e-12) else "  <-- VIOLATION"
            worst = max(worst, r / bound)
            if k in (0, 2, 4, 6, 8, 10, 12) or flag:
                print(f"a={a:4d} n={n:3d} t={t} k={k:2d} rho={r:.5f} ({how}) bound={bound:.4g} 2^-k={lb:.4g}{flag}")
    print("max rho/bound =", worst)
