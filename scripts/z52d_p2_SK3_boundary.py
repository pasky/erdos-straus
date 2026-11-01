# z52d pass2 SK3, item Z2240: strata of (*) witnesses at the least level Cmin(p), p = 1 mod 4 <= 2*10^5.
# (u,B,C) with 4uBC-u-B=p, gcd(u,B)=1, u+B odd (FRONTIER 2.1 pair form). Boundary := min(u,B)=1 or u=B.
# Reports: #primes with a witness at Cmin; #with an interior (all of u,B>=2, u!=B) witness at Cmin; #with only boundary witnesses.
import math
def primes1mod4(hi):
    s = bytearray([1])*(hi+1); s[0]=s[1]=0
    for i in range(2, int(hi**0.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [p for p in range(5, hi+1) if s[p] and p % 4 == 1]
from math import gcd
res = dict(n=0, boundary_only=0, has_interior=0, none_le40=0, interior_only=0, eg=[])
for p in primes1mod4(200000):
    found = None
    for C in range(1, 41):
        m = 4*C; N = m*p + 1; sols = []
        a = m-1
        while a*a <= N:
            if N % a == 0:
                b = N // a
                sols.append(((a+1)//m, (b+1)//m))
            a += m
        if sols:
            found = (C, sols); break
    if not found:
        res['none_le40'] += 1; continue
    C, sols = found
    res['n'] += 1
    valid = []
    for (u, B) in sols:
        for (x, y) in ((u, B), (B, u)):
            if gcd(x, y) == 1 and (x+y) % 2 == 1:
                valid.append((x, y))
    if not valid:
        res['none_le40'] += 1; continue   # level present only via non-admissible pairs
    interior = [(x, y) for (x, y) in valid if x >= 2 and y >= 2 and x != y]
    if interior:
        res['has_interior'] += 1
    else:
        res['boundary_only'] += 1
        if len(res['eg']) < 5: res['eg'].append((p, C, valid))
print(res)
