# R225: solve the Thm 2.2 shape equations for k (sympy), to inspect the sign of k on every solution branch.
import sympy as sp
m, k = sp.symbols('m k')
n = m**2 + k
A, C, L, u, v, la, lc, ld, r, s, q = sp.symbols('A C L u v la lc ld r s q')
def C_(expr): return sp.Poly(sp.expand(expr), m).all_coeffs()
def run(name, a, c, d, typ, bdeg, edeg, solvefor):
    bs = sp.symbols('b0:%d' % (bdeg + 1)); es = sp.symbols('e0:%d' % (edeg + 1))
    b = sum(bs[i]*m**i for i in range(bdeg + 1)); e = sum(es[i]*m**i for i in range(edeg + 1))
    if typ == 'I':
        f = 4*a*c*d - n
        eqs = C_(f*b - n*a - c) + C_(f*e - 4*a**2*d - 1) + C_(c*e - a - b)
    else:
        f = 4*a*c*d - 1
        eqs = C_(e*f - n - 4*a**2*d) + C_(c*e - a - b) + C_(4*a*b*d - n - e)
    eqs = [x for x in eqs if x != 0]
    sols = sp.solve(eqs, list(bs) + list(es) + solvefor, dict=True)
    print('==', typ, name, 'deg b,e =', bdeg, edeg, ' #branches', len(sols))
    for S in sols:
        print('   k =', sp.factor(S.get(k, k)), '| others:', {str(x): sp.factor(S[x]) for x in solvefor if x in S and x != k},
              '| f =', sp.factor(f.subs(S)), '| e =', sp.factor(e.subs(S)), '| b =', sp.factor(b.subs(S)))
# Type I
run('(0,0,2)', A, C, L*(m**2+u*m+v), 'I', 0, 0, [k, u, v])
run('(0,0,2)', A, C, L*(m**2+u*m+v), 'I', 1, 1, [k, u, v])
run('(0,0,2)', A, C, L*(m**2+u*m+v), 'I', 2, 2, [k, u])
run('(1,0,1)', la*(m-r), C, ld*(m-s), 'I', 1, 1, [k, C, s])   # Lambda>1
run('(1,0,1)', la*(m-r), C, ld*(m-s), 'I', 2, 2, [k, C, s])   # Lambda=1
run('(0,1,1)', A, lc*(m-r), ld*(m-s), 'I', 0, -0, [k, r, s])
run('(0,1,1)', A, lc*(m-r), ld*(m-s), 'I', 1, 0, [k, r, s])
# Type II  (deg e as given; b = ce - a)
run('e2 (0,0,0)', A, C, L, 'II', 2, 2, [k])
for nm, a, c, d in [('(1,0,0,1)', la*(m-r), C, L), ('(0,1,0,1)', A, lc*(m-r), L), ('(0,0,1,1)', A, C, ld*(m-s))]:
    bd = 1 if nm != '(0,0,0,1)' else 1
    run(nm, a, c, d, 'II', 2 if nm == '(0,1,0,1)' else 1, 1, [k, r] if 'r' in str(a)+str(c) else [k, s])
run('(0,0,2,0)', A, C, L*(m**2+u*m+v), 'II', 0, 0, [k, u])
run('(0,1,1,0)', A, lc*(m-r), ld*(m-s), 'II', 1, 0, [k, s])
run('(1,1,0,0)', la*(m-r), lc*(m-q), L, 'II', 1, 0, [k, q])
run('(1,0,1,0)', la*(m-r), C, ld*(m-s), 'II', 1, 0, [k, s])
run('(2,0,0,0)', la*(m**2+u*m+v), C, L, 'II', 2, 0, [k, u])
run('(0,2,0,0)', A, lc*(m**2+u*m+v), L, 'II', 2, 0, [k, u])
