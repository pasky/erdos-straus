# R225: symbolic (sympy) re-derivation of the Thm 2.2 shape analysis, no restriction on roots/coeffs.
# For each degree shape we impose polynomial divisibility identities exactly (Groebner basis over Q(params))
# and print the resulting ideal; reviewer inspects for escaping solutions with k > 0.
import sympy as sp
m, k = sp.symbols('m k')
n = m**2 + k
def report(name, eqs, unknowns):
    eqs = [sp.expand(e) for e in eqs if sp.expand(e) != 0]
    G = sp.groebner(eqs, *unknowns, k, order='lex') if eqs else []
    print('==', name); print('   ', list(G) if eqs else 'no constraints')
def coeffs(expr):
    return sp.Poly(sp.expand(expr), m).all_coeffs()
A, C, L, u, v, la, lc, ld, r, s, q, E, mu, B1, B0 = sp.symbols('A C L u v la lc ld r s q E mu B1 B0')
# ---------- Type I : f = 4acd - n, need f*b = n a + c, f*e = 4a^2 d + 1, c e = a + b (b,e polys)
def typeI(name, a, c, d, bdeg, edeg, params):
    f = sp.expand(4*a*c*d - n)
    bs = sp.symbols('b0:%d' % (bdeg + 1)); es = sp.symbols('e0:%d' % (edeg + 1))
    b = sum(bs[i]*m**i for i in range(bdeg + 1)); e = sum(es[i]*m**i for i in range(edeg + 1))
    eqs = coeffs(f*b - n*a - c) + coeffs(f*e - 4*a**2*d - 1) + coeffs(c*e - a - b)
    report('TypeI ' + name + ' degb=%d dege=%d' % (bdeg, edeg), eqs, list(bs) + list(es) + params)
# (0,0,2): a=A, c=C, d=L(m^2+u m+v). deg f in {0,1,2}; b = (na+c)/f, e=(4a^2d+1)/f
for bd, ed in [(0, 0), (1, 1), (2, 2)]:
    typeI('(0,0,2)', A, C, L*(m**2 + u*m + v), bd, ed, [A, C, L, u, v])
# (1,0,1): a = la(m-r), c = C, d = ld(m-s). na+c cubic, 4a^2d+1 cubic, f deg 1 or 2
for bd, ed in [(2, 2), (1, 1)]:
    typeI('(1,0,1)', la*(m - r), C, ld*(m - s), bd, ed, [la, C, ld, r, s])
# (0,1,1): a = A, c = lc(m-r), d = ld(m-s)
for bd, ed in [(1, 0), (0, -1 + 1)]:
    typeI('(0,1,1)', A, lc*(m - r), ld*(m - s), bd, ed, [A, lc, ld, r, s])
