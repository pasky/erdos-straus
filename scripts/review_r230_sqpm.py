"""R230 from scratch: CONJECTURE PM-SQ_± and the prime-modulus class mass of CAP_GROWING §3.

Ticket for n (n = 1 mod 8): a prime l, an integer u not in {0, -n} with l | n+u, u | l+1 or u | l-1, and (n/l) = -1.
Then word: A = l (u | l+1) or A = -l (u | l-1), t = (A+1)/u, v = (n+u)/A; verified: t u v - u - v = n and
Jacobi(-A, n) = -1 (computed directly, not via reciprocity).
Usage: N  -> checks all n = 1 (8), n <= N (squares: confirms NO ticket with |u| <= n+1 for squares <= SQMAX).
Also prints mass sum_{l <= N, prime} omega_pm(l)/l / log N, omega_pm(l) = #{r in R(l): (r/l) = -1}."""
import sys, math
from sympy import jacobi_symbol, divisors

N = int(sys.argv[1]); SQMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
M = 2*N + 10
spf = list(range(M + 1))
for i in range(2, int(M**0.5) + 1):
    if spf[i] == i:
        for j in range(i*i, M + 1, i):
            if spf[j] == j: spf[j] = i

def primes_of(m):
    m = abs(m); s = set()
    while m > 1:
        q = spf[m]; s.add(q); m //= q
    return s

def ticket(n, umax):
    for a in range(1, umax + 1):
        for u in (a, -a):
            if u == -n: continue
            for l in primes_of(n + u):
                if l == 2 or n % l == 0: continue
                for A in (l, -l):
                    if (A + 1) % u: continue
                    if jacobi_symbol(n % l, l) != -1: continue
                    t = (A + 1)//u; v = (n + u)//A
                    assert t*u*v - u - v == n and t != 0 and v != 0
                    assert jacobi_symbol((-A) % n, n) == -1
                    return (t, u, v, A)
    return None

exc = []; maxu = 0; cnt = 0
for n in range(9, N + 1, 8):
    r = math.isqrt(n)
    if r*r == n: continue
    cnt += 1
    w = ticket(n, 200)
    if w is None:
        w = ticket(n, n + 1)
        if w is None: exc.append(n); continue
    maxu = max(maxu, abs(w[1]))
print(f"non-squares n = 1 (8) <= {N}: {cnt}, exceptions: {exc[:20]} ({len(exc)}), max least |u| = {maxu}")

sq_hits = []
for r in range(3, math.isqrt(SQMAX) + 1, 2):
    n = r*r
    if n % 8 != 1: continue
    if ticket(n, n + 1) is not None: sq_hits.append(n)
print(f"odd squares <= {SQMAX} with a ticket (complete |u| <= n+1 search): {sq_hits}")

# mass over primes l <= N
S = 0.0
for l in range(5, N + 1, 2):
    if spf[l] != l: continue
    R = set()
    for D in (l + 1, l - 1):
        for d in divisors(D):
            for u in (d, -d):
                R.add((-u) % l)
    R.discard(0)
    w = sum(1 for r in R if jacobi_symbol(r, l) == -1)
    S += w/l
print(f"mass sum_(l<=N) omega_pm/l = {S:.3f}, / log N = {S/math.log(N):.3f}")
