"""z18: CRT search for Type I / Type II polynomial families at the unit-square point mu = 0 of n = c0*Y^D + k,
Y = 2^{s/D} (mu = 0: Y -> 1 at odd places, Y -> 0 at 2).  Every polynomial Type II family is
   n + m = 4abd,  m | a + b  (c = (a+b)/m),          x = abd, y = acdn, z = bcdn      (witness f = 4acd - 1)
and every Type I family is
   n e + 1 = 4abd, e | a + b  (c = (a+b)/e),          x = abdn, y = acd, z = bcd.
Given primitive integer polys a1, b1 (a = lam*a1, b = lam*r*b1) the residue m = -n mod a1 b1 (resp. e = -1/n mod a1 b1)
is forced; we need it to divide a + b.  Integrality near mu = 0 of the polynomials a, b, c, d in Q[Y] is: value at Y = 1
odd-integral, value at Y = 0 2-integral (both exact, PROVED in MENU_LADDER §2).  Positivity: leading coefficients > 0.
usage: z18_crt.py c0 k D degA degB coefrange [rlist]"""
import sys, itertools, math
from fractions import Fraction as Fr
import cypari2
pari = cypari2.Pari(); pari.allocatemem(4*10**8, silent=True)

def val(q, p):
    q = Fr(q)
    if q == 0: return math.inf
    v = 0; a, b = q.numerator, q.denominator
    while a % p == 0: a //= p; v += 1
    while b % p == 0: b //= p; v -= 1
    return v

def primes_of(qs):
    s = set()
    for q in qs:
        q = Fr(q)
        if q == 0: continue
        for x in (q.numerator, q.denominator):
            x = abs(x)
            for p in pari.factor(x)[0] if x > 1 else []:
                s.add(int(p))
    return s

def fr(x): return Fr(str(x))

def polys(deg, R):
    """primitive integer polys of exact degree deg, positive leading coefficient, coefficients in [-R, R]"""
    for co in itertools.product(range(-R, R+1), repeat=deg):
        for lc in range(1, R+1):
            cs = list(co) + [lc]   # low to high
            if deg > 0 and math.gcd(*cs) != 1: continue
            if deg == 0 and lc != 1: continue
            yield pari.Pol(list(reversed(cs)), 'Y')

def check(typ, n, a1, b1, Rres, r):
    """return lam (Fraction) making a,b,c,d integral & positive near mu=0, or None"""
    g = a1 + r*b1
    if g == 0: return None
    cq = pari.divrem(g, Rres)
    if cq[1] != 0: return None
    c1 = cq[0]
    num = n + Rres if typ == 'II' else n*Rres + 1
    d1 = pari.divrem(num, 4*r*a1*b1)
    if d1[1] != 0: return None
    d1 = d1[0]
    if pari.poldegree(d1) < 0 or pari.poldegree(c1) < 0: return None
    # positivity: lam*lc(a1) > 0 -> lam > 0 (lc(a1) > 0); r*lc(b1) > 0 -> r > 0; lc(c1) > 0; lc(d1)/r > 0
    if fr(pari.pollead(c1)) <= 0 or fr(pari.pollead(d1)) <= 0 or r <= 0: return None
    if fr(pari.pollead(Rres)) <= 0: return None
    vals = {}
    for nm, P in (('a', a1), ('b', r*b1), ('c', c1), ('d', d1)):
        vals[nm] = (fr(pari.subst(P, 'Y', 1)), fr(pari.subst(P, 'Y', 0)))
    lam = Fr(1)
    for p in primes_of([v for pr in vals.values() for v in pr]) | {2}:
        k = 1 if p == 2 else 0
        lo = max(-val(vals[x][k], p) for x in 'abc')
        vd = val(vals['d'][k], p)
        hi = math.floor(vd/2) if vd < math.inf else math.inf
        if lo > hi: return None
        L = lo if lo > -math.inf else (min(0, hi) if hi < math.inf else 0)
        lam *= Fr(p)**int(L)
    return lam

def main():
    c0, k, D, dA, dB, R = map(int, sys.argv[1:7])
    rlist = [Fr(x) for x in sys.argv[7].split(',')] if len(sys.argv) > 7 else [Fr(1)]
    n = pari(f'{c0}*Y^{D}+{k}')
    hits = 0; tried = 0
    for a1 in polys(dA, R):
        for b1 in polys(dB, R):
            if dA == dB and str(a1) > str(b1): continue
            ab = a1*b1
            if pari.poldegree(ab) > D: continue
            if pari.gcd(ab, n) != 1: continue
            for typ in ('II', 'I'):
                tried += 1
                if typ == 'II':
                    Rres = -pari.lift(pari.Mod(n, ab))
                else:
                    Rres = pari.lift(-1/pari.Mod(n, ab))
                if Rres == 0: continue
                Rres = pari(Rres)
                if pari.poldegree(Rres) > max(dA, dB): continue
                rs = rlist
                if pari.poldegree(Rres) >= 1:
                    # forced ratio: (a1 mod R) + r (b1 mod R) == 0
                    am, bm = pari.lift(pari.Mod(a1, Rres)), pari.lift(pari.Mod(b1, Rres))
                    if bm == 0: continue
                    q = -am/bm
                    if str(pari.type(q)) in ('t_RFRAC', 't_POL') and (str(pari.type(q)) == 't_RFRAC' or pari.poldegree(q) > 0): continue
                    rs = [fr(q)]
                for r in rs:
                    if r <= 0: continue
                    lam = check(typ, n, a1, b1, Rres, r)
                    if lam is not None:
                        hits += 1
                        print(f'HIT {typ} a1={a1} b1={b1} r={r} lam={lam} R={Rres}', flush=True)
    print('tried', tried, 'hits', hits)

if __name__ == '__main__':
    main()
