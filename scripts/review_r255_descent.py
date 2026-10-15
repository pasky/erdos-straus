"""R255 from-scratch check of MENU_LADDER Computation 1.2.
beta = theta(theta-1) in A = Q[Y]/(c0 Y^D + k).  beta is a square in K_p (p | 2) iff p splits in K(sqrt beta)/K
(or beta is a global square).  Method: rnfidealprimedec on K(sqrt(beta)) -- independent of nfislocalpower.
Also an elementary third method: Hensel criterion u unit is a square in K_p iff u = s^2 mod p^(2e+1), checked by
enumerating residues via nfmodpr when the residue ring is small (N(p)^(2e+1) <= LIM).
usage: review_r255_descent.py c0 k Dmax"""
import sys, cypari2
pari = cypari2.Pari(); pari.allocatemem(4 * 10**8, silent=True)
c0, k, Dmax = map(int, sys.argv[1:4])
assert (k - 1) % 8 == 0 and c0 + k > 0 and bin(c0 + k).count('1') == 1 and (c0 + k).bit_length() % 2 == 1
for D in range(1, Dmax + 1):
    fac = pari(f'factor({c0}*y^{D}+{k})')[0]
    out = []
    for g in fac:
        dg = int(pari.poldegree(g))
        if dg == 1:
            th = -pari.polcoef(g, 0) / pari.polcoef(g, 1)
            b = th * (th - 1)
            sq = bool(pari(f'issquare({b} + O(2^80))'))
            out.append(f'Q:{"sq" if sq else "NS"}')
            continue
        a = pari.pollead(g)
        gm = pari(f'subst({g}, y, y/({a}))*({a})^({dg}-1)')  # monic in eta = a*theta
        K = pari.nfinit(gm)
        beta = pari(f'Mod(y*(y-({a})), {gm})')  # = a^2 * theta(theta-1): same square class, integral
        globsq = len(pari.nffactor(K, pari(f'x^2 - lift({beta})'))[0]) == 2
        pats = []
        for pr in pari.idealprimedec(K, 2):
            if globsq:
                pats.append('sq'); continue
            rnf = pari.rnfinit(K, pari(f'x^2 - lift({beta})'))
            dec = pari.rnfidealprimedec(rnf, pr)
            pats.append('sq' if len(dec) == 2 else 'NS')
        out.append(f'deg{dg}:' + ','.join(pats))
    print(D, ' | '.join(out), '=> some NS' if any('NS' in s for s in out) else '=> ALL SQUARE (descent-sterile!)', flush=True)
