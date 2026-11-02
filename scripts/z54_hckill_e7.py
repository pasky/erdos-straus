# z54 HCKILL: rational points on the line-7 confinement curve E7 and the quadratic families they give.
# Families p = (y^2 + delta)/(4a) with line 4 confined need (a,delta) ~ (U^2-W^2, 16W^2-U^2)/15 (mod squares).
# Line 7 (endpoint + level) confined by chi_{-7} needs 9U^2-4W^2 in 35*Q^2 and 36W^2-U^2 in 5*Q^2; parametrising the
# second conic through (U,W,r)=(4,1,2) gives U/W = 4(5m^2-5m-1)/(5m^2+1) and the condition y^2 = 7(m-1)(5m-7)(5m+1)(7m+1).
# Usage: uv run --with cypari2 python z54_hckill_e7.py HEIGHT XMAX
import sys, math
import cypari2
pari = cypari2.Pari(); pari.allocatemem(1_500_000_000)
H = int(sys.argv[1]); XMAX = int(sys.argv[2])
from fractions import Fraction
def sqfree(n):
    n = int(n); assert n > 0
    f = pari.factor(n); s = 1
    for p, e in zip(f[0], f[1]):
        if int(e) % 2: s *= int(p)
    return s
def fd_neg(n):
    s = sqfree(n); d = -s
    return d if d % 4 == 1 else -4 * s
def allowed(D, x):
    if x % (-D): return False
    if x % 8 == 7 and D % 8 != 1: return False
    return True
Cx = [x for x in range(4, XMAX + 1) if x % 4 == 0 or x % 8 == 7]
def family(U, W):
    A0, B0 = U*U - W*W, 16*W*W - U*U
    if A0 <= 0 or B0 <= 0: return None
    g = math.gcd(A0, B0); t = 1
    if g % 3: t *= 3
    if g % 5: t *= 5
    a, de = t*t*A0 // 15, t*t*B0 // 15
    assert t*t*A0 % 15 == 0 and t*t*B0 % 15 == 0
    # remove common square factors
    g2 = math.gcd(a, de); f = pari.factor(g2) if g2 > 1 else [[], []]
    for p, e in zip(f[0], f[1]):
        p = int(p); e = int(e)
        while a % (p*p) == 0 and de % (p*p) == 0: a //= p*p; de //= p*p
    return a, de
def lines_reached(a, de):
    k = 0; Ds = []
    for x in Cx:
        De = fd_neg(de + 4*a*x); Dl = fd_neg(x*(x*de + 4*a))
        if not (allowed(De, x) and allowed(Dl, x)): return x, Ds
        Ds.append((x, De, Dl))
    return None, Ds
def local_ok(a, de):
    # -delta must be a square mod 4a  (p = (y^2+delta)/(4a) integral for some y)
    m = 4*a
    if (-de) % 4 not in (0, 1): return False
    f = pari.factor(m)
    for p, e in zip(f[0], f[1]):
        p, e = int(p), int(e); q = p**e; t = (-de) % q
        if not any((y*y - t) % q == 0 for y in range(q)) if q < 10**6 else True: return False
    return True
pts = pari.hyperellratpoints(pari('7*(x-1)*(5*x-7)*(5*x+1)*(7*x+1)'), H)
seen = set()
for P in pts:
    mm = Fraction(int(pari.numerator(P[0])), int(pari.denominator(P[0])))
    if P[1] == 0: continue
    n, d = mm.numerator, mm.denominator
    U = 4*(5*n*n - 5*n*d - d*d); W = 5*n*n + d*d
    U = abs(U); g = math.gcd(U, W); U //= g; W //= g
    if (U, W) in seen: continue
    seen.add((U, W))
    fam = family(U, W)
    if fam is None: print(f"m={mm} (U,W)=({U},{W}) degenerate"); continue
    a, de = fam
    fail, Ds = lines_reached(a, de)
    print(f"m={mm} (U,W)=({U},{W}) a={a} delta={de} local_ok={local_ok(a,de)} first_failing_line={fail} confined={Ds}")
