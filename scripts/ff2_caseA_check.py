"""ff2_caseA_check.py (O166): brute-force check of Case A at x_u (x = 1 off T, u at T), q = p prime, A = T^k.
Enumerates monic a0, b0 (deg <= DM), monic-up-to-unit divisors E of a0+b0 (via all E with deg<=deg(a0+b0)),
and checks: T^(k+j)L' | P+E  <=>  E = -u mod T^(k+j), E = -1 mod L';  lc(E) in achievable lc set of the
Case A type pairs.  usage: ff2_caseA_check.py p k DM u_digits(high->low)"""
import sys, itertools
sys.path.insert(0, 'scripts')
from ff2_polyq import *
p, k, DM = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); u = parse(sys.argv[4], p)
def monics(d):
    for t in itertools.product(range(p), repeat=d): yield list(t) + [1]
def gcd(a, b):
    while b: a, b = b, mod(a, b, p)
    return [x * pow(a[-1], p - 2, p) % p for x in a]
def vT(a):
    v = 0
    while a[v] == 0: v += 1
    return v
hits = 0
for da in range(DM + 1):
    for a0 in monics(da):
        for db in range(DM + 1):
            for b0 in monics(db):
                g = gcd(a0, b0); L = divmod_(mul(a0, b0, p), g, p)[0]
                j = vT(L); Lp = L[j:]
                s = add(a0, b0, p)
                if not s: continue
                # lc of a+b in Case A: same type & same degree -> 2 (char odd) else 1; types (0,0),(1,1): a0+b0 ;(2,2),(3,3): equal deg iff da==db
                lcs = {1}
                if da == db: lcs.add(2 % p)
                M = mul([0] * (k + j) + [1], Lp, p)
                for dE in range(1, len(s)):
                    for lcE in range(1, p):
                        if lcE not in lcs: continue
                        for E0 in monics(dE):
                            E = [x * lcE % p for x in E0]
                            if mod(s, E, p): continue
                            if mod(add(E, u, p), [0] * (k + j) + [1], p): continue
                            if Lp != [1] and mod(add(E, [1], p), Lp, p): continue
                            hits += 1; print('HIT a0', a0, 'b0', b0, 'E', E)
print('hits', hits)
