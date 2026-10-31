"""z52d audit A3, item Z3075: is the T1 failure of 4Cm^2+1 (no divisor = -1 mod 4C) explained by a
local condition at 2 / primes dividing C, or by the genus character chi_{-4C} (sign at infinity)?
(a) T1 check; (b) every prime factor l of 4Cm^2+1 has chi_{-4C}(l)=+1; (c) union over odd m of divisor
classes mod 4C = all of ker chi_{-4C}?  (d) local solubility of 4Ckj-k-j = m^2 mod 2^6 * C^2 (and mod l^2
for small l): is there a local obstruction at any finite place?"""
from sympy import factorint, jacobi_symbol
from math import gcd

def kron(a, n):  # Kronecker symbol (a/n) for n>0 odd or even
    from sympy.ntheory import legendre_symbol
    from sympy.ntheory.residue_ntheory import jacobi_symbol as js
    res = 1
    while n % 2 == 0:
        n //= 2
        if a % 2 == 0:
            return 0
        res *= 1 if a % 8 in (1, 7) else -1
    if n == 1:
        return res
    return res * js(a % n, n)

def divisors_from_f(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q**i for d in ds for i in range(e + 1)]
    return ds

out = []
for C in range(1, 31):
    t = 4 * C
    ker = {a for a in range(1, t) if gcd(a, t) == 1 and kron(-t, a) == 1}
    hit = set()
    t1_ok = True
    allsplit = True
    for m in range(1, 402, 2):
        N = t * m * m + 1
        f = factorint(N)
        for l in f:
            if kron(-t, l) != 1:
                allsplit = False
        for d in divisors_from_f(f):
            r = d % t
            hit.add(r)
            if r == t - 1:
                t1_ok = False
    # local solubility of 4Ckj - k - j = m^2 for m odd, modulo M = 2^6*C^2*(3*5*7)^2 (cheap brute over k,j mod M? too big)
    # instead: (4Ck-1)(4Cj-1) = 4Cm^2+1 mod q^a has solutions with X=-1 mod 4C? test q-adically by lifting: count mod q^a
    loc = {}
    for q in sorted(set([2, 3, 5, 7] + list(factorint(C).keys()))):
        a = 6 if q == 2 else 3
        Mq = q ** a
        okm = []
        for m in range(1, 2 * Mq, 2):
            target = (m * m) % Mq
            found = any(((t * k * j - k - j) % Mq) == target for k in range(Mq) for j in range(Mq)) if Mq <= 64 else None
            if found is None:
                # use: k free, solve j: j*(t*k-1) = m^2 + k  mod Mq ; solvable iff gcd(t*k-1,Mq) | (m^2+k)
                found = any(((target + k) % gcd((t * k - 1) % Mq or Mq, Mq)) == 0 for k in range(Mq))
            okm.append(found)
            if len(okm) > 40:
                break
        loc[q] = all(okm)
    out.append((C, t1_ok, allsplit, hit == ker, len(hit), len(ker), loc))
    print(C, "T1", t1_ok, "allfactors_chi=+1", allsplit, "classes_hit==ker", hit == ker, len(hit), len(ker), "local", loc)
