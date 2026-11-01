# z52d pass2 SK3, item Z2139: ES SL2 form (FRONTIER 2.1): M=[[a,p],[c,d]] in SL2(Z), c in 4N, a,d>=1, a=d=-1 mod c.
# Right action by g_k=[[1,0],[k,1]] keeps p and det: M g_k = [[a+pk, p],[c+dk, d]].  Test: which neighbours (k != 0) are again
# ES-form solutions for the same p?  S(p) enumerated exactly: C<=CMAX, pairs of divisors (a,d) of N=4Cp+1 with a=d=-1 mod 4C.
import math, sys
from collections import Counter
def S(p, CMAX):
    out = []
    for C in range(1, CMAX+1):
        c = 4*C; N = c*p + 1
        for a in range(c-1, int(math.isqrt(N))+1, c):   # a = -1 mod c, a^2 <= N  (a is the smaller factor)
            if N % a == 0:
                d = N // a
                out.append((a, c, d))
                if a != d: out.append((d, c, a))
    return out
def is_es(a, c, d, p):
    return c >= 4 and c % 4 == 0 and a >= 1 and d >= 1 and (a+1) % c == 0 and (d+1) % c == 0 and a*d - p*c == 1
def primes1mod4(lo, hi):
    s = bytearray([1])*(hi+1); s[0]=s[1]=0
    for i in range(2, int(hi**0.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [p for p in range(max(lo,5), hi+1) if s[p] and p % 4 == 1]
KMAX = 60
tot_nb = 0; tot_es = 0; per_p = []
ps = primes1mod4(5, 3000)
for p in ps:
    sol = S(p, 40)
    if not sol: continue
    nb = 0; es = 0
    for (a, c, d) in sol:
        for k in range(-KMAX, KMAX+1):
            if k == 0: continue
            a2, c2, d2 = a + p*k, c + d*k, d
            if c2 <= 0: continue
            nb += 1
            if is_es(a2, c2, d2, p): es += 1
    tot_nb += nb; tot_es += es
    per_p.append((p, len(sol), nb, es))
print(f"primes 1 mod 4 <= 3000 with >=1 level<=40: {len(per_p)}; neighbour moves (|k|<={KMAX}) tested: {tot_nb}; landing in S(p): {tot_es} (rate {tot_es/max(tot_nb,1):.4f})")
# Orbit check: is S(p) closed under the moves?  count solutions that have at least one solution neighbour
closed = 0
for p, ns, nb, es in per_p:
    if es > 0: closed += 1
print("primes where some neighbour move stays in S(p):", closed, "of", len(per_p))
print("sample:", per_p[:8])
