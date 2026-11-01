# z53 HCSHIFTS: why are hard primes hard?  For primes with HC >= 20 (from the samples) versus random controls of the same
# scale, compare over the lines x in C ∩ [4, 20): mean log2 tau(N), the model's expected-hit sum
# H = sum_x (tau(N^e)/phi(x) + tau(N^l)/(2 phi(x))), and the small-prime pattern of p (#{ell in 3..13 : p = 1 mod ell},
# #{ell in 3..23 odd prime : (p/ell) = +1}).
import sys, random, math
import cypari2
pari = cypari2.Pari()
from math import gcd
def phi(n): return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)
LINES = [x for x in range(4, 20) if x % 4 == 0 or x % 8 == 7]
PH = {x: phi(x) for x in LINES}
def stats(p):
    lt = []; H = 0.0
    for x in LINES:
        te = int(pari.numdiv(p + x)); tl = int(pari.numdiv(x * p + 1))
        lt += [math.log2(te), math.log2(tl)]; H += te / PH[x] + tl / (2 * PH[x])
    ones = sum(1 for l in (3, 5, 7, 11, 13) if p % l == 1)
    qr = sum(1 for l in (3, 5, 7, 11, 13, 17, 19, 23) if pow(p, (l - 1) // 2, l) == 1)
    return sum(lt) / len(lt), H, ones, qr
random.seed(1)
for fn in sys.argv[1:]:
    rows = [l.split() for l in open(fn) if not l.startswith('#')]
    hard = [int(r[0]) for r in rows if int(r[1]) >= 20]
    ctrl = [int(r[0]) for r in random.sample(rows, 3000)]
    out = []
    for name, S in (('HC>=20', hard), ('random', ctrl)):
        v = [stats(p) for p in S]; n = len(v)
        out.append(f"{name}: n={n} mean log2 tau = {sum(a for a,_,_,_ in v)/n:.2f}, mean H = {sum(b for _,b,_,_ in v)/n:.2f}, "
                   f"median H = {sorted(b for _,b,_,_ in v)[n//2]:.2f}, mean #{{ell<=13: p=1 mod ell}} = {sum(c for _,_,c,_ in v)/n:.2f}, "
                   f"mean #{{ell<=23: (p/ell)=1}} = {sum(d for _,_,_,d in v)/n:.2f}")
    print(f"== {fn}\n   " + "\n   ".join(out))
