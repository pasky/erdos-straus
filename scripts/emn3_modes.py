"""EXCEPTIONAL_MN3 §3: enumerate 'single-progression' parametrisations of the Type I variety.
Variety (all n): (a,c,d,n) free, b=(na+c)/f, e=(4a^2d+1)/f, f=4acd-n  (ET (2.1)-(2.9)).
For each set S of 3 fixed coordinates among a..f and a free coordinate v (not in S), eliminate the
other coordinates and test whether the relation G(n,v)=0 on the curve {S fixed} makes n an affine
function of v (G of degree 1 in n and in v, with no n*v term). Prints the affine cases with n(v)."""
import itertools, sympy as sp
a,b,c,d,e,f,n = sp.symbols('a b c d e f n')
X = dict(a=a,b=b,c=c,d=d,e=e,f=f)
eqs = [4*a*b*d-n*e-1, c*e-a-b, 4*a*c*d-n-f, e*f-4*a**2*d-1, b*f-n*a-c]
names = 'abcdef'
fixed_syms = {k: sp.Symbol(k+'0') for k in names}
for S in itertools.combinations(names, 3):
    for v in names:
        if v in S: continue
        sub = {X[k]: fixed_syms[k] for k in S}
        E = [sp.expand(q.subs(sub)) for q in eqs]
        others = [X[k] for k in names if k not in S and k != v]
        G = sp.groebner(E, *others, n, X[v], order='lex')
        rel = [g for g in G.exprs if not (g.free_symbols & set(others))]
        if not rel: continue
        g = rel[0]
        P = sp.Poly(g, n, X[v])
        if P.degree(n) == 1 and P.degree(X[v]) <= 1 and P.coeff_monomial(n*X[v]) == 0 and P.degree(X[v]) == 1:
            sol = sp.solve(g, n)[0]
            print(f"fix {S}, free {v}: n = {sp.factor(sol)}")
