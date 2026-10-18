"""O262 Prop 3.1 check: build primes p = 1 + Q t with the slice cofactors P_theta = N_theta(p)/N_theta(1) prime, then
count the solutions in each slice by literal reconstruction (divisors of N_theta(p) -> (a,b,c,d) -> check the ET
equation).  Controls: random primes p ≡ 1 (mod 24) of the same size.  Usage: uv run --with python-flint python ..."""
import random, math, sys
from flint import fmpz
def divisors(n):
    ds = [1]
    for q, e in fmpz(n).factor():
        q = int(q); ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
def isprime(n): return fmpz(n).is_prime()
# slices: (kind, params) -> (N(p), test(p, N) -> number of solutions)
def II_ac(a, c):
    N = lambda p: c*p + a
    def cnt(p):
        n = 0
        for f in divisors(N(p)):
            if (f + 1) % (4*a*c) == 0:
                d = (f + 1)//(4*a*c); b = N(p)//f
                n += (4*a*b*c*d == a + b + c*p)
        return n
    return ('II{a,c}', (a, c), N, cnt)
def II_cd(c, d):
    N = lambda p: 4*c*c*d*p + 1
    def cnt(p):
        n = 0
        for f in divisors(N(p)):
            g = N(p)//f
            if (f + 1) % (4*c*d) == 0 and (g + 1) % (4*c*d) == 0:
                a = (f + 1)//(4*c*d); b = (g + 1)//(4*c*d); n += (4*a*b*c*d == a + b + c*p)
        return n
    return ('II{c,d}', (c, d), N, cnt)
def I_ac(a, c):
    N = lambda p: a*p + c
    def cnt(p):
        n = 0
        for f in divisors(N(p)):
            if (f + p) % (4*a*c) == 0:
                d = (f + p)//(4*a*c); b = N(p)//f; n += (4*a*b*c*d == p*(a + b) + c)
        return n
    return ('I{a,c}', (a, c), N, cnt)
def eslice(t, e):
    N = (lambda p: (p + e)//4) if t == 'II' else (lambda p: (p*e + 1)//4)
    def cnt(p):
        n = 0; Nv = N(p); ds = divisors(Nv)
        for a in ds:
            for b in ds:
                if b >= a and Nv % (a*b) == 0 and (a + b) % e == 0:
                    c = (a + b)//e; d = Nv//(a*b)
                    n += (4*a*b*c*d == (a + b + c*p) if t == 'II' else 4*a*b*c*d == p*(a + b) + c)
        return n
    return (t + '-e', e, N, cnt)
Theta = [II_ac(1,1), II_ac(1,2), II_ac(2,1), II_cd(1,1), I_ac(1,1), eslice('II',3), eslice('II',7), eslice('I',3), eslice('I',7)]
Q = 1
for kind, par, N, cnt in Theta:
    qN = {'II{a,c}': 4*par[0]*par[1]*N(1) if 'a,c' in kind else 0}.get(kind, 0)
    if kind == 'II{a,c}' or kind == 'I{a,c}': q = 4*par[0]*par[1]
    elif kind == 'II{c,d}': q = 4*par[0]*par[1]
    else: q = par
    Q = Q * q * N(1) // math.gcd(Q, q * N(1))
for l in (2, 3, 5, 7, 11): Q = Q * l // math.gcd(Q, l)
print('Q =', Q, '|Theta| =', len(Theta))
random.seed(262); found = []; t = random.randrange(10**12 // Q, 2 * 10**12 // Q)
while len(found) < 3:
    t += 1; p = 1 + Q*t
    if isprime(p) and all(N(p) % N(1) == 0 and isprime(N(p)//N(1)) for _, _, N, _ in Theta): found.append(p)
for p in found:
    print('shadow p =', p, [cnt(p) for _, _, _, cnt in Theta])
for _ in range(3):
    while True:
        p = 24*random.randrange(10**12//24, 2*10**12//24) + 1
        if isprime(p): break
    print('control p =', p, [cnt(p) for _, _, _, cnt in Theta])
