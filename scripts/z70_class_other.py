# z70 CLASS §1.6b (pre-registered): unexplained overlaps at the translation-prime classes vs the in-sample chance rate.
# A pair (g, g') of good classes is EXPLAINED if natural representatives R of g, R' of g' (R_A, R_B, R_E of z70_class_repid)
# divide one another as ideals.  O_u(t) = #unexplained ordered pairs with g' - g = t.  Controls: all t of order > 2 in the
# principal genus except +-t_1, +-t_2, +-t_3;  lambda = mean O_u over the controls.  U1 = O_u(t_1) vs lambda,
# U3 = sum_i O_u(t_i) vs 3 lambda; Poisson z = sum(obs - exp)/sqrt(sum exp).
# Z70_SMALLCTL=1 (post hoc, after the registered run): controls = classes of the next 20 split primes with class in the
#   principal genus (norm-matched small translations) instead of all translations.
# Usage: python scripts/z70_class_other.py d range P0 P1 [mod res] | list n1 ...
import sys, math, os
SMALLCTL = os.environ.get('Z70_SMALLCTL') == '1'
sys.path.insert(0, 'scripts')
from collections import Counter
from sympy import primerange
from z69_twist_i17 import reduce
from z70_class_core import Fact, ClassData, solutions
from z70_class_null import translations
from z70_class_repid import vec_of

def divides(I, J):
    # registered definition (§1.6b): the D_d-parts must be EQUAL (review fix: earlier version allowed a rep without D to
    # divide one with D)
    if ('D' in I) != ('D' in J): return False
    return all((q in J) and (J[q] * k > 0) and abs(J[q]) >= abs(k) for q, k in I.items())

def analyse(n, d, F):
    sols = solutions(n, d, F)
    if not sols: return None
    if any(math.gcd(x, d*n) > 1 for (a, b, c, e) in sols for x in (e, 4*a*c*d - 1, 4*b*c*d - 1)): return 'gcd'
    C = ClassData(n, d); G = C.G
    reps = {}
    for (a, b, c, e) in sols:
        A = 4*a*c*d - 1; B = 4*b*c*d - 1
        g = G.coords[reduce(A, 4*a*d, d*e)]
        reps.setdefault(g, []).extend([vec_of(C, F, A, 2*a*d), vec_of(C, F, B, 2*b*d, conj=True),
                                       vec_of(C, F, e, 2*a*d, conj=True, D=(d > 1))])
    X = list(reps)
    if len(X) < 2: return None
    tl, tlp = translations(C)
    Ou = Counter(); nexp = 0
    for g in X:
        for g2 in X:
            if g2 == g: continue
            if any(divides(R, R2) or divides(R2, R) for R in reps[g] for R2 in reps[g2]): nexp += 1; continue
            Ou[G.add(g2, G.negd[g])] += 1
    H = set(G.add(u, u) for u in G.coords.values())
    excl = set(tl) | set(G.negd[t] for t in tl)
    Tc = [t for t in H if G.add(t, t) != G.one and t not in excl]
    if not Tc or not tl: return None
    if SMALLCTL:   # post hoc (after the registered run): norm-matched controls = classes of the next 20 split primes l
        from sympy import isprime, jacobi_symbol   # with class in the principal genus, of order > 2, not +-t_i
        D = C.D; Tc = []; l = max(tlp) + 2
        while len(Tc) < 20 and l < 10**5:
            if isprime(l) and D % l != 0 and jacobi_symbol(D % l, l) == 1:
                r = next(x for x in range(l) if (x*x - D//4) % l == 0)
                u = G.coords[reduce(l, 2*r, (r*r - D//4)//l)]
                if u in H and G.add(u, u) != G.one and u not in excl and u not in Tc and G.negd[u] not in Tc: Tc.append(u)
            l += 2
    lam = sum(Ou[t] for t in Tc) / len(Tc)
    return dict(U1=Ou[tl[0]], U3=sum(Ou[t] for t in tl), lam=lam, nt=len(tl), k=len(X), nexp=nexp, npairs=len(X)*(len(X)-1))

if __name__ == "__main__":
    d = int(sys.argv[1]); spec = sys.argv[2:]
    if spec[0] == 'range':
        mod, res = (int(spec[3]), int(spec[4])) if len(spec) > 4 else (8, 1)
        nl = [p for p in primerange(int(spec[1]), int(spec[2])) if p % mod == res]
    else: nl = sorted(set(int(x) for x in spec[1:]))
    F = Fact(max(nl)//3 + 10)
    t = Counter(); m = 0; sk = 0
    for n in nl:
        o = analyse(n, d, F)
        if o == 'gcd': sk += 1; continue
        if not o: continue
        m += 1
        t['U1'] += o['U1']; t['E1'] += o['lam']; t['U3'] += o['U3']; t['E3'] += o['nt']*o['lam']
        t['k'] += o['k']; t['nexp'] += o['nexp']; t['npairs'] += o['npairs']
    z1 = (t['U1'] - t['E1'])/math.sqrt(t['E1']) if t['E1'] > 0 else float('nan')
    z3 = (t['U3'] - t['E3'])/math.sqrt(t['E3']) if t['E3'] > 0 else float('nan')
    print(f"# other{'(SMALLCTL)' if SMALLCTL else ''} d={d} {' '.join(spec[:3])}: n analysed {m} (gcd-skipped {sk}); classes {t['k']}; ordered pairs {t['npairs']}, explained {t['nexp']}; "
          f"U1 {t['U1']} vs {t['E1']:.1f} (z {z1:+.2f}); U3 {t['U3']} vs {t['E3']:.1f} (z {z3:+.2f}); "
          f"U1sum_obs_exp {t['U1']} {t['E1']:.3f} U3sum_obs_exp {t['U3']} {t['E3']:.3f}")
