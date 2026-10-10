"""R131 from scratch: (i) §3.2 theta identities for cd | 6 (all n <= N), (ii) Prop 4.1 divisor form
(full (c,d) box for n <= NB; on-support for n <= N), (iii) Thm 5.2 divisor form + genus factor for primes."""
import sys
from collections import defaultdict
from itertools import product
from math import gcd, isqrt
from sympy import factorint, divisors, jacobi_symbol, isprime
N, NB, sol = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
S = [defaultdict(int) for _ in range(4)]; D = [defaultdict(int) for _ in range(4)]   # (n,c,d) -> count, diag
for line in open(sol):
    f, n, a, b, c, d = map(int, line.split()); S[f][(n, c, d)] += 1
    if a == b: D[f][(n, c, d)] += 1
def kron(D_, m):   # Kronecker (D_/m), m odd positive
    return jacobi_symbol(D_ % m, m) if m > 1 else 1
def Acls(M, q, r): return sum(1 for X in divisors(M) if X % q == r % q)
def realchars(q):  # all +-1 homomorphisms of (Z/q)^x, by brute force
    U = [u for u in range(1, q) if gcd(u, q) == 1]; out = []
    for vals in product([1, -1], repeat=len(U)):
        ch = dict(zip(U, vals))
        if all(ch[(x*y) % q] == ch[x]*ch[y] for x in U for y in U): out.append(ch)
    return U, out
bad = defaultdict(int); tested = defaultdict(int)
# (i) §3.2
for (c, d) in [(c, d) for c in (1,2,3,6) for d in (1,2,3,6) if 6 % (c*d) == 0]:
    q = 4*c*d; U, chs = realchars(q); assert len(chs) == len(U)   # exponent 2: all chars real
    for n in range(1, N+1):
        M = 4*c*c*d*n + 1; dv = divisors(M)
        A = sum(1 for X in dv if X % q == q-1)
        th = sum(ch[q-1]*sum(ch[X % q] for X in dv) for ch in chs) / len(chs)
        tested['3.2'] += 1
        if A != th or A != 2*S[2][(n,c,d)] - D[2][(n,c,d)]: bad['3.2'] += 1
        if (c, d) == (1, 1):
            r2 = sum(1 for x in range(-isqrt(M), isqrt(M)+1) for y in [isqrt(M - x*x)] if y*y == M - x*x for _ in ((1,) if y == 0 else (1, 1)))
            if 2*A != len(dv) - r2//4: bad['A11'] += 1
# (ii) Prop 4.1: per-slice identities and totals
for n in range(1, N+1):
    keys = {(c, d) for f in (2, 3) for (m, c, d) in S[f] if m == n} if n > NB else {(c, d) for c in range(1, n+2) for d in range(1, n//2+2)}
    tot_odd = tot_even = 0
    for (c, d) in keys:
        q = 4*c*d; M = 4*c*c*d*n + 1; dv = divisors(M)
        Ap = sum(1 for X in dv if X % q == 1); Am = sum(1 for X in dv if X % q == q-1)
        tested['4.1slice'] += 1
        if Ap != 2 + 2*S[3][(n,c,d)] - D[3][(n,c,d)] or Am != 2*S[2][(n,c,d)] - D[2][(n,c,d)]: bad['4.1slice'] += 1
        tot_odd += Ap - Am - 2; tot_even += Ap + Am - 2
    if n <= NB:
        tp = sum(v for (m, c, d), v in S[2].items() if m == n); tm = sum(v for (m, c, d), v in S[3].items() if m == n)
        dp = sum(v for (m, c, d), v in D[2].items() if m == n); dm = sum(v for (m, c, d), v in D[3].items() if m == n)
        tested['4.1total'] += 1
        if tot_odd != 2*(tm - tp) - (dm - dp) or tot_even != 2*(tm + tp) - (dm + dp): bad['4.1total'] += 1
# (iii) Thm 5.2 on primes
pdiv = 0
for (n, c, d), v in S[0].items():
    if isprime(n) and (c*d) % n == 0: pdiv += 1
for p in range(5, N+1):
    if not isprime(p): continue
    keys = {(c, d) for (m, c, d) in S[0] if m == p}
    keys |= {(c, d) for c in range(1, 8) for d in range(1, 40)}
    for (c, d) in keys:
        if (2*c*d) % p == 0: continue
        q = 4*c*d; Nm = p*p + 4*c*c*d; fs = [f for f in divisors(Nm) if f % q == (-p) % q]
        tested['5.2'] += 1
        if len(fs) != 2*S[0][(p,c,d)] - D[0][(p,c,d)]: bad['5.2'] += 1
        if fs and kron(-4*d, p) != -1: bad['5.2inert'] += 1
        if any(kron(-4*d, f) != 1 for f in divisors(Nm)): bad['5.2allnorms'] += 1
print('tested', dict(tested)); print('failures', dict(bad)); print('T1+ prime solutions with p | cd:', pdiv)
