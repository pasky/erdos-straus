from sympy import symbols, discriminant, factor, div, expand, simplify, Poly
T,s,e,n,x=symbols('T s e n x')
f=4*T**2*(T-s)+e*(4*T-n)
D=factor(discriminant(f,T)); print('disc(T) =',D)
# given a root x: e = 4x^2(s-x)/(4x-n); quotient quadratic and its disc
ex=4*x**2*(s-x)/(4*x-n)
q,r=div(Poly(expand(f.subs(e,ex)*(4*x-n)),T),Poly(T-x,T)); print('rem',simplify(r.as_expr()))
print('quadratic disc =',factor(discriminant(q.as_expr(),T)))
