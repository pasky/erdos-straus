"""R272: from-scratch check of Thm 3.4 (forced criterion fails at p == 1 mod M), all four lines.
Forced set (Prop 3.2): s = B-smooth part of N, L = N/s (opaque, treated as one prime).
unsigned lines (b=1: N=p+4d, t=4d; c-line: N=cp+1, t=4c, odd divisors only):
  forced iff exists w in {u, u*L} (u | s, w odd for c-line) with w == -1 mod t.
signed e-slices (N=(p+e)/4 or (pe+1)/4, e==3 mod 4): forced iff exist a,b with ab | s*L-pattern,
  L in at most one of a,b, and a+b == 0 mod e (classes mod e)."""
import sys, random
from math import gcd, prod
from sympy import isprime, primerange, divisors
def run(D, B, nprimes, seed=1):
    E = {}
    for q in primerange(2, B+1):
        e = 1
        while q**e <= 16*D*(D+1): e += 1
        E[q] = e
    M = 4
    for k in range(2, D+1): M = M*k//gcd(M, k)
    M = M*prod(q**e for q, e in E.items())//gcd(M, prod(q**e for q, e in E.items()))
    # make M the lcm properly
    from sympy import lcm
    M = lcm(4*__import__('math').factorial(D), prod(q**e for q, e in E.items()))
    found, k, fires = 0, 1, 0
    rnd = random.Random(seed)
    while found < nprimes:
        k += rnd.randint(1, 50)
        p = 1 + M*k
        if not isprime(p): continue
        found += 1
        lines = [(p+4*d, 4*d, 'u', False) for d in range(1, D+1)]
        lines += [(c*p+1, 4*c, 'u', True) for c in range(1, D+1)]
        lines += [((p+e)//4, e, 's', False) for e in range(3, D+1, 4)]
        lines += [((p*e+1)//4, e, 's', False) for e in range(3, D+1, 4)]
        for N, t, kind, oddonly in lines:
            s = 1; n = N
            for q in primerange(2, B+1):
                while n % q == 0: n//= q; s *= q
            L = n
            if kind == 'u':
                for u in divisors(s):
                    for w in (u, u*L):
                        if oddonly and w % 2 == 0: continue
                        if gcd(w, t) == 1 and w % t == t-1: fires += 1; print("FIRE", p, N, t, w)
            else:
                for a0 in divisors(s):
                    for b0 in divisors(s//a0):
                        for a, b in ((a0, b0), (a0*L, b0), (a0, b0*L)):
                            if (a+b) % t == 0:
                                fires += 1; print("FIRE", p, N, t, a, b)
    print(f"D={D} B={B} M~10^{len(str(M))-1}: {found} primes p==1 (M), forced firings: {fires}")
for D, B in [(6, 26), (12, 50), (12, 5), (20, 82)]:
    run(D, B, 8)
