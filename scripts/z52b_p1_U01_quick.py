"""U01 quick checks: Z1877 (multiplicative variant), Z2854 (3x3 matrix relaxation), Z1316 (reciprocal additive energy),
Z0140 (M(p) structure), Z0179 (binary-digit correlation), Z1416 (greedy first term -> two-term remainder)."""
import sys, os, math, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import *
from fractions import Fraction as Fr
import numpy as np
P = primes_upto(10000)[1:]
def part(name): print("==", name, flush=True)
# Z1877: (1+1/x)(1+1/y)(1+1/z) = (p+4)/p, x<=y<=z, x>=2 ; brute with bound x,y <= 2p
part("Z1877 multiplicative variant")
fails = []
for p in P[:400]:
    target = Fr(p+4, p); ok = False
    for x in range(2, 2*p+1):
        a = Fr(x+1, x)
        if target / a <= 1: break
        for y in range(x, 2*p+1):
            b = a*Fr(y+1, y)
            r = target / b
            if r <= 1: break
            if r.numerator == 1 or True:
                # need 1 + 1/z = r  => z = 1/(r-1)
                if r - 1 > 0 and (1/(r-1)).denominator == 1 and 1/(r-1) >= y:
                    ok = True; break
        if ok: break
    if not ok: fails.append(p)
print("primes<=2000 with no solution (x,y<=2p search):", len(fails), fails[:10])
# Z2854: 4/p = 1^T M^{-1} 1, M = [[a,-1,0],[-1,b,0],[0,0,c]] pos def integers; M^{-1}: block (a,b) inverse has sum (a+b+2)/(ab-1)
part("Z2854 one off-diagonal -1 in 3x3")
cnt = 0; tot = 0
for p in P[1:300]:
    tot += 1; hit = False
    for a in range(2, 2*p+1):
        for b in range(a, 2*p+1):
            d = a*b-1
            if d <= 0: continue
            rest = Fr(4, p) - Fr(a+b+2, d)
            if rest > 0 and rest.numerator == 1:
                hit = True; break
        if hit: break
    cnt += hit
print("primes p<=2000 with 4/p = (a+b+2)/(ab-1) + 1/c (a,b in [2,2p]):", cnt, "of", tot)
# Z1316: additive energy of inverses of an interval mod q
part("Z1316 reciprocal additive energy")
for q in (101, 503, 1009):
    for L in (q//4,):
        S = [pow(x, q-2, q) for x in range(1, L+1)]
        cnt = collections.Counter((a+b) % q for a in S for b in S)
        E = sum(v*v for v in cnt.values())
        Eint = sum(v*v for v in collections.Counter((a+b) for a in range(1, L+1) for b in range(1, L+1)).values())
        print(f"q={q}, interval 1..{L}: E(inverses)={E}, E(integers)={Eint}, ratio={E/Eint:.3f}, |S|^4/q-ish={L**4/q:.1f}")
# Z0140: M(p) ∩ [1,48] = {m: U_m(p)>0}; differences mod 4 among elements
part("Z0140 M(p) structure (m<=48, p<=1e5)")
U = {m: load_m(m) for m in range(5, 49)}
Mp = {p: [m for m in range(5, 49) if U[m][p] > 0] for p in U[5] if p > 5}
dif4 = collections.Counter(); tot = 0
for p, ms in Mp.items():
    for m in ms: dif4[m % 4] += 1
    tot += len(ms)
print("residues mod 4 of m in M(p) over primes:", {k: round(v/tot, 3) for k, v in sorted(dif4.items())})
# Z0179: binary-digit correlation of U4(p) with popcount / low bits (p<=3e4)
part("Z0179 binary digits vs ES counts")
f4 = load_counts(os.path.join(RAW, "f4_all_30000.txt"))
pr = [p for p in primes_upto(30000) if p > 5 and p in f4]
A = np.array([math.log(f4[p][0]+1) for p in pr]); lp = np.array([math.log(p) for p in pr])
res = A - np.polyval(np.polyfit(lp, A, 2), lp)
for name, feat in (("popcount", [bin(p).count("1") for p in pr]), ("bit1", [(p >> 1) & 1 for p in pr]), ("bit2", [(p >> 2) & 1 for p in pr]), ("bit3", [(p >> 3) & 1 for p in pr])):
    f = np.array(feat, float)
    print(name, "corr with residual:", round(np.corrcoef(f, res)[0, 1], 3))
