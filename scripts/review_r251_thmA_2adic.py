from cypari import pari
# A = Q[y]/(y^4+27), y = 3*eta, eta = 2*theta, 48 theta^4 + 1 = 0.  X* - theta at 2 is -theta, at odd primes 1/2 - theta.
# Theorem A + Theorem B predict: theta/(theta - 1/2) ~ eta(eta-1) ~ y(y-3) is NOT a square in A (x) Q_2.
pari('nf=nfinit(y^4+27)')
print('primes over 2 in K:', [(int(P[2]), int(P[3])) for P in pari('idealprimedec(nf,2)')])
for name, beta in [('y(y-3) [should be NON-square at 2]', 'y*(y-3)'), ('sanity -1', '-1'), ('sanity 17 (square in Q2)', '17'),
                   ('sanity 3', '3'), ('y', 'y'), ('y-3', 'y-3')]:
    try:
        L = pari('rnfequation(nf, x^2 - (%s))' % beta)
    except Exception as e:
        print(name, 'global square?', e); continue
    dec = pari('idealprimedec(nfinit(polredbest(%s)),2)' % L)
    print(name, ' K(sqrt beta) primes over 2 (e,f):', [(int(P[2]), int(P[3])) for P in dec], ' => local square' if len(dec) == 2 else ' => non-square')
