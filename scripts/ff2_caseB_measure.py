"""ff2_caseB_measure.py (O166): mass of the T-adic cylinder C = {u = 1 + cT + dT^2 mod T^3} (slice x = 1 off T,
q = 3, A = T^2) covered by Case B families with deg L' <= LMAX, j <= JMAX.  A family (L', j, g = T^gam g', E) with
E | D = 1 + T^(N+1+gam) L' g', E = E' = -1 mod L', E, E' monic, covers u = -E mod T^(N+1), N = j+1.
Prints, per deg L', the summed mass and the union mass (relative to C).  usage: p c d LMAX JMAX"""
import sys, itertools
sys.path.insert(0, 'scripts')
from ff2_polyq import *
from sympy import Poly, symbols
T = symbols('T')
p, c, d, LMAX, JMAX = map(int, sys.argv[1:6]); k = 2
def topoly(a): return Poly(list(reversed(a)), T, modulus=p)
def frompoly(P):
    a = trim([int(x) % p for x in reversed(P.all_coeffs())]); inv = pow(a[-1], p - 2, p); return [x * inv % p for x in a]
def mdivs(f):
    divs = [[1]]
    for g, e in topoly(f).factor_list()[1]:
        g = frompoly(g); new = []
        for dd in divs:
            x = dd; new.append(x)
            for _ in range(e): x = mul(x, g, p); new.append(x)
        divs = new
    return divs
cyl = set(); summ = 0.0
for l in range(0, LMAX + 1):
    for t in itertools.product(range(p), repeat=l):
        Lp = list(t) + [1]
        if Lp[0] == 0: continue
        dl = mdivs(Lp)
        for j in range(0, JMAX + 1):
            N = k + j - 1
            for gam in range(0, j + 1):
                for gp in dl:
                    D = add([1], mul([0] * (N + 1 + gam) + [1], mul(Lp, gp, p), p), p)
                    for E in mdivs(D):
                        cof, r = divmod_(D, E, p)
                        if r or cof[-1] != 1: continue
                        if Lp != [1] and (mod(add(E, [1], p), Lp, p) or mod(add(cof, [1], p), Lp, p)): continue
                        u = (mod(neg(E, p), [0] * (N + 1) + [1], p) + [0] * (N + 2))[:N + 1]
                        if u[:3] != [1, c % p, d % p]: continue
                        cyl.add(tuple(u)); summ += float(p) ** (3 - (N + 1))
    # union mass: cylinders u mod T^(N+1); compute exactly by refining to max length
    M = max([len(x) for x in cyl], default=3)
    covered = set()
    def mass(cyls):
        cs = sorted(cyls, key=len); kept = []
        for x in cs:
            if not any(x[:len(y)] == y for y in kept): kept.append(x)
        return sum(float(p) ** (3 - len(x)) for x in kept)
    print("deg L' <=", l, "families-mass-sum %.5f" % summ, "union-mass %.5f" % mass(cyl), "#cyl", len(cyl), flush=True)
