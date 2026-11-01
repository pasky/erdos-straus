# Batch of quick concrete checks for NC3 items: Z2824 (cyclotomic norms), Z2828 (Dedekind-sum identity over L3),
# Z2861 (Farey/SL2 move and Jacobi symbol), Z2880 (SL2(Z/4) conjugacy classes), Z2889 (multiplicative energy),
# Z2899 (continuant Bezout identity for 4-chains).
import sys, cmath, math, itertools
from fractions import Fraction
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
from sympy import jacobi_symbol
from collections import defaultdict, Counter
def ded(h, k):
    def saw(x):
        if x.denominator == 1: return Fraction(0)
        return x - (x.numerator // x.denominator) - Fraction(1, 2)
    return sum(saw(Fraction(i, k)) * saw(Fraction(h*i % k, k)) for i in range(1, k))
print("== Z2824: norm of (1-zeta^A)/(1-zeta) from Q(zeta_p) to Q(sqrt p*) ==")
for p in [13, 17, 29, 37, 41, 53]:
    z = cmath.exp(2j*math.pi/p)
    H = [h for h in range(1, p) if L.legendre(h, p) == 1]
    res = []
    for A in range(2, p):
        if L.legendre(A, p) == 0: continue
        num = 1; den = 1
        for h in H:
            num *= (1 - z**((A*h) % p)); den *= (1 - z**h)
        N = num/den
        res.append((L.legendre(A, p), round(abs(N), 6), round(N.real, 4), round(N.imag, 4)))
    byS = defaultdict(set)
    for s, a, re, im in res: byS[s].add((a, re, im))
    print(f"p={p}: QR A give |N| set {sorted({x[0] for x in byS[1]})}, QNR A give |N| set {sorted({x[0] for x in byS[-1]})}")
print("== Z2828: Dedekind sums over L3(p) vs (D2) prediction 12 s(A,p) = t+u+v-9 + (A+A*)/p ==")
ok = bad = 0
for p in [13, 17, 29, 37, 53, 61, 73, 89, 97, 101, 109, 113]:
    for (t, u, v) in L.words(p):
        A = t*u-1; As = t*v-1
        lhs = 12*ded(A, p)
        rhs = (t+u+v-9) + Fraction(A+As, p)
        if lhs == rhs: ok += 1
        else: bad += 1
print("words checked:", ok+bad, "identity holds:", ok, "fails:", bad)
print("== Z2861: Farey move p -> p + kA preserves Jacobi (p/A)?  ==")
ok = bad = 0
for p in L.primes_upto(400):
    if p < 17 or p % 8 != 1: continue
    for (t, u, v) in L.words(p):
        A = t*u-1
        if A % 2 == 0 or A < 3: continue
        for k in (1, 2, 3):
            if jacobi_symbol((p + k*A) % A, A) == jacobi_symbol(p % A, A): ok += 1
            else: bad += 1
print("Jacobi (p+kA / A) = (p / A):", ok, "holds,", bad, "fails")
print("== Z2880: is the sign a class function on SL2(Z/4)? (conjugacy classes of SL2(Z/4)) ==")
G = []
for a, b, c, d in itertools.product(range(4), repeat=4):
    if (a*d - b*c) % 4 == 1: G.append((a, b, c, d))
def mul(x, y):
    a,b,c,d = x; e,f,g,h = y
    return ((a*e+b*g)%4, (a*f+b*h)%4, (c*e+d*g)%4, (c*f+d*h)%4)
def inv(x):
    a,b,c,d = x; return (d%4, (-b)%4, (-c)%4, a%4)
cls = {}; cid = 0
for x in G:
    if x in cls: continue
    orbit = set()
    for g in G:
        orbit.add(mul(mul(g, x), inv(g)))
    for y in orbit: cls[y] = cid
    cid += 1
print("|SL2(Z/4)| =", len(G), "conjugacy classes:", cid)
cons = defaultdict(set); cnt = 0
for p in L.primes_upto(3000):
    if p < 17 or p % 8 != 1: continue
    for (t, u, v) in L.words(p):
        A = t*u-1; As = t*v-1
        M = (p % 4, (-As) % 4, A % 4, (-t) % 4)
        cons[cls[M]].add(L.legendre(A, p)); cnt += 1
print("words", cnt, "conjugacy classes hit:", len(cons), "classes with both signs:", sum(1 for s in cons.values() if len(s) > 1))
print("== Z2899: 4-chain Bezout identity p*K(b,c) - K(a,b,c)*K(b,c,d) = ±1 ==")
def K(seq):
    if not seq: return 1
    if len(seq) == 1: return seq[0]
    return seq[0]*K(seq[1:]) - (K(seq[2:]) if len(seq) > 2 else 1)
cnt = Counter()
for a, b, c, d in itertools.product(range(2, 12), repeat=4):
    p = K([a, b, c, d]); 
    cnt[p*K([b, c]) - K([a, b, c])*K([b, c, d])] += 1
print("values of K(abcd)K(bc) - K(abc)K(bcd) over 2..11^4:", dict(cnt))

print("== Z2889: multiplicative energy E(S) = #{a b = c d mod p} of S_3(p) (L3) and S_4(p) (4-chain cofactors) ==")
def energy(S, p):
    from collections import Counter
    c = Counter((a*b) % p for a in S for b in S)
    return sum(v*v for v in c.values())
for p in [1009, 10009, 100003]:
    if p % 8 != 1: continue
    S3 = L.L3(p)
    E3 = energy(S3, p)
    print(f"p={p}: |S3|={len(S3)} E(S3)={E3}  E/|S|^3={E3/len(S3)**3:.4f}  E/|S|^2={E3/len(S3)**2:.3f}")
