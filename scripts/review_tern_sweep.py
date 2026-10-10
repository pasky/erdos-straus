"""R124 from-scratch re-derivation of POINTWISE_TERNARY Comp 6.1 (not reusing scripts/tern_sweep.py).

Independent setup: the total spaces T^I, T^II are written as graphs of ET's rational parametrisations by (a,b,c,d)
(ET p.11 / Prop 2.6 proof):
  Type I : 4abcd = n(a+b) + c, e = (a+b)/c, f = 4acd - n
  Type II: 4abcd = a+b+nc,     e = (a+b)/c, f = 4acd - 1
ideal = (generators) saturated by (a+b)*c*(all coords) via an auxiliary variable t.
For each 4-subset V of {a..f}: eliminate the rest and look for an eliminant linear in n with a leading coefficient
not vanishing on T. Then for each set F (|F| = 0,1,2) of fixed coordinates in V, test whether n is a polynomial of
total degree <= 2 in the free coordinates over Q(F); report quadratic part, rank, isotropy over Q(F).
Also sanity-check every eliminant numerically on random points of T.
"""
import itertools, random, sympy as sp

a, b, c, d, e, f, n, t = sp.symbols('a b c d e f n t')
C = [a, b, c, d, e, f]

def gens(typ):
    if typ == 'I':
        return [4*a*b*c*d - n*(a+b) - c, c*e - (a+b), f - 4*a*c*d + n]
    return [4*a*b*c*d - (a+b) - n*c, c*e - (a+b), f - 4*a*c*d + 1]

def point(typ):
    A, B, Cc, D = [sp.Rational(random.randint(1, 50), random.randint(1, 7)) for _ in range(4)]
    E = (A+B)/Cc
    N = Cc*(4*A*B*D-1)/(A+B) if typ == 'I' else (4*A*B*Cc*D-A-B)/Cc
    F = 4*A*Cc*D - N if typ == 'I' else 4*A*Cc*D - 1
    return {a: A, b: B, c: Cc, d: D, e: E, f: F, n: N}

def n_of_V(typ, V):
    others = [x for x in C if x not in V]
    eqs = gens(typ) + [t*c*(a+b)*a*b*d*e*f*n - 1]
    G = sp.groebner(eqs, t, *others, n, *V, order='lex')
    elim = [g for g in G.exprs if not (g.free_symbols & set(others + [t]))]
    rel_V = [g for g in elim if not g.has(n)]
    if rel_V:
        return None, 'V dependent: %s' % rel_V
    for g in elim:
        P = sp.Poly(g, n)
        if P.degree() == 1:
            sol = sp.cancel(-P.coeff_monomial(1)/P.coeff_monomial(n))
            for _ in range(3):  # numerical sanity check on T
                pt = point(typ)
                assert sp.simplify(sol.subs(pt) - pt[n]) == 0
            return sol, None
    return None, 'no eliminant linear in n (degrees %s)' % [sp.Poly(g, n).degree() for g in elim]

def quad(sol, free, fixed):
    num, den = sp.fraction(sp.cancel(sol))
    if den.free_symbols & set(free):
        return None
    P = sp.Poly(sp.expand(num), *free)
    if P.total_degree() != 2:
        return None
    q = sum(co*sp.prod([x**k for x, k in zip(free, mon)]) for mon, co in P.terms() if sum(mon) == 2) / den
    H = sp.hessian(q, free)
    r = H.rank(simplify=True)
    if r < len(free):
        iso = True  # degenerate => isotropic
    elif len(free) == 2:
        # disc = -det(Hessian) must be a square in Q(F): even multiplicities, constant a rational square
        nu, de = sp.fraction(sp.cancel(-H.det()))
        cst, fl = sp.factor_list(sp.expand(nu*de))
        iso = all(m % 2 == 0 for _, m in fl) and cst > 0 and sp.sqrt(cst).is_rational
    else:
        iso = 'check by hand'
    return sp.factor(q), r, iso

if __name__ == '__main__':
    random.seed(1)
    tot = 0; ranks = {}
    for typ in ['I', 'II']:
        print('===== Type', typ)
        for V in itertools.combinations(C, 4):
            sol, why = n_of_V(typ, V)
            if sol is None:
                print(V, ':', why); continue
            print(V, ': n =', sp.factor(sol))
            for k in (0, 1, 2):
                for F in itertools.combinations(V, k):
                    free = [x for x in V if x not in F]
                    res = quad(sol, free, F)
                    if res:
                        tot += 1; ranks[res[1]] = ranks.get(res[1], 0) + 1
                        print('   fix', F, '-> q =', res[0], 'rank', res[1], 'isotropic', res[2])
    print('TOTAL', tot, 'by rank', ranks)
