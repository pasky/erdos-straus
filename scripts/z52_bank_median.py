"""Check of Corollary 1(f) (z52 bank).  For primes p = 1 (24), p <= LIM: H_av(p) := largest H with H^2 < p such that p
avoids every E_(a,v) (p = -a-v mod av, 1<=a<v<=H coprime, minus (1,2),(2,3)) and every C_(A,d) (p = -d mod A, 2<=A<=H,
d | A+1, d<A, minus (2,1),(3,2)).  Verify: every certifying word (u<=v, a coordinate in C_p) has min(A,A*,v) > H_av and
med(t,u,v) > sqrt(H_av+1).  Also prints M2(p) = min med over certifying words at the board's hard primes."""
import sys, math
from sympy import primerange, divisors
from math import gcd
def inC(x, p): return x % 4 == 0 or (x + p) % 8 == 0
def cert_words(p):
    W = []
    u = 1
    while u * u - 2 * u <= p:          # t >= 1, v >= u  =>  u(tu-1) <= p+u
        for A in divisors(p + u):
            if (A + 1) % u: continue
            t, v = (A + 1) // u, (p + u) // A
            if v < u: continue
            if inC(t, p) or inC(u, p) or inC(v, p): W.append((t, u, v, A, t * v - 1))
        u += 1
    return W
def H_av(p):
    H = 1
    while (H + 1) ** 2 < p:
        h = H + 1
        bad = any(gcd(a, h) == 1 and (a, h) not in ((1, 2), (2, 3)) and (p + a + h) % (a * h) == 0 for a in range(1, h))
        bad = bad or any((h, d) not in ((2, 1), (3, 2)) and (p + d) % h == 0 for d in divisors(h + 1) if d < h)
        if bad: break
        H = h
    return H
LIM = int(sys.argv[1]); n = viol = 0; mx = (0, 0)
for p in primerange(25, LIM):
    if p % 24 != 1: continue
    H = H_av(p); W = cert_words(p); n += 1
    if H > mx[0]: mx = (H, p)
    for (t, u, v, A, As) in W:
        if not (min(A, As, v) > H and sorted((t, u, v))[1] > math.sqrt(H + 1)): viol += 1; print('VIOL', p, H, (t, u, v))
print(f'primes p=1(24) < {LIM}: {n}, violations {viol}, largest H_av = {mx[0]} at p = {mx[1]}')
for p in (73, 193, 409, 577, 2521, 3361, 5569, 9601, 66529):
    print('M2', p, min(sorted((t, u, v))[1] for (t, u, v, A, As) in cert_words(p)))
