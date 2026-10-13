"""R166: brute-force Case A at the point x = u (mod T^inf), x = 1 at every prime != T, A = T^k.
Case A: E | a0 + b0 (equivalently E | a1 + b1 after removing gcd), validity congruences
  E = -u (mod T^{k+j}),  E = -1 (mod L'),  L = lcm(a0,b0) = T^j L'.
All divisors E (every leading coefficient) are tried; hits are reported with lc(E) and lc(a0+b0)
(lc(s) is 1 or lc(a0+b0) depending on types; lc(E) must equal lc(s)).
usage: review_ff2_caseA.py p k u_coeffs(low first, comma) maxdeg"""
import sys
from review_ff2_poly import *

p, k = int(sys.argv[1]), int(sys.argv[2])
setp(p)
u = tr([int(x) for x in sys.argv[3].split(',')])
md = int(sys.argv[4])
T = (0, 1)
mons = list(monics_upto(md))
alld = {}


def vT(a):
    v = 0
    while a and a[0] == 0:
        a = a[1:]
        v += 1
    return v, a


hits = []
npairs = 0
for i, a0 in enumerate(mons):
    for b0 in mons[i:]:
        npairs += 1
        g = egcd(a0, b0)[0]
        L = dm(mul(a0, b0), g)[0]
        j, Lp = vT(L)
        s0 = add(a0, b0)
        if not s0:
            continue
        mT = Tpow(k + j)
        tgt = mod(neg(u), mT)
        for d in monics_upto(deg(s0)):
            if not divides(d, s0):
                continue
            for lam in range(1, p):
                E = scal(lam, d)
                if mod(sub(E, tgt), mT) != ():
                    continue
                if deg(Lp) > 0 and mod(add(E, (1,)), Lp) != ():
                    continue
                hits.append((a0, b0, E, E[-1], s0[-1]))
print("pairs", npairs, "hits(any lc)", len(hits))
for h in hits[:30]:
    print("a0", h[0], "b0", h[1], "E", h[2], "lcE", h[3], "lc(a0+b0)", h[4])
ok = [h for h in hits if h[3] == 1 or h[3] == h[4]]
print("hits with lc(E) in {1, lc(a0+b0)}:", len(ok))
for h in ok[:30]:
    print("  ", h)
