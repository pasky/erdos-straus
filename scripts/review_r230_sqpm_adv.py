"""R230 from scratch: adversarial n = 1 (mod 8*prod_{3<=q<=Q} q): count tickets (u, l), |u| <= U (Lemma 3.1 criterion,
Jacobi computed directly on the word).  Usage: Q samples U seed"""
import sys, random, math
from sympy import primerange, factorint, jacobi_symbol
Q, S, U, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
P = 8
for q in primerange(3, Q + 1): P *= q
res = []
for _ in range(S):
    n = 1 + P*rng.randrange(1, 10**5)
    if math.isqrt(n)**2 == n: continue
    T = 0; least = None
    for a in range(1, U + 1):
        for u in (a, -a):
            for l in factorint(abs(n + u)):
                if l == 2 or n % l == 0: continue
                for A in (l, -l):
                    if (A + 1) % u == 0 and jacobi_symbol((-A) % n, n) == -1:
                        t = (A + 1)//u; v = (n + u)//A; assert t*u*v - u - v == n
                        T += 1; least = least or a
    res.append((T, least, n))
print(f"Q={Q}: min tickets {min(r[0] for r in res)}, max least |u| {max(r[1] or 10**9 for r in res)}, n up to {max(r[2] for r in res):.3g}")
