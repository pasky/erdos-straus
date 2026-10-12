"""O141: symbolic checks of the identities used in BRAINSTORM/logic_weak_arithmetic.md.
(i) root construction: n = m*q, m = s/s0 - 1, x=y=n*s/(2 s0), z=q*s/(4 s0).
(ii) scaling: 4/n0 = 1/a+1/b+1/c  =>  x = a n/n0 etc.
(iii) signed identity for n = 1 mod 4: x=y=n(1-n)/2, z=(n-1)/4.
(iv) concrete instance: n = 1 + t^4 written in s, signed solution with constant terms 0 via factor q1.
"""
import sympy as sp
s, s0, q, n, n0, a, b, c = sp.symbols('s s0 q n n0 a b c', positive=True)
m = s/s0 - 1
N = m*q
x = N*s/(2*s0); z = q*s/(4*s0)
print('(i)', sp.simplify(2/x + 1/z - 4/N) == 0, ' x(0)=', sp.simplify(x.subs(s, 0)), ' z(0)=', z.subs(s, 0))
# (ii)
expr = n0/(a*n) + n0/(b*n) + n0/(c*n) - 4/n
print('(ii)', sp.simplify(expr.subs(1/a + 1/b + 1/c, 4/n0)) == 0 or sp.simplify(expr.subs(c, 1/(4/n0 - 1/a - 1/b))) == 0)
# (iii)
X = n*(1 - n)/2; Z = (n - 1)/4
print('(iii)', sp.simplify(2/X + 1/Z - 4/n) == 0)
# (iv) n = s^4 + 1, q1 = s^2 + sqrt2 s + 1, w = -2 q1
nn = s**4 + 1; q1 = s**2 + sp.sqrt(2)*s + 1; q2 = s**2 - sp.sqrt(2)*s + 1
assert sp.expand(q1*q2 - nn) == 0
w = -2*q1; X = sp.expand(nn*(w + 2)/4); Z = sp.expand((-q2/2)*(w + 2)/4)  # nn/w = -q2/2
print('(iv) q2 =', q2, ' identity:', sp.simplify(2/X + 1/Z - 4/nn) == 0,
      ' X(0),Z(0)=', X.subs(s, 0), Z.subs(s, 0), ' lc signs:', sp.Poly(X, s).LC(), sp.Poly(Z, s).LC())
