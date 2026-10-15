# R246 from scratch: (a) s6_divisor_pigeonhole numerics; (b) s6_unique_forced_cap0 for admissible composite windows;
# (c) Cauchy–Davenport signed-sum bound min(u, 2N+1) and its sharpness, brute force for small prime u.
import sys
from itertools import product
def primes(n):
    s = bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2, int(n**.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
def fac(n):
    f = {}; d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d, 0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f
def jac(a, n):  # Jacobi symbol
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
PR = primes(N + 20000)
tot = crit = cap = 0
for p in PR:
    if p < 5 or p > N or p % 4 != 1: continue
    q = next(q for q in PR if q % 4 == 3 and jac(q, p) == -1 and ((p + q)//4) % 2 == 1)
    K = (p + q)//4
    P = {1}
    for s, e in fac(K).items():
        P = {(a * pow(s, k, q)) % q for a in P for k in range(e + 1)}
    c = len(P) > (q - 1)//2; h = any((q - a) % q in P for a in P)
    tot += 1; crit += c; cap += h
    assert h or not c
print(f"(a) primes p=1(4) <= {N}: {tot}; criterion fires {crit}; cap0 at least odd-K forced window {cap}")
# (b) admissible windows m (all prime factors = 3 mod 4), m <= 300: forced classes g (Jacobi-wise non-residue at every q_i);
# cap 0 forced for all K iff every forced g ... a prime K = s = g gives Sigma = {1, g, 1/g}; -1 in it iff g = -1.
bad = []
for m in range(3, 301):
    f = fac(m)
    if any(q % 4 != 3 for q in f): continue
    forced = [g for g in range(1, m) if all(jac(g, q) == -1 for q in f) and all(g % q for q in f)]
    allcap0 = all(g == m - 1 for g in forced)
    if allcap0: bad.append(m)
print("(b) admissible windows m<=300 where every forced prime K has cap 0:", bad)
# (c) signed sums over Z/u, u prime: N copies of {-a,0,a}
for u in (5, 7, 11, 13):
    for Nn in range(1, 6):
        mins = min(len({sum(x) % u for x in product(*[(-a, 0, a) for a in A])})
                   for A in product(range(1, u), repeat=Nn))
        assert mins == min(u, 2*Nn + 1), (u, Nn, mins)
print("(c) min |signed sumset| = min(u, 2N+1) for u in 5,7,11,13, N<=5: OK")
