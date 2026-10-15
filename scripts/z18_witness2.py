"""z18: witness symbol at mu = 0.  For a family with witness polynomial f(Y) on n = c0*Y^D + k (Y = 2^{s/D}),
Theorem A's computation gives (f(Y)/n(Y)) = W(f) := prod_{v | 2} (f(theta), theta(theta-1))_v  for Y near mu = 0,
so a Type I/II family can pass through mu = 0 only if W(f) = -1.  Also prints the decomposition by the product formula:
odd places above c0*k, and the remaining odd places (primes of Res(f, phi)).
usage: z18_witness2.py c0 k D 'f(Y)'"""
import sys, cypari2
pari = cypari2.Pari(); pari.allocatemem(4*10**8, silent=True)
c0, k, D = map(int, sys.argv[1:4]); fY = sys.argv[4]
phi = pari(f'{c0}*x^{D}+{k}')
tot = {'2': 1, 'c0k': 1, 'other': 1, 'inf': 1}
for g in pari.factor(phi)[0]:
    a = pari.pollead(g); e = pari.poldegree(g)
    gm = pari(f'subst({g}, x, x/({a}))*({a})^({e}-1)')
    nf = pari.nfinit(gm)
    th = pari(f'Mod(x/({a}), {gm})')
    al = pari.subst(pari(fY.replace('Y', 'yy')), 'yy', th)
    be = th*(th-1)
    al = pari.lift(al); be = pari.lift(be)
    N = pari.abs(pari.idealnorm(nf, al)); Nb = pari.abs(pari.idealnorm(nf, be))
    ps = set(int(p) for p in pari.factor(pari.numerator(N)*pari.denominator(N)*pari.numerator(Nb)*pari.denominator(Nb)*2)[0])
    for p in ps:
        for pr in pari.idealprimedec(nf, p):
            h = pari.nfhilbert(nf, al, be, pr)
            key = '2' if p == 2 else ('c0k' if (c0*k) % p == 0 else 'other')
            tot[key] *= int(h)
print('W(f) [places above 2] =', tot['2'], '| odd above c0k:', tot['c0k'], '| other odd:', tot['other'])
