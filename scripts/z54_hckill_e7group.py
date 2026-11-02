# z54 HCKILL: enumerate points of the line-7 confinement curve via its elliptic-curve group (rank 1) and test the
# resulting quadratic families p = (y^2+delta)/(4a) for (i) real positivity, (ii) integrality (-delta square mod 4a),
# (iii) how many lines of C ∩ [4,XMAX] are confined.  Quartic: y^2 = 7(m-1)(5m-7)(5m+1)(7m+1); m = 1 + 1/z gives
# Y^2 = 7(5-2z)(6z+5)(8z+7) (Y = y z^2); X' = c3 z, Y' = c3 Y with c3 = -672.
# Usage: uv run --with cypari2 --with sympy python z54_hckill_e7group.py NMAX XMAX
import sys, math
from fractions import Fraction
import cypari2, sympy as sp
pari = cypari2.Pari(); pari.allocatemem(1_500_000_000)
NMAX = int(sys.argv[1]); XMAX = int(sys.argv[2])
z = sp.symbols('z'); f = sp.Poly(sp.expand(7*(5-2*z)*(6*z+5)*(8*z+7)), z)
c3, c2, c1, c0 = [int(c) for c in f.all_coeffs()]
E = pari.ellinit([0, c2, 0, c1*c3, c0*c3*c3])
gens = pari.ellrank(E)[3]; tors = pari.elltors(E)[2]
print("E:", [int(v) for v in E[:5]], "gens", gens, "tors", tors)
Cx = [x for x in range(4, XMAX+1) if x % 4 == 0 or x % 8 == 7]
def sqfree(n):
    F = pari.factor(n); s = 1
    for p, e in zip(F[0], F[1]):
        if int(e) % 2: s *= int(p)
    return s
def fd_neg(n):
    s = sqfree(n); d = -s
    return d if d % 4 == 1 else -4*s
def allowed(D, x): return x % (-D) == 0 and not (x % 8 == 7 and D % 8 != 1)
def analyse(U, W):
    A0, B0 = U*U - W*W, 16*W*W - U*U
    if A0 <= 0 or B0 <= 0: return "real-place failure"
    g = math.gcd(A0, B0); t = (3 if g % 3 else 1) * (5 if g % 5 else 1)
    a, de = t*t*A0//15, t*t*B0//15
    g2 = math.gcd(a, de)
    for p in [int(q) for q in pari.factor(g2)[0]] if g2 > 1 else []:
        while a % (p*p) == 0 and de % (p*p) == 0: a //= p*p; de //= p*p
    # integrality: odd primes l | a, l ∤ delta must have (-delta/l) = 1; 2-part checked by brute force mod 2^k
    bad = []
    for p, e in zip(*pari.factor(a)):
        p = int(p)
        if p == 2 or de % p == 0: continue
        if pari.kronecker(-de, p) != 1: bad.append(p)
    reached = []
    for x in Cx:
        De, Dl = fd_neg(de + 4*a*x), fd_neg(x*(x*de + 4*a))
        if not (allowed(De, x) and allowed(Dl, x)): break
        reached.append(x)
    return f"a={a} delta={de} (digits {len(str(a))},{len(str(de))}) bad_odd_primes_of_a={bad[:6]} confined_lines={reached}"
seen = set()
for n in range(-NMAX, NMAX+1):
    for T in tors:
        P = pari.elladd(E, pari.ellmul(E, gens[0], n), T)
        if P == [0]: continue
        Xp = Fraction(int(pari.numerator(P[0])), int(pari.denominator(P[0])))
        zz = Xp / c3
        if zz == 0: continue
        m = 1 + 1/zz
        nn, dd = m.numerator, m.denominator
        U = abs(4*(5*nn*nn - 5*nn*dd - dd*dd)); W = 5*nn*nn + dd*dd
        g = math.gcd(U, W); U //= g; W //= g
        if (U, W) in seen: continue
        seen.add((U, W))
        print(f"n={n} T={T}: (U,W) digits ({len(str(U))},{len(str(W))}) ->", analyse(U, W), flush=True)
