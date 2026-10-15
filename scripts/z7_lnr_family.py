"""O231 memo z7_lnr_family: growing families built on the least non-residue q = q(p) (p = 1 (8) prime < HI).
Counts primes having (a) a word with q | A and q | B (all three sides unclean automatically: q | A | N_t, N_u; q | B | N_v);
(b) a word with u = q or v = q (u-side unclean automatically); (c) a word with q | N_t and psi(u) = psi(v) = -1 (unforced
by symbols + q).  Also checks K(p) < q(p) (p+q has psi = -1).  usage: z7_lnr_family.py HI"""
import sys
from math import isqrt
HI = int(sys.argv[1]); M = 2 * HI + 10
spf = list(range(M + 1))
for i in range(2, isqrt(M) + 1):
    if spf[i] == i:
        for j in range(i * i, M + 1, i):
            if spf[j] == j: spf[j] = i
def leg(a, p): return pow(a % p, (p - 1) // 2, p)
cnt = [0, 0, 0, 0]; worst = None
for p in range(17, HI):
    if p % 8 != 1 or spf[p] != p: continue
    q = 3
    while leg(q, p) == 1 or spf[q] != q: q += 2
    a = b = c = False
    for u in range(1, isqrt(p) + 3):
        if (u - 2) * u > p: break
        x = p + u; ds = [1]
        while x > 1:
            r = spf[x]; e = 0
            while x % r == 0: x //= r; e += 1
            ds = [d * r ** k for d in ds for k in range(e + 1)]
        for v in ds:
            if v < u or (p + u + v) % (u * v): continue
            t = (p + u + v) // (u * v); A, B = t * u - 1, t * v - 1
            if A % q == 0 and B % q == 0: a = True
            if u == q or v == q: b = True
            if (t * p + 1) % q == 0 and leg(u, p) != 1 and leg(v, p) != 1: c = True
    cnt[0] += 1; cnt[1] += a; cnt[2] += b; cnt[3] += c
    if not (a or c) and (worst is None or q > worst[1]): worst = (p, q)
print(f"primes {cnt[0]}: q|gcd(A,B) {cnt[1]}, u or v = q {cnt[2]}, q|N_t & psi(u)=psi(v)=-1 {cnt[3]}; largest q with neither (a) nor (c): {worst}")
