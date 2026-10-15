"""z18: 2-adic descent test at the unit-square point mu=0 of n = c*Y^d + k (Y = 2^{e s/d}).
Theorem A (MENU_STERILITY) + Chebotarev: mu=0 lies in Ster(phi) iff theta(theta-1) is a square in A (x) Q_2,
A = Q[x]/(c x^d + k).  Prints, per d, the square/non-square pattern over the primes above 2 of each factor.
usage: z18_descent2.py c k dmax"""
import sys, cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**8, silent=True)
c, k, dmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
for d in range(1, dmax+1):
    fac = pari(f'factor({c}*x^{d}+{k})')[0]
    res = []
    for g in fac:
        if pari.poldegree(g) == 1:
            th = -pari.polcoef(g, 0)/pari.polcoef(g, 1)
            a = th*(th-1)
            res.append('Q:' + ('sq' if pari(f'ispower({a},2)') or pari(f'issquare(({a})*1+O(2^60))') else 'NS'))
            continue
        a = pari.pollead(g); e = pari.poldegree(g)
        gm = pari(f'subst({g}, x, x/({a}))*({a})^({e}-1)')   # monic in Z = a*theta
        nf = pari.nfinit(gm)
        out = []
        el = pari(f'Mod((x/({a}))*(x/({a})-1), {gm})')
        for pr in pari.idealprimedec(nf, 2):
            out.append('sq' if pari.nfislocalpower(nf, pr, el, 2) else 'NS')
        res.append(f'deg{pari.poldegree(g)}:' + ','.join(out))
    print(d, ' | '.join(res), flush=True)
