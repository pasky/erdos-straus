# z58 TERNARY: pure-cusp regime screen. For elliptic curves E of conductor supported on {2,3,5,7} (weight-2 newforms
# that are Shimura lifts of weight-3/2 forms of level 4N with N | 2^a 3 5 7), compute for the in-M (★)-zero primes p
# and for control primes in the same classes: root number and analytic rank of the quadratic twist E^(-4p)
# (Waldspurger: the weight-3/2 eigen-coefficient at p has square proportional to L(1/2, E x chi_{-4p})).
# A *valid* single-eigenform proxy of this kind must vanish at the zero primes, i.e. rank(E^(-4p)) >= 1 there.
import cypari2, sys
pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
M = {1, 121, 169, 289, 361, 529}
zeros = [int(x) for x in open('data/z58/screens/star_prime_zeros.txt') if x.strip() and x[0] != '#']
zM = [p for p in zeros if p % 840 in M]
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000000
zM = [p for p in zM if p <= PMAX]
# controls: next 2 primes in the same class mod 840 with R(p) >= 1 (all primes > 8813281 or not in list)
ctrl = []
for p in zM:
    q = p + 840; k = 0
    while k < 2:
        if pari.isprime(q) and q not in zeros: ctrl.append(q); k += 1
        q += 840
curves = [[1,0,1,4,-6],[1,1,1,-10,-10],[0,1,0,4,4],[1,0,0,-4,-1],[0,-1,0,-4,4],[1,0,1,1,2],[0,1,1,9,1],[0,0,0,0,1],[1,1,1,-4,5],[1,-1,0,0,-5],[0,1,0,-4,-4],[0,0,0,1,2],[1,-1,0,9,0],[0,0,0,-1,0],[0,0,0,4,0],[0,0,1,0,-7]]  # Weierstrass models; conductor recomputed below, kept only if supported on {2,3,5,7}
print('# in-M zero primes used:', zM, ' controls:', ctrl)
print('# curve | per prime: p:root_number/analytic_rank   (Z = zero prime, c = control)')
for lab in curves:
    E = pari.ellinit(lab); Nc = int(pari.ellglobalred(E)[0])
    if any(Nc % q == 0 for q in pari.factor(Nc)[0] if int(q) not in (2, 3, 5, 7)) or Nc == 1: continue
    lab = 'N=%d %s' % (Nc, lab)
    row = []
    for tag, P in (('Z', zM), ('c', ctrl)):
        for p in P:
            Et = pari.ellinit(pari.elltwist(E, -4 * p))
            w = int(pari.ellrootno(Et)); r = int(pari.ellanalyticrank(Et)[0])
            row.append('%s%d:%+d/%d' % (tag, p, w, r))
    print(lab, ' '.join(row)); sys.stdout.flush()
