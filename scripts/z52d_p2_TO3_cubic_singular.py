from sympy import symbols, diff, solve, Poly, factor, groebner
x,y,z,w,p=symbols('x y z w p')
F=4*x*y*z - p*(x*y+y*z+z*x)*w
eqs=[diff(F,v) for v in (x,y,z,w)]+[F]
G=groebner(eqs, x,y,z,w, p, order='lex')
print('groebner basis (lex, p last):')
for g in G.exprs: print('  ',factor(g))
