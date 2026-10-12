"""O158 Prop 4.2(a)-(c): solve F(g(x)) = mu*F(x) for affine g with monomial linear part (all permutations),
in sympy; n symbolic, or a fixed integer given as argv[1] (sympy.solve sometimes misses solutions with symbolic n,
so run with two or three integer values as well). Prints all solutions (lambda, beta, mu)."""
import itertools, sympy as sp
import sys
n = sp.Integer(int(sys.argv[1])) if len(sys.argv) > 1 else sp.symbols('n', nonzero=True)
def run(name, vars_, F):
    k = len(vars_)
    lam = sp.symbols(f'l0:{k}'); bet = sp.symbols(f'b0:{k}'); mu = sp.symbols('mu')
    for perm in itertools.permutations(range(k)):
        sub = {vars_[i]: lam[i] * vars_[perm[i]] + bet[i] for i in range(k)}
        expr = sp.expand(F.xreplace(sub) - mu * F)
        eqs = sp.Poly(expr, *vars_).coeffs()
        sols = sp.solve(eqs, list(lam) + list(bet) + [mu], dict=True)
        sols = [s for s in sols if all(s.get(l, l) != 0 for l in lam) and s.get(mu, mu) != 0]
        for s in sols:
            print(name, 'perm', perm, s)
x, y, z, t, u, v, a, b, c, kk = sp.symbols('x y z t u v a b c k')
run('ES', [x, y, z], 4 * x * y * z / n - (x * y + y * z + z * x))
run('X', [t, u, v], t * u * v - u - v - n)
run('TII', [a, b, c, kk], 4 * a * b * c * kk - a - b - n * kk)
