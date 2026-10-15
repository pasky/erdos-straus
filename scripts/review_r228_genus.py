"""R228 from-scratch recheck of NEAR_SQUARE_EXIST §3 (pointwise u-genus flagging) on a subrange.
Admissible F at level u: Q(sqrt(-D)), D squarefree with every odd prime dividing u and F inside Sigma_u decided by the
DIRECT character criterion (review_r228_signfield.F_in_Sigma), not by the Cor 2.3 table.
Per prime: p Nw Nm Ncl Nfl_beyond_clean Nflm  (same conventions as the paper: words with u <= v, multiplicity 2 if u != v).
"""
import sys
from math import isqrt
argv = sys.argv[1:]
sys.argv = ['x', '1', '1', '1', '1']
src = open(__file__.replace('review_r228_genus.py', 'review_r228_signfield.py')).read().rsplit('\nmain()', 1)[0]
exec(src)
from sympy import factorint, primerange, divisors, legendre_symbol
LO, HI = int(argv[0]), int(argv[1])
STEP = int(argv[2]) if len(argv) > 2 else 1

def F_in_Sigma_fast(D, u):
    # D | 2*rad(u): Q(sqrt(-D)) and Sigma_u both inside Q(zeta_{8u}); Gal(Q(zeta_8u)/Sigma_u) = {c = 1+u*j mod 8u : (-u/c) = 1}
    L = 8 * u
    for j in range(8):
        c = 1 + u * j
        if c % 2 == 0 or gcd(c, L) != 1:
            continue
        if (1 if c == 1 else jacobi_symbol((-u) % c, c)) != 1:
            continue
        if kron(-D, c) != 1:
            return False
    return True

for _u in range(1, 60):
    for _D in range(1, 2 * _u + 1):
        if (2 * _u) % _D == 0 and sqfree(_D) == _D:
            assert F_in_Sigma_fast(_D, _u) == F_in_Sigma(_D, _u), (_D, _u)

def admissible_D(u):
    qs = [q for q in factorint(u) if q % 2]
    out = []
    for mask in range(1 << len(qs)):
        D = 1
        for i, q in enumerate(qs):
            if mask >> i & 1:
                D *= q
        for D2 in (D, 2 * D):
            if F_in_Sigma_fast(D2, u):
                out.append(D2)
    return out

def genus(p, u):
    rs = [r for r in factorint(p + u) if r % 2]
    for D in admissible_D(u):
        if all(legendre_symbol((-D) % r, r) == 1 if (-D) % r else False for r in rs):
            return True
    return False

def leg(a, p):
    return legendre_symbol(a % p, p)

tot = [0] * 5
ps = [p for p in primerange(LO, HI) if p % 4 == 1][::STEP]
for p in ps:
    Nw = Nm = Ncl = Nfl = Nflm = 0
    u = 1
    while (u - 2) * u <= p:
        N = p + u
        gu = None
        for A in divisors(N):
            if (A + 1) % u:
                continue
            t = (A + 1) // u
            v = N // A
            if v < u:
                continue
            As = t * v - 1
            c = leg(A, p)
            mult = 1 if u == v else 2
            Nw += mult
            Nm += mult * (c == -1)
            iscl = all(leg(r, p) == 1 for r in factorint(t * p + 1))
            Ncl += mult * iscl
            fl = False
            if A % 2:
                gu = genus(p, u) if gu is None else gu
                fl = gu
            if not fl and As % 2:
                fl = genus(p, v)
            if fl:
                Nfl += mult * (not iscl)
                Nflm += mult * (c == -1)
        u += 1
    print(p, Nw, Nm, Ncl, Nfl, Nflm)
    for i, x in enumerate((Nw, Nm, Ncl, Nfl, Nflm)):
        tot[i] += x
print("TOTAL primes", len(ps), "Nw Nm Ncl Nfl_beyond Nflm =", tot, file=sys.stderr)
