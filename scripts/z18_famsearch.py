"""z18: search Type I/II families polynomial in Y = 2^{(s-j)/D} for n = c0*2^j*Y^D + k at the unit-square point mu=0
(s -> 0 in Zhat: Y -> 1 at odd places, Y -> 0 at 2).  Parameters c = cc*Y^al, d = dd*Y^be (monomials).
Type I : f f' = n^2 + 4c^2 d, A = (f+n)/(4cd), B = (f'+n)/(4cd);  x = A B d n, y = A c d, z = B c d.
Type II: f f' = 4c^2 d n + 1, A = (f+1)/(4cd), B = (f'+1)/(4cd); x = A B d, y = A c d n, z = B c d n.
Report every (type, D, j, c, d, f) for which P factors over Q, and whether A, B are integer-valued on a class containing mu=0
(polynomial divisibility by Y^{al+be}; constant denominators checked at Y=1 (odd primes) and Y=0 (2)), and positivity.
usage: z18_famsearch.py c0 k Dmax ccmax ddmax almax bemax"""
import sys, itertools, cypari2
pari = cypari2.Pari(); pari.allocatemem(4*10**8, silent=True)
c0, k, Dmax, ccmax, ddmax, almax, bemax = map(int, sys.argv[1:8])
Y = pari('Y')
def vden(q, p):  # p-adic valuation of rational q
    return pari.valuation(q, p) if q != 0 else 10**9
def ok_int(poly, Ypow):
    """poly in Q[Y]: integer-valued near mu=0 after dividing by Y^Ypow?"""
    # polynomial divisibility by Y^Ypow
    for i in range(Ypow):
        if pari.polcoef(poly, i, 'Y') != 0: return False
    q = pari(f'({poly})/Y^{Ypow}')
    v1, v0 = pari.subst(q, 'Y', 1), pari.subst(q, 'Y', 0)
    den1 = pari.denominator(v1); den0 = pari.denominator(v0)
    # odd denominators must vanish at Y=1, 2-power denominators at Y=0; coefficient denominators:
    cd = pari.denominator(pari.content(q)) if q != 0 else 1
    for p, e in zip(*[list(r) for r in pari.factor(cd)]) if cd != 1 else []:
        if p == 2:
            if vden(v0, 2) < 0: return False
        else:
            if vden(v1, p) < 0: return False
    return True
hits = 0
for D in range(1, Dmax+1):
  for j in (0,):   # R-O245: j = ±D would need the odd specialisation Y -> 2^{-j/D}, not 1 (bug fixed: only j = 0)
    n = pari(f'{c0}*2^({j})*Y^{D}+{k}')
    for cc, dd, al, be in itertools.product(range(1, ccmax+1), range(1, ddmax+1), range(almax+1), range(bemax+1)):
        c = pari(f'{cc}*Y^{al}'); d = pari(f'{dd}*Y^{be}')
        for typ in ('I', 'II'):
            P = n**2 + 4*c**2*d if typ == 'I' else 4*c**2*d*n + 1
            F = pari.factor(P); gs = list(F[0]); ms = [int(m) for m in F[1]]
            if sum(ms) == 1: continue
            lc = pari.content(P)
            base = [pari(g)/pari.content(g) for g in gs]
            for es in itertools.product(*[range(m+1) for m in ms]):
                if sum(es) == 0 or es == tuple(ms): continue
                g = pari(1)
                for b_, e_ in zip(base, es): g = g*b_**e_
                gp = pari(P)/g
                # kappa: try divisors of the values (rational scalings) -- scan kappa = u/v with small u, v
                for u in (1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 16, 20, 30, 60):
                  for v in (1, 2, 3, 4, 5, 15):
                    for sgn in (1, -1):
                        f = sgn*g*u/v; fp = P/f
                        t = n if typ == 'I' else pari(1)
                        A = f + t; B = fp + t
                        if pari.poldegree(A) < 0 or pari.poldegree(B) < 0: continue
                        if pari.pollead(A) <= 0 or pari.pollead(B) <= 0: continue
                        A4 = A/(4*cc*dd); B4 = B/(4*cc*dd)
                        if ok_int(A4, al+be) and ok_int(B4, al+be) and ok_int(f, 0) and ok_int(fp, 0):
                            hits += 1
                            print(f'HIT {typ} D={D} j={j} c={c} d={d} f={f} fp={fp}', flush=True)
print('hits', hits)
