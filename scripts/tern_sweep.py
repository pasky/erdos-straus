"""O124 step 1: sweep ET's Type I / Type II varieties for quadratic substructures.

Total space T^I = {(n,a,b,c,d,e,f)}: 4abd = ne+1, ce = a+b, 4acd = n+f, ef = 4a^2 d+1 (ET (2.1),(2.2),(2.6),(2.7)),
T^II: 4abd = n+e, ce = a+b, 4acd = f+1, ef = n+4a^2 d (ET (2.13),(2.14),(2.18),(2.19)). Both are 4-dimensional.
For each 4-subset V of {a..f}, eliminate the other two coordinates and test whether n is a rational function of V
(the eliminant is linear in n). If n = P(V) is a POLYNOMIAL, for every way of fixing 0, 1 or 2 coordinates of V
(as symbolic parameters) check whether n is a quadratic polynomial in the free ones; if so report the quadratic part,
its rank and whether it is isotropic over Q(params) (binary: -disc a square; ternary/quaternary: reported).
"""
import itertools, sympy as sp

n,a,b,c,d,e,f = sp.symbols('n a b c d e f', positive=True)
C = [a,b,c,d,e,f]
SYS = {
 'I':  [4*a*b*d-n*e-1, c*e-a-b, 4*a*c*d-n-f, e*f-4*a**2*d-1],
 'II': [4*a*b*d-n-e,   c*e-a-b, 4*a*c*d-f-1, e*f-n-4*a**2*d],
}

def n_as_function(eqs, V):
    others = [x for x in C if x not in V]
    G = sp.groebner(eqs, *others, n, *V, order='lex')
    rel = [g for g in G.exprs if not (set(g.free_symbols) & set(others)) and g.has(n)]
    sols = []
    for g in rel:
        P = sp.Poly(g, n)
        if P.degree() == 1:
            sols.append(sp.factor(-P.coeff_monomial(1)/P.coeff_monomial(n)))
    return sols, rel

def quad_report(expr, free, params):
    P = sp.Poly(sp.expand(expr), *free)  # coefficients may involve fixed params
    if P.total_degree() != 2:
        return None
    Hs = sp.Matrix(len(free), len(free), lambda i,j: sp.diff(expr, free[i], free[j]))
    rank = Hs.rank()
    out = {'quad_part': sp.factor(sum(t for t in sp.Add.make_args(sp.expand(expr))
                        if sp.Poly(t, *free).total_degree() == 2)), 'rank': rank}
    if len(free) == 2:
        disc = sp.factor(Hs[0,1]**2 - Hs[0,0]*Hs[1,1])   # = B^2-4AC for A x^2+Bxy+Cy^2
        out['disc'] = disc
        rt = sp.sqrt(disc)   # symbols are positive, so sqrt of a square rational function simplifies
        out['isotropic'] = bool(rt.is_rational_function(*params)) if disc != 0 else True
    else:
        out['det'] = sp.factor(Hs.det())
    # trivially isotropic: some free coordinate vector is a zero of the quadratic part
    out['coord_isotropic'] = [str(x) for i,x in enumerate(free) if Hs[i,i] == 0]
    return out

for typ, eqs in SYS.items():
    print(f'===== Type {typ}')
    for V in itertools.combinations(C, 4):
        sols, rel = n_as_function(eqs, list(V))
        if not sols:
            print(V, ': n not a rational function of V'); continue
        for s in sols:
            num, den = sp.fraction(sp.together(s))
            print(V, ': n =', s)
            for r in (0, 1, 2):
                for fixed in itertools.combinations(V, r):
                    free = [x for x in V if x not in fixed]
                    if den.free_symbols & set(free):
                        continue   # n not polynomial in the free coordinates
                    q = quad_report(s, free, list(fixed))
                    if q: print('    fix', fixed, '->', q)
